class ReadFile:

    def __init__(self):
        pass

    def read_mc(self, filepath, obj):
        file = open(filepath,'r')
        for lines in file:
            try:
                requiredMemoryLocation, instruction = map(str, lines.split())
                obj.setMAR(requiredMemoryLocation[2:])
                obj.setMDR(instruction[2:])
                obj.storeData(2)
            except:
                pass
