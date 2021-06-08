import pandas as pd
import os
import sys
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


class Processor:

    def __init__(self, initialiseDetails):
        self.stats = {"Cycles":0, "Instructions":0, "CPI":0, "Data transfer instructions":0, "ALU instructions":0, "Control instructions":0, "Total Stall Count":0, "Data Hazard":0, "Control Hazard":0, "Mispredictions":0, "Stalls(data hazard)":0, "Stalls(control Hazard)":0}
        self.initialise(initialiseDetails)
        self.initialiseTempRegisters()
        self.initialiseControls()
        self.initializeStats()
        self._BTB = BTB(self._isBTB,self.PC_select,self.S_select, initialiseDetails[-1])

    def initialise(self, initialiseDetails):
        self._PMI = memory.PMI(*initialiseDetails[1:-1])
        self.initialiseDetails = initialiseDetails
        self._ALU = ALU.ALU()
        self._IAG = IAG.IAG()
        self.buffer = Hazard.Buffer()
        self._fileReader = ReadFile()
        self._registerFile = RegisterFile()
        self._currFolderPath = initialiseDetails[0]
        
        self.df_control = pd.read_csv(os.path.join(self._currFolderPath, 'repository', "controls.csv"))
        self.df_control = self.df_control.dropna(axis=0, how='any')
        self.df_main = pd.read_csv(os.path.join(self._currFolderPath, 'repository', "instructions.csv"))
        
        self.hdu = Hazard.HDU(self.df_control)
        self._outputLogFile = open(os.path.join(self._currFolderPath, 'generated', "outputLog.txt"), "w")
        filenameinit = os.path.join(self._currFolderPath, "generated", 'CacheInfo.txt')
        fileinit = open(filenameinit, 'w')
        fileinit.close()
        self.bufferStore = [[], [], [], []]
        self.outputD = {0:{}, 1:{}, 2:{}, 3:{}, 4:{}}
        self.cycle = 0
        sys.stdout = self._outputLogFile
        
        
        
    def initializeStats(self):
        # Stats to be printed in an output file at the end of the simulation.
        self.cacheSetInfo={"F":-1,"L":-1,"S":-1}

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
        self.branch_Miss = 0
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
        elif A_select==1:
            return self.buffer.get(2)[1] #auipc / PC
        elif A_select==2:
            return self.buffer.get(3)[1]
        else:
            return self.buffer.get(4)[1]
        
    def muxB(self, B_select):
        if B_select == 0:
            return self.buffer.get(2)[3]
        elif B_select==1:
            return self.buffer.get(2)[8]
        elif B_select==2:
            return self.buffer.get(3)[1]
        else:
            return self.buffer.get(4)[1]

    def muxM(self, M_select):
        if M_select == 0:
            return self.buffer.get(4)[1]
        else:
            return self.buffer.get(3)[3]

    def muxY(self, Y_select):
        if(Y_select == 0):
            return self.buffer.get(3)[1] #RZ
        elif(Y_select == 1):
            return self._PMI.getMDR()
        else:
            return self.buffer.get(3)[6] #PC_temp

    def load(self, currFileName, isMC):
        filepath = os.path.join(self._currFolderPath,'test', currFileName)
        self._fileReader.read_mc(filepath, self._PMI, self._currFolderPath,isMC)

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

        self.cacheSetInfo['F']=self._PMI.getCache(0)

        self.bufferStore[0] = [self._IAG.getPC(), self._IR, self._IAG.getPC_Temp()]

        self.outputD[0]["buffer"] = self.bufferStore[0]
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

    def execute(self,executeControl):

        if not self.buffer.ifPresent(2):
            return False, 0, [[False, "NO", 0],[False, "NO", 0]] #if no memory buffer value set before it, don't run and don't set it's buffer too

        currOpID, PC, RA, RB, RM, rd, rs1, rs2, imm, PC_temp, resultarray = self.buffer.get(2)

        currALU_select = executeControl["currALU_select"] #ALU
        currMuxB = executeControl["currMuxB"]
        currMuxA = executeControl["currMuxA"]

        operand1 = self.muxA(currMuxA)
        operand2 = self.muxB(currMuxB)
        self.outputD[2]["o1"] = operand1
        self.outputD[2]["o2"] = operand2
        
        self._RZ = self._ALU.operate(operand1, operand2, currALU_select)
        self.outputD[2]["RZ"] = self._RZ


        #self._IAG.output_muxPC is PC+imm
        target = hexToDec(PC)+hexToDec(imm)
        target = decToHex(target)
        Miss = self._BTB.isFlush(PC, self._RZ, currOpID, target, PC_temp) #order wise first
        self._BTB.addInstruction(PC, PC_temp, imm, target , currOpID)
        self.bufferStore[2] = [currOpID, self._RZ, rd, RM, rs1, rs2, PC_temp,PC]
        self.outputD[2]["buffer"] = self.bufferStore[2]

        return True, Miss, resultarray       

    def memoryAccess(self,memControl):

        if not self.buffer.ifPresent(3):
            return False #if no memory buffer value set before it, then don't go further

        currOpID, RZ, rd, RM, rs1, rs2, PC_temp,PC = self.buffer.get(3) #buffer access
        currMemoryEnable = memControl["currMemoryEnable"]
        currSizeEnable = memControl["currSizeEnable"]

        outputmuxMA = self.muxMA(0)

        self._PMI.setMAR(outputmuxMA)
        M_select = memControl["M_select"]
        outputMuxM = self.muxM(M_select)
        self._PMI.setMDR(outputMuxM)

        if currMemoryEnable:
            self.outputD[3]["MDR"] = self._PMI.getMDR()
            
            self.outputD[3]["MAR"] =  self._PMI.getMAR()

            if currMemoryEnable==1:
                self.cacheSetInfo['L']=self._PMI.getCache(1)
            elif currMemoryEnable==2:
                self.cacheSetInfo['S']=self._PMI.getCache(1)

        self._PMI.accessMemory(currMemoryEnable, currSizeEnable)

        self._RY = self.muxY(memControl["Y_select"])
        self.bufferStore[3] = [currOpID, self._RY, rd,PC]
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

    def registerUpdate(self,WBControl,knob2=True):
        # write back function
        if not self.buffer.ifPresent(4):
            return #if no memory buffer value set before it, then don't go further

        currOpID, RY, rd,PC = self.buffer.get(4)

        self.incrementInstructions(currOpID)
        
        if not knob2:
            # knob2 is True so we stall
            self.hdu.update_process(currOpID, rd)

        currWriteEnable = WBControl["currWriteEnable"]
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


    def pipelinedHelper(self, k1, k2, k3, k4 = 0, k5 = 0):
        self.Pipeline_cycle = 0
        self.Stall_Count = 0
        self.Miss_Count = 0
        self.outputF = {"EE1": "F","EE2": "F","ME1": "F","ME2": "F","MM": "F"}
        self.isStall = 0 
        self.PrevIsStall = 0
        self.executeControl = {}
        self.memControl = {}
        self.WBControl = {}
        self.knob2 = k1
        self.knob3 = k2
        self.knob4 = k3
        self.knob5 = k4
        self.ins_num = k5


    def pipelined(self):
        #defaults to non-forwarding when knob is unset or False in our code
         
        # self.printForwardingInfo()
        self.outputF = {"EE1": "F","EE2": "F","ME1": "F","ME2": "F","MM": "F"}
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
                DecodeBufferSignal, self.isStall, hazardlist = self.decode(self.knob2)
                self.outputD[1]["Stalling"] =  self.isStall
                if self.isStall:
                    break
            if i == 2:
                ExecBufferSignal, Miss, hazardlistE = self.execute(self.executeControl)
                if Miss:
                    self.Miss_Count += 1
                    if(self.S_select[self.buffer.get(2)[0]]):
                        self.branch_Miss+=1
                    break
            if i == 1:
                MemBufferSignal = self.memoryAccess(self.memControl)
            if i == 0:
                self.registerUpdate(self.WBControl,self.knob2)
        


        # self.printCycleInfo()
        # if(self.knob3):
        #     self.printRegisters(self.Pipeline_cycle)
        

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

        # updating PC for next cycle
        if ExecBufferSignal and Miss:  # edits of execute

            currOpID = self.buffer.get(2)[0]

            if self.PC_select[currOpID]:          #jalr
                PC_select = 1
            else:
                PC_select = 3

            S_select = self.S_select[currOpID]
            INC_select = self.INC_select[currOpID]

            self._IAG.muxPC(PC_select,self.buffer)
            self._IAG.updatePC(1)
            self._IAG.muxINC(INC_select,S_select,self.buffer.get(2)[8],self._RZ)
            self._IAG.adder()
            self._IAG.muxPC(0,self.buffer)
            self._IAG.updatePC(1)

        if not Miss and not self.isStall and FetchBufferSignal:  # edits of fetch
            predict = self._BTB.predict(self._IAG.getPC())

            if predict[0]:
                PC_select1 = 4
                PC_select2 = 2
            else:
                PC_select1 = 2
                PC_select2 = 0

            self._IAG.muxPC(PC_select1, self.buffer, predict[1])
            self._IAG.updatePC(1)
            self._IAG.muxINC(0, 0, self.buffer.get(2)[8], self._RZ)
            self._IAG.adder()
            self._IAG.muxPC(PC_select2, self.buffer)
            self._IAG.updatePC(1)

        if  not self.knob2:
            if self.PrevIsStall==0 and self.isStall:
                self.Data_Hazards += 1
        
        self.PrevIsStall = self.isStall


        if MemBufferSignal:
            self.bufferUpdate(3)
        else:
            self.buffer.clearStage(4)
        
        if ExecBufferSignal:
            self.bufferUpdate(2)
        else: #it's a miss or no fetch buffer before it
            self.buffer.clearStage(3)

        if DecodeBufferSignal and Miss == False and self.isStall == 0: #set buffer only here
            self.bufferUpdate(1)
        else: #delete pre existing buffer
            self.buffer.clearStage(2)
        
        if self.isStall:
            self.Stall_Count += 1
            self.isStall -= 1
        
        else:
            if FetchBufferSignal and Miss == False: #set buffer only here
                self.bufferUpdate(0)
            else:
                self.buffer.clearStage(1)

            # clear buffer store
            self.bufferStore = [[],[],[],[]]

            if MemBufferSignal == ExecBufferSignal == DecodeBufferSignal == FetchBufferSignal == False:
                return 0

        # execute_control
        self.executeControl.clear()
        currOpID = self.buffer.get(2)[0]
        self.executeControl["currALU_select"] = self._ALU_select[currOpID]  # ALU
        self.executeControl["currMuxB"] = self._muxB[currOpID]
        self.executeControl["currMuxA"] = self._muxA[currOpID]

        # mem_control
        self.memControl.clear()
        currOpID = self.buffer.get(3)[0]
        self.memControl["currMemoryEnable"] = self._memoryEnable[currOpID]
        self.memControl["currSizeEnable"] = self.SizeEnable[currOpID]
        self.memControl["Y_select"] = self._muxY[currOpID]
        self.memControl["M_select"] = 1

        # wb_control
        self.WBControl.clear()
        currOpID = self.buffer.get(4)[0]
        self.WBControl["currWriteEnable"] = self._writeEnable[currOpID]

        if self.knob2 and not self.PrevIsStall:  # forwarding occurs
            if DecodeBufferSignal:
                if hazardlist[0][0]==True or hazardlist[1][0]==True:
                    self.Data_Hazards += 1

                if hazardlist[0][0] == True and self.executeControl["currMuxA"]==0:            #rs1
                    if hazardlist[0][1] == "ME":
                        self.outputF["ME1"] = "T"
                        self.executeControl["currMuxA"] = 3               # RY value to RA

                    elif hazardlist[0][1] == "EE":
                        self.outputF["EE1"] = "T"
                        self.executeControl["currMuxA"] = 2               # RZ value to RA

                if hazardlist[1][0] == True and self.executeControl["currMuxB"]==0:                                               # rs2

                    if hazardlist[1][1] == "ME":
                        self.outputF["ME2"] = "T"
                        self.executeControl["currMuxB"] = 3    # RY value to RB

                    elif hazardlist[1][1] == "EE":
                        self.outputF["EE2"] = "T"
                        self.executeControl["currMuxB"] = 2  # RZ value to RB

            if hazardlistE[0][0] == True and hazardlistE[0][1] == "MM":
                self.memControl["M_select"] = 0

            if hazardlistE[1][0] == True and hazardlistE[1][1] == "MM":
                self.outputF["MM"] = "T"
                self.memControl["M_select"] = 0
                
                
        # if(self.knob4):
        #     self.printBuffer(self.Pipeline_cycle)
                
        # if(self.knob5):
        #     PC_tocheck = self.checkPC(self.ins_num)
        #     fPC = self.buffer.get(1)[0]
        #     dPC = self.buffer.get(2)[1]
        #     ePC = self.buffer.get(3)[7]
        #     maPC = self.buffer.get(4)[3]
        #     if str(fPC)==PC_tocheck:
        #         self.printBuffer2("Fetch", 1)
        #     if str(dPC)==PC_tocheck:
        #         self.printBuffer2("Decode", 2)
        #     if str(ePC)==PC_tocheck:
        #         self.printBuffer2("Execute", 3)
        #     if str(maPC)==PC_tocheck:
        #         self.printBuffer2("MemoryAccess", 4)
                
        return 1
        # se
        # lf.printForwardingInfo()           


    def nonPipelined(self):        
        self.outputD =  {0:{}, 1:{}, 2:{}, 3:{}, 4:{}}
        FetchBufferSignal = self.fetch()
        if not FetchBufferSignal:
            return 0
        self.bufferUpdate(0)

        self.decode()
        self.bufferUpdate(1)

        currOpID = self.buffer.get(2)[0]

        executeControl = {}
        memControl = {}
        WBControl = {}

        executeControl["currALU_select"] = self._ALU_select[currOpID]  # ALU
        executeControl["currMuxB"] = self._muxB[currOpID]
        executeControl["currMuxA"] = self._muxA[currOpID]

        memControl["currMemoryEnable"] = self._memoryEnable[currOpID]
        memControl["currSizeEnable"] = self.SizeEnable[currOpID]
        memControl["Y_select"] = self._muxY[currOpID]
        memControl["M_select"] = 1

        WBControl["currWriteEnable"] = self._writeEnable[currOpID]

        currINCSelect = self.INC_select[currOpID]
        currSSelect = self.S_select[currOpID]

        self.execute(executeControl)

        self._IAG.muxPC(self.PC_select[currOpID], self.buffer)
        self._IAG.updatePC(1)
        self._IAG.muxINC(currINCSelect, currSSelect, self.buffer.get(2)[8], self._RZ)
        self._IAG.adder()
        self._IAG.muxPC(0,self.buffer.get(2)[2])
        self._IAG.updatePC(1)

        self.bufferUpdate(2)

        self.memoryAccess(memControl)
        self.bufferUpdate(3)

        self.registerUpdate(WBControl)
        for i in range(5):
            if("buffer" in self.outputD[i]):
                del self.outputD[i]["buffer"]
        self.printCycleInfo()
        return 1


    def checkPC(self, ins_num):
        temp = ins_num-1
        temp*=4
        temp = decToHex(temp)
        return temp
        
        
    def printCycleInfo(self):
        filename = os.path.join(self._currFolderPath, "generated", 'outputLog.txt')
        file = open(filename, 'a')
        out = json.dumps(self.outputD)
        file.write(str(out))
        file.write("\n")
        file.close()

        filename = os.path.join(self._currFolderPath, "generated", 'CacheInfo.txt')
        file = open(filename, 'a')
        out = json.dumps(self.cacheSetInfo)
        file.write(str(out))
        file.write("\n")
        file.close()
        self.cacheSetInfo={"F":-1,"L":-1,"S":-1}
        
    def printData(self):
        memorySnapshot = self._PMI.getMemory(1)
        filename = os.path.join(self._currFolderPath, "generated", 'memory.txt')
        self._fileReader.printMemory(memorySnapshot, filename)
        
    def printForwardingInfo(self):
        filename = os.path.join(self._currFolderPath, "generated", 'forwarding.txt')
        out = json.dumps(self.outputF)
        file = open(filename, 'a')
        file.write(str(out))
        file.write("\n")
        file.close()

    def printRegisters(self, cycle = -1):
        registers = self._registerFile.get_registerFile()
        if(cycle == -1):
            filename = os.path.join(self._currFolderPath, "generated", 'registers.txt')
        else:
            filename = os.path.join(self._currFolderPath, "generated","Register Snapshots", 'registers'+str(cycle)+'.txt')
            
        self._fileReader.printRegisters(registers, filename)
        
    def printBuffer2(self, stage, stageNo):
        filename = os.path.join(self._currFolderPath, "generated", 'buffer.txt')
        self._fileReader.printBuffer(stage,self.buffer.get(stageNo), filename)
        
        
        
    def printBuffer(self, cycle = -1):
        filename = os.path.join(self._currFolderPath, "generated","Buffer Snapshot", 'buffer'+str(cycle)+'.txt')
        
        self._fileReader.printBuffer("Fetch",self.buffer.get(1), filename)
        self._fileReader.printBuffer("Decode",self.buffer.get(2), filename)
        self._fileReader.printBuffer("Execute",self.buffer.get(3), filename)
        self._fileReader.printBuffer("MemoryAccess",self.buffer.get(4), filename)
        
        

    def getRegisters(self):
        return self._registerFile.get_registerFile()
        
    def getData(self):
        return self._PMI.getMemory()
        
    def getCaches(self):
        self._PMI.printCaches(self._currFolderPath)
        
    def getStats(self):
        try:
            self.CPI = round(self.Pipeline_cycle/self.instructions_executed,3)
        except:
            self.CPI = 0
            
        self.Total_Stall_Count= self.Stall_Count + self.Miss_Count*2
        self.Flush = self.Miss_Count*2
        self.stats = {"Cycles":self.Pipeline_cycle, "Instructions":self.instructions_executed, "CPI":self.CPI, "Data transfer instructions":self.Data_transfer_instructions, "ALU instructions":self.ALU_instructions, "Control instructions":self.control_instructions, "Total Stall Count":self.Total_Stall_Count, "Data Hazard":self.Data_Hazards, "Control Hazard":self.control_Hazards, "Mispredictions":self.branch_Miss, "Stalls(data hazard)":self.Stall_Count, "Stalls(control Hazard)":self.Flush}
        statsArray = [self.Pipeline_cycle, self.instructions_executed, self.CPI, self.Data_transfer_instructions, self.ALU_instructions, self.control_instructions, self.Total_Stall_Count, self.Data_Hazards, self.control_Hazards, self.branch_Miss, self.Stall_Count, self.Flush]
        
            
        return statsArray
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
        f.write("Total Branch mispredictions are :"+str(self.branch_Miss)+"\n")
        f.write("\n")
        f.write("Number of stalls due to data hazards are :"+str(self.Stall_Count)+"\n")
        f.write("\n")
        self.Flush = self.Miss_Count*2
        f.write("Number of stalls due to control hazards are :"+str(self.Flush)+"\n")
        f.write("\n")
        f.close()

    def reset(self, initialiseDetails2):
        self.initialiseDetails[1:] = initialiseDetails2
        self._outputLogFile = open(os.path.join(self._currFolderPath, 'generated', "outputLog.txt"), "w")
        sys.stdout = self._outputLogFile
        self._registerFile.initialise_registers()
        self._PMI.clearMemory()
        del self._PMI
        del self._BTB
        self._BTB = BTB(self._isBTB,self.PC_select,self.S_select, initialiseDetails2[-1])
        self._PMI = memory.PMI(*initialiseDetails2[:-1])
        self._IAG.initialiseIAG()
        self.initialiseTempRegisters()
        self.initialiseControls()
        self.initializeStats()
        self.bufferStore = [[], [], [], []]
        self.buffer.flush()
        self.cycle = 0