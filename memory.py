from collections import defaultdict


class Memory:

    """
    represents memory in dictionary
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
        :return:1byte data stored at address in hex, str of length 2(without 0x)
        """

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

    """
    
    store functions
    :param address: byte address str of length 8(without 0x)
           data: data to be stored at address, str of appropriate size(without 0x)
    """

    def make_length(self, data, length):
        data = "0"*length+data
        return data[-length:]

    def store_byte(self, address, data):
        data = self.make_length(data, 2)
        self.__memory[address] = data

    def store_word(self, address, data):
        data = self.make_length(data, 8)
        address_in_dec = self.hexToDec(address)
        for i in range(4):
            address_in_hex = "0" * 8 + hex(address_in_dec + i)[2:]
            address_in_hex = address_in_hex[-8:]
            self.store_byte(address_in_hex, data[6 - 2 * i:8 - 2 * i])

    def store_halfword(self, address, data):
        data = self.make_length(data, 4)
        address_in_dec = self.hexToDec(address)
        for i in range(2):
            address_in_hex = "0" * 8 + hex(address_in_dec + i)[2:]
            address_in_hex = address_in_hex[-8:]
            self.store_byte(address_in_hex, data[2 - 2 * i:4 - 2 * i])


mem = Memory()
mem.store_word("10000000", "AAA")

print("dictionary is :", end="")
mem.print_memory()
