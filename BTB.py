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
        # initialized to -1 as it is matched to RZ which has value either 1 or 0

    # prediction - 1 -> Taken
    # prediction - 0 -> Not Taken
    # isBTB for jump and branch
    # S_Select  for branch
    # isBTB is True and S_Select is False means jal
    
    def isImmediatePositive(self,imm):
        # returns 1 if imm is greater than 0
        # imm is in hex and sign extended
        return int(imm[0],16)<8

    def predict(self, PC):
        return [True, self.lookup[PC]] if PC in self.lookup else [False, "0"*8]

    def isFlush(self, PC, RZ, isJalr, S_Select, isBTB):
        # True means Flush
        # False means we do not flush
        
        if PC not in self.lookup and isBTB:
            # if the jump or branch instruction is occuring for the first time we return True
            # because our prediction for the first time is False
            return True
        
        elif isJalr:
            # we always Flush in jalr
            return True
        
        elif not isBTB:
            # if it is any other instruction like add etc we do not flush
            return False

        elif not S_Select:
            # JAL instruction
            # this instruction is JAL as isBTB is True and sselect if False
            # we dont flush as jal comes as this is not the first occurence of jal (when it comes for the first time is checked earlier)
            return False
        
        elif self.predicted[PC] != int(RZ[-1],16):
            # if our prediction is False we Flush
            return True
        
        # our prediction is True and so we do not flush
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

    def clearBTB(self):
        self.lookup.clear()
        self.predicted.clear()
