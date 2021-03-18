from sys import stdin,stdout
import sys
from collections import defaultdict

#use
#import input
#pass object of Memory class to Input class
#to be used in main.py

class Input:

    def __init__(self):
        self.code = defaultdict(lambda:"00")
        #code has all the code lines corresponding to their number in the .mc file
        #this will be used in 
    
    def read_mc(self, obj):
        file = open('test1.mc','r')
        flag = 0
        for lines in file:
            if(lines == "$\n"):
                #data segment to be read after this
                flag = 1
                continue
            if(flag == 0):
                #text segment
                IC, instruction = map(str, lines.split())
                IC = int(IC, 16)
                instruction = int(instruction,16)
                self.code[IC] = instruction
                #maps instruction address to individual instruction
                #may change the instruction to binary to facilitate easier use
            else:
                #data segment
                address, data = map(str, lines.split())
                obj.store_word(address, data[2:])
