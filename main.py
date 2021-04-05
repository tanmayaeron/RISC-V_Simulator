from simulator import Processor
import os

pathtofolder = os.getcwd()
processor = Processor(pathtofolder)
processor.load_mc("bubble.mc")

while True:
    processor.fetch()
    if processor.getIR() == '0'*8:
        break
    processor.decode()
    processor.execute()
    processor.memoryAccess()
    processor.registerUpdate()
    

processor.printRegisters()
processor.printData()
