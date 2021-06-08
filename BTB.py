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
import sys
# backward:
# beq x11,x12, backward
# # RZ = 0
# # self.predicted[PC] = 1
"""
0 SNT
1 WNT
2 WT
3 ST


not taken = max(0,prev-1)
taken = min(3,prev+1)
"""
"""
0 not taken;
1 taken;

not taken = 0
taken = 1[functiontype, st]
"""
class BTB:

    def __init__(self,isBTB,muxPC,muxS, initialState=[2,0]):
        """
        initialState[0] is 0 or 1 and is the initial state of one bit branch predictor
        initialState[1] is 0(SNT) 1(WNT) 2(WT) or 3(ST) and is the initial state of two bit branch predictor
        functiontype is 0 for all taken 1 (all not taken) 2 (btfnt) 3(one bit predictor) 4(two bit branch predictor)
        """
        self.lookup = defaultdict(int)
        # sys.stderr.write(str(initialState)+"\n")
        #  branch and jal instruction in self.lookup
        self.predicted = defaultdict(int)
        self.isBTB = isBTB
        self.muxPC = muxPC
        self.muxS  = muxS
        self.stateOneBit= defaultdict(lambda: initialState[1])
        self.stateTwoBit = defaultdict(lambda: initialState[1])
        self.function=[self.addtoAllTaken,self.addtoAllNotTaken,self.addInstructionBTFNT,self.oneBitBranchPredictor,self.twoBitBranchPredictor]
        self.functiontype=initialState[0]
        

    # prediction - 1 -> Taken
    # prediction - 0 -> Not Taken
    
    def isImmediatePositive(self,imm):
        # returns 1 if imm is greater than 0
        # imm is in hex and sign extended
        return int(imm[0],16)<8

    def predict(self, PC):
        return [True, self.lookup[PC]] if PC in self.lookup else [False, "0"*8]

    def updatepredict(self,PC, target, PC_temp):
        if self.functiontype ==3:
            self.predicted[PC] = True if self.stateOneBit[PC] else False
            self.lookup[PC] = target if self.stateOneBit[PC] else PC_temp
        elif self.functiontype==4:
            self.predicted[PC] = True if self.stateTwoBit[PC] in [2,3] else False
            self.lookup[PC] = target if self.stateTwoBit[PC] in [2,3] else PC_temp
    
    def isFlush(self, PC, RZ, currOpID, target, PC_temp):
        # True means Flush
        # False means we do not flush
        if self.isBTB[currOpID] or self.muxPC[currOpID]:

            if self.muxS[currOpID]: #branch

                if PC not in self.lookup: #if PC was not in lookup, it's assumed not taken
                    #if RZ == 0 then that was correct
                    if int(RZ[-1],16) == 0:
                        return False
                    return True
                
                if int(RZ[-1],16)==1:
                    self.stateTwoBit[PC] = min(3, self.stateTwoBit[PC] + 1)
                elif int(RZ[-1],16) == 0:
                    self.stateTwoBit[PC] = max( 0, self.stateTwoBit[PC] - 1)

                self.stateOneBit[PC] = int(RZ[-1],16)

                if self.predicted[PC] == False and int(RZ[-1],16) == 1:
                    
                    self.updatepredict(PC, target, PC_temp)
                    return True

                if self.predicted[PC] == True and int(RZ[-1],16) == 0:
                    self.updatepredict(PC, target, PC_temp)
                    return True
            
                self.updatepredict(PC, target, PC_temp)
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
        """
        0 all taken
        1 all not taken
        2 BTFNT
        3 one bit
        4 two bit
        """
        self.function[self.functiontype]( PC, PC_temp, imm, target, currOpID)

        

    def addInstructionBTFNT(self, PC, PC_temp, imm, target, currOpID):
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

    def twoBitBranchPredictor(self,PC, PC_temp, imm, target, currOpID):
        if not self.isBTB[currOpID]:
            return
        
        if PC not in self.lookup:
            if self.muxS[currOpID]:
                self.lookup[PC] = target if self.stateTwoBit[PC] in [2,3] else PC_temp
                self.predicted[PC] = True if self.stateTwoBit[PC] in [2,3] else False
                # if it is in lookup and positive then we predict it as False and take the next instruction(pc_temp)
                # else we predict it as true and and take the target
            elif self.isBTB[currOpID] and not self.muxS[currOpID]:
                self.lookup[PC] = target
                self.predicted[PC] = True
                # it is jal instruction and so we take the target

    def oneBitBranchPredictor(self,PC, PC_temp, imm, target, currOpID):
        if not self.isBTB[currOpID]:
            return
        
        if PC not in self.lookup:
            if self.muxS[currOpID]:
                self.lookup[PC] = target if self.stateOneBit[PC] else PC_temp
                self.predicted[PC] = True if self.stateOneBit[PC] else False
                # if it is in lookup and positive then we predict it as False and take the next instruction(pc_temp)
                # else we predict it as true and and take the target
            elif self.isBTB[currOpID] and not self.muxS[currOpID]:
                self.lookup[PC] = target
                self.predicted[PC] = True
                # it is jal instruction and so we take the target
    

    
    def addtoAllTaken(self, PC, PC_temp, imm, target, currOpID):
        if not self.isBTB[currOpID]:
            return
        
        if PC not in self.lookup:
            if self.muxS[currOpID]:

                self.lookup[PC] = target
                self.predicted[PC] = True
                
            elif self.isBTB[currOpID] and not self.muxS[currOpID]:
                self.lookup[PC] = target
                self.predicted[PC] = True
                # it is jal instruction and so we take the target

    def addtoAllNotTaken(self, PC, PC_temp, imm, target, currOpID):
        if not self.isBTB[currOpID]:
            return
        
        if PC not in self.lookup:
            if self.muxS[currOpID]:

                self.lookup[PC] = PC_temp
                self.predicted[PC] = False

            elif self.isBTB[currOpID] and not self.muxS[currOpID]:

                self.lookup[PC] = target
                self.predicted[PC] = True
                # it is jal instruction and so we take the target


    def clearBTB(self):
        self.lookup.clear()
        self.predicted.clear()
        self.stateOneBit.clear()
        self.stateTwoBit.clear()

if __name__ == "__main__":
    btb = BTB()
    imm = "7FFFFFFC"
    print(btb.isImmediatePositive(imm))
