from collections import defaultdict

"""
    normal
    normal

    sw
    normal

    lw
    normal

lw x10 add
sw x10 add //hazard


    lw  x10 add // addi x10 x10 x10
    sw x10 adress2 M->M

    addi x10 
    lw x10 add //1 stalling
    sw x11 0(x10)

        sw x10 add //no hazard
        lw x11 add
"""

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
        self.dict = defaultdict(int)

    def isHazard(self, cycle, rs1 = -1, rs2 = -2, rd = -3): #don't call for branch instruction beq, blt
        if rd == 0:
            return False  # no hazard as x0 register
        
        if self.dict[(6,cycle-1)] and (self.dict[(2,cycle-1)] == rs2 and rs2):
            return True
        
        rdprev1 = self.dict[(2,cycle-1)] if self.dict[(2,cycle-1)] else -4 # (stage, cycle number)
        rdprev2 = self.dict[(2,cycle-2)] if self.dict[(2,cycle-2)] else -5
        return False if len(set([rs1, rs2, rdprev1, rdprev2])) == 4 else True

    def set_hdu(self, cycle, stage, result, ifload = False, ifstore = False):
        if type(result) == str:
            result = int(result, 16)
        if ifload:
            self.dict[(6,cycle)] = 1
        if ifstore:
            self.dict[(7,cycle)] = 1
        self.dict[(stage, cycle)] = result

    def RAW(self):
        #M->E
        #Eend->Estart
        #M->M
        pass
