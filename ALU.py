from register import RegisterFile
from bitstring import BitArray
from bitstring import Bits


# increment PC += 4 by default


class ALU:

    """
    PC needs to be dealt with separately
    RM, RY, RZ are temporary registers
    all functions deal and pass integers
    """

    def __init__(self):
        self.RA = 0  # set by decode
        self.RB = 0  # set by decode
        self.imm = 0  # set by decode
        self.RM = 0
        self.RY = 0
        self.RZ = 0
        self.PC_temp = 0
        self.muxB = 0  # set by decode

    def add(self):
        if(self.muxB == 0):
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
        if(self.muxB == 0):
            self.RZ = self.RA & self.RB
        else:
            self.RZ = self.RA & self.imm

    def _or(self):
        if(self.muxB == 0):
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
        # execute increments PC by 4
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
        # imm is assumed to be shifted by 12
        self.RZ = self.PC - 4 + self.imm

    def lui(self):
        # imm is assumed to be shifted by 12
        self.add()

    def jal(self):
        self.PC_temp = self.PC
        self.PC = self.PC - 4 + self.imm

    def jalr(self):
        self.PC_temp = self.PC
        self.PC = self.RA + self.imm

    def lbhw(self):
        self.add()

    def sbhw(self):
        self.RM = self.RB
        self.add()
