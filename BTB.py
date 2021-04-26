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

    def __init__(self,isBTB,muxPC,muxS):
        self.lookup = defaultdict(int)
        #  branch and jal instruction in self.lookup
        self.predicted = defaultdict(lambda: 0)
        self.isBTB = isBTB
        self.muxPC = muxPC
        self.muxS  = muxS

        # stores True if taken else False
        # initialized to -1 as it is matched to RZ which has value either 1 or 0

    # prediction - 1 -> Taken
    # prediction - 0 -> Not Taken
    
    def isImmediatePositive(self,imm):
        # returns 1 if imm is greater than 0
        # imm is in hex and sign extended
        return int(imm[0],16)<8

    def predict(self, PC):
        return [True, self.lookup[PC]] if PC in self.lookup else [False, "0"*8]

    def isFlush(self, PC, RZ, currOpID):
        # True means Flush
        # False means we do not flush
        if self.isBTB[currOpID] or self.muxPC[currOpID]:

            if self.muxS[currOpID]: #branch

                if PC not in self.lookup: #if PC was not in lookup, it's assumed not taken
                    #if RZ == 0 then that was correct
                    if int(RZ[-1],16) == 0:
                        return False
                    return True
                
                if self.predicted[PC] == False and int(RZ[-1],16) == 1:
                    return True
                if self.predicted[PC] == True and int(RZ[-1],16) == 0:
                    return True
                
                return False
            
            elif self.isBTB[currOpID] and not self.muxS[currOpID]: #jal

                if PC not in self.lookup:
                    return True
                else:
                    return False
                
            else: #jalr
                return True
        else:
            return False

    def addInstruction(self, PC, PC_temp, imm, target, currOpID):
        if not self.isBTB[currOpID]:
            return
        
        if PC not in self.lookup:
            if self.muxS[currOpID]:
                self.lookup[PC] = PC_temp if self.isImmediatePositive(imm) else target
                self.predicted[PC] = False if self.isImmediatePositive(imm) else True
                # if it is in lookup and positive then we predict it as False and take the next instruction(pc_temp)
                # else we predict it as true and and take the target
            elif self.isBTB[currOpID] and not self.muxS[currOpID]:
                self.lookup[PC] = target
                self.predicted[PC] = True
                # it is jal instruction and so we take the target

    def ifSetInstruction(self,PC):
        return PC in self.lookup

    def clearBTB(self):
        self.lookup.clear()
        self.predicted.clear()

if __name__ == "__main__":
    btb = BTB()
    imm = "7FFFFFFC"
    print(btb.isImmediatePositive(imm))
