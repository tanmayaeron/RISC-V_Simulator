class CU:
    def __init__(self, k1, k2):
        self.k1 = k1
        self.k2 = k2
        
    def control(self):
        
        
    # FF non pipeline
    # TF pipeline w/0 forward
    # TT pipline w forward
    
    def one(self):
        self.processor.load_mc(filePath)
        while True:
            self.processor.fetch()
            if self.processor.getIR() == '0'*8:
                break
            self.processor.decode()
            self.processor.execute()
            self.processor.memoryAccess()
            self.processor.registerUpdate()
        self.processor.printRegisters()
        self.processor.printData()
        
    def stall():
        return 1
        
    def two(self):
        isStall = 0
        
        watchArray = [1, 0, 0, 0, 0]
        callArray = [self.processor.fetch, self.processor.decode,self.processor.execute,self.processor.memoryAccess,self.processor.registerUpdate]
        if(isStall):
            self.stall()
            
        else:
            for i in reversed(range(5)):
                if(watchArray[i] == 0):
                    continue
                else:
                    callArray[i]()
                    
                    
                    
                


            