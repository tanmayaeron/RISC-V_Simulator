
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

    def isHazard(self, cycle, rs1=-1, rs2=-2, rd=-3):
        # don't call for branch instruction beq, blt
        if rd == 0:
            return False  # no hazard as x0 register
        # (stage, cycle number)
        rdprev1 = self.dict[(2, cycle-1)] if self.dict[(2, cycle-1)] else -4
        rdprev2 = self.dict[(2, cycle-2)] if self.dict[(2, cycle-2)] else -5
        return False if len(set([rs1, rs2, rdprev1, rdprev2])) == 4 else True

    def isAfterLoadHazard(self, cycle, rs1=-1, rs2=-1, rd=-3):
        # load then store hazard
        """
        li x12 0x1000000
        ld x11,0(x12)
        addi x11,x11,x11
        """
        if rd == 0:
            return False  # no hazard as x0 register
        rdprev1 = self.dict[(2, cycle-1)] if self.dict[(2, cycle-1)] else -4
        rdprev2 = self.dict[(2, cycle-2)] if self.dict[(2, cycle-2)] else -5
        rdprev3 = self.dict[(2, cycle-3)] if self.dict[(2, cycle-3)] else -6
        return False if len(set([rs1, rs2, rdprev1, rdprev2, rdprev3])) == 5 else True

    def isStoreLoadHazard(self, cycle, rs1=-1, rs2=-1, rd=-3):
        """
        sw x11,0(x12)
        lw x12,0(x12)
        """
        if rd == 0:
            return False  # no hazard as x0 register

        pass

    def set_hdu(self, cycle, stage, result):

        self.dict[(stage, cycle)] = result if type(result) == str else result = int(result, 16)

    def RAW(self):
        # M->E
        # Eend->Estart
        # M->M
        pass
