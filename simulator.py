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
import Hazard
# M_select RM_select to be added
class Processor:

    def __init__(self, currFolderPath):
        self._PMI = memory.PMI()
        self._ALU = ALU.ALU()
        self._IAG = IAG.IAG()
        self._fileReader = ReadFile()
        self._registerFile = RegisterFile()
        self.buffer = Hazard.Buffer()
        
        self._currFolderPath = currFolderPath
        self.df_control = pd.read_csv(os.path.join(self._currFolderPath, 'repository', "controls.csv"))
        self.df_control = self.df_control.dropna(axis=0, how='any')
        self.df_main = pd.read_csv(os.path.join(self._currFolderPath, 'repository', "instructions.csv"))
        
        self.hdu = Hazard.HDU(self.df_control)
        self._outputLogFile = open(os.path.join(self._currFolderPath, 'generated', "outputLog.txt"), "w")
        self.initialiseTempRegisters()
        self.initialiseControls()
        self.bufferStore = [(), (), (), ()]
        
        #sys.stdout = self._outputLogFile
        currOpID = 0
        self.cycle = 0

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
        #self._muxM = list(self.df_control['muxM'].astype(int))
        #self._muxRM = list(self.df_control['muxRM'].astype(int))
        self._writeEnable = list(self.df_control['WE'].astype(int))
        self.SizeEnable = list(self.df_control['SE'].astype(int))

    def muxMA(self, MA_select):
        if(MA_select == 0):
            return self.buffer.get(3)[1] #RZ
        else:
            return self._IAG.getPC() #getPC
        
    def comparator(self,reg1,reg2,control,select_mux1,select_mux2):
        in1 = 0
        in2 = 0
        if(select_mux1==0):
            in1 = self._registerFile.get_register(reg1)         #value of register
        elif(select_mux1==1):
            in1 =  self.buffer.get(3)[1]                        #E to D
        else:
            in1 =  self.buffer.get(4)[1]                        #M to D

        if(select_mux2 ==0):
            in2 = self._registerFile.get_register(reg2)         #value of register
        elif(select_mux2==1):
            in2 =  self.buffer.get(3)[1]                        #E to D
        else:
            in2 =  self.buffer.get(4)[1]  

        if(control == 0):
            return(in1 == in2)
        if(control == 1):
            return(in1 != in2)
        if(control == 2):
            return(in1 >= in2)
        if(control == 3):
            return(in1 < in2)
        
    def setIR(self, enable):
        if enable == 1:
            self._IR = self._PMI.getMDR(0)
            
    def getIR(self):
        return self._IR

    def muxA(self, A_select):
        if(A_select == 0):
            return self.buffer.get(2)[2] #RA
        elif(A_select == 1):
            return self.buffer.get(2)[1] #auipc / PC
            #return self._IAG.getPC()
        # elif(A_select == 2):
        #     return self.buffer.get(3)[1]
        # else:
        #     return self.buffer.get(4)[1]
        
    def muxB(self, B_select):
        if(B_select == 0):
            return self._RB
        elif(B_select == 1):
            return self._imm
        # elif(B_select == 2):
        #     return self.buffer.get(3)[1]
        # else:
        #     return self.buffer.get(4)[1]
        
    def muxM(self, M_select): #new
        if(M_select == 0):
            return self.buffer.get(4)[1]

        else:
            return self.buffer.get(3)[3]
        
    def muxRM(self, RM_select): #new
        #doubt
        if(RM_select == 0):
            return self._RY
        elif(RM_select == 1):
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

    def fetch(self):
        print("Fetch stage:")
        print("PC:", self._IAG.getPC())
        outputmuxMA = self.muxMA(1)  # MAR gets value of PC

        #PC_temp
        self._IAG.updatePC_temp()  # PC_Temp gets PC+4

        self._PMI.setMAR(outputmuxMA, 0)
        # MDR gets value stored at address in MAR
        self._PMI.accessMemory(1, 2, 0)

        self.setIR(1)  # IR gets value of MDR
        if self.getIR() == "0"*8:
            return False
        
        self.bufferStore[0] = (self._IAG.getPC(), self._IR, self._IAG.getPC_Temp())

        self._IAG.adder(self._IAG.getPC())
        self._IAG.muxPC(0, "0"*8)
        self._IAG.updatePC(1)
        
        print("IR:", self._IR)
        return True

    def decode(self):

        if not self.buffer.ifPresent(1):
            return False, 0, [[False, "NO", 0],[False, "NO", 0]] #if no memory buffer value set before it, don't run and don't set it's buffer too

        print("Decode stage:")
        PC, IR, PC_temp = self.buffer.get(1)
        info_code = identify(IR, self.df_main)
        print("code:", info_code)
        
        currOpID = info_code['id']
        #currMuxRM = self._muxRM[currOpID]
        rs1 = int(info_code['rs1'], 2)
        self._RA = self._registerFile.get_register(rs1)
        print("RA:", self._RA)

        rs2 = int(info_code['rs2'], 2)
        self._RB = self._registerFile.get_register(rs2)
        #self._RM = self.muxRM(currMuxRM) #new
        self._RM = self._RB #change RM along with rs2 Data forwarding
        print("RB:", self._RB)

        self._rd = int(info_code['rd'], 2)
        print("rd:", self._rd)

        immediate = extendImmediate(info_code['immediate'])
        self._imm = binToHex(immediate)
        print("imm:", self._imm)
        resultarray = self.hdu.stalling3(currOpID, self._rd, rs1, rs2)

        self.bufferStore[1] = (currOpID, PC, self._RA, self._RB, self._RM, self._rd, rs1, rs2, self._imm, PC_temp, resultarray)

        return True, max(resultarray[0][2], resultarray[1][2]), resultarray

    def execute(self):

        if not self.buffer.ifPresent(2):
            return False, 0, [[False, "NO", 0],[False, "NO", 0]] #if no memory buffer value set before it, don't run and don't set it's buffer too

        print("Execute stage:")
        currOpID, PC, RA, RB, RM, rd, rs1, rs2, imm, PC_temp, resultarray = self.buffer.get(2)
        #controls
        currALU_select = self._ALU_select[currOpID] #ALU 
        currMuxB = self._muxB[currOpID]
        currMuxA = self._muxA[currOpID]

        ##
        currINCSelect = self.INC_select[currOpID]
        currSSelect = self.S_select[currOpID]
        ##

        operand1 = self.muxA(currMuxA)
        operand2 = self.muxB(currMuxB)
        print("operand1:", operand1)
        print("operand2:", operand2)
        self._RZ = self._ALU.operate(operand1, operand2, currALU_select)
        print("RZ:", self._RZ)

        #to edit, start
        # self._IAG.muxPC(self.PC_select[currOpID], RA)
        # self._IAG.updatePC(1)
        # self._IAG.muxINC(currINCSelect, currSSelect, imm, self._RZ)
        # self._IAG.adder()
        # self._IAG.muxPC(0, RA)
        # self._IAG.updatePC(1)
        #end
        Miss = False
        if 18 <= currOpID <= 23:
            if 18 <= currOpID <= 21: #beq, ..
                if RZ[-1] == "0": #false
                    self._IAG.adder(PC)
                else: #true
                    self._IAG.adder(PC, imm)
                    Miss = True
            elif id == 22: #jal
                self._IAG.adder(PC, imm)
                Miss = True
            else: #jalr
                self._IAG.adder(PC)
                Miss = True
        else:
            self._IAG.adder(PC)
        
        self._IAG.muxPC(self.PC_select[currOpID], RA)
        self._IAG.updatePC(1)
        
        self.bufferStore[2] = (currOpID, self._RZ, rd, RM, rs1, rs2, PC_temp)
        print((self.bufferStore[2]))
        return True, Miss, resultarray       

    def memoryAccess(self):

        if not self.buffer.ifPresent(3):
            return False #if no memory buffer value set before it, then don't go further

        currOpID, RZ, rd, RM, rs1, rs2, PC_temp = self.buffer.get(3) #buffer access
        print("Memory Access stage:")
        currMemoryEnable = self._memoryEnable[currOpID]
        currSizeEnable = self.SizeEnable[currOpID]


        # currMuxM = self._muxM[currOpID] #not needed

        outputmuxMA = self.muxMA(0)

        self._PMI.setMAR(outputmuxMA)
        #print((self.buffer.get(3)))
        print("RM :", RM, type(RM))
        self._PMI.setMDR(RM) #csv me baki hai


        print("MDR:", self._PMI.getMDR())
        print("MAR:", self._PMI.getMAR())

        self._PMI.accessMemory(currMemoryEnable, currSizeEnable)

        self._RY = self.muxY(self._muxY[currOpID])
        self.bufferStore[3] = (currOpID, self._RY, rd)
        return True

    def registerUpdate(self):

        if not self.buffer.ifPresent(4):
            return #if no memory buffer value set before it, then don't go further
        currOpID, RY, rd = self.buffer.get(4)
        self.hdu.update_process(currOpID, rd)
        print("Register Update Stage:")
        currWriteEnable = self._writeEnable[currOpID]
        self._registerFile.set_register(rd, RY, currWriteEnable)
        print("RD: ", rd)
        print("RY: ", RY)
        
    def bufferUpdate(self, i):
        if(i == 0):
            self.buffer.fetchB(*self.bufferStore[0])
        if(i == 1):
            self.buffer.decodeB(*self.bufferStore[1])
        if(i == 2):
            self.buffer.executeB(*self.bufferStore[2])
        if(i == 3):
            self.buffer.memoryB(*self.bufferStore[3])

    def run_this(self):
        Pipeline_cycle = 0
        while True:
            Pipeline_cycle += 1
            MemBufferSignal = ExecBufferSignal = DecodeBufferSignal = FetchBufferSignal = True
            Miss = False
            isStall = False
            hazardlist = [[False, "NO", 0],[False, "NO", 0]]
            hazardlistE = [[False, "NO", 0],[False, "NO", 0]]
            for i in range(5):
                if i == 4:
                    FetchBufferSignal = self.fetch()
                if i == 3:
                    DecodeBufferSignal, isStall, hazardlist = self.decode()
                    print("Stalling :", isStall)
                    if isStall:
                        break
                if i == 2:
                    ExecBufferSignal, Miss, hazardlistE = self.execute()
                if i == 1:
                    MemBufferSignal = self.memoryAccess()
                if i == 0:
                    self.registerUpdate()
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

            # if DecodeBufferSignal and isStall == 0:
            #     if hazardlist[0][0] == True: #rs1
            #         if hazardlist[0][1] == "ME":
            #             pass #take RY and make RA = RY
            #         elif hazardlist[0][1] == "EE":
            #             pass #take RZ and make RA = RY
                        
            #     if hazardlist[1][0] == True: #rs2
            #         if hazardlist[1][1] == "ME":
            #             pass
            #         elif hazardlist[1][1] == "EE":
            #             pass
            
            # if ExecBufferSignal:
            #     if hazardlistE[0][0] == True: #rs1
            #         if hazardlistE[0][1][0] == 'M':
            #             pass #M->M in this case only
            #         else:
            #             pass
            #pass the hazard list to buffer decode buffer used in execute and helps resolve M->M
            
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
                isStall -= 1
                continue
            if FetchBufferSignal and Miss == False: #set buffer only here
                self.bufferUpdate(0)
            else:
                self.buffer.clearStage(1)
            #clear buffer store
            self.bufferStore = [(), (), (), ()]

            if MemBufferSignal == ExecBufferSignal == DecodeBufferSignal == FetchBufferSignal == False:
                break
            if Pipeline_cycle > 100:
                break
        
    def printData(self):
        filename = 'output.txt'
        filename = os.path.join(self._currFolderPath, "generated", 'memory.txt')
        memorySnapshot = self._PMI.getMemory()
        self._fileReader.printMemory(memorySnapshot, filename)
        self._outputLogFile.close()

    def printRegisters(self):
        registers = self._registerFile.get_registerFile()
        filename = os.path.join(self._currFolderPath, "generated", 'registers.txt')
        self._fileReader.printRegisters(registers, filename)
        
        
    def getRegisters(self):
        return self._registerFile.get_registerFile()
        
    def getData(self):
        return self._PMI.getMemory()

    def reset(self):
        self._outputLogFile = open(os.path.join(self._currFolderPath, 'generated', "outputLog.txt"), "w")
        sys.stdout = self._outputLogFile
        self._registerFile.initialise_registers()
        self._PMI.clearMemory()
        self._IAG.initialiseIAG()
        self.initialiseTempRegisters()
        self.initialiseControls()
        self.cycle = 0
