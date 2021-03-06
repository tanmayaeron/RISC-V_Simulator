
















import math
from helperFunctions import *
import json
import os



def make_length(data, length):
    data = "0"*length+data
    return data[-length:]

class Cache:

    def __init__(self, cache_size, block_size, ways):
        self.initialise(cache_size, block_size, ways)
        
    def initialise(self, cache_size, block_size, ways):
        self.cache_size = cache_size
        self.block_size = block_size
        self.ways = ways #number of ways
        self._cache = [] #list for now
        self._LRU = []
        self._missDetails = []
        self.index = int(math.log2(cache_size/block_size)) - int(math.log2(ways)) #index bits
        self.BO = int(math.log2(block_size)) #block offset bits
        self.tag = 32 - self.index - self.BO #tage bits
        self.miss = 0
        self.hit = 0
        self.cacheDetails = {"Index":-1, "Set":-1, "isMiss":-1, "Victim":-1}
        self.total_accesses = 0
        self.createCache()
        self.initialiseLRU()

    def address_break(self, address): #takes the hex string
        #should return binary, returns decimal for now
        address = hexToBin(address)
        address = make_length(address, 32)
        tag = address[:self.tag]
        index = address[self.tag:self.tag+self.index]
        BO = address[-self.BO:]
        return tag, index, BO

    def createCache(self):
        """
            let there be a cache of 8 byte size
            and a block is of size 1 byte
            there will be 8 blocks i.e., 8 dicts, one for each block
            cache = [{}, {}, {}, {}]
        """
        
        for i in range(2**self.index):
            self._cache.append({})

        
    def initialiseLRU(self):
        for ind in range(2**self.index):
            self._LRU.append([])
            for blocks in range(self.ways):
                self._LRU[ind].append([0,0,0])
                
    def checkCache(self, index, tag):
        if tag in self._cache[index]:
            return True
        return False
        
    def updateLRU(self, tag, index):

        for i in range(self.ways):
            if self._LRU[index][i][0] == 1 and self._LRU[index][i][2] == tag:
                self._LRU[index][i][1] = self.ways
                for j in range(self.ways):
                    self._LRU[index][j][1] = max(self._LRU[index][j][1]-1, 0)
                return -1
            
        for i in range(self.ways):
            if self._LRU[index][i][0] == 0:
                self._LRU[index][i][0] = 1
                self._LRU[index][i][1] = self.ways
                self._LRU[index][i][2] = tag
                for j in range(self.ways):
                    self._LRU[index][j][1] = max(self._LRU[index][j][1]-1, 0)
                return -1
            
        minS = 1e9
        victim = 0
        for i in range(self.ways):
            if(minS > self._LRU[index][i][1]):
                minS = self._LRU[index][i][1]
                victim = i
                 
        self._LRU[index][victim][0] = 1
        self._LRU[index][victim][1] = self.ways
        oldTag = self._LRU[index][victim][2]
        self._LRU[index][victim][2] = tag
        for j in range(self.ways):
            self._LRU[index][j][1] = max(self._LRU[index][j][1]-1, 0)
            
        self._missDetails.append((self.miss+1, self._cache[index][oldTag]))
        return (0, oldTag)

    def write(self, address, memory_obj, data, size, control):
        self.total_accesses += 1
        tag, index, BO = self.address_break(address)
        oldindex=index
        index = int(index, 2)
        BO = int(BO, 2)
        isVictim = self.updateLRU(tag, index)
        self.cacheDetails["Index"] = index
        self.cacheDetails["Set"] = self._cache[index]
        
        address2 = tag+oldindex+"0"*self.BO
        address2 = binToHex(address2)
        memory_obj.store_block( address, data, size, control)
        data2=memory_obj.load_block(address2, self.block_size, control)
        if(self.checkCache(index, tag)):
            self.cacheDetails["isMiss"] = "F"
            self.hit+=1
            self._cache[index][tag] = data2
            
        else:
            self.cacheDetails["isMiss"] = "T"
            self.miss+=1
            if(isVictim == -1):
                self._cache[index][tag] = data2
            else:
                if(isVictim != -1):
                    self.cacheDetails["Victim"] = {"tag": isVictim[1] , "data":self._cache[index][isVictim[1]]}
                del self._cache[index][isVictim[1]]
                self._cache[index][tag] = data2
        
        
    def read(self, address, memory_obj, size, control):
        self.total_accesses += 1
        tag, index, BO = self.address_break(address)
        oldindex = index
        index = int(index, 2)
        BO = int(BO, 2)
        isVictim = self.updateLRU(tag, index)
        self.cacheDetails["Index"] = index
        self.cacheDetails["Set"] = self._cache[index]
        # if(isVictim != -1):
        #     self.cacheDetails["Victim"] = {"tag": isVictim[1] , "data":self._cache[index][isVictim[1]]}
        
        if(self.checkCache(index, tag)):
            self.cacheDetails["isMiss"] = "F"
            self.hit += 1
            return self.slice(2*BO,2*BO+(2**(size+1)),index,tag)
        else:
            self.miss += 1
            self.cacheDetails["isMiss"] = "T"
            address2 = tag+oldindex+"0"*self.BO
            address2 = binToHex(address2)
            data = memory_obj.load_block(address2, self.block_size, control)

            if(isVictim == -1):
                self._cache[index][tag] = data  
            else:
                if(isVictim != -1):
                    self.cacheDetails["Victim"] = {"tag": isVictim[1] , "data":self._cache[index][isVictim[1]]}
                del self._cache[index][isVictim[1]]
                self._cache[index][tag] = data
            return self.slice(2*BO,2*BO+(2**(size+1)),index,tag)
            
    def slice(self,start,end,index,tag):
        """
        end-start=len(slicing)
        """
        string=self._cache[index][tag]
        new_str=''
        for i in range(end,start,-2):
            new_str+=string[i-2:i]
        return new_str
    
    def getDetails(self):
        temp = self.cacheDetails
        self.cacheDetails = {"Index":-1, "Set":-1, "isMiss":-1, "Victim":-1}
        return temp
    

        

    
