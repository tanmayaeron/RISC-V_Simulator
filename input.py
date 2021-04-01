from memory import PMI
from collections import defaultdict


class ReadFile:

    def __init__(self):
        pass

    def write_file(obj, filename):
        file = open(filename, 'w')
        # we want to print only data segment
        dict = obj.getMemory()
        for i in dict:
            if i[0] == '1' and len(i) == 8:  # >=10000000
                file.write(i+" ")
                file.write(dict[i]+"\n")

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
