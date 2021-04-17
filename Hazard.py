from collections import defaultdict

class Buffer:

    def __init__(self):
        self.dict = defaultdict(list)
    
    def fetchB(self, PC, IR):
        self.dict[1] = PC, IR

    #instruction -> index of instruction in csv, PC, RA, RB->hex string, rd -> destination register = -1
    def decodeB(self, id, PC, RA = "0"*8, RB = "0"*8, RM = "0"*8, rd = -1):
        #those who don't have rd should give -1 to this function, decode update
        if 15 <= id <= 17:
            rd = -1
        self.dict[2] = id, PC, RA, RB, RM, rd

    def executeB(self, id, RZ, rd, RM): #RZ, rd #dict[3][1]
        self.dict[3] = id, RZ, rd, RM # RZ is the result

    def memoryB(self, id, RY, rd): #RY, rd #dict[4][1]
        self.dict[4] = id, RY, rd # RY is the result

    def get(self, stage):
        if stage in self.dict:
            return self.dict[stage]
        return [-1]*6

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

    def __init__(self, bufferobj, registerobj):
        self.obj = bufferobj #bufferobj
        self.registerobj = registerobj
        self.inf = float("inf")

    #don't call for branch instructions positively
    def detectHazard(self, id, rs1 = 0, rs2 = 0): #data forwarding
        # dict[3] or dict[4] #rdprev1, rdprev2
        rdprev1 = self.obj.get(3)[2] #execute buffer rd
        rdprev2 = self.obj.get(4)[2] #memory buffer rd

        prevtype1 = self.obj.get(3)[0] #lw, lh, lb #stalling
        prevtype2 = self.obj.get(4)[0] #MM
        
        # return [ifHazard, type, stalls, rs1value, rs2value]
        if rs1 == rs2 == 0:
            return [False, "NO", 0, 0, 0]
        
        if rdprev1 == 0:
            rdprev1 = -1

        if rdprev2 == 0:
            rdprev2 = -1
        
        if rdprev1 == rdprev2 == -1:
            return [False, "NO", 0, self.registerobj.get_register(rs1), self.registerobj.get_register(rs2)]

        if 12<=prevtype1<=14 and 15 <= id <= 17 and rdprev1 == rs2: #load then store
            """
            lw x10,0(x11)
            sw x10,0(x11) # rs1+imm and rs2==rdprev1
            """
            return [True, "MM", 0, self.registerobj.get_register(rs1), self.obj.get(4)[1]] #MM

        if 12<=prevtype1<=14 and rdprev1 in [rs1, rs2]: #if the prev were load type and we use it then we need to stall
            
            return [True, "ME", 1, self.inf, self.inf] # inf value, check after stall cycle to get original value

        if 12<=prevtype2<=14 and rdprev2 in [rs1, rs2]: #if the previous of previous were load then M->E beginning
            rs1_value=self.registerobj.get_register(rs1) if rs1!=rdprev2 else self.obj.get(4)[1]
            rs2_value=self.registerobj.get_register(rs2) if rs1!=rdprev2 else self.obj.get(4)[1]
            return [True, "ME", 0, rs1_value, rs2_value]

        if rdprev1 in [rs1, rs2]: #E->E
            rs1_value=self.registerobj.get_register(rs1) if rs1!=rdprev1 else self.obj.get(3)[1]
            rs2_value=self.registerobj.get_register(rs2) if rs1!=rdprev1 else self.obj.get(3)[1]
            return [True, "EE", 0, rs1_value, rs2_value]

        if rdprev2 in [rs1, rs2]: #M->E
            rs1_value=self.registerobj.get_register(rs1) if rs1!=rdprev2 else self.obj.get(4)[1]
            rs2_value=self.registerobj.get_register(rs2) if rs1!=rdprev2 else self.obj.get(4)[1]
            return [True, "ME", 0, rs1_value, rs2_value]

        return [False, "NO", 0, self.registerobj.get_register(rs1), self.registerobj.get_register(rs2)]

    def detectHazardS(self, id, rs1 = 0, rs2 = 0): # stalling

        rdprev1 = self.obj.get(3)[2] #execute buffer rd
        rdprev2 = self.obj.get(4)[2] #memory buffer rd

        prevtype1 = self.obj.get(3)[0] #lw, lh, lb #stalling
        prevtype2 = self.obj.get(4)[0] #MM

        #return [ifHazard, type, stalls]  returned type for printing
        if rs1 == rs2 == 0:
            return [False, "NO", 0]
        
        if rdprev1 == 0:
            rdprev1 = -1

        if rdprev2 == 0:
            rdprev2 = -1

        if rdprev1 == rdprev2 == -1:
            return [False, "NO", 0]

        if 12<= prevtype1 <=14 and 15 <= id <= 17 and rdprev1 in [rs1, rs2]: #load then store(15<=id<=17)
            return [True, "MM", 1] #MM

        if 12<=prevtype1<=14 and rdprev1 in [rs1, rs2]: #if the prev were load type and we use it then we need to stall
            return [True, "ME", 2] #ME

        if 12<=prevtype2<=14 and rdprev2 in [rs1, rs2]: #if the previous of previous were load then M->E beginning
            return [True, "ME", 1]

        if rdprev1 in [rs1, rs2]: #E->E
            return [True, "EE", 2]

        if rdprev2 in [rs1, rs2]: #M->E
            return [True, "ME", 1]

        return [False,"NO", 0]

    def dataForwarding(self, id, rs1, rs2):
        
        return self.detectHazard(id, rs1, rs2)[1:]
    
    def stalling(self, id, rs1, rs2):

        return self.detectHazardS(id, rs1, rs2)[1:]

        
        
