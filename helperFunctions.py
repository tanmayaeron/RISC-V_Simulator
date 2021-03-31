class HelperFunctions:
    def __init__():
        pass
    
    def hexToDec(self, operand):
    
        if (int(operand[0], 16) > 7):
            operand = int(operand, 16)
            operand -= 1 << 32
            return operand
        return int(operand, 16)

    def decToHex(self, operand):
        if(operand >= 0):
            return '{:08x}'.format(operand)[-8:]
        else:
            operand = (1 << 32) - (abs(operand))
            return '{:08x}'.format(operand)[-8:]
        
    def extendimmediate(immediate,isSignExtended = True):
    
    """
    if isSignExtended is True, immediate is sign extended
    else immediate is padded with "0"
    """

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
        generatedHexNumber = "{0:08x}".format(int(operand,2))               #operand not taken as twos complement 
        return generatedBinaryNumber
            