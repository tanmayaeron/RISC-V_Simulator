import os
from input import ReadFile
import memory
import IAG
import ALU

fileName = 'test1.mc'
folderPath = os.getcwd()
filepath = os.path.join(folderPath, 'test', fileName)
print(filepath)

fileReader = ReadFile()
fileReader.read_mc(filepath, PMI)

class Processor:
    
    cycles = 0

    def __init__(self):
        self._PMI = memory.PMI()
        self._ALU = ALU.ALU()
        self._IAG = IAG.IAG()
        self._IR = '0'*8
        self.
        

while(1):
    simulator.runInstruction()


