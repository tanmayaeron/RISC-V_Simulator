from simulator import Processor
from helperFunctions import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import json
import os
import glob
class frontBackEndInteraction:
    def __init__(self, startDetails):
        self.processor = Processor(startDetails)
        self.directoryPath = startDetails[0]
        
    def runProgram(self, filePath, knobsL):
        if(not knobsL[0]):
            self.processor.load_mc(filePath)
            self.processor.nonPipelined(knobsL[2])
            
        else:
            self.processor.load_mc(filePath)
            self.processor.pipelined(knobsL[1], knobsL[2], knobsL[3], knobsL[4], knobsL[5])
            self.processor.printStat()
            
        self.processor.printRegisters()
        self.processor.printData()
        self.processor.getCaches()
        
        
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

    def reset(self, initialiseControls):
        self.clearData(os.path.join(self.directoryPath, "generated", "outputLog.txt"))
        self.clearData(os.path.join(self.directoryPath, "generated", "forwarding.txt"))
        self.clearData(os.path.join(self.directoryPath, "generated", "memory.txt"))
        self.clearData(os.path.join(self.directoryPath, "generated", "registers.txt"))
        self.clearData(os.path.join(self.directoryPath, "generated", "buffer.txt"))
        self.clearData(os.path.join(self.directoryPath, "generated", "stats.txt"))
        self.clearData(os.path.join(self.directoryPath, "generated", "InstructionCache.txt"))
        self.clearData(os.path.join(self.directoryPath, "generated", "DataCache.txt"))
        self.clearData(os.path.join(self.directoryPath, "generated", "CacheInfo.txt"))
        files = glob.glob(os.path.join(self.directoryPath, "generated", "Buffer Snapshot", "*"))
        for f in files:
            os.remove(f)
        files = glob.glob(os.path.join(self.directoryPath, "generated", "Register Snapshots", "*"))
        for f in files:
            os.remove(f)
        self.processor.reset(initialiseControls)
        # del self.processor
        # self.processor = Processor(self.directoryPath)
        
         
    def parseData(self, path):
        with open(path) as f:
            data = [json.loads(line.replace("'", "\"")) for line in f]
        return data
    

    def clearData(self, path):
        file = open(path, 'w')
        file.close()
