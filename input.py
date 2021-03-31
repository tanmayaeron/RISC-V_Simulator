class ReadFile:

    def __init__(self):
        pass 
    
    def read_mc(self, filepath, obj):
        file = open(filepath,'r')
        flag = 0
        for lines in file:
            if(lines == "$\n"):
                flag = 1
                continue
            if(flag == 0):
                #text segment
                requiredMemoryLocation, instruction = map(str, lines.split())
                obj.setMAR(requiredMemoryLocation[2:])
                obj.setMDR(instruction[2:])
                obj.storeData(2)
    
            else:
                requiredMemoryLocation, instruction = map(str, lines.split())
                obj.setMAR(requiredMemoryLocation[2:])
                obj.setMDR(instruction[2:])
                obj.storeData(2)
