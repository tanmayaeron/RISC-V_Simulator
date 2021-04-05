from simulator import Processor

class frontBackEndInteraction:
    def __init__(self, directoryPath):
        self.processor = Processor(directoryPath)
        
    def runProgram(self, filePath):
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
        
        
    def getRegisterSnapshot(self):
        l = self.processor.getRegisters()
        return l
    
    def getMemorySnapshot(self, address):
        l = [[]*4]*10
        return l

    