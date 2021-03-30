from collections import defaultdict


def make_length(data, length):
    data = "0"*length+data
    return data[-length:]

class Memory:

    """
    represents memory in default dictionary
    each key value pair is of form byte-address:data(one byte of data)
    keys - address in hex (without 0x) represented as string of fixed size 8
    values - 1 byte of data in hex(without 0x) represented as string of size 2
    """

    def __init__(self):
        self.__memory = defaultdict(lambda: "00")  # only relevant data stored

    def print_memory(self):
        print(self.__memory)

    def hexToDec(self, address):
        address_in_dec = int(address, 16)
        return address_in_dec

    def getMemoryDisplay(self, address):
        l = []
        """
        
        :param address: byte address str of length 8(without 0x)
        :return: 10 words in contiguous location, in hex, str of length 8(without 0x)
        """
        address_in_dec = self.hexToDec(address)
        data = ""
        for i in reversed(range(40)):
            address_in_hex = "0" * 8 + hex(address_in_dec + i)[2:]
            address_in_hex = address_in_hex[-8:]
            data = self.load_byte(address_in_hex)
            l.append(data)
        return l

    def load_byte(self, address):
        """
        :param address:byte address str of length 8(without 0x)
        :return:1byte data stored at address, in hex, str of length 2(without 0x)
        """
        address = make_length(address,8)
        return self.__memory[address]

    def load_halfword(self, address):
        """
        :param address: byte address str of length 8(without 0x)
        :return: halfword data stored at address, in hex, str of length 4(without 0x)
        """
        address_in_dec = self.hexToDec(address)
        data = ""
        for i in reversed(range(2)):
            address_in_hex = "0" * 8 + hex(address_in_dec + i)[2:]
            address_in_hex = address_in_hex[-8:]
            data = data + self.load_byte(address_in_hex)
        return data

    def load_word(self, address):
        """
        :param address: byte address str of length 8(without 0x)
        :return: word data stored at address, in hex, str of length 4(without 0x)
        """
        address_in_dec = self.hexToDec(address)
        data = ""
        for i in reversed(range(4)):
            address_in_hex = "0" * 8 + hex(address_in_dec + i)[2:]
            address_in_hex = address_in_hex[-8:]
            data = data + self.load_byte(address_in_hex)
        return data
    """
    
    store functions
    :param address: byte address str of length 8(without 0x)
           data: data to be stored at address, str of appropriate size(without 0x)
    """



    def store_byte(self, address, data):
        address = make_length(address,8)
        data = make_length(data, 2)
        self.__memory[address] = data

    def store_word(self, address, data):
        address = make_length(address,8)
        data = make_length(data, 8)
        address_in_dec = self.hexToDec(address)
        for i in range(4):
            address_in_hex = "0" * 8 + hex(address_in_dec + i)[2:]
            address_in_hex = address_in_hex[-8:]
            self.store_byte(address_in_hex, data[6 - 2 * i:8 - 2 * i])

    def store_halfword(self, address, data):
        address = make_length(address,8)
        data = make_length(data, 4)
        address_in_dec = self.hexToDec(address)
        for i in range(2):
            address_in_hex = "0" * 8 + hex(address_in_dec + i)[2:]
            address_in_hex = address_in_hex[-8:]
            self.store_byte(address_in_hex, data[2 - 2 * i:4 - 2 * i])

class PMI:
    def __init__(self):
        self.__MDR = "0"*8
        self.__MAR = "0"*8
        self.__memory = Memory()

    def getMDR(self):
        return self.__MDR
    
    def getMAR(self):
        return self.__MAR

    def setMDR(self,data):
        data = make_length(data,8)
        self.__MDR = data
        
    def setMAR(self,address):
        address = make_length(address,8)
        self.__MAR = address

    def print_memory(self):
        self.__memory.print_memory()

    def getData(self,size):

        """
        size : 0 - byte
               1 - halfword
               2 - word
        """

        getArray = [self.__memory.load_byte, self.__memory.load_halfword, self.__memory.load_word]
        data = getArray[size](self.__MAR)
        data = make_length(data,8)
        self.__MDR = data
                
    
    def storeData(self,size):
        getArray = [self.__memory.store_byte, self.__memory.store_halfword, self.__memory.store_word]
        getArray[size](self.__MAR,self.__MDR)

if __name__=='__main__':
    interface = PMI()
    interface.setMAR("1000000f")
    interface.setMDR("DEADBEAF")
    interface.storeData(2)
    print(interface.print_memory())