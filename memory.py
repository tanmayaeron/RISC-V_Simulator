from collections import defaultdict


class Memory:

    """
    represents memory in dictionary
    each key value pair is of form byte-address:data(one byte of data)
    keys - address in hex (without 0x) represented as string of fixed size 8
    values - 1 byte of data in hex(without 0x) represented as string of size 2
    """

    def __init__(self):
        self._memory = defaultdict(lambda: "00")  # only relevant data stored

    def hexToDec(self, address):
        address_in_dec = int(address, 16)
        return address_in_dec

    def load_byte(self, address):
        """

        :param address:byte address str of length 8(without 0x)
        :return:1byte data stored at address in hex, str of length 2(without 0x)
        """
        if address in self._memory.keys():
            return self._memory[address]
        else:
            return "00"

    def load_word(self, address):
        """

        :param address: byte address str of length 8(without 0x)
        :return: 1word data stored at address, in hex, str of length 8(without 0x)
        """
        address_in_dec = self.hexToDec(address)
        data = ""
        for i in reversed(range(4)):
            address_in_hex = "0" * 8 + hex(address_in_dec + i)[2:]
            address_in_hex = address_in_hex[-8:]
            data = data + self.load_byte(address_in_hex)
        return data

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

    def store_byte(self, address, data):
        self._memory[address] = data

    def store_word(self, address, data):
        address_in_dec = self.hexToDec(address)
        for i in range(4):
            address_in_hex = "0" * 8 + hex(address_in_dec + i)[2:]
            address_in_hex = address_in_hex[-8:]
            self.store_byte(address_in_hex, data[6 - 2 * i:8 - 2 * i])

    def store_halfword(self, address, data):
        address_in_dec = self.hexToDec(address)
        for i in range(2):
            address_in_hex = "0" * 8 + hex(address_in_dec + i)[2:]
            address_in_hex = address_in_hex[-8:]
            self.store_byte(address_in_hex, data[2 - 2 * i:4 - 2 * i])

# mem = Memory()
# mem.store_byte("00000000","0A")
# print(mem.load_word("00000000"))
