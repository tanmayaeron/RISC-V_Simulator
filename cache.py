import math
from helperFunctions import *
import json
import os
from queue import Queue
from random import random, randrange, randint

def make_length(data, length):
    data = "0"*length+data
    return data[-length:]

class Cache:

    def __init__(self, cache_size, block_size, ways, blockReplacementPolicyType):
        self.initialise(cache_size, block_size, ways, blockReplacementPolicyType)
        
    def initialise(self, cache_size, block_size, ways, blockReplacementPolicyType):
        self.choice = blockReplacementPolicyType
        #0->LRU 1->FIFO 2->Random 3->NRU
        self.cache_size = cache_size
        self.block_size = block_size
        self.ways = ways #number of ways
        self._cache = [] #list for now
        self._LRU = []
        self._FIFO = []
        self._Random = []
        self._NRU=[]
        self._missDetails = []
        self.index = int(math.log2(cache_size/block_size)) - int(math.log2(ways)) #index bits
        self.BO = int(math.log2(block_size)) #block offset bits
        self.tag = 32 - self.index - self.BO #tag bits
        self.miss = 0
        self.hit = 0
        self.cacheDetails = {"Index":-1, "Set":-1, "isMiss":-1, "Victim":-1}
        self.total_accesses = 0
        self.BlockTracker = {}
        self.coldMiss = 0
        self.conflictMiss = 0
        self.capacityMiss = 0
        self.totalBlocks = cache_size/block_size
        self.createCache()
        self.initialiseLRU()
        self.initialiseFIFO()
        self.initialiseRandom()
        self.initialiseNRU()

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


    def initialiseFIFO(self):
        for ind in range(2**self.index):
            self._FIFO.append([])
            for blocks in range(self.ways):
                self._FIFO[ind].append([0,0,0])   
        """
        self._FIFO[i] contains [0,0,0]
        in [0,0,0] the first element represents if the element is present or not
        Here the priority is given according to the elements present in the FIFO queue
        the last element contains tag
        """
    
    def initialiseRandom(self):
        for ind in range(2**self.index):
            self._Random.append([])
            for blocks in range(self.ways):
                self._Random[ind].append([0,0,0]) 
        """
        self._FIFO[i] contains [0,0,0]
        in [0,0,0] the first element represents if the element is present or not
        the middle element is useless.
        the last element contains tag
        """
    
    def initialiseNRU(self):
        for ind in range(2**self.index):
            self._NRU.append([])
            for blocks in range(self.ways):
                self._NRU[ind].append([0,0,0]) 

        """
        self._FIFO[i] contains [0,0,0]
        in [0,0,0] the first element represents if the element is present or not
        
        the last element contains tag
        """
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

    def updateFIFO(self,tag,index):
        # first we find if the tag is present in the FIFO or not
        for i in range(self.ways):
            if self._FIFO[index][i][0] == 1 and self._FIFO[index][i][2] == tag:
                
                
                return -1

        # then we find if there is empty space in the queue or not
        for i in range(self.ways):
            if self._FIFO[index][i][0] == 0:
                self._FIFO[index][i][0] = 1
                
                self._FIFO[index][i][2] = tag
                
                return -1 

        # if there is no empty space and the tag is not present means we have to delete victim block 
        # here the victim is the first block as it appeared first therefore victim = 0
        victim = 0
        
                 
        # we store the oldTag for cache use
        oldTag = self._FIFO[index][victim][2]

        #we pop the victim(first) block from the self._FIFO using pop(0)
        self._FIFO[index].pop(victim)
        # now we append the new block using append 
        # [1,0,tag] is appended
        self._FIFO[index].append([1,0,tag])
        
        
    
        self._missDetails.append((self.miss+1, self._cache[index][oldTag]))
        return (0, oldTag)  
    

    def updateRandom(self, tag, index):
        # first we find if the tag is present in the Random or not

        for i in range(self.ways):
            if self._Random[index][i][0] == 1 and self._Random[index][i][2] == tag:
                
                
                return -1
    
        # then we find if there is empty space in the Random or not

        for i in range(self.ways):
            if self._Random[index][i][0] == 0:
                self._Random[index][i][0] = 1
                
                self._Random[index][i][2] = tag
                
                return -1 
        # if there is no empty space and the tag is not present means we have to delete victim block 
        # here the victim block will be the random block between 0 and sel.ways-1
        victim = randrange(self.ways) # generates a number between [0,self.ways-1]
        # equivalent to randint(self.ways-1)

        # we store the oldTag for cache use
        oldTag = self._Random[index][victim][2]

        # self._Random[index].pop(victim)
        # # now we append the new block using append 
        # # [1,0,tag] is appended
        # self._Random[index].append([1,0,tag])
        
        self._Random[index][victim]=[1,0,tag]#the randomly selected victim blocked is replaced by new tag
    
        self._missDetails.append((self.miss+1, self._cache[index][oldTag]))
        return (0, oldTag)

    def updateNRU(self, tag, index):

        for i in range(self.ways):
            if self._NRU[index][i][0] == 1 and self._NRU[index][i][2] == tag:
                self._NRU[index][i][1] += 1
                return -1
        
        for i in range(self.ways):
            if self._NRU[index][i][0] == 0:
                self._NRU[index][i][0] = 1
                self._NRU[index][i][1] = 1
                self._NRU[index][i][2] = tag
                return -1

        minS = 1e9
        victim = 0
        for i in range(self.ways):
            if(minS > self._NRU[index][i][1]):
                minS = self._NRU[index][i][1]
                victim = i
                 
        self._NRU[index][victim][0] = 1
        self._NRU[index][victim][1] = 1
        oldTag = self._NRU[index][victim][2]
        self._NRU[index][victim][2] = tag
            
        self._missDetails.append((self.miss+1, self._cache[index][oldTag]))
        return (0, oldTag)
        
        
    def write(self, address, memory_obj, data, size, control):
        self.total_accesses += 1
        tag, index, BO = self.address_break(address)
        oldindex=index
        index = int(index, 2)
        BO = int(BO, 2)

        isVictim = -1
        if(self.choice == 0):
            isVictim = self.updateLRU(tag, index)
        elif(self.choice == 1):
            isVictim = self.updateFIFO(tag, index)
        elif(self.choice == 2):
            isVictim = self.updateRandom(tag, index)
        else:
            isVictim = self.updateNRU(tag, index)
        
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
            if (tag, index) not in self.BlockTracker:
                self.coldMiss += 1
            else:
                if(len(self._cache) == self.totalBlocks):
                    self.capacityMiss += 1
                else:
                    self.conflictMiss += 1
            
            self.cacheDetails["isMiss"] = "T"
            self.miss+=1
            if(isVictim == -1):
                self._cache[index][tag] = data2
            else:
                if(isVictim != -1):
                    self.cacheDetails["Victim"] = {"tag": isVictim[1] , "data":self._cache[index][isVictim[1]]}
                del self._cache[index][isVictim[1]]
                self._cache[index][tag] = data2
            self.BlockTracker[(tag, index)] = True
        
        
    def read(self, address, memory_obj, size, control):
        self.total_accesses += 1
        tag, index, BO = self.address_break(address)
        oldindex = index
        index = int(index, 2)
        BO = int(BO, 2)

        isVictim = -1
        if(self.choice == 0):
            isVictim = self.updateLRU(tag, index)
        elif(self.choice == 1):
            isVictim = self.updateFIFO(tag, index)
        elif(self.choice == 2):
            isVictim = self.updateRandom(tag, index)
        else:
            isVictim = self.updateNRU(tag, index)

        # isVictim = self.updateLRU(tag, index)

        self.cacheDetails["Index"] = index
        self.cacheDetails["Set"] = self._cache[index]
        
        # if(isVictim != -1):
        #     self.cacheDetails["Victim"] = {"tag": isVictim[1] , "data":self._cache[index][isVictim[1]]}
        
        if(self.checkCache(index, tag)):
            self.cacheDetails["isMiss"] = "F"
            self.hit += 1
            return self.slice(2*BO,2*BO+(2**(size+1)),index,tag)
        else:
            if (tag, index) not in self.BlockTracker:
                self.coldMiss += 1
            else:
                if(len(self._cache) == self.totalBlocks):
                    self.capacityMiss += 1
                else:
                    self.conflictMiss += 1
            
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
            self.BlockTracker[(tag, index)] = True
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

