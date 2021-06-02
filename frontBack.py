from simulator import Processor
from helperFunctions import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import json
import os
import glob, sys
class frontBackEndInteraction:
    def __init__(self, startDetails):
        self.processor = Processor(startDetails)
        self.directoryPath = startDetails[0]
        
    def load(self, filePath, isMC = 1):
        self.processor.load(filePath,isMC)
        
    def runProgram(self, filePath, knobsL, isMC = 1):
        
        if(not knobsL[0]):
            self.processor.load(filePath,isMC)
            while(self.step(0)):
                continue
            
        else:
            self.processor.load(filePath, isMC)
            self.processor.pipelinedHelper(knobsL[1], knobsL[2], knobsL[3], knobsL[4], knobsL[5])
            sys.stderr.write(str(knobsL))
            while(self.step(1)):
                continue
            
            self.processor.printStat()
            
        self.processor.printRegisters()
        self.processor.printData()
        self.processor.getCaches()
        
    def step(self, isPipeline):
        if(isPipeline):
            a = self.processor.pipelined()
        else:
            a = self.processor.nonPipelined()
        if(a == 0):
            return 0
        else:
            return 1
                
        
        
        
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
        del self.processor
        self.processor = Processor([self.directoryPath]+initialiseControls)
        # del self.processor
        # self.processor = Processor(self.directoryPath)
        
         
    def parseData(self, path):
        with open(path) as f:
            data = [json.loads(line.replace("'", "\"")) for line in f]
        return data
    

    def clearData(self, path):
        file = open(path, 'w')
        file.close()
