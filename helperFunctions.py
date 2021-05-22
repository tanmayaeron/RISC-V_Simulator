def hexToDec(operand):

    if (int(operand[0], 16) > 7):
        operand = int(operand, 16)
        operand -= 1 << 32
        return operand
    return int(operand, 16)

def decToHex(operand):
    if(operand >= 0):
        return '{:08x}'.format(operand)[-8:]
    else:
        operand = (1 << 32) - (abs(operand))
        return '{:08x}'.format(operand)[-8:]
    
def decToBin(operand):
    if(operand >= 0):
        return '{:032b}'.format(operand)[-32:]
    else:
        operand = (1 << 32) - (abs(operand))
        return '{:032b}'.format(operand)[-32:]

def extendImmediate(immediate,isSignExtended = True):

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
    return immediate

def hexToBin(operand):
    generatedBinaryNumber = "{0:08b}".format(int(operand, 16))
    return generatedBinaryNumber

def binToHex(operand):
    generatedHexNumber = "{0:08x}".format(int(operand,2))               #operand not taken as twos complement
    return generatedHexNumber


def getAltNameOfRegister():
    alt_name = ["zero", "ra", "sp", "gp", "tp", "t0", "t1", "t2", "s0/fp", "s1", "a0", "a1", "a2", "a3",
                          "a4", "a5", "a6", "a7", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9", "s10", "s11", "t3", "t4", "t5", "t6"]
    
    return alt_name