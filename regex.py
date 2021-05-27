import re
import pandas as pd
import os
from collections import defaultdict
from helperFunctions import  *
from string import hexdigits

class cleanFile:
    def __init__(self, filePath):
        self.cleanFile = open("clean.s", 'w')
        self.file = open(filePath, 'r')
        self.file = self.file.readlines()
        self.PC = 0
        self.state = 2
        self.dataTable = {}
        self.textTable = {}
        self.dataPC = 0x10000000
        self.df_control = pd.read_csv(os.path.join( 'repository', "instructions.csv"))
        self.df_neu = list(self.df_control['neumonic'].astype(str))

    def addToTextTable(self, s):
        self.textTable[s] = self.PC

    def addToDataTable(self,s):
        self.dataTable[s]=self.dataPC
        
    def isInstruction(self, s):    
        for i in self.df_neu:
            if(i in s):
                return 1
        return 0   
    
    def handleDir(self, s, di):
        
        if(di == ".word"):
            self.dataPC +=4
        elif(di == ".byte"):
            self.dataPC +=1
        elif(di == ".half"):
            self.dataPC +=2
        elif(di == ".asciiz"):
            self.dataPC += len(s[1:-1])+1

    def dirStatement(self, s):
        dirT = [".asciiz", ".word",".byte", ".half"]
        dirC = ""
        s = re.findall(r'[^,\s]+',s)
        for i in range(len(s)):
            if(s[i] in dirT):
                dirC = s[i]
            else:
                self.handleDir(s[i], dirC)
                

    def clear(self):
        for line in self.file:
            if(line != "\n"):
                j = line.strip()
                if("#" in j):
                    jj = line.find("#")
                    j = j[:jj]
                if(j == "\n"):
                    continue
                if(".data" in j):
                    self.state = 1
                    j = j.split()[1:]
                    j = " ".join(j)
                    self.cleanFile.write(".data")
                if(".text" in j):
                    self.state = 2
                    j = j.split()[1:]
                    j = " ".join(j)
                    self.cleanFile.write(".text")
                if(self.state == 1):
                    isLabel = re.search("[^\n]+:", j)
                    if(isLabel is not None):
                        cornerCase = list(j.split(":"))
                        self.addToDataTable(cornerCase[0])
                        self.dirStatement(cornerCase[1])
                        if(cornerCase[1]!=""):
                                self.cleanFile.write(cornerCase[1].strip()+"\n")
                    else:
                        self.dirStatement(j)
                        self.cleanFile.write(j+"\n")
                elif(self.state == 2):
                    isLabel = re.search("[^\n]+:", j)
                    if(isLabel is not None):
                        cornerCase = list(j.split(":"))
                        self.addToTextTable(cornerCase[0])
                        if(self.isInstruction(cornerCase[1])):
                            self.PC+=4
                        if(cornerCase[1]!=""):
                            self.cleanFile.write(cornerCase[1].strip()+"\n")
                        
                    else:
                        if(self.isInstruction(j)):
                            self.PC+=4
                        self.cleanFile.write(j+"\n")
                    
                    
        self.cleanFile.close()
        

class parseInstruction:
    def __init__(self):
        self.df_control = pd.read_csv(os.path.join( 'repository', "instructions.csv"))
        self.df_neu = list(self.df_control['neumonic'].astype(str))
        self.df_format = list(self.df_control['format'])
        self.df      = list(self.df_control['parts'].astype(int))
        self.df_1    = list(self.df_control['part1'].astype(int))
        self.df_2    = list(self.df_control['part2'].astype(int))
        self.df_3    = list(self.df_control['part3'].astype(int))
        self.cleaner = cleanFile(os.path.join("test", "bubble_sort.s"))
        self.cleaner.clear()
        self.textTable = self.cleaner.textTable
        self.dataTable = self.cleaner.dataTable
        self.state = 2
        self.PC = 0
        self.dataPC = 0x10000000
        self.openFile = open(os.path.join("clean.s"), 'r')
        self.finalmc = open(os.path.join("main.mc"), 'w')
        self.dataSegment = []

    def printDetails(self):
        print(self.textTable)
        print(self.dataTable)

    def getTextTable(self):
        return self.textTable
    
    def getDataTable(self):
        return self.dataTable

    def getDetails(self):
        return [self.dataTable,self.textTable]

    def split(self,string):
        # splits the string at commas,spaces(tabs and \n), (,)
        # used to extract 12 and x16 from 12(x16)
        # also extracts lw x11 12 x12 from lw x11,12(x12)
        l=re.findall(r'[^,\s()]+',string)
        return l

    def isHeader(self,line):
        if(".text" in line):
            return 2
        if(".data" in line):
            return 1
        return self.state
        
    def checkifLabel(self, string):
        l = list(string.split(":"))
        if(len(l) >= 2):
            return 1
        return 0
    
    def CheckInstruction(self):
        # the instruction may be header or label or datainstruction(.word : 24) or
        # the real instruction
        for line in self.openFile.readlines():
            self.state = self.isHeader(line)
            # print(self.state)
            if self.checkifLabel(line):
                continue
            
            if self.state == 1:
                if(".data" in line):
                    continue
                self.processDataInstruction(line)
            
            if self.state == 2:
                if(".text" in line):
                    continue
                mc = self.processInstruction(line)
                self.finalmc.write(str(hex(self.PC))+" "+mc+"\n")
                self.PC+=4
        if(len(self.dataSegment) > 0):
            self.finalmc.write("$\n")
        for element in self.dataSegment:
            self.finalmc.write(element[0] + element[1] + "\n")
    
    def BytebyByte(self, s, dirC):
        """
        assuming s is a hex string.
        or a string (without double quotes) in case of asciiz
        """
        if(dirC == ".word"):
            s = "0"*8 + s
            for i in range(4):
                self.dataSegment.append((str(hex(self.dataPC)), " 0x"+ s[len(s)-2*(i+1):len(s)-2*i]))
                self.dataPC += 1
        elif(dirC == ".half"):
            s = "0"*4 + s
            for i in range(2):
                self.dataSegment.append((str(hex(self.dataPC)), " 0x"+ s[len(s)-2*(i+1):len(s)-2*i]))
                self.dataPC += 1
        elif(dirC == ".byte"):
            s = "0"*2 + s
            self.dataSegment.append((str(hex(self.dataPC)), " 0x"+ s[-2:]))
            self.dataPC += 1
        elif(dirC == ".asciiz"):
            for i in range(len(s)):
                self.dataSegment.append((str(hex(self.dataPC)), " "+ str(hex(ord(s[i])))))
                self.dataPC += 1
            self.dataSegment.append((str(hex(self.dataPC)), " 0x00"))
            self.dataPC += 1

    def convertThis(self, s, dirC):
        if dirC in [".word", ".half", ".byte"]:
            n = int(s, 0)
            return decToHex(n)
        else:
            n = s[1:-1]
            return n
            

    def processDataInstruction(self, s):
        dirT = [".asciiz", ".word", ".byte", ".half"]
        dirC = ""
        s = re.findall(r'[^,\s]+',s)
        for i in range(len(s)):
            if(s[i] in dirT):
                dirC = s[i]
            else:
                if(len(dirC) == 0):
                    print("ERROR :")
                s[i] = self.convertThis(s[i], dirC)
                self.BytebyByte(s[i], dirC)
                

    def processInstruction(self, instruction):
        l = self.split(instruction)
        try:
            instructionIndex = self.df_neu.index(l[0])
        except:
            return "Unknown instruction as %s is not recognized" %l[0]


        if(len(l)-1 != self.df[instructionIndex]):
            return "Insufficient/Excess parameters as the instruction has %d instead of %d"%(len(l)-1,self.df[instructionIndex] )

        else:
            if(l[0] == "lw" or l[0] == "lh" or l[0] == "lb"):
                l[2], l[3] = l[3], l[2]
            
            if(self.check(l[1], self.df_1[instructionIndex]) == None):
                return "Incorrect syntax1"
            try:
                if(self.check(l[2], self.df_2[instructionIndex]) == None):
                    
                    return "Incorrect syntax2"
                else:
                    if(self.df_2[instructionIndex] == 1):
                        l[2] = self.check(l[2], self.df_2[instructionIndex])
            except:
                pass
            try:
                if(self.check(l[3], self.df_3[instructionIndex]) == None):
                    self.finalmc.write("\n\n\n"+str(l)+"\n\n\n")
                    return "Incorrect syntax3"
                else:
                    if(self.df_3[instructionIndex] == 1):
                        l[3] = self.check(l[3], self.df_3[instructionIndex])
            except:
                pass
            '''
            l = [neumonic, part1, part2, part3]
            '''
            mc = self.assmToMC(l)
            return mc
        return "instruction %s has no error "%l

    def check(self, string, type):
        if(type == 0):
            if(re.search(r'^x(([0-9])|([1-2][0-9])|(3[0-1]))$', string)):
                return 1
            else:
                return None

        elif(type == 1):

            try:
                number = str(int(string, 0))
                return number
            except:
                return str(self.getLabelDiff(string))
        elif(type == -1):
            return 1

    def getLabelDiff(self,labelName):
        labelUsed = self.PC
        labelDefined = self.textTable[labelName]
        return labelDefined-labelUsed

    def assmToMC(self,l):
        mapTomethods = {"R":self.Rconvert,"I":self.Iconvert,"S":self.Sconvert,
                        "SB":self.SBconvert,"UJ":self.UJconvert,"U":self.Uconvert}

        try:
            instructionIndex = self.df_neu.index(l[0])
        except:
            return "instruction not supported"

        format = self.df_format[instructionIndex]
        return mapTomethods[format](l,instructionIndex)

    def Rconvert(self,l,instructionIndex):
        machine_code = ""
        funct7 = self.df_control['funct7'][instructionIndex]
        machine_code+=funct7[2:]
        rs2 = bin(int(l[3][1:]))[2:]
        rs2 = ("0"*5+rs2)[-5:]
        machine_code+=rs2
        rs1 = bin(int(l[2][1:]))[2:]
        rs1 = ("0" * 5 + rs1)[-5:]
        machine_code += rs1
        funct3 = self.df_control['funct3'][instructionIndex]
        machine_code+=funct3[2:]
        rd = bin(int(l[1][1:]))[2:]
        rd = ("0" * 5 + rd)[-5:]
        machine_code += rd
        opcode = self.df_control['opcode'][instructionIndex]
        machine_code+=opcode[2:]
        machine_code = binToHex(machine_code)
        machine_code = "0"*8+machine_code
        machine_code = machine_code[-8:]
        return "0x"+machine_code

    def Iconvert(self,l,instructionIndex):
        #immediate is assummed to be third field
        #hence, don't support load instructions rn

        machine_code = ""
        imm = int(l[3],0)
        imm = decToBin(imm)[-12:] #2's complement conversion
        machine_code +=imm
        rs1 = bin(int(l[2][1:]))[2:]
        rs1 = ("0" * 5 + rs1)[-5:]
        machine_code += rs1
        funct3 = self.df_control['funct3'][instructionIndex]
        machine_code += funct3[2:]
        rd = bin(int(l[1][1:]))[2:]
        rd = ("0" * 5 + rd)[-5:]
        machine_code += rd
        opcode = self.df_control['opcode'][instructionIndex]
        machine_code += opcode[2:]
        machine_code = binToHex(machine_code)
        machine_code = "0" * 8 + machine_code
        machine_code = machine_code[-8:]
        return "0x" + machine_code

    def Sconvert(self,l,instructionIndex):
        machine_code = ""

        imm = int(l[2], 0)
        imm = decToBin(imm)[-12:] # 2's complement conversion
        machine_code += imm[:7]

        rs2 = bin(int(l[1][1:]))[2:]
        rs2 = ("0" * 5 + rs2)[-5:]
        machine_code += rs2

        rs1 = bin(int(l[3][1:]))[2:]
        rs1 = ("0" * 5 + rs1)[-5:]
        machine_code += rs1

        funct3 = self.df_control['funct3'][instructionIndex]
        machine_code += funct3[2:]

        machine_code+=imm[-5:]

        opcode = self.df_control['opcode'][instructionIndex]
        machine_code += opcode[2:]

        machine_code = binToHex(machine_code)
        machine_code = "0" * 8 + machine_code
        machine_code = machine_code[-8:]
        return "0x" + machine_code

    def SBconvert(self,l,instructionIndex):
        machine_code = ""

        imm = int(l[3], 0)
        imm = decToBin(imm)[-13:]  # 2's complement conversion
        machine_code += imm[0]
        machine_code+=imm[2:8]

        rs2 = bin(int(l[2][1:]))[2:]
        rs2 = ("0" * 5 + rs2)[-5:]
        machine_code += rs2

        rs1 = bin(int(l[1][1:]))[2:]
        rs1 = ("0" * 5 + rs1)[-5:]
        machine_code += rs1

        funct3 = self.df_control['funct3'][instructionIndex]
        machine_code += funct3[2:]

        machine_code += imm[-5:-1]
        machine_code+=imm[1]

        opcode = self.df_control['opcode'][instructionIndex]
        machine_code += opcode[2:]

        machine_code = binToHex(machine_code)
        machine_code = "0" * 8 + machine_code
        machine_code = machine_code[-8:]
        return "0x" + machine_code

    def UJconvert(self,l,instructionIndex):
        machine_code = ""

        imm = int(l[2], 0)
        imm = decToBin(imm)[-21:] # 2's complement conversion
        # self.finalmc.write("\n\n\n\n"+str(imm))
        machine_code += imm[0]
        machine_code += imm[-11:-1]
        machine_code += imm[-12]
        machine_code+=imm[1:9]

        rd = bin(int(l[1][1:]))[2:]
        rd = ("0" * 5 + rd)[-5:]
        machine_code += rd
        opcode = self.df_control['opcode'][instructionIndex]
        machine_code += opcode[2:]
        machine_code = binToHex(machine_code)
        machine_code = "0" * 8 + machine_code
        machine_code = machine_code[-8:]
        return "0x" + machine_code

    def Uconvert(self,l,instructionIndex):
        machine_code = ""

        #since user entered value is shifted
        #it is added as it is
        imm = int(l[2], 0)
        imm = decToBin(imm)[-20:] # 2's complement conversion
        machine_code += imm

        rd = bin(int(l[1][1:]))[2:]
        rd = ("0" * 5 + rd)[-5:]
        machine_code += rd
        opcode = self.df_control['opcode'][instructionIndex]
        machine_code += opcode[2:]
        machine_code = binToHex(machine_code)
        machine_code = "0" * 8 + machine_code
        machine_code = machine_code[-8:]
        return "0x" + machine_code

    def dump(self,file):
        f = open(file, 'r')
        f = f.readlines()
        for i in f:
            processInstruction(i)

class SyntaxCheck:
    def __init__(self, dataTable, textTable):
        self.df_control = pd.read_csv(os.path.join( 'repository', "instructions.csv"))
        self.df_neu = list(self.df_control['neumonic'].astype(str))
        self.df_format = list(self.df_control['format'])
        self.df      = list(self.df_control['parts'].astype(int))
        self.df_1    = list(self.df_control['part1'].astype(int))
        self.df_2    = list(self.df_control['part2'].astype(int))
        self.df_3    = list(self.df_control['part3'].astype(int))
        self.cleanedFile=open('clean.s','r')
        
        self.dataTable=dataTable
        self.textTable=textTable
        self.state=2
        self.dataStatesList = ['.asciiz','.word','.half','.byte']
        self.dataState = -1
        self.Errors=[]
        self.hexDigits=set(hexdigits)
        self.linenumber=0
    
    def isHeader(self,line):
        if(".text" in line):
            return 2
        if(".data" in line):
            return 1
        return self.state
    
    def isString(self,words):
        return len(words)>=2 and words[0]==words[-1]=='"'
    
    def printErrors(self):
        if len(self.Errors)==0:
            print("No errors in the file")
        else:
            print(self.Errors)
    
    def isHexDigit(self,words):
        for j in words:
            if j not in self.hexDigits:
                return 0;
                break;
        else:
            return 1;

    def checkDataSyntax(self,line):
        for words in line.split():

            if words in self.dataStatesList:
                self.dataState=self.dataStatesList.index(words)
            elif words in ['.data','.text']:
                continue
            elif words[0]=='.':
                self.Errors.append("Error in %s line as %s is not recognised"%(line.strip(),words))
            else:
                if self.dataState==0:
                    if self.isString(words):
                        # should be of the form "ABC"
                        continue;
                    else:
                        self.Errors.append("Error in %s line as %s is not a string"%(self.linenumber,words))
                else:
                    if self.isString(words):
                        self.Errors.append("Error in %s line as %s is a string"%(line,words))
                    elif words.isdigit():
                        continue;
                    else:
                        if words in self.textTable:
                            continue;
                        elif words in self.dataTable:
                            continue;
                        else:
                            self.Errors.append("Error in %s line as %s is not a digit and not a label"%(line,words))
                        
                


    def main(self):
        for line in self.cleanedFile.readlines():
            self.linenumber+=1
            self.state=self.isHeader(line)
            if self.state==1:
                self.checkDataSyntax(line)

        self.cleanedFile.close()

if __name__=='__main__':
    # print(int("21", 0))
    # print(int("0x21", 0))
    # print(int("0b11", 0))
    # print(int("0b01", 0))
    # output=parseInstruction.processInstruction(".data")
    # print(output)


    # a = cleanFile(os.path.join( 'test', "bubble_sort.s"))
    # a.clear()
    
    # # a.clear()
    # print(a.textTable)
    # print("\nparse instruction class\n")

    a=parseInstruction()
    a.CheckInstruction()
    tables=a.getDetails()
    print(tables)

    b=SyntaxCheck(tables[0],tables[1])
    b.main()
    b.printErrors()



# # s = "label:"
# # print(list(s.split(":")))


