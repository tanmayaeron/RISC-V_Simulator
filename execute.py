

class Execute:
    #indenttation of 4 space
    def __init__(self):
        self.PC = 0
        self.IR = 0
        self.REG = [0]*32

    def explanation(self, obj):
        #obj.code defaultdict from decimal to decimal
        #obj.code[0] 1st line
        #obj.code[4] 2nd line pc+=4
        #all integers
        pass;
    def runRISCV(self, obj):
        while self.PC in obj.code:
            self.fetch(obj)
            self.decode()

    def fetch(self, obj):
        self.IR = obj.code[self.PC]
        self.PC += 4
            # because 0 4 8 ... are stored
    
    def checkFormat(self):
        return 
        pass
    def decode(self):
        # input is integer
        #self.IR is the instruction to be decoded

        pass
    

    
        
execute=Execute()
