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
        self._numOfSupportedOperations = 15
        self._lookup = [self._add, self._sub, self._mul, self._div, self._rem, self._xor, self._and, self._or, self._sll, self._srl, self._sra, self._eq, self._ne, self._ge, self._lt]
        self._control = 0
        self._output = 0

    def _hexToDec(self, operand):
        decValue = int(operand, 16)
        return decValue
    def _decToHex(self, operand):
        hexValue = '{:08x}'.format(operand)
        return hexValue
    
    def operate(self, operand1, operand2, control):
        self._input1 = self._hexToDec(operand1)
        self._input2 = self._hexToDec(operand2)
        if(control < self._numOfSupportedOperations):
            self._control = control
        else:
            print("unsupported operation")
        self._lookup[self._control]()
        self._output = self._decToHex(self._output)
        return self._output
    
    
        
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

alu = ALU()
a = "00000023"
b = "00000014"
print(alu.operate(a, b, 0))
