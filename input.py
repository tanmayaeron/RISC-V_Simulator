from sys import stdin,stdout
import sys
from collections import defaultdict
from memory import Memory
file=open('test/test1.mc','r')
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
        
        memory.store_word(address,data)
