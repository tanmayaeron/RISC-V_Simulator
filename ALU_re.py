from helperFunctions import HelperFunctions
class ALU(HelperFunctions):

    """
    input1 : first input
    input2 : second input
    control : operation select

    ALU will recieve data in hexadecimal format, to call ALU one needs to call operate function with
    """

    def __init__(self):
        self._input1 = 0
        self._input2 = 0
        self._numOfSupportedOperations = 15
        self._lookup = [self._add, self._sub, self._mul, self._div, self._rem, self._xor, self._and,
                        self._or, self._sll, self._srl, self._sra, self._eq, self._ne, self._ge, self._lt]
        self._control = 0
        self._output = 0


    def operate(self, operand1, operand2, control):
        self._input1 = self.hexToDec(operand1)
        self._input2 = self.hexToDec(operand2)
        if(control < self._numOfSupportedOperations):
            self._control = control
            self._lookup[self._control]()
            self._output = self.decToHex(self._output)
            return self._output
        else:
            print("unsupported operation")
            return 404

    def _add(self):
        self._output = self._input1 + self._input2

    def _sub(self):
        self._output = self._input1 - self._input2

    def _mul(self):
        self._output = self._input1 * self._input2

    def _div(self):
        self._output = self._input1 // self._input2

    def _rem(self):
        self._output = self._input1 % self._input2

    def _xor(self):
        self._output = self._input1 ^ self._input2

    def _and(self):
        self._output = self._input1 & self._input2

    def _or(self):
        self._output = self._input1 | self._input2

    def _sll(self):
        self._output = self._input1 << self._input2

    def _srl(self):
        self._input1 &= 0xffffffff
        self._output = self._input1 >> self._input2

    def _sra(self):
        self._output = self._input1 >> self._input2

    def _eq(self):
        if(self._input1 == self._input2):
            self._output = 1
        else:
            self._output = 0

    def _ne(self):
        if(self._input1 != self._input2):
            self._output = 1
        else:
            self._output = 0

    def _ge(self):
        if(self._input1 >= self._input2):
            self._output = 1
        else:
            self._output = 0

    def _lt(self):
        if(self._input1 < self._input2):
            self._output = 1
        else:
            self._output = 0


class alu_interface:

    """
    PC needs to be dealt with separately
    RM, RY, RZ are temporary registers
    all functions deal and pass integers
    """

    def __init__(self):
        self.RA = "0"*8
        self.RB = "0"*8
        self.imm = "0"*8
        self.RM = "0"*8
        self.RY = "0"*8
        self.RZ = "0"*8
        self.PC_temp = "0"*8
        self.muxB = 0
        self.alu = ALU()
        self.muxY = 0

    def add(self):
        if(self.muxB == 0):
            self.RZ = self.alu.operate(self.RA, self.RB, 0)
        else:
            self.RZ = self.alu.operate(self.RA, self.imm, 0)

    def sub(self):
        self.RZ = self.alu.operate(self.RA, self.RB, 1)
        print(self.RZ)

    def mul(self):
        self.RZ = self.alu.operate(self.RA, self.RB, 2)

    def div(self):
        self.RZ = self.alu.operate(self.RA, self.RB, 3)

    def rem(self):
        self.RZ = self.alu.operate(self.RA, self.RB, 4)

    def xor(self):
        self.RZ = self.alu.operate(self.RA, self.RB, 5)

    def _and(self):
        if(self.muxB == 0):
            self.RZ = self.alu.operate(self.RA, self.RB, 6)
        else:
            self.RZ = self.alu.operate(self.RA, self.imm, 6)
        print(self.RZ)

    def _or(self):
        self.RZ = self.alu.operate(self.RA, self.RB, 7)

    def sll(self):
        self.RZ = self.alu.operate(self.RA, self.RB, 8)

    def srl(self):
        self.RZ = self.alu.operate(self.RA, self.RB, 9)

    def sra(self):
        self.RZ = self.alu.operate(self.RA, self.RB, 10)

    def beq(self):

        # execute increments PC by 4
        if(self.alu.operate(self.RA, self.RB, 11)):
            self.PC = self.PC - 4 + self.imm

    def bne(self):
        if(self.alu.operate(self.RA, self.RB, 12)):
            self.PC = self.PC - 4 + self.imm

    def bge(self):
        if(self.RA >= self.RB):
            self.PC = self.PC - 4 + self.imm

    def blt(self):
        if(self.RA < self.RB):
            self.PC = self.PC - 4 + self.imm

    def slt(self):
        if(self.RA < self.RB):
            self.RZ = 1
        else:
            self.RZ = 0

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


if __name__ == "__main__":
    alu_interface = alu_interface()
    alu_interface.sub()
