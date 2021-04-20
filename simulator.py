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

        self._outputLogFile = open(os.path.join(self._currFolderPath, 'generated', "outputLog.txt"), "w")
        self.initialiseTempRegisters()
        self.initialiseControls()
        self.bufferStore = [(), (), (), ()]
        
        sys.stdout = self._outputLogFile
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
        self._muxM = list(self.df_control['muxM'].astype(int))
        self._muxRM = list(self.df_control['muxRM'].astype(int))
        self._writeEnable = list(self.df_control['WE'].astype(int))
        self.SizeEnable = list(self.df_control['SE'].astype(int))

    def muxMA(self, MA_select):
        if(MA_select == 0):
            return self._RZ
        else:
            return self._IAG.getPC()
        
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
            self._IR = self._PMI.getMDR()
            
    def getIR(self):
        return self._IR

    def muxA(self, A_select):
        if(A_select == 0):
            return self._RA
        elif(A_select == 1):
            return self.buffer.get(1)[2] #auipc
            #return self._IAG.getPC()
        elif(A_select == 2):
            return self.buffer.get(3)[1]
        else:
            return self.buffer.get(4)[1]
        
    def muxB(self, B_select):
        if(B_select == 0):
            return self._RB
        elif(B_select == 1):
            return self._imm
        elif(B_select == 2):
            return self.buffer.get(3)[1]
        else:
            return self.buffer.get(4)[1]
        
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
            return self._RZ
        elif(Y_select == 1):
            return self._PMI.getMDR()
        else:
            return self._IAG.getPC_Temp()

    def load_mc(self, currFileName):
        filepath = os.path.join(self._currFolderPath,'test', currFileName)
        self._fileReader.read_mc(filepath, self._PMI)

    def fetch(self):
        print("Fetch stage:")
        print("PC:", self._IAG.getPC())
        outputmuxMA = self.muxMA(1)  # MAR gets value of PC
        self._IAG.updatePC_temp()  # PC_Temp gets PC+4
        self._PMI.setMAR(outputmuxMA)
        # MDR gets value stored at address in MAR
        self._PMI.accessMemory(1, 2, 0)
        self.setIR(1)  # IR gets value of MDR
        
        self.bufferStore[0] = (self._IAG.getPC(), self._IR)
        
        print("IR:", self._IR)

    def decode(self):
        print("Decode stage:")
        PC, IR = self.buffer.get(1)
        info_code = identify(IR, self.df_main)
        print("code:", info_code)
        
        currOpID = info_code['id']
        currMuxRM = self._muxRM[currOpID]
        self.rs1 = int(info_code['rs1'], 2)
        self._RA = self._registerFile.get_register(rs1)
        print("RA:", self._RA)

        self.rs2 = int(info_code['rs2'], 2)
        self._RB = self._registerFile.get_register(rs2)
        self._RM = self.muxRM(currMuxRM) #new
        print("RB:", self._RB)

        self._rd = int(info_code['rd'], 2)
        print("rd:", self._rd)

        immediate = extendImmediate(info_code['immediate'])
        self._imm = binToHex(immediate)
        print("imm:", self._imm)
        
        self.bufferStore[1] = (currOpID, PC, self._RA, self._RB, self._RM, self._rd, self._imm)

    def execute(self):
        print("Execute stage:")
        currOpID, PC, RA, RB, RM, rd, imm = self.buffer.get(2)
        #controls
        currALU_select = self._ALU_select[currOpID]
        currMuxB = self._muxB[currOpID]
        currMuxA = self._muxA[currOpID]
        currINCSelect = self.INC_select[currOpID]
        currSSelect = self.S_select[currOpID]

        operand1 = self.muxA(currMuxA)
        operand2 = self.muxB(currMuxB)
        print("operand1:", operand1)
        print("operand2:", operand2)
        self._RZ = self._ALU.operate(operand1, operand2, currALU_select)
        print("RZ:", self._RZ) 

        #to edit, start
        self._IAG.muxPC(self.PC_select[currOpID], RA)
        self._IAG.updatePC(1)
        self._IAG.muxINC(currINCSelect, currSSelect, imm, self._RZ)
        self._IAG.adder()
        self._IAG.muxPC(0, RA)
        self._IAG.updatePC(1)
        #end
        
        self.bufferStore[1] = (currOpId, self._RZ, rd, RM)
       

    def memoryAccess(self):
        currOpId, RZ, rd, RM = self.buffer.get(3)
        print("Memory Access stage:")
        currMemoryEnable = self._memoryEnable[currOpID]
        currSizeEnable = self.SizeEnable[currOpID]
        currMuxM = self._muxM[currOpID]
        outputmuxMA = self.muxMA(0)
        self._PMI.setMAR(outputmuxMA)
        self._PMI.setMDR(self.muxM(currMuxM)) #csv me baki hai
        print("MDR:", self._PMI.getMDR())
        print("MAR:", self._PMI.getMAR())
        self._PMI.accessMemory(currMemoryEnable, currSizeEnable)
        self._RY = self.muxY(self._muxY[currOpID])
        self.bufferStore[3] = (currOpId, self._RY, rd)    

    def registerUpdate(self):
        currOpId, RY, rd = self.buffer.get(4)
        print("Register Update Stage:")
        currWriteEnable = self._writeEnable[currOpID]
        self._registerFile.set_register(rd, RY, currWriteEnable)
        print("RD: ", rd)
        print("RY: ", RY)
        self.cycle += 1
        print("Cycles:", self.cycle)
        
    def bufferUpdate(self, watchArray):
        if(watchArray[0]):
            self.buffer.fetchB(*self.bufferStore[0])
        if(watchArray[1]):
            self.buffer.decodeB(*self.bufferStore[1])
        if(watchArray[2]):
            self.buffer.executeB(*self.bufferStore[2])
        if(watchArray[3]):
            self.buffer.memoryB(*self.bufferStore[3])
        self.bufferStore = [(), (), (), ()]
        
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
