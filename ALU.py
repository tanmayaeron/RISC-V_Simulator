from helperFunctions import *
class ALU:

    """
    input1 : first input
    input2 : second input
    control : operation select

    ALU will recieve data in hexadecimal format, to call ALU one needs to call operate function with
    """

    def __init__(self):
        self._input1 = 0
        self._input2 = 0
        self._numOfSupportedOperations = 17
        self._lookup = [self._add, self._sub, self._mul, self._div, self._rem, self._xor, self._and,
                        self._or, self._sll, self._srl, self._sra, self._eq, self._ne, self._ge, self._lt, self._selectA, self._selectB]
        self._control = 0
        self._output = 0

    def operate(self, operand1, operand2, control):
        self._input1 = hexToDec(operand1)
        self._input2 = hexToDec(operand2)
        if(control < self._numOfSupportedOperations):
            self._control = control
            self._lookup[self._control]()
            self._output = decToHex(self._output)
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
            
            
    def _selectA(self):
        self._output = self._input1

    def _selectB(self):
        self._output = self._input2


