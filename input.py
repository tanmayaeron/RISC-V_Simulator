from sys import stdin,stdout
import sys
from collections import defaultdict

class Memory:

    def __init__(self):
        self.__memory = defaultdict(lambda:"00")    #only relevant data stored

    def load_byte(self, address):
        if address in self.__memory.keys():
            return self.__memory[address]
        else:
            return "00"

    def load_word(self, address):
        address_in_dec = int(address, 16)
        data = ""
        for i in reversed(range(4)):
            address_in_hex ="0"*8+hex(address_in_dec + i)[2:]
            address_in_hex = address_in_hex[-8:]
            data = data + self.load_byte(address_in_hex)
        return data

    def store_byte(self, address, data):
        self.__memory[address] = data

    # def store_word(self, address, data):
    #     address_in_dec = int(address, 16)
    #     for i in range(4):
    #         address_in_hex = "0"*8+hex(address_in_dec+i)[2:]
    #         address_in_hex = address_in_hex[-8:]
    #         self.store_word(address_in_hex,data[6-2*i:8-2*i])
    def store_word_(self,address,data):
        # data is a string containing 0x
        data=data[2:]
        additional_zeroes=8-len(data)
        
        data="0"*additional_zeroes+data
        # address is in string of hex
        address=int(address,16)
        # converting address to decimal
        # data is of 8 bit else error
        iterator=6
        for i in range(4):
            self.__memory[address]=data[iterator:iterator+2]
            iterator-=2
            address+=1
        print(self.__memory)
file=open('test.mc','r')
# sys.stdout=open('output.txt','w')
memory=Memory()
input=1
for i in file:
    
    if i=="$\n":
        input=0
        continue
    if input==1:
        pc,instruction = map(str,i.split())
        pc=int(pc,16)
        instruction=int(instruction,16)
        print(pc,instruction)
    else:
        address,data=map(str,i.split())
        
        memory.store_word_(address,data)
