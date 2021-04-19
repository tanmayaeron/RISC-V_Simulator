from collections import defaultdict
from register import RegisterFile
class Buffer:

    def __init__(self):
        self.dict = {}
    
    def fetchB(self, PC, IR):
        self.dict[1] = PC, IR

    #instruction -> index of instruction in csv, PC, RA, RB->hex string, rd -> destination register = -1
    def decodeB(self, id, PC , RA = "0"*8, RB = "0"*8, RM = "0"*8, rd = -1):
        #those who don't have rd should give -1 to this function, decode update
        self.dict[2] = id, PC, RA, RB, RM, rd

    def executeB(self, id, RZ, rd, RM): #RZ, rd #dict[3][1]
        self.dict[3] = id, RZ, rd, RM # RZ is the result

    def memoryB(self, id, RY, rd): #RY, rd #dict[4][1]
        self.dict[4] = id, RY, rd # RY is the result

    def get(self, stage):
        if stage in self.dict:
            return self.dict[stage]
        return (-1, -1, -1, -1, -1, -1)

    def ifPresent(self, stage): #erased buffers won't be accessed and we'll get out of that stage
        if stage in self.dict:
            return True
        return False

    def flush(self):
        self.dict.clear()

    def clearStage(self, stage):
        #delete dict[1] dict[2] and so on
        if stage in self.dict:
            del self.dict[stage]


class HDU:
    """
    F->IR -> string
    D->rd -> number
    E->RZ -> string
    M->RY -> string
    W->rd -> no need here
    """

    def __init__(self, bufferobj):
        self.obj = bufferobj #bufferobj
        
    def detectHazard(self, id, rs1 = 0, rs2 = 0): #data forwarding
        # dict[3] or dict[4] #rdprev1, rdprev2
        
        if id == 24 or id == 25: #if the instruction is lui or auipc, no forwarding/stalling
            return [False, "NO", 0]

        rdprevbranch = self.obj.get(2)[5] #decode buffer rd, one stall in branch
        rdprev1 = self.obj.get(3)[2] #execute buffer rd
        rdprev2 = self.obj.get(4)[2] #memory buffer rd

        prevtype1 = self.obj.get(3)[0] #lw, lh, lb #stalling
        prevtype2 = self.obj.get(4)[0] #MM
        
        # return [ifHazard, type of hazard, no of stalls, rs1value, rs2value]
        if rs1 == rs2 == 0:
            return [False, "NO", 0]
        
        if rdprev1 == 0:
            rdprev1 = -1

        if rdprev2 == 0:
            rdprev2 = -1

        if 18 <= id <= 21: #branch
            if rdprevbranch in [rs1, rs2]: #one stall case
                return [True, "ED", 1]
            if rdprev1 in [rs1, rs2]:
                rs1_value = self.registerobj.get_register(rs1) if rs1!=rdprev1 else self.obj.get(3)[1]
                rs2_value = self.registerobj.get_register(rs2) if rs2!=rdprev1 else self.obj.get(3)[1]
                return [True, "ED", 0]
            if rdprev2 in [rs1, rs2]:
                rs1_value=self.registerobj.get_register(rs1) if rs1!=rdprev2 else self.obj.get(4)[1]
                rs2_value=self.registerobj.get_register(rs2) if rs2!=rdprev2 else self.obj.get(4)[1]
                return [True, "MD", 0]
        
        if rdprev1 == rdprev2 == -1:
            return [False, "NO", 0]

        if 12 <= prevtype1 <= 14 and 15 <= id <= 17 and rdprev1 == rs2 and rdprev1 != rs1: #load then store
            """
            lw x10,0(x11)
            sw x10,0(x11) # rs1+imm and rs2==rdprev1
            """
            return [True, "MM", 0] #MM

        if 12<=prevtype1<=14 and rdprev1 in [rs1, rs2]: #if the prev were load type and we use it then we need to stall
            return [True, "ME", 1] # inf value, check after stall cycle to get original value

        if 12<=prevtype2<=14 and rdprev2 in [rs1, rs2]: #if the previous of previous were load then M->E beginning
            rs1_value=self.registerobj.get_register(rs1) if rs1!=rdprev2 else self.obj.get(4)[1]
            rs2_value=self.registerobj.get_register(rs2) if rs2!=rdprev2 else self.obj.get(4)[1]
            return [True, "ME", 0]

        if rdprev1 in [rs1, rs2]: #E->E
            rs1_value=self.registerobj.get_register(rs1) if rs1!=rdprev1 else self.obj.get(3)[1]
            rs2_value=self.registerobj.get_register(rs2) if rs2!=rdprev1 else self.obj.get(3)[1]
            return [True, "EE", 0]

        if rdprev2 in [rs1, rs2]: #M->E
            rs1_value=self.registerobj.get_register(rs1) if rs1!=rdprev2 else self.obj.get(4)[1]
            rs2_value=self.registerobj.get_register(rs2) if rs2!=rdprev2 else self.obj.get(4)[1]
            return [True, "ME", 0]

        return [False, "NO", 0]

    def detectHazardS(self, id, rs1 = 0, rs2 = 0): # stalling
        
        if id == 24 or id == 25:
            return [False, "NO", 0]

        rdprev1 = self.obj.get(3)[2] #execute buffer rd
        rdprev2 = self.obj.get(4)[2] #memory buffer rd

        prevtype1 = self.obj.get(3)[0] #lw, lh, lb #stalling
        prevtype2 = self.obj.get(4)[0] #MM

        #return [ifHazard, type, no of stalls]  returned type for printing
        if rs1 == rs2 == 0:
            return [False, "NO", 0]
        
        if rdprev1 == 0:
            rdprev1 = -1

        if rdprev2 == 0:
            rdprev2 = -1

        if 18 <= id <= 21: #branch
            
            if rdprev1 in [rs1, rs2]:
                return [True, "EE", 2]
            if rdprev2 in [rs1, rs2]:
                return [True, "ME", 1]

        if rdprev1 == rdprev2 == -1:
            return [False, "NO", 0]

        if 12<= prevtype1 <=14 and 15 <= id <= 17 and rdprev1 == rs2 and rdprev1 != rs1: #load then store(15<=id<=17)
            return [True, "MM", 1] #MM

        if 12 <= prevtype1 <= 14 and rdprev1 in [rs1, rs2]: #if the prev were load type and we use it then we need to stall
            return [True, "ME", 2] #ME

        if 12 <= prevtype2 <= 14 and rdprev2 in [rs1, rs2]: #if the previous of previous were load then M->E beginning
            return [True, "ME", 1]

        if rdprev1 in [rs1, rs2]: #E->E
            return [True, "EE", 2]

        if rdprev2 in [rs1, rs2]: #M->E
            return [True, "ME", 1]

        return [False,"NO", 0]

    def dataForwarding(self, id, rs1, rs2):
        return self.detectHazard(id, rs1, rs2)
    
    def stalling(self, id, rs1, rs2):
        return self.detectHazardS(id, rs1, rs2)
    
    def getDataFromBuffer(i):
        return obj.get(i)
        

if __name__ == "__main__":
    Buffer=Buffer()
    register = RegisterFile()
    HDU = HDU(Buffer,register)
    
    
    #Test case 1: NO
    #     addi x10,x11,1 #  F D E M W
    #     addi x10,x10,1 #    F D E M W
    # Buffer.executeB(9, "0"*7+"1", 10, "0"*8)
    # l = HDU.detectHazard(9, 10, 3)
    # print(l)
    
    #Test case 2: NO
    #     sw x10,0(x10)
    #     sw x11,0(x11)
    # Buffer.executeB(17, "0"*7+"1", 0, "0"*8)
    # l = HDU.detectHazard(17, 11, 11)
    # print(l)
    
    #Test case 3: NO
    #     sw x10,0(x10)
    #     sw x11,0(x10)
    # Buffer.executeB(17, "0"*7+"1", 0, "0"*8)
    # l = HDU.detectHazard(17, 11, 10)
    # print(l)
    
    #Test case 4: M->M
    #   lw x10,0(x9) 
    #   sw x11,0(x10) 
    # rdprev1 = x10= rs1 so hazard # 15 <= id <= 17 
    # Buffer.executeB(14, "0"*7+"1", 10, "0"*8)
    # l = HDU.detectHazard(17, 11, 10)
    # print(l)
    
    #Test case 5: M->E and 1 stall
    #    lw x10,0(x9) # 15 <= id <= 17 
    #    add x11,x10,x10 
    # rdprev1 = x10= rs1 so hazard # 15 <= id <= 17 
    # Buffer.executeB(14, "0"*7+"1", 10, "0"*8)
    # l = HDU.detectHazard(0, 10, 10)
    # print(l)
    
    #Test case 6: M->E
    #    lw x10,0(x9) # 15 <= id <= 17 
    #    add x0,x0,x0
    #    add x11,x10,x10 
    # rdprev1 = x10= rs1 so hazard # 15 <= id <= 17 
    # Buffer.memoryB(14, "0"*7+"1", 10)
    # Buffer.executeB(0, "0"*7+"1", 0, "0"*8)
    # l = HDU.detectHazard(0, 10, 11)
    # print(l)        
    
    #Test case 7: E->E
    #    addi x10,x0,10
    #    add x11,x10,x10 
    # rdprev1 = x10= rs1 so hazard # 15 <= id <= 17 
    # Buffer.executeB(9, "0"*7+"1", 10, "0"*8)
    # l = HDU.detectHazard(0, 10, 10)
    # print(l)  
    
    #Test case 8: M->E
    #    addi x10,x0,10 # 15 <= id <= 17 
    #    add x31,x0,x0
    #    add x11,x10,x10 
    # rdprev1 = x10= rs1 so hazard # 15 <= id <= 17 
    # Buffer.memoryB(9, "0"*7+"2", 10)
    # Buffer.executeB(0, "0"*7+"1", 31, "0"*8)
    # l = HDU.detectHazard(0, 10, 10)
    # print(l)
    
    #Test case 9: M->E
    #    add x4,x5,x6 # 15 <= id <= 17 
    #    add x9,x7,x8
    #    beq x9,x4,label 
    # rdprev1 = x10= rs1 so hazard # 15 <= id <= 17 
    # Buffer.memoryB(0, "0"*7+"2", 4)
    # Buffer.executeB(0, "0"*7+"1", 9, "0"*8)
    # l = HDU.detectHazard(18, 0, 4)
    # print(l)
    # l = HDU.detectHazard(18, 9, 0)
    # print(l)
