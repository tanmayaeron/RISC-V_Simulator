import pandas as pd
import os
import ALU
import memory
import IAG
from register import RegisterFile
from decode import identify
from helperFunctions import *
from input import ReadFile

df_control = pd.read_csv('controls.csv')
df_control = df_control.dropna(axis=0,how='any')

class Processor:

    cycle = 0

    def __init__(self):
        self._PMI = memory.PMI()
        self._ALU = ALU.ALU()
        self._IAG = IAG.IAG()
        self._fileReader = ReadFile()
        self._registerFile = RegisterFile()
        self.initialiseTempRegisters()
        self.initialiseControls()
        self._currFileName = 'test1.mc'
        self._currFolderPath = os.getcwd()
        self._currOperationId = 0
        
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
        self._ALU_select = list(df_control['ALU_select'].astype(int))
        self._muxB = list(df_control['muxB'].astype(int))
        self._muxA = list(df_control['muxA'].astype(int))
        self._muxY = list(df_control['muxY'].astype(int))
        self._memoryEnable = list(df_control['ME'].astype(int))
        self.INC_select = list(df_control['muxINC'].astype(int))
        self.PC_select = list(df_control['muxPC'].astype(int))
        self.S_select = list(df_control['muxS'].astype(int))
        self._writeEnable = list(df_control['WE'].astype(int))
        self.SizeEnable = list(df_control['SE'].astype(int))
        

    def muxMA(self, MA_select):
        if(MA_select==0):
            return self._RZ
        else:
            return self._IAG.getPC()

    def demuxMDR(self,MDR_select):
        if(MDR_select==0):
            self._RY = self._PMI.getMDR()
        else:
            self._IR = self._PMI.getMDR()
            
    def muxA(self,A_select):
        if(A_select == 0):
            return self._RA
        else:
            return self._IAG.getPC()

    def muxB(self,B_select):
        if(B_select == 0):
            return self._RB
        else:
            return self._imm

    def muxY(self,Y_select):
        if(Y_select==0):
            return self._RZ
        elif(Y_select==1):
            return self._PMI.getMDR()
        else:
            return self._IAG.getPC_Temp()
    
    def load_mc(self):
        filepath = os.path.join(self._currFolderPath, 'test', self._currFileName)
        self._fileReader.read_mc(filepath, self._PMI)

    def fetch(self):
        outputmuxMA = self.muxMA(1)                     #MAR gets value of PC
        self._IAG.updatePC_temp()                       #PC_Temp gets PC+4
        self._PMI.setMAR(outputmuxMA)                   
        self._PMI.getData(2)                           #MDR gets value stored at address in MAR
        self.demuxMDR(1)                               #IR gets value of MDR

    def decode(self):
        info_code = identify(self._IR)
        print("code :", info_code)
        self._currOperationId = info_code['id']
        try:
            registernumber = int(info_code['rs1'],2)
            self._RA = self._registerFile.get_register(registernumber)
        except:
            pass

        try:
            registernumber = int(info_code['rs2'],2)
            self._RB = self._registerFile.get_register(registernumber)
            self._RM = self._RB
        except:
            pass

        try:
            rd = int(info_code['rd'],2)
            self._rd = rd
        except:
            pass
            
        try:
            immediate = extendImmediate(info_code['immediate']) 
            self._imm = binToHex(immediate)
        except:
            pass

    def execute(self):
        currALU_select = self._ALU_select[self._currOperationId]
        currMuxB = self._muxB[self._currOperationId]
        currMuxA = self._muxA[self._currOperationId]
        currINCSelect = self.INC_select[self._currOperationId]
        currSSelect = self.S_select[self._currOperationId]
        print("ALUs, MUXb",currALU_select, currMuxB)
        
        operand1 = self.muxA(currMuxA)
        operand2 = self.muxB(currMuxB)
        self._RZ = self._ALU.operate(operand1, operand2, currALU_select)

        print("PCs, INCs", self.PC_select[self._currOperationId], self.INC_select[self._currOperationId])
        print("PC, PC_temp :",self._IAG.getPC(), self._IAG.getPC_Temp())
        
        self._IAG.muxPC(self.PC_select[self._currOperationId], self._RA)
        self._IAG.updatePC(1)
        self._IAG.muxINC(currINCSelect, currSSelect, self._imm, self._RZ)
        self._IAG.adder()
        self._IAG.muxPC(0, self._RA)
        self._IAG.updatePC(1)
        print("PC, PC_temp :",self._IAG.getPC(), self._IAG.getPC_Temp())

        
    def memoryAccess(self):
        currMemoryEnable =self._memoryEnable[self._currOperationId]      
        currSizeEnable = self.SizeEnable[self._currOperationId]
        self._PMI.accessMemory(currMemoryEnable, currSizeEnable)
        
    def registerUpdate(self):
        self._RY = self.muxY(self._muxY[self._currOperationId])
        currWriteEnable = self._writeEnable[self._currOperationId]
        self._registerFile.set_register(self._rd,self._RY, currWriteEnable)
        print("RD: RY:", self._rd, self._RY)
    def printData(self):
        filename = 'output.txt'
        obj = self._PMI
        self._fileReader.write_file(obj, filename)

if __name__=='__main__':
    run = Processor()
    run.load_mc()
    for i in range(3):
        run.fetch()
        print(run._IR)
        run.decode()
        print(run._currOperationId)
        run.execute()
        run.memoryAccess()
        run.registerUpdate()
        run._registerFile.print_registers()
        run._PMI.print_memory()
        run.printData()
