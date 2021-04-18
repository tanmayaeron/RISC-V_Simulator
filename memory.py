from collections import defaultdict
from helperFunctions import *

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
    def __init__(self):
        self.__MDR = ["0"*8, "0"*8]
        self.__MAR = ["0"*8, "0"*8]
        self.__memory = Memory()

    def getMDR(self, control = 1):
        return self.__MDR[control]

    def getMAR(self, control = 1):
        return self.__MAR[control]

    def getMemoryDisplay(self, control = 1):
        self.__memory.getMemoryDisplay(control)

    def setMDR(self, data, control = 1):
        data = make_length(data, 8)
        self.__MDR[control] = data

    def setMAR(self, address, control = 1):
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

    def getData(self, size, control = 1):
        """
        size : 0 - byte
               1 - halfword
               2 - word
        """

        getArray = [self.__memory.load_byte,
                    self.__memory.load_halfword, self.__memory.load_word]
        data = getArray[size](self.__MAR[control], control)
        data = make_length(data, 8)
        self.__MDR[control] = data

    def storeData(self, size, control = 1):
        getArray = [self.__memory.store_byte,
                    self.__memory.store_halfword, self.__memory.store_word]
        getArray[size](self.__MAR[control], self.__MDR[control], control)

    def accessMemory(self, currMemoryEnable, size, control = 1):
        if currMemoryEnable == 0:
            pass
        
        elif currMemoryEnable == 1:
            self.getData(size, control)
        elif currMemoryEnable == 2:
            self.storeData(size, control)
       