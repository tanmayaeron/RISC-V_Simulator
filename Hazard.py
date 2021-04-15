from collections import defaultdict


class HDU:
    """
    we are making dictionaries for cycle as key 
    F->IR
    D->rd -> number
    E->RZ -> number, change type from string
    ME->RY -> number, change type from string 
    WB->rd
    """

    def __init__(self):
        self.dict = defaultdict(int)

    def isHazard(self, cycle, rs1 = -1, rs2 = -2, rd = -3): #don't call for branch instruction beq, blt
        if rd == 0:
            return False  # no hazard as x0 register
        rdprev1 = self.dict[(2,cycle-1)] if self.dict[(2,cycle-1)] else -4 # (stage, cycle number)
        rdprev2 = self.dict[(2,cycle-2)] if self.dict[(2,cycle-2)] else -5
        return False if len(set([rs1, rs2, rdprev1, rdprev2])) == 4 else True

    def set_hdu(self, cycle, stage, result):
        if type(result) == str:
            result = int(result, 16)
        self.dict[(stage, cycle)] = result

    def RAW(self):
        #M->E
        #Eend->Estart
        #M->M
        pass