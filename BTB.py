from collections import defaultdict


class BTB:

    def __init__(self):
        self.lookup = defaultdict(int)
        
        #  branch and jal instruction in self.lookup
        
        self.predicted = defaultdict(int)
        # stores True if taken else False

    # prediction - 1 -> Taken
    # prediction - 0 -> Not Taken
    # isBTB for jump and branch
    # S_Select  for branch
    def isImmediatePositive(self,imm):
        # returns 1 if imm is greater than 0
        # imm is in hex and sign extended
        return int(imm[0],16)>=8

    def predict(self, PC ):
        
        return [True, self.lookup[PC]] if PC in self.lookup else [False, "0"*8]

    def HitMiss(self, RZ, PC):
        # prediction 
        if self.lookup[PC] == RZ:
            return True
        return False

    def addInstruction(self, PC, PC_temp, imm, target, S_Select, isBTB):
        if PC not in self.lookup:

            if S_Select:
                self.lookup[PC] = PC_temp if self.isImmediatePositive(imm) else target
                self.predicted[PC] = False if self.isImmediatePositive(imm) else True
                # if it is in lookup and positive then we predict it as False and take the next instruction(pc_temp)
                # else we predict it as true and and take the target
            elif isBTB:
                self.lookup[PC] = target
                self.predicted[PC] = True
                # it is jal instruction and so we take the target

    def ifSetInstruction(self,PC):
        return PC in self.lookup
