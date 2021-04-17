from collections import defaultdict

class Buffer:

    def __init__(self):
        self.dict = defaultdict()
    
    def fetchB(self, PC, IR):
        self.dict[1] = PC, IR

    #instruction -> index of instruction in csv, PC, RA, RB->hex string, rd -> destination register = -1
    def decodeB(self, id, PC, RA = "0"*8, RB = "0"*8, RM = "0"*8, rd = -1):
        #those who don't have rd should give -1 to this function, decode update
        if 15 <= id <= 17:
            rd = -1
        self.dict[2] = id, PC, RA, RB, RM, rd

    def executeB(self, id, RZ, rd): #RZ, rd
        self.dict[3] = id, RZ, rd

    def memoryB(self, id, RY, rd): #RY, rd
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

    def __init__(self, bufferobj):
        self.obj = bufferobj #bufferobj

    #don't call for branch instructions positively
    def detectHazard(self, id, rs1 = -2, rs2 = -3): #data forwarding
        # dict[3] or dict[4] #rdprev1, rdprev2
        rdprev1 = self.obj.get(3)[2] #execute buffer rd
        rdprev2 = self.obj.get(4)[2] #memory buffer rd

        prevtype1 = self.obj.get(3)[0] #lw, lh, lb #stalling
        prevtype2 = self.obj.get(4)[0] #MM

        #return [ifHazard, type, stalls]
        if rdprev1 == rdprev2 == -1:
            return [False, "NO", 0]

        if 12<=prevtype1<=14 and 15 <= id <= 17 and rdprev1 in [rs1, rs2]: #load then store
            return [True, "MM", 0] #MM

        if 12<=prevtype1<=14 and rdprev1 in [rs1, rs2]: #if the prev were load type and we use it then we need to stall
            return [True, "ME", 1]

        if 12<=prevtype2<=14 and rdprev2 in [rs1, rs2]: #if the previous of previous were load then M->E beginning
            return [True, "ME", 0]

        if rdprev1 in [rs1, rs2]: #E->E
            return [True, "EE", 0]

        if rdprev2 in [rs1, rs2]: #M->E
            return [True, "ME", 0]

        return [False, "NO", 0]

    def detectHazardS(self, id, rs1 = -2, rs2 = -3): # stalling

        rdprev1 = self.obj.get(3)[2] #execute buffer rd
        rdprev2 = self.obj.get(4)[2] #memory buffer rd

        prevtype1 = self.obj.get(3)[0] #lw, lh, lb #stalling
        prevtype2 = self.obj.get(4)[0] #MM

        #return [ifHazard, type, stalls]
        if rdprev1 == rdprev2 == -1:
            return [False, 0]

        if 12<= prevtype1 <=14 and 15 <= id <= 17 and rdprev1 in [rs1, rs2]: #load then store
            return [True, 1] #MM

        if 12<=prevtype1<=14 and rdprev1 in [rs1, rs2]: #if the prev were load type and we use it then we need to stall
            return [True, 2] #ME

        if 12<=prevtype2<=14 and rdprev2 in [rs1, rs2]: #if the previous of previous were load then M->E beginning
            return [True, 1]

        if rdprev1 in [rs1, rs2]: #E->E
            return [True, 2]

        if rdprev2 in [rs1, rs2]: #M->E
            return [True, 1]

        return [False, 0]


class controlHazard:
    def __init__(self,btb_obj):
        self.obj=btb_obj

    def branchHazard(self, PC, id, RZ, newTarget):
        # PC is str id is int RZ is str of hex newTarget is str of hex
        # newTarget comes from IAG
        
        if not 18<=id<=23: # if it is not beq or jump return False
            return 
        if 22<=id<=23:
            RZ="0"*7+"1"
        self.obj.changeState(PC, RZ, newTarget)
        
