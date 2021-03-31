import pandas as pd
from ALU_re import alu_interface
from register import RegisterFile
from bitstring import BitArray
from bitstring import Bits
from decode import identify

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
        self._RZ = '0'*8
        self._RM = '0'*8
        self._RY = '0'*8
        self._imm = '0'*8

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
        try:
            pass
        except:
            pass
        try:
            pass
        except:
            pass

    def execute(self):
        pass

    def memoryAccess(self):
        pass

    def registerUpdate(self):
        pass


    """
    def twos_complement(self, a):
        return Bits(bin=a).int

    def R_format(self, fields):

        instruction = fields['neumonic']
        rs1 = int(fields['rs1'], 2)
        rs2 = int(fields['rs2'], 2)
        rd = int(fields['rd'], 2)
        self.obj.RA = self.registers.get_register(rs1)
        self.obj.RB = self.registers.get_register(rs2)

        self.obj.muxB = 0 # muxB and muxY = 0
        self.obj.muxY = 0
        if instruction == "add":
            self.obj.add()
        elif instruction == "and":
            self.obj._and()
        elif instruction == "or":
            self.obj._or()
        elif instruction == "sll":
            self.obj.sll()
        elif instruction == "slt":
            self.obj.slt()
        elif instruction == "sra":
            self.obj.sra()
        elif instruction == "srl":
            self.obj.srl()
        elif instruction == "sub":
            self.obj.sub()
        elif instruction == "xor":
            self.obj.xor()
        elif instruction == "mul":
            self.obj.mul()
        elif instruction == "div":
            self.obj.div()
        elif instruction == "rem":
            self.obj.rem()

    def I_format(self, fields):
        instruction = fields['neumonic']
        rs1 = int(fields['rs1'], 2)
        imm = self.twos_complement(fields['immediate'])
        rd = int(fields['rd'], 2)

        self.obj.imm = imm
        self.obj.RA = self.registers.get_register(rs1) #hex string (8 character)
        self.obj.imm = self.int_to_hex(imm) #hex string (8 character)

        self.obj.muxB = 1
        self.obj.muxY = 0
        if instruction == "addi":
            self.obj.add()
            print(self.obj.RZ)
        elif instruction == "ori":
            self.obj._or()
            print(self.obj.RZ)
        elif instruction == "andi":
            self.obj._and()
            print(self.obj.RZ)
        elif instruction in ["lb", "lw", "lh"]:
            self.obj.muxY = 1
            self.obj.lbhw()
            print(self.obj.RZ)
        elif instruction == "jalr":
            self.obj.muxY = 2
            self.obj.jalr()
            print(self.obj.PC)

    def S_format(self, fields):

        instruction = fields['neumonic']
        rs1 = int(fields['rs1'], 2)
        rs2 = int(fields['rs2'], 2)
        self.obj.RA = self.registers.get_register(rs1)
        self.obj.RB = self.registers.get_register(rs2)
        imm = self.twos_complement(fields['immediate'])
        self.obj.imm = self.int_to_hex(imm)
        print(self.obj.imm)
        #self.obj.muxB = 1
        self.obj.muxY = 1  # dont care

        if instruction in ["sb", "sh", "sw"]:
            self.obj.sbhw()

        print("location is:", self.obj.RZ)
        print("the value is : ", self.obj.RM)

    def SB_format(self, fields):
        instruction = fields['neumonic']
        rs1 = int(fields['rs1'], 2)
        rs2 = int(fields['rs2'], 2)
        imm = self.twos_complement(fields['immediate'])
        imm *= 2  # to left shift as imm[0] is 0

        self.obj.RA = self.registers.get_register(rs1)
        self.obj.RB = self.registers.get_register(rs2)
        self.obj.imm = self.int_to_hex(imm)

        #print(self.obj.RA, self.obj.RB, self.obj.imm, self.obj.PC)
        self.obj.muxB = 0
        self.obj.muxY = 2
        if instruction == "beq":
            self.obj.beq()
            print(self.obj.PC)
        elif instruction == "bne":
            self.obj.bne()
            print(self.obj.PC)
        elif instruction == "bge":
            self.obj.bge()
            print(self.obj.PC)
        elif instruction == "blt":
            self.obj.blt()
            print(self.obj.PC)

    def U_format(self, fields):
        instruction = fields['neumonic']
        rd = int(fields['rd'], 2)
        imm = self.twos_complement(fields['immediate'])
        imm = imm*2**12  # left shifting 12 bits
        self.obj.imm = self.int_to_hex(imm)
        self.obj.muxB = 0
        self.obj.muxY = 0
        if instruction == "lui":
            self.obj.lui()
        elif instruction == "auipc":
            self.obj.muxY = 2
            self.obj.auipc()
            print(self.obj.RZ)

    def UJ_format(self, fields):
        instruction = fields['neumonic']
        rd = int(fields['rd'], 2)
        imm = self.twos_complement(fields['immediate'])
        imm *= 2  # to left shift as imm[0] is 0
        self.obj.imm = self.int_to_hex(imm)
        self.obj.muxB = 0
        self.obj.muxY = 2
        if instruction == "jal":
            self.obj.jal()
            print(self.obj.PC_temp)
            print(self.obj.PC)

    def alu_caller(self, machine_code):

        fields = self.decode(machine_code)

        format = fields['format']
        print(fields)
        if format == 0:
            print("not found")
            return
        if format == 'R':
            self.R_format(fields)
        elif format == 'I':
            self.I_format(fields)
        elif format == "S":
            self.obj.muxY = 0
            self.S_format(fields)
        elif format == "SB":
            self.obj.muxY = 2  # pc+=imm
            self.SB_format(fields)
        elif format == "U":
            self.obj.muxY = 0  # doubt
            self.U_format(fields)
        else:
            self.obj.muxY = 2
            self.UJ_format(fields)
    """

    def memoryAccess(self):
        pass

    def writeBack(self):
        pass

if __name__=='__main__':
    execute_obj = Execute()
    execute_obj.fetch()
