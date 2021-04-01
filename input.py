from collections import defaultdict


class ReadFile:

    def __init__(self):
        pass

    def write_file(self, obj, filename):
        file = open(filename, 'w')
        # we want to print only data segment
        dict = obj.getMemory()
        for i in sorted(dict.keys()):
            if i[0] != '0':  # >=10000000
                file.write("0x"+i+" ")
                file.write("0x"+dict[i]+"\n")

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
