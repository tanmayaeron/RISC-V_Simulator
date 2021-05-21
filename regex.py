import re
import pandas as pd
import os
from collections import defaultdict
from helperFunctions import  *

# df_control = pd.read_csv(os.path.join(currFolderPath, 'repository', "instructions.csv"))


def dump(file):
    f = open(file, 'r')
    f = f.readlines()
    for i in f:
        processInstruction(i)
class parseInstruction:
    def __init__(self):
        self.df_control = pd.read_csv(os.path.join( 'repository', "instructions.csv"))
        self.df_neu = list(self.df_control['neumonic'].astype(str))
        self.df      = list(self.df_control['parts'].astype(int))
        self.df_1    = list(self.df_control['part1'].astype(int))
        self.df_2    = list(self.df_control['part2'].astype(int))
        self.df_3    = list(self.df_control['part3'].astype(int))

        self.dotDataOccured=0;
        self.dotTextOccured=0;

        self.labels=defaultdict(str)

        # labels contains label name and its pc for eg {"exit":"3C","if":"28"}
    def printDetails(self):
        if self.dotTextOccured:
            print("Text instructions parsing ahead")
        else:
            print("Data Instructions Parsing ahead")
        print(self.labels)
    
    def getDetails(self):
        return self.labels
    
    def split(self,string):
        # splits the string at commas,spaces(tabs and \n), (,)
        # used to extract 12 and x16 from 12(x16)
        # also extracts lw x11 12 x12 from lw x11,12(x12)
        l=re.findall(r'[^,\s()]+',string)
        return l;
    
    def CheckInstruction(self,string,PC="0"*8):
        # the instruction may be header or label or datainstruction(.word : 24) or 
        # the real instruction
        if self.checkIfHeader(string):
            return "Header";

            
        elif self.checkifLabel(string,PC):
            return "Label";

        elif self.dotTextOccured==0 and self.dotDataOccured==0:
            # .data and .text has not occured and it is not label
            # so it must be .text instructions
            self.dotTextOccured=1
        
        if self.dotDataOccured==1:
            # process data instruction;
            pass;
        elif self.dotTextOccured==1:
            return self.processInstruction(string)

    def checkIfHeader(self,string):
        # check if it is .data or .text
        if string==".text":
            self.dotTextOccured=1;
            self.dotDataOccured=0
            return 1;
        elif string==".data":
            self.dotDataOccured=1
            self.dotTextOccured=0
            return 1;
        return 0;

    def checkifLabel(self,string, PC="0"*8):
        """
        checks if the string is label or not
        for eg:
        label:
        exit:
        if label is present it returns label with the PC
        """
        if string.endswith(":"):
            labels[string]=PC # stores the PC to calculate the difference in the future
            return 1;
        return 0;

    def processInstruction(self, instruction):
        lWithNeumonic = self.split(instruction)
        
        instructionIndex = 0
        try:
            instructionIndex = self.df_neu.index(lWithNeumonic[0])
        except:
            return "Unknown instruction as %s is not recognized" %lWithNeumonic[0]
        
        l=lWithNeumonic[1:]
        if(len(l) != self.df[instructionIndex]):
            return "Insufficient/Excess parameters as the instruction has %d instead of %d"%(len(l),self.df[instructionIndex] )
        
        else:
            if(self.check(l[1], self.df_1[instructionIndex]) == None):
                return "Incorrect syntax"
            if(self.check(l[2], self.df_2[instructionIndex]) == None):
                return "Incorrect syntax"
            else:
                l[2] = int(string, 2)
            try:
                if(self.check(l[3], self.df_3[instructionIndex]) == None):
                    return "Incorrect syntax"
            except:
                pass
            '''
            l = [neumonic, part1, part2, part3]
            '''
            
            
            
            
        
        
    def check(self,string, type):
        if(type == 0):
            if(re.search(r'^x(([0-9])|([1-2][0-9])|(3[0-1]))$', string)):
                return 1
            else:
                return None
        elif(type == 1):
            try:
                number = int(string, 0)
                return number
            except:
                return None
            
        elif(type == -1):
            return 1
def getLabelPC(string):
    # the label must have occured earlier to get the PC 
    # should be run after adding all the labels into the labels dict
    if string in labels:
        return labels[string]
    else:
        return "ERROR: Label never defined in the code"

def getLabelDiff(labelName,PC):
    labelUsed=PC;
    labelDefined=getLabelPC(labelName)
    if labelDefined.startswith("ERROR"):
        return "ERROR: Label never defined in the code";
    labelUsedInDec=hexToDec(PC)
    labelDefinedInDec=hexToDec(labelName)
    return labelDefinedInDec-labelUsedInDec



        




if __name__=='__main__':
    # print(int("21", 0))
    # print(int("0x21", 0))
    # print(int("0b11", 0))
    # print(int("0b01", 0))
    # output=parseInstruction.processInstruction(".data")
    # print(output)

    print("\nparse instruction class\n")

    a=parseInstruction()
    output=a.CheckInstruction(".data")
    print(output)
    a.printDetails()

    print(a.CheckInstruction(".text"))
    a.printDetails()

    print(a.CheckInstruction("add x0 x0 x0"))
    # string = "x21"
    # if(re.search(r'^x(([0-9])|([1-2][0-9])|(3[0-1]))$', string)):
    #     print(2)
    # string = "x211"
    # print(re.search(r'^x(([0-9])|([1-2][0-9])|(3[0-1]))$', string))
    # string = "1x21"
    # print(re.search(r'^x(([0-9])|([1-2][0-9])|(3[0-1]))$', string))
  
    
    
    
#     def stringsplit(string):
#         # this function splits according to space and comma only
#     l=[]
#     for i in string.split():
#         j=i.split(",")
#         l+=[k for k in j if k!=""]


#     return l;


# def stringsplit2(string,splitarray=" ,\n"):
#     # this function splits the string and arguments are all the elements in the splitarray
#     l=[]
#     splitarray=frozenset(splitarray)
#     # as the query is search frozenset performs faster over list
#     for i in string:
#         if i in splitarray:
#             if len(l)==0 or l[-1]!="":
#                 # we have to split here
#                 l.append("")
#         else:
#             if len(l)==0:
#                 l.append(i)
#             else:
#                 l[-1]+=i
#     if l and l[-1]=="":
#         l.pop()
#     return l;

# def splitstringregex(string):
#     # splits the string at commas and spaces(spaces tabs and \n)
#     l=re.findall(r'[^,\s]+',string)
#     return l;
