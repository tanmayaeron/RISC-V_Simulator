from collections import defaultdict
# beq x11,x11,fib
# addi x11,x11,10
# fib:
# # runs for the second time
# # RZ = 1
# # self.predicted[PC] = 0
# # our prediction = False and flush = True we are correct


# back:
# beq x11,x11, back

# # RZ =1
# # self.predicted[PC] = 1
# # our prediction = True and Flush = False


# backward:
# beq x11,x12, backward
# # RZ = 0
# # self.predicted[PC] = 1

class BTB:

    def __init__(self):
        self.lookup = defaultdict(int)
        #  branch and jal instruction in self.lookup
        self.predicted = defaultdict(lambda: -1)
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

    def isFlush(self, PC, RZ, isJalr, S_Select, isBTB):
        # True means Flush
        # False means we do not flush
        
        if PC not in self.lookup and isBTB:
            # if the jump or branch instruction is occuring for the first time we return True
            return True
        
        elif isJalr:
            # we always Flush in jalr
            return True
        
        elif not isBTB:
            return False

        elif not S_Select:
            # this instruction is JAL as isBTB is True and not sselect
            # we dont flush as jal if jal comes ( when it comes for the first time is checked earlier)
            return False
        
        elif self.predicted[PC] != int(RZ[-1],16):
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
