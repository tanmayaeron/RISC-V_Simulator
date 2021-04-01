import pandas as pd
import os
import ALU_re
import memory
import IAG
from ALU_re import ALU
from register import RegisterFile
from bitstring import BitArray
from bitstring import Bits
from decode import identify
from helperFunctions import HelperFunctions
from input import ReadFile
# we will use register objects here

def twos_complement(a):
    return Bits(bin=a).int


df_main = pd.read_csv('instructions.csv')
df2_main = pd.read_csv('controls.csv')

class Processor:

    cycle = 0

    def __init__(self):
        self._PMI = memory.PMI()
        self._ALU = ALU_re.ALU()
        self._IAG = IAG.IAG()
        self._IR = '0'*8
        self._registerFile = RegisterFile()
        self._RA = '0'*8
        self._RB = '0'*8
        self._rd = 0
        self._RZ = '0'*8
        self._RM = '0'*8
        self._RY = '0'*8
        self._imm = '0'*8
        self._fileReader = ReadFile()
        self._currFileName = 'test1.mc'
        self._currFolderPath = os.getcwd()
        self._ALU_select = [int(x) for x in list(df2_main['ALU_select'].dropna())]
        self._muxB = [int(x) for x in list(df2_main['muxB'].dropna())]
        self._muxY = [int(x) for x in list(df2_main['muxY'].dropna())]
        self._memoryEnable = [int(x) for x in list(df2_main['ME'].dropna())]
        self.INC_select = [int(x) for x in list(df2_main['muxINC'].dropna())]
        self.PC_select = [int(x) for x in list(df2_main['muxPC'].dropna())]
        self.WriteEnable = [int(x) for x in list(df2_main['WE'].dropna())]
        self._currOperationId = 0

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
        #MAR gets value of PC
        outputmuxMA = self.muxMA(1)
        self._IAG.updatePC_temp()                       #PC_Temp gets PC+4
        self._PMI.setMAR(outputmuxMA)
        #MDR gets value stored at MDR
        self._PMI.getData(2)
        #IR gets value of MDR
        self.demuxMDR(1)

    def decode(self):
        info_code = identify(self._IR)
        self._neumonic = info_code['neumonic']
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
            immediate = twos_complement(info_code['immediate'])
            self._imm = '{:08x}'.format(immediate)[-8:]
            #print("imm", self._imm)
        except:
            pass

    def execute(self):
        currALU_select = self._ALU_select[self._currOperationId]
        currMuxB = self._muxB[self._currOperationId]
        print("ALUs, MUXb",currALU_select, currMuxB)
        operand1 = self._RA
        operand2 = self.muxB(currMuxB)
        self._RZ = self._ALU.operate(operand1, operand2, currALU_select)

        print("PCs, INCs", self.PC_select[self._currOperationId], self.INC_select[self._currOperationId])
        #control determining part
        if self._neumonic == 'auipc':
            self._RZ = self._IAG.AUIPC(self._imm)

        print("PC, PC_temp :",self._IAG.getPC(), self._IAG.getPC_Temp())
        self._IAG.muxPC(self.PC_select[self._currOperationId], self._RA)
        self._IAG.updatePC(1)
        print("neumonic, ALU_res",self._neumonic, self._RZ)
        if self._neumonic in ['beq', 'bne', 'blt', 'bge'] and self._RZ == "0"*7+'1':
            self._IAG.muxINC(1, self._imm)
        else:
            self._IAG.muxINC(self.INC_select[self._currOperationId], self._imm)
        self._IAG.adder()
        self._IAG.muxPC(0, self._RA)
        self._IAG.updatePC(1)
        print("PC, PC_temp :",self._IAG.getPC(), self._IAG.getPC_Temp())

        
    def memoryAccess(self):
        currMemoryEnable =self._memoryEnable[self._currOperationId]
        #print("mem ",currMemoryEnable)
        size = 0
        if self._neumonic[1]=='b':
            size = 0
        elif self._neumonic[1]=='h':
            size = 1
        elif self._neumonic[1]=='w':
            size = 2

        if(currMemoryEnable == 1):                             #load
            self._PMI.setMAR(self._RZ)
            self._PMI.getData(size)

        elif(currMemoryEnable == 2):                           #store
            self._PMI.setMAR(self._RZ)
            self._PMI.setMDR(self._RM)
            self._PMI.storeData(size)
        
    def registerUpdate(self):
        #lui, done
        #beq, done
        #t
        self._RY = self.muxY(self._muxY[self._currOperationId])
        #print(self._muxY[self._currOperationId])
        if self.WriteEnable[self._currOperationId]:
            self._registerFile.set_register(self._rd,self._RY)
        print("RD: RY:", self._rd, self._RY)
        #reset
        self._RA = '0'*8
        self._RB = '0'*8

if __name__=='__main__':
    ll = [int(x) for x in list(df2_main['muxB'].dropna())]
    run = Processor()
    run.load_mc()
    run.fetch()
    print(run._IR)
    run.decode()
    print(run._currOperationId)
    print(run._neumonic)
    run.execute()
    run.memoryAccess()
    run.registerUpdate()
    run._registerFile.print_registers()
    run._PMI.print_memory()
