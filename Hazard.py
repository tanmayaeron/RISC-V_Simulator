from collections import defaultdict

class Buffer:

    def __init__(self):
        self.dict = defaultdict()
    
    def fetchB(self, PC, IR):
        self.dict[1] = PC, IR

    #instruction -> index of instruction in csv, PC, RA, RB->hex string, rd -> destination register = -1
    def decodeB(self, id, PC, RA = "0"*8, RB = "0"*8, RM = "0"*8, rd = -1):
        #those who don't have rd should give -1 to this function, decode update
        self.dict[2] = id, PC, RA, RB, RM, rd

    def executeB(self, id, RZ, rd = -1): #RZ, rd
        self.dict[3] = id, RZ, rd

    def memoryB(self, id, RY, rd = -1): #RY, rd
        self.dict[4] = id, RY, rd

    def get(self, stage):
        if stage in self.dict:
            return self.dict[stage]

    def flush(self):
        self.dict.clear()

    def clearStage(self, stage):
        #delete dict[1] dict[2] and so on
        if stage in self.dict:
            del self.dict[stage]


class HDU:
    """
    we are making dictionaries for cycle as key 
    F->IR
    D->rd -> number
    6 -> lw..
    (6,cycle) = 1
    7 -> sw..
    (7,cycle) = 1
    E->RZ -> number, change type from string
    ME->RY -> number, change type from string 
    WB->rd
    """

    def __init__(self):
        self.obj = Buffer()

    def detectHazard(self, rs1 = -2, rs2 = -3):
        # dict[3] or dict[4] #rdprev1, rdprev2
        rdprev1 = self.obj.get(3)[1] #execute buffer rd
        rdprev2 = self.obj.get(4)[1] #memory buffer rd

        prevtype1 = self.obj.get(3)[2] #lw, lh, lb #stalling
        prevtype2 = self.obj.get(4)[2] #MM

        #return [ifHazard, type, stalls]
        if rdprev1 == rdprev2 == -1:
            return [False, "NO", 0]

        if 12<=prevtype1<=14 and rdprev1 in [rs1, rs2]:
            return [False, "ME", 1]

        if 12<=prevtype2<=14 and rdprev2 in [rs1, rs2]:
            return [False, "MM", 0]

        if rdprev1 in [rs1, rs2]: #E->E
            return [True, "EE", 0]

        if rdprev2 in [rs1, rs2]: #M->E
            return [True, "ME", 0]


        return [False, "NO", 0]
