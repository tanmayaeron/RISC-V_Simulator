import pandas as pd
import os
import sys
import io
import ALU
import memory
import IAG
from register import RegisterFile
from decode import identify
from helperFunctions import *
from input import ReadFile
from BTB import BTB
import Hazard
import json

# M_select RM_select to be added
class Processor:

    def __init__(self, currFolderPath):
        self._PMI = memory.PMI()
        self._ALU = ALU.ALU()
        self._IAG = IAG.IAG()
        self._fileReader = ReadFile()
        self._registerFile = RegisterFile()
        self.buffer = Hazard.Buffer()
        self.outputD = {0:{}, 1:{}, 2:{}, 3:{}, 4:{}}
        self._currFolderPath = currFolderPath
        self.df_control = pd.read_csv(os.path.join(self._currFolderPath, 'repository', "controls.csv"))
        self.df_control = self.df_control.dropna(axis=0, how='any')
        self.df_main = pd.read_csv(os.path.join(self._currFolderPath, 'repository', "instructions.csv"))
        
        self.hdu = Hazard.HDU(self.df_control)
        self._outputLogFile = open(os.path.join(self._currFolderPath, 'generated', "outputLog.txt"), "w")
        self.initialiseTempRegisters()
        self.initialiseControls()
        self.bufferStore = [[], [], [], []]
        # self.bufferStore is list of list as it is updated in forwardingE 
        sys.stdout = self._outputLogFile
        self.cycle = 0
        self._BTB = BTB()
        self.initializeStats()

    def initializeStats(self):
        # Stats to be printed in an output file at the end of the simulation.
    
        self.Pipeline_cycle = 0
        self.instructions_executed = 0
        self.CPI = 0
        self.Data_transfer_instructions = 0
        self.ALU_instructions = 0
        self.control_instructions = 0
        self.Total_Stall_Count = 0
        self.Data_Hazards = 0
        self.control_Hazards = 0
        self.Miss_Count = 0
        self.Stall_Count = 0
        self.Flush = 0 


    
    def initialiseTempRegisters(self):
        self._IR = '0'*8
        self._RA = '0'*8
        self._RB = '0'*8
        self._rd = 0
        self._RZ = '0'*8
        self._RM = '0'*8
        self._RY = '0'*8
        self._imm = '0'*8

    def initialiseControls(self):
        self._ALU_select = list(self.df_control['ALU_select'].astype(int))
        self._muxB = list(self.df_control['muxB'].astype(int))
        self._muxA = list(self.df_control['muxA'].astype(int))
        self._muxY = list(self.df_control['muxY'].astype(int))
        self._memoryEnable = list(self.df_control['ME'].astype(int))
        self.INC_select = list(self.df_control['muxINC'].astype(int))
        self.PC_select = list(self.df_control['muxPC'].astype(int))
        self.S_select = list(self.df_control['muxS'].astype(int))
        self._writeEnable = list(self.df_control['WE'].astype(int))
        self.SizeEnable = list(self.df_control['SE'].astype(int))
        self._isBTB = list(self.df_control['isBTB'].astype(int))

    def muxMA(self, MA_select):
        if MA_select == 0:
            return self.buffer.get(3)[1] #RZ
        else:
            return self._IAG.getPC() #getPC
        
    def setIR(self, enable):
        if enable == 1:
            self._IR = self._PMI.getMDR(0)
            
    def getIR(self):
        return self._IR

    def muxA(self, A_select):
        if A_select == 0:
            return self.buffer.get(2)[2] #RA
        else:
            return self.buffer.get(2)[1] #auipc / PC
        
    def muxB(self, B_select):
        if B_select == 0:
            return self._RB
        else:
            return self._imm

        
    def muxM(self, M_select): #new
        if M_select == 0:
            return self.buffer.get(4)[1]
        else:
            return self.buffer.get(3)[3]
        
    def muxRM(self, RM_select): #new
        #doubt
        if RM_select == 0:
            return self._RY
        elif RM_select == 1:
            return self._RZ
        else:
            return self._RB
        

    def muxY(self, Y_select):
        if(Y_select == 0):
            return self.buffer.get(3)[1] #RZ
        elif(Y_select == 1):
            return self._PMI.getMDR()
        else:
            return self.buffer.get(3)[6] #PC_temp

    def load_mc(self, currFileName):
        filepath = os.path.join(self._currFolderPath,'test', currFileName)
        self._fileReader.read_mc(filepath, self._PMI)

        #print(self._PMI.getMemory(0))


    def fetch(self):
        outputmuxMA = self.muxMA(1)  # MAR gets value of PC
        self._IAG.updatePC_temp()
        self._PMI.setMAR(outputmuxMA, 0)
        self._PMI.accessMemory(1, 2, 0)

        self.setIR(1)  # IR gets value of MDR
        self.outputD[0]["IR"] = self.getIR()
        self.outputD[0]["PC"] = self._IAG.getPC()
        if self.getIR() == "0"*8:
            return False
        
        predict = self._BTB.predict(self._IAG.getPC())
        self.bufferStore[0] = [self._IAG.getPC(), self._IR, self._IAG.getPC_Temp()]

        self.outputD[0]["buffer"] = self.bufferStore[0]


        if predict[0]:
            self._IAG.setPC(predict[1])
            # predict[1] is target
        else:
            self._IAG.adder(self._IAG.getPC())
            self._IAG.muxPC(0, "0"*8)
            self._IAG.updatePC(1)
        
        self.outputD[0]["IR"] = self.getIR()
        return True

    def decode(self,knob2=True):

        if not self.buffer.ifPresent(1):
            return False, 0, [[False, "NO", 0],[False, "NO", 0]] #if no memory buffer value set before it, don't run and don't set it's buffer too

        PC, IR, PC_temp = self.buffer.get(1)
        info_code = identify(IR, self.df_main)
        self.outputD[1]["code"] = info_code
        
        currOpID = info_code['id']
        
        rs1 = int(info_code['rs1'], 2)
        self._RA = self._registerFile.get_register(rs1)
        self.outputD[1]["RA"] = self._RA

        rs2 = int(info_code['rs2'], 2)
        self._RB = self._registerFile.get_register(rs2)
        
        self._RM = self._RB #change RM along with rs2 Data forwarding
        self.outputD[1]["RB"] = self._RB

        self._rd = int(info_code['rd'], 2)
        self.outputD[1]["rd"] = self._rd

        immediate = extendImmediate(info_code['immediate'])
        self._imm = binToHex(immediate)
        self.outputD[1]["imm"] = self._imm
        
        
        if not knob2:
            #knob2 is false we stall as we stall
            resultarray = self.hdu.stalling3(currOpID, self._rd, rs1, rs2)
        else:
            #knob2 is true we call forwarding(knob2=true means we data forward)
            resultarray = self.hdu.forwarding2(self.buffer, currOpID, rs1, rs2)
        
        self.bufferStore[1] = [currOpID, PC, self._RA, self._RB, self._RM, self._rd, rs1, rs2, self._imm, PC_temp, resultarray]
        self.outputD[1]["buffer"] = self.bufferStore[1]

        return True, max(resultarray[0][2], resultarray[1][2]), resultarray

    def execute(self):

        if not self.buffer.ifPresent(2):
            return False, 0, [[False, "NO", 0],[False, "NO", 0]] #if no memory buffer value set before it, don't run and don't set it's buffer too

        currOpID, PC, RA, RB, RM, rd, rs1, rs2, imm, PC_temp, resultarray = self.buffer.get(2)

        currALU_select = self._ALU_select[currOpID] #ALU 
        currMuxB = self._muxB[currOpID]
        currMuxA = self._muxA[currOpID]

        currINCSelect = self.INC_select[currOpID]
        currSSelect = self.S_select[currOpID]
        isBTB = self._isBTB[currOpID]
        isJalr = self.PC_select[currOpID]

        operand1 = self.muxA(currMuxA)
        operand2 = self.muxB(currMuxB)
        self.outputD[2]["o1"] = operand1
        self.outputD[2]["o2"] = operand2
        
        self._RZ = self._ALU.operate(operand1, operand2, currALU_select)
        self.outputD[2]["RZ"] = self._RZ

        self._IAG.adder(PC, imm)
        self._IAG.muxPC(0, RA)

        Miss = self._BTB.isFlush(PC, self._RZ, currOpID) #order wise first

        self._BTB.addInstruction(PC, PC_temp, imm, self._IAG.output_muxPC, currOpID)


        if Miss:
            if currOpID == 23:
                self._IAG.adder(RA, imm)
            else:
                if currOpID == 22:
                    self._IAG.adder(PC, imm)
                else:
                    if self._RZ[-1] == "1":
                        self._IAG.adder(PC, imm)
                    else:
                        self._IAG.adder(PC)
            self._IAG.muxPC(0, RA)
            self._IAG.updatePC(1)

        self.bufferStore[2] = [currOpID, self._RZ, rd, RM, rs1, rs2, PC_temp]
        self.outputD[2]["buffer"] = self.bufferStore[2]

        return True, Miss, resultarray       

    def memoryAccess(self):

        if not self.buffer.ifPresent(3):
            return False #if no memory buffer value set before it, then don't go further

        currOpID, RZ, rd, RM, rs1, rs2, PC_temp = self.buffer.get(3) #buffer access
        currMemoryEnable = self._memoryEnable[currOpID]
        currSizeEnable = self.SizeEnable[currOpID]

        outputmuxMA = self.muxMA(0)

        self._PMI.setMAR(outputmuxMA)
        
        self._PMI.setMDR(RM)

        if currMemoryEnable:
            self.outputD[3]["MDR"] = self._PMI.getMDR()
            
            self.outputD[3]["MAR"] =  self._PMI.getMAR()

        self._PMI.accessMemory(currMemoryEnable, currSizeEnable)

        self._RY = self.muxY(self._muxY[currOpID])
        self.bufferStore[3] = [currOpID, self._RY, rd]
        self.outputD[3]["buffer"] = self.bufferStore[3]
        
        return True

    def incrementInstructions(self,currOpID):

        self.instructions_executed += 1

        if 12 <= currOpID <= 17:
            self.Data_transfer_instructions += 1
        elif 18 <= currOpID <= 23:
            self.control_instructions += 1
        else:
            self.ALU_instructions += 1


    def registerUpdate(self,knob2=True):
        # write back function
        if not self.buffer.ifPresent(4):
            return #if no memory buffer value set before it, then don't go further

        currOpID, RY, rd = self.buffer.get(4)


        self.incrementInstructions(currOpID)
        
        if not knob2:
            # knob2 is True so we stall
            self.hdu.update_process(currOpID, rd)


        currWriteEnable = self._writeEnable[currOpID]
        self._registerFile.set_register(rd, RY, currWriteEnable)
        self.outputD[4]["rd"] = self._rd
        self.outputD[4]["RY"] =  self._RY
        
    def bufferUpdate(self, i):
        if i == 0:
            self.buffer.fetchB(*self.bufferStore[0])
        elif i == 1:
            self.buffer.decodeB(*self.bufferStore[1])
        elif i == 2:
            self.buffer.executeB(*self.bufferStore[2])
        elif i == 3:
            self.buffer.memoryB(*self.bufferStore[3])

    ###Control unit that decides the type of forwarding
    def forwarding(self, hazardlist, isStall, DecodeBufferSignal):
        if hazardlist[0][0]==hazardlist[1][0]==False:
            return 
        

        if isStall:
            return
        if not DecodeBufferSignal:
            return 
        
        self.Data_Hazards += 1
        
        if hazardlist[0][0] == True: #rs1

            if hazardlist[0][1] == "ME":
                self.bufferStore[1][2]=self.bufferStore[3][1]# RY value to RA

            elif hazardlist[0][1] == "EE":
                self.bufferStore[1][2]=self.bufferStore[2][1]# RZ value to RA
        
        if hazardlist[1][0] == True: #rs2

            if hazardlist[1][1] == "ME":
                self.bufferStore[1][3]=self.bufferStore[3][1]# RY value to RB
            
            elif hazardlist[1][1] == "EE":
                self.bufferStore[1][3]=self.bufferStore[2][1]# RZ value to RB
    
            
    def forwardingE(self, hazardlistE, isStall, DecodeBufferSignal):
        if hazardlistE[0][0]==hazardlistE[1][0]==False:
            return 
        if isStall:
            return
        if not DecodeBufferSignal:
            return 
        
        if hazardlistE[0][0]==True and hazardlistE[0][1]=="MM":
            #RY vale to RZ
            self.bufferStore[2][1]=self.bufferStore[3][1]
        
        if hazardlistE[1][0]==True and hazardlistE[1][1]=="MM":
            #RY vale to RZ
            self.bufferStore[2][1]=self.bufferStore[3][1]
    ###uptil here


    def runPipelining_False_for_Forwarding(self, knob2 = False):
        #defaults to stalling when knob is unset or True in our code
        self.Pipeline_cycle = 0
        self.Stall_Count = 0
        self.Miss_Count = 0
        isStall = 0
        PrevIsStall = 0
        while True:
            self.Pipeline_cycle += 1
            MemBufferSignal = ExecBufferSignal = DecodeBufferSignal = FetchBufferSignal = True
            Miss = False
            hazardlist = [[False, "NO", 0],[False, "NO", 0]]
            hazardlistE = [[False, "NO", 0],[False, "NO", 0]]
            self.outputD =  {0:{}, 1:{}, 2:{}, 3:{}, 4:{}}
            for i in range(5):
                
                if i == 4:
                    FetchBufferSignal = self.fetch()
                if i == 3:
                    DecodeBufferSignal, isStall, hazardlist = self.decode(knob2)
                    self.outputD[1]["Stalling"] =  isStall
                    if isStall:
                        break
                if i == 2:
                    ExecBufferSignal, Miss, hazardlistE = self.execute()
                    if Miss:
                        self.Miss_Count += 1
                        break
                if i == 1:
                    MemBufferSignal = self.memoryAccess()
                if i == 0:
                    self.registerUpdate(knob2)
                
            out = json.dumps(self.outputD)
            print(out)
            # with open(self._outputLogFile, 'w') as json_file:
            #     json.dump(self.outputD, json_file)
            # json.dump(self.outputD, self._outputLogFile)
        
            #In case of a miss
            #send a signal from execute to clear buffers of decode and fetch
            #PC is already updated to the required by IAG and will be fetched next

            #In case of stall = 1, we know
            #M->E, we realise it in decode, pass a signal
            #The signal will tell us the stall
            #Don't update decode buffer and fetch, don't delete the fetch buffer but decode is deleted
            #as the decode buffer was deleted no execute occurs in the next cycle
            #fetch buffer wasn't deleted or updated so decode occurs with same IR, PC
            #this way we stalled the whole thing by one cycle

            
            if  not knob2:
                if PrevIsStall==0 and isStall:
                    self.Data_Hazards += 1
            
            PrevIsStall = isStall
            
            if not knob2 == False: #forwarding occurs
              
                self.forwarding(hazardlist, isStall, DecodeBufferSignal)
                self.forwardingE(hazardlistE, isStall, DecodeBufferSignal)
            
            if MemBufferSignal:
                self.bufferUpdate(3)
            else:
                self.buffer.clearStage(4)
            
            if ExecBufferSignal:
                self.bufferUpdate(2)
            else: #it's a miss or no fetch buffer before it
                self.buffer.clearStage(3)

            if DecodeBufferSignal and Miss == False and isStall == 0: #set buffer only here
                self.bufferUpdate(1)
            else: #delete pre existing buffer
                self.buffer.clearStage(2)
            
            if isStall:
                self.Stall_Count += 1
                isStall -= 1
                continue
            
            if FetchBufferSignal and Miss == False: #set buffer only here
                self.bufferUpdate(0)
            else:
                self.buffer.clearStage(1)
            #clear buffer store
            self.bufferStore = [[], [], [], []]

            if MemBufferSignal == ExecBufferSignal == DecodeBufferSignal == FetchBufferSignal == False:
                break

        
        #self._registerFile.print_registers()
        #if knob2:
        #    print("Stalls in Forwarding case with a static branch predictor:", Stall_Count)
        #else:
        #    print("Stalls in Non-Forwarding case with a static branch predictor:", Stall_Count)


        # if not knob2:
        #     print("Stalls in only Forwarding case with a static branch predictor:", self.Stall_Count)
        # else:
        #     print("Stalls in only Stalling case with a static branch predictor:", self.Stall_Count)

        # print("Total number of branch misses:", self.Miss_Count)

    def printData(self):
        memorySnapshot = self._PMI.getMemory(1)
        filename = os.path.join(self._currFolderPath, "generated", 'memory.txt')
        self._fileReader.printMemory(memorySnapshot, filename)

    def printRegisters(self):
        registers = self._registerFile.get_registerFile()
        filename = os.path.join(self._currFolderPath, "generated", 'registers.txt')
        self._fileReader.printRegisters(registers, filename)
        
    def getRegisters(self):
        return self._registerFile.get_registerFile()
        
    def getData(self):
        return self._PMI.getMemory()
        
    def printStat(self):
        filename = os.path.join(self._currFolderPath, "generated", 'stats.txt')
        f = open(filename,'w')
        f.write("Total number of Cycles in the program :"+str(self.Pipeline_cycle)+"\n")
        f.write("\n")
        f.write("Total number of Instructions executed :"+str(self.instructions_executed)+"\n")
        f.write("\n")
        try:
            self.CPI = self.Pipeline_cycle/self.instructions_executed
        except:
            self.CPI = 0
        f.write("CPI is :"+str(self.CPI)+"\n")
        f.write("\n")
        f.write("Data Transfer Instructions Executed :"+str(self.Data_transfer_instructions)+"\n")
        f.write("\n")
        f.write("ALU instructions are :"+str(self.ALU_instructions)+"\n")
        f.write("\n")
        f.write("Contol instructions :"+str(self.control_instructions)+"\n")
        f.write("\n")

        self.Total_Stall_Count= self.Stall_Count + self.Miss_Count*2
        f.write("Total Stall Count are :"+str(self.Total_Stall_Count)+"\n")
        f.write("\n")
        f.write("Number of Data Hazards are :"+str(self.Data_Hazards)+"\n")
        f.write("\n")
        self.control_Hazards = self.Miss_Count
        f.write("Total Control Hazards are :"+ str(self.control_Hazards)+"\n")
        f.write("\n")
        f.write("Total Branch mispredictions are :"+str(self.Miss_Count)+"\n")
        f.write("\n")
        f.write("Number of stalls due to data hazards are :"+str(self.Stall_Count)+"\n")
        f.write("\n")
        self.Flush = self.Miss_Count*2
        f.write("Number of stalls due to control hazards are :"+str(self.Flush)+"\n")
        f.write("\n")

    def reset(self):
        self._outputLogFile = open(os.path.join(self._currFolderPath, 'generated', "outputLog.txt"), "w")
        sys.stdout = self._outputLogFile
        self._registerFile.initialise_registers()
        self._PMI.clearMemory()
        self._IAG.initialiseIAG()
        self.initialiseTempRegisters()
        self.initialiseControls()
        self.initializeStats()
        self.cycle = 0

