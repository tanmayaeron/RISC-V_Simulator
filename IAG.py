from helperFunctions import HelperFunctions
        
class IAG(HelperFunctions):

    '''
    data:

    method:
    '''
    def __init__(self):
        self._PC = "0"*8
        self._PC_Temp = "0"*8
        self.__constantoffset = "0"*7+"4"                        #is also kept as 32 bit binary to keep uniformity                                    #isSignExtended extended to 32bits, stored as binary
        self.output_adder = "0"*8
        self.inputB_adder = "0"*8
        self.output_muxPC = "0"*8
        

    def getPC(self):
        return self._PC
        
    def getPC_Temp(self):
        return self._PC_Temp
        
    def muxPC(self,PC_select, RA): 
        if PC_select == 1 :
            self.output_muxPC =  RA
        else:
            self.output_muxPC = self.output_adder
            
    def muxINC(self, INC_select, S_select, imm, RZ):
        if(S_select == 1):
            INC_select = int(RZ[-1], 16)%2
            
        if INC_select==0 :
            self.inputB_adder = self.__constantoffset
        else:
            self.inputB_adder = imm

    def adder(self):
        operandA = int(self._PC,16)
        operandB = int(self.inputB_adder,16)
        output = operandA+operandB
        self.output_adder = '{:08x}'.format(output)[-8:]
        
    def updatePC(self,PC_enable):
        if PC_enable == 1 :
            self._PC = self.output_muxPC

    def updatePC_temp(self):
        PC = int(self._PC,16)
        PC+=4
        self._PC_Temp = '{:08x}'.format(PC)[-8:]

    def AUIPC(self, imm): #this function is jugaad
        PC = int(self._PC,16)
        PC += self.hexToDec(imm)
        print("AUIPC", '{:08x}'.format(PC)[-8:])
        return '{:08x}'.format(PC)[-8:]
