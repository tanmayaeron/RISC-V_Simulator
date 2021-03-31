import pandas as pd
from ALU_re import alu_interface
from register import RegisterFile
from bitstring import BitArray
from bitstring import Bits
from decode import identify
from helperFunctions import HelperFunctions
# we will use register objects here

df_main = pd.read_csv('instructions.csv')

def int_to_hex(self, a):
    b = 0x100000000
    if a >= 0:
        a = '{:08x}'.format(a)[-8:]
    else:
        a += b
        a = hex(a)
        a = a[2:]
        return a

def twos_complement


class Processor:

    cycle = 0

    def __init__(self):
        self._PMI = memory.PMI()
        self._ALU = ALU.ALU()
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
        self._ALU_select = []
        self._muxB = []
        self._muxY = []
        self._memoryEnable = []
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
        self._currOperationId = info_code["id"]
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
            self._rd = 0
            
        try:
            immediate = twos_complement(inf_code['immediate'])
            self._imm = {'.08x'}.format(immediate)[-8:]
        except:
            pass

    def execute(self):
        currALU_select = self._ALU_select[self._currOperationId]
        currMuxB = self._muxB[self._currOperationId]
        operand1 = self._RA
        operand2 = self.muxB(currMuxB)
        self._RZ = ALU.operate(operand1, operand2, currALU_select)
        
    def memoryAccess(self):
        currMemoryEnable =self._memoryEnable[self._currOperationId]
        size = 0
        if self._neumonic[1]=='b':
            size = 0
        elif self._neumonic[1]=='h':
            size = 1
        elif self._neumonic[1]=='w':
            size = 2

        if(currMemoryEnable == 1):                             #load
            self._PMI.setMAR(self._RZ)
            self.getData(size)

        elif(currMemoryEnable == 2):                           #store
            self._PMI.setMAR(self._RZ)
            self._PMI.setMDR(self._RM)
            self._PMI.storeData(size)
        
    def registerUpdate(self):
        self._RY = self.muxY(self._muxY[self._currOperationId])
        self._registerFile.set_register(self._rd,self._RY)

if __name__=='__main__':
    execute_obj = Execute()
    execute_obj.fetch()
