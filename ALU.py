from register import RegisterFile
from bitstring import BitArray
from bitstring import Bits

obj = RegisterFile()
obj2 = ALU()
obj2.add()

class ALU:

    """
    We are passing obj of RegisterFile type as obj
    RM, RY, RZ are temporary registers
    all functions deal and pass integers

    """ 

    def __init__(self):
        self.RA = 0 #set by decode
        self.RB = 0 #set by decode
        self.imm = 0 #set by decode
        self.RM = 0
        self.RY = 0
        self.RZ = 0
        self.muxB = 0 #set by decode

    def add(self):
        if(muxB == 0):
            self.RZ = self.RA + self.RB
        else:
            self.RZ = self.RA + self.imm
    
    def sub(self):
        self.RZ = self.RA - self.RB
    
    def mul(self):
        self.RZ = self.RA * self.RB

    def div(self):
        self.RZ = self.RA // self.RB

    def rem(self):
        self.RZ = self.RA % self.RB

    def xor(self):
        self.RZ = self.RA ^ self.RB
    
    def _and(self):
        if(muxB == 0):
            self.RZ = self.RA & self.RB
        else:
            self.RZ = self.RA & self.imm
    
    def _or(self):
        if(muxB == 0):
            self.RZ = self.RA | self.RB
        else:
            self.RZ = self.RA | self.imm

    def sll(self):
        self.RZ = self.RA << self.RB
    
    def sra(self):
        self.RZ = self.RA >> self.RB

    def srl(self):
        self.RA &= 0xffffffff
        self.RZ = self.RA >> self.RB

    def slt(self):
        if(self.RA < self.RB):
            self.RZ = 1
        else:
            self.RZ = 0
    
    def beq(self):
        #execute increments PC by 4
        if(self.RA == self.RB):
            self.PC = self.PC - 4 + self.imm
    
    def bne(self):
        if(self.RA != self.RB):
            self.PC = self.PC - 4 + self.imm
    
    def bge(self):
        if(self.RA >= self.RB):
            self.PC = self.PC - 4 + self.imm
    
    def blt(self):
        if(self.RA < self.RB):
            self.PC = self.PC - 4 + self.imm

    def auipc(self):
        self.RZ = self.PC - 4 + self.imm
    
    def lui(self):
        pass