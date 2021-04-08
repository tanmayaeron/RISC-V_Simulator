class ReadFile:

    def __init__(self):
        pass

    def printMemory(self, memory, filename):
        file = open(filename, 'w')
        # we want to print only data segment
        dict = memory
        for i in sorted(dict.keys()):
            if int(i,16) >= int("10007FE8",16):
                break
            if i[0] != '0':  # >=10000000
                file.write("0x"+i+" ")
                file.write("0x"+dict[i]+"\n")
                
        file.close()

    def printRegisters(self, registers, filename):
        # write 'a' instead of 'w' to appending text here
        file = open(filename, 'w')
        for index, i in enumerate(registers):
            file.write("x"+str(index)+" "+i+"\n")
            
        file.close()

    def read_mc(self, filepath, obj):
        file = open(filepath, 'r')
        for lines in file:
            try:
                requiredMemoryLocation, instruction = map(str, lines.split())
                obj.setMAR(requiredMemoryLocation[2:])
                obj.setMDR(instruction[2:])
                obj.storeData(2)
            except:
                pass
        