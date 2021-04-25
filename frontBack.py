from simulator import Processor
from helperFunctions import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import json
class frontBackEndInteraction:
    def __init__(self, directoryPath):
        self.processor = Processor(directoryPath)
        
    def runProgram(self, filePath):
        self.processor.load_mc(filePath)
        self.processor.runPipelining_False_for_Forwarding(True)
        # while True:
        #     self.processor.fetch()
        #     if self.processor.getIR() == '0'*8:
        #         break
        #     self.processor.decode()
        #     self.processor.execute()
        #     self.processor.memoryAccess()
        #     self.processor.registerUpdate()
        self.processor.printRegisters()
        self.processor.printData()
        self.processor.printStat()
        # return "Compiled"
        
        
    def getRegisterSnapshot(self):
        l = self.processor.getRegisters()
        return l
    
    def getMemorySnapshot(self, address):
        mem = self.processor.getData()
        l=[]
        address_in_dec = hexToDec(address)
        temp = address_in_dec%4
        address_in_hex = "0" * 8 + hex(address_in_dec -temp)[2:]
        address_in_dec = hexToDec(address_in_hex)
        for i in range(40):
            address_in_hex = "0" * 8 + hex(address_in_dec + i)[2:]
            address_in_hex = address_in_hex[-8:]
            if i%4==0:
                l.append([])
                l[-1].append("0x"+address_in_hex)
            l[-1].append(mem[address_in_hex])
        return l

    def reset(self):
        self.processor.reset()
         
    def parseData(self):
        with open('generated/outputLog.txt') as f:
            data = [json.loads(line) for line in f]
        return data
