from collections import defaultdict
from helperFunctions import *
from cache import Cache
import os
def make_length(data, length):
    data = "0"*length+data
    return data[-length:]


class Memory:

    """
    represents memory in default dictionary
    each key value pair is of form byte-address:data(one byte of data)
    keys - address in hex (without 0x) represented as string of fixed size 8
    values - 1 byte of data in hex(without 0x) represented as string of size 2
    memory is defined as array of two
    """

    def __init__(self):
        self.__memory = [defaultdict(lambda: "00"), defaultdict(lambda: "00")]  # only relevant data stored

    def print_memory(self, control = 0):
        print(self.__memory[control])

    def getMemory(self, control =0):
        return self.__memory[control]

    def clearMemory(self):
        for i in range(2):
            self.__memory[i].clear()

    def getMemoryDisplay(self, address, control = 1):
        l = []
        """
        :param address: byte address str of length 8(without 0x)
        :return: 10 words in contiguous location, in hex, str of length 8(without 0x)
        """
        address_in_dec = hexToDec(address)
        data = ""
        for i in reversed(range(40)):
            address_in_hex = "0" * 8 + hex(address_in_dec + i)[2:]
            address_in_hex = address_in_hex[-8:]
            data = self.load_byte(address_in_hex, control)
            l.append(data)
        return l

    def load_byte(self, address, control = 1):
        """
        :param address:byte address str of length 8(without 0x)
        :return:1byte data stored at address, in hex, str of length 2(without 0x)
        """
        address = make_length(address, 8)
        return self.__memory[control][address]

    def load_halfword(self, address, control = 1):
        """
        :param address: byte address str of length 8(without 0x)
        :return: halfword data stored at address, in hex, str of length 4(without 0x)
        """
        address_in_dec = hexToDec(address)
        data = ""
        for i in reversed(range(2)):
            address_in_hex = "0" * 8 + hex(address_in_dec + i)[2:]
            address_in_hex = address_in_hex[-8:]
            data = data + self.load_byte(address_in_hex, control)
        return data

    def load_word(self, address, control = 1):
        """
        :param address: byte address str of length 8(without 0x)
        :return: word data stored at address, in hex, str of length 4(without 0x)
        """
        address_in_dec = hexToDec(address)
        data = ""
        for i in reversed(range(4)):
            address_in_hex = "0" * 8 + hex(address_in_dec + i)[2:]
            address_in_hex = address_in_hex[-8:]
            data = data + self.load_byte(address_in_hex, control)
        return data
    """
    store functions
    :param address: byte address str of length 8(without 0x)
           data: data to be stored at address, str of appropriate size(without 0x)
    """
    
    def load_block(self, address, blockSize, control = 1):
        address_in_dec = hexToDec(address)
        data = ""
        for i in range(blockSize):
            address_in_hex = "0" * 8 + hex(address_in_dec + i)[2:]
            address_in_hex = address_in_hex[-8:]
            data = data + self.load_byte(address_in_hex, control)
        return data
        
    def store_block(self, address, data, Size, control = 1):
        if Size==0:
            self.store_byte(address,data,control)
        elif Size==1:
            self.store_halfword(address,data,control)
        elif Size==2:
            self.store_word(address,data,control)

    def store_byte(self, address, data, control = 1):
        address = make_length(address, 8)
        data = make_length(data, 2)
        self.__memory[control][address] = data

    def store_word(self, address, data, control = 1):
        address = make_length(address, 8)
        data = make_length(data, 8)
        address_in_dec = hexToDec(address)
        for i in range(4):
            address_in_hex = "0" * 8 + hex(address_in_dec + i)[2:]
            address_in_hex = address_in_hex[-8:]
            self.store_byte(address_in_hex, data[6 - 2 * i:8 - 2 * i], control)

    def store_halfword(self, address, data, control = 1):
        address = make_length(address, 8)
        data = make_length(data, 4)
        address_in_dec = hexToDec(address)
        for i in range(2):
            address_in_hex = "0" * 8 + hex(address_in_dec + i)[2:]
            address_in_hex = address_in_hex[-8:]
            self.store_byte(address_in_hex, data[2 - 2 * i:4 - 2 * i], control)


class PMI:
    def __init__(self, cache_size, block_size, ways, blockReplacementPolicyType):
        self.__MDR = ["0"*8, "0"*8]
        self.__MAR = ["0"*8, "0"*8]
        
        self.instantiate(cache_size, block_size, ways, blockReplacementPolicyType)
    def instantiate(self, cache_size, block_size, ways, blockReplacementPolicyType):
        self.__memory = Memory()
        self._instCache = Cache(cache_size[0], block_size[0], ways[0], blockReplacementPolicyType[0])
        self._dataCache = Cache(cache_size[1], block_size[1], ways[1], blockReplacementPolicyType[1])

    def getMDR(self, control = 1):
        return self.__MDR[control]

    def getMAR(self, control = 1):
        return self.__MAR[control]

    def getMemoryDisplay(self, control = 1):
        self.__memory.getMemoryDisplay(control)
    
    def printMemory(self, control=1):
        self.__memory.print_memory(control)

    def setMDR(self, data, control = 1):
        data = make_length(data, 8)
        self.__MDR[control] = data

    def setMAR(self, address, control = 1):
        address = make_length(address, 8)
        if control == 0:
            address_in_dec = hexToDec(address)
            temp = address_in_dec%4
            address = "0" * 8 + hex(address_in_dec -temp)[2:]
        address = make_length(address, 8)
        self.__MAR[control] = address

    def getMemory(self, control = 1):
        return self.__memory.getMemory(control)

    def clearMemory(self):
        self.__memory.clearMemory()
        
    def printCaches(self, datapath):
        file2 = os.path.join(datapath, "generated", 'InstructionCache.txt')
        file2 = open(file2, 'w')
        d = {"Cache":self._instCache._cache, "Total Access":self._instCache.total_accesses, "Miss":self._instCache.miss, "Hit":self._instCache.hit}
        file2.write(str(d))
        file2.close()
        file2 = os.path.join(datapath, "generated", 'DataCache.txt')
        file2 = open(file2, 'w')
        d = {"Cache":self._dataCache._cache, "Total Access":self._dataCache.total_accesses, "Miss":self._dataCache.miss, "Hit":self._dataCache.hit}
        file2.write(str(d))
        file2.close()
        

    def getData(self, size, control = 1):
        """
        size : 0 - byte
               1 - halfword
               2 - word
        """

        
        if(control == 0):
            data = self._instCache.read(self.getMAR(0), self.__memory, size, control)
        else:
            data = self._dataCache.read(self.getMAR(1), self.__memory, size, control)
            
        data = make_length(data, 8)
        self.__MDR[control] = data

    def storeData(self, size, control = 1):

        
        if(control == 0):
            self._instCache.write(self.__MAR[control], self.__memory, self.__MDR[control], size, control)
        elif(control == 1):
            self._dataCache.write(self.__MAR[control], self.__memory, self.__MDR[control], size, control)
            
        elif(control == 2):
            self.__memory.store_word(self.__MAR[0], self.__MDR[0], 0)
            
        else:
            self.__memory.store_word(self.__MAR[1], self.__MDR[1], 1)
            
        

    def accessMemory(self, currMemoryEnable, size, control = 1):
        if currMemoryEnable == 0:
            pass
        
        elif currMemoryEnable == 1:
            self.getData(size, control)
        elif currMemoryEnable == 2:
            self.storeData(size, control)

    def getCache(self, control=1):
        if control==0:
            return self._instCache.getDetails()
        else:
            return self._dataCache.getDetails()
    
