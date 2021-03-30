def extendimmediate(immediate,isSignExtended = True):

    """
    if isSignExtended is True, immediate is sign extended
    else immediate is padded with "0"
    """"
    
    if isSignExtended == True and immediate[0]=='1':
        immediate = "1"*32+immediate
        immediate = immediate[-32:]
    else:
        immediate = "0"*32+immediate
        immediate = immediate[-32:]
        
        
def hexToBin(operand):
    generatedBinaryNumber = "{0:08b}".format(int(operand, 16))
    return generatedBinaryNumber
    
def binToHex(operand):
    generatedHexNumber = "{0:08x}".format(int(operand,2))
    return generatedBinaryNumber
        
        
class IAG:

    '''
    data:

    method:
    '''
    def __init__(self):
        self._PC = "0"*8
        self._PC_Temp = "0"*8
        self.__constantoffset = "0"*7+"4"                        #is also kept as 32 bit binary to keep uniformity
        self._imm = "0"*8                                       #isSignExtended extended to 32bits, stored as binary
        self._RA = "0"*8
        self.output_adder = "0"*8
        self.inputB_adder = "0"*8
        self.output_muxPC = "0"*8
        

    def getPC(self):
        return self._PC
        
    def getPC_Temp(self):
        return self._PC_Temp
        
    def muxPC(self,PC_select): 
        if PC_select == 0 :
            self.output_muxPC =  self._RA
        else:
            self.output_muxPC = self.output_adder
            
    def muxINC(self,INC_select):
        if INC_select==0 :
            return self.__constantoffset
        else:
            return self._imm

    def adder(self):
        operandA = int(self._PC,16)
        operandB = int(inputB_adder,16)
        output = operandA+operandB
        self.output_adder = '{:08x}'.format(output)[-8:]
        
    def updatePC(self,PC_enable):
        if PC_enable == 1 :
            self._PC = self.output_muxPC

    def updatePC_temp(self):
        pass


    
    
        