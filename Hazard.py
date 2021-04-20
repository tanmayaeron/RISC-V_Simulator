import pandas as pd

class Buffer:

    def __init__(self):
        self.dict = {}
    
    """
        buffers are set after their repective stages, fetch after the fetch stage and so on
        set after each cycle
    """
    def fetchB(self, PC, IR):
        self.dict[1] = PC, IR

    #instruction -> index of instruction in csv, PC, RA, RB->hex string, rd -> destination register = -1
    def decodeB(self, id, PC , rs1, rs2, RA = "0"*8, RB = "0"*8, RM = "0"*8, rd = -1):
        #those who don't have rd should give -1 to this function, decode update
        #TO_NOTE: we need to access HDU from inside the decode for branch instructions
        #we also need rs1, rs2 in later stages
        self.dict[2] = id, PC, RA, RB, RM, rd, rs1, rs2 #RM contains the value of rs2 by default if it's not to be written then ME = 0
        #RA and RB may not be used and rejected by muxes

    def executeB(self, id, RZ, rd, RM, rs1, rs2):
        #included rs1, rs2 in the after execute buffer, this will be needed for X->M forwarding/stalling
        self.dict[3] = id, RZ, rd, RM, rs1, rs2 # RZ is the result

    def memoryB(self, id, RY, rd): #RY, rd #dict[4][1]
        self.dict[4] = id, RY, rd # RY is the result

    def get(self, stage):
        if stage in self.dict:
            return self.dict[stage]
        return (-1, -1, -1, -1, -1, -1, -1, -1) #the Buffer is empty and shouldn't be accessed

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

    def __init__(self, df_control):
        self.df_control = df_control #read csv and pass to HDU object
        self.initialiseControls()
    
    def initialiseControls(self):
        self.isDecoders1 = list(self.df_control['rs1D'].astype(int))
        self.isDecoders2 = list(self.df_control['rs2D'].astype(int))
        self.isExecuters1 = list(self.df_control['rs1E'].astype(int))
        self.isExecuters2 = list(self.df_control['rs2E'].astype(int))
        self.isMemoryrs1 = list(self.df_control['rs1M'].astype(int))
        self.isMemoryrs2 = list(self.df_control['rs2M'].astype(int))
        
    def detectHazard(self, bufferobj, id, stage, rs1 = 0, rs2 = 0): #data forwarding
        #passing the 'stage' to it to confirm with csv if we need to do dataforwarding for the instruction
        #in the given stage, if not we set those to 0
        
        if id == 24 or id == 25: #if the instruction is lui or auipc, no forwarding/stalling
            return [False, "NO", 0]

        if stage == 2: #decode stage # called inside the decode, only valid for branch instructions
            rs1 = rs1 if self.isDecoders1[id] == 1 else 0
            rs2 = rs2 if self.isDecoders2[id] == 1 else 0
        elif stage == 3: #before execute stage
            rs1 = rs1 if self.isExecuters1[id] == 1 else 0
            rs2 = rs2 if self.isExecuters2[id] == 1 else 0
        elif stage == 4: #before memory stage
            rs1 = rs1 if self.isMemoryrs1[id] == 1 else 0
            rs2 = rs2 if self.isMemoryrs2[id] == 1 else 0
        else:
            return [False, "NO", 0]

        #print("rs1 :"+rs1, "rs2 :"+rs2)
        print(rs1, rs2)
        if rs1 == rs2 == 0:
            return [False, "NO", 0]

        decodeBufferID = bufferobj.get(2)[0]
        executeBufferID = bufferobj.get(3)[0]
        memoryBufferID = bufferobj.get(4)[0]

        rdDecodeBuffer = bufferobj.get(2)[5] #rd of decode in the last cycle
        #decode buffer rd, one stall in branch

        rdExecuteBuffer = bufferobj.get(3)[2] #rd of execute in the last cycle
        #execute buffer rd

        rdMemoryBuffer = bufferobj.get(4)[2] #rd of the mem stage of the last cycle
        #memory buffer rd
        
        if rdDecodeBuffer == 0:
            rdDecodeBuffer = -1

        if rdExecuteBuffer == 0:
            rdExecuteBuffer = -1

        if rdMemoryBuffer == 0:
            rdMemoryBuffer = -1

        """
        F D E M W        lw x10 add
          F     D E M W  beq x10 x9 label #2 stall case

        F D E M W      addi x10 x0 9
          F   D E M W  beq x10 x9 label #1 stall case

        F D E M W      addi x10 x0 9 
          F D E M W    random instr
            F D E M W  beq x10 x9 label # at the start of decode x10 is in execute buffer, data forward E->D start
        """

        if rdExecuteBuffer == rdMemoryBuffer == rdDecodeBuffer == -1:
            return [False, "NO", 0]


        if 18 <= id <= 21 or id == 23: #branch This needs to be checked inside the decode stage
            #NOTE_TO_SELF -> this will need to be called inside the decode
            if 12 <= decodeBufferID <= 14 and rdDecodeBuffer in [rs1,rs2]:
                return [True, "MD", 2] #take from M buffer after 2 stalls, stall F and D

            if rdDecodeBuffer in [rs1, rs2]: #one stall case
                return [True, "ED", 1] #we take from E after one cycle and stall F and D

            if rdExecuteBuffer in [rs1, rs2]:
                return [True, "ED", 0]

            if rdMemoryBuffer in [rs1, rs2]:
                return [True, "MD", 0]
            
            return [False, "NO", 0] #the branch doesn't cause a data hazard
        
        if rdExecuteBuffer == rdMemoryBuffer == -1:
            return [False, "NO", 0]

        if 12 <= executeBufferID <= 14 and 15 <= id <= 17 and rdExecuteBuffer == rs2 and rdExecuteBuffer != rs1: #load then store
            """
            lw x10,0(x11)
            sw x10,0(x11) # rs1+imm and rs2==rdprev1
            """
            return [True, "MM", 0] #MM

        if 12 <= executeBufferID <= 14 and rdExecuteBuffer in [rs1, rs2]: #if the prev were load type and we use it then we need to stall
            return [True, "ME", 1] # inf value, check after stall cycle to get original value

        if 12 <= memoryBufferID <= 14 and rdMemoryBuffer == rs2 and stage == 4:
            return [True, "MM", 0]

        if 12 <= memoryBufferID <= 14 and rdMemoryBuffer == rs2:
            return [True, "ME", 0]

        if rdExecuteBuffer in [rs1, rs2]: #E->E
            return [True, "EE", 0]

        if rdMemoryBuffer in [rs1, rs2]: #M->E
            return [True, "ME", 0]

        return [False, "NO", 0]

    def detectHazardStall(self, bufferobj, id, stage, rs1 = 0, rs2 = 0):
        #in case of only stalling
        #passing the 'stage' to it to confirm with csv if we need to do dataforwarding for the instruction
        #in the given stage, if not we set those to 0
        
        if id == 24 or id == 25: #if the instruction is lui or auipc, no forwarding/stalling
            return [False, "NO", 0]

        if stage == 2: #decode stage # called inside the decode, only valid for branch instructions
            rs1 = rs1 if self.isDecoders1[id] == 1 else 0
            rs2 = rs2 if self.isDecoders2[id] == 1 else 0
        elif stage == 3: #execute stage
            rs1 = rs1 if self.isExecuters1[id] == 1 else 0
            rs2 = rs2 if self.isExecuters2[id] == 1 else 0
        elif stage == 4: #memory stage
            rs1 = rs1 if self.isMemoryrs1[id] == 1 else 0
            rs2 = rs2 if self.isMemoryrs2[id] == 1 else 0
        else:
            return [False, "NO", 0]

        if rs1 == rs2 == 0:
            return [False, "NO", 0]

        decodeBufferID = bufferobj.get(2)[0]
        executeBufferID = bufferobj.get(3)[0]
        memoryBufferID = bufferobj.get(4)[0]

        rdDecodeBuffer = bufferobj.get(2)[5] #rd of decode in the last cycle
        #decode buffer rd, one stall in branch

        rdExecuteBuffer = bufferobj.get(3)[2] #rd of execute in the last cycle
        #execute buffer rd

        rdMemoryBuffer = bufferobj.get(4)[2] #rd of the mem stage of the last cycle
        #memory buffer rd
        
        if rdDecodeBuffer == 0:
            rdDecodeBuffer = -1

        if rdExecuteBuffer == 0:
            rdExecuteBuffer = -1

        if rdMemoryBuffer == 0:
            rdMemoryBuffer = -1

        """
        explanation for branch instruction data hazard handling in stall case

        F D E M W          lw x10 add
          F       D E M W  beq x10 x9 label #3 stalls

        F D E M W          addi x10 x0 9
          F       D E M W  beq x10 x9 label #3 stalls

        F D E M W          addi x10 x0 9 
          F D E M W        random instr
            F     D E M W  beq x10 x9 label #2 stalls

        F D E M W          addi x10 x0 9 
          F D E M W        random instr
            F D E M W      random instr 2
              F   D E M W  beq x10 x9 label #1 stall
        """

        if rdExecuteBuffer == rdMemoryBuffer == rdDecodeBuffer == -1:
            return [False, "NO", 0]


        if 18 <= id <= 21 or id == 23: #branch This needs to be checked inside the decode stage
            #NOTE_TO_SELF -> this will need to be called inside the decode

            #the next 2 cases have the same stall in data stalling
            if 12 <= decodeBufferID <= 14 and rdDecodeBuffer in [rs1,rs2]:
                return [True, "MD", 3] #3 stalls, stall F and D

            if rdDecodeBuffer in [rs1, rs2]: #one stall case
                return [True, "ED", 3] #3 stalls, stall F and D

            if rdExecuteBuffer in [rs1, rs2]:
                return [True, "ED", 2] #2 stalls, stall F and D

            if rdMemoryBuffer in [rs1, rs2]:
                return [True, "MD", 1] #1 stall, stall F and D
            
            return [False, "NO", 0] #the branch doesn't cause a data hazard
        
        if rdExecuteBuffer == rdMemoryBuffer == -1:
            return [False, "NO", 0]

        if 12 <= executeBufferID <= 14 and 15 <= id <= 17 and rdExecuteBuffer == rs2 and rdExecuteBuffer != rs1: #load then store
            """
            lw x10,0(x11)
            sw x10,0(x11) # rs1+imm and rs2 == rdExecuteBuffer

            F D E M W          lw x10 address
              F D E   M W      sw x10, 0(x11)

            """
            return [True, "MM", 1] #1 stall, W works, rest stall


        """
        F D E M W          lw x10 address
          F D     E M W    addi x9 x10 1

          #2 stalls
        """
        if 12 <= executeBufferID <= 14 and rdExecuteBuffer in [rs1, rs2]: #if the prev were load type and we use it then we need to stall
            return [True, "ME", 2] #2 stall, M and WB works in the next two cycles

        """
        F D E M W        lw x10 address
          F D E M W      random instruction
            F D   E M W  addi x9 x10 1
          #1 stalls
        """

        if 12 <= memoryBufferID <= 14 and rdMemoryBuffer == rs2 and stage == 4:
            return [True, "MM", 1] #1 stall

        if 12 <= memoryBufferID <= 14 and rdMemoryBuffer == rs2:
            return [True, "ME", 1] #1 stall

        """
        F D E M W         addi x10 x9 1
          F D     E M W   addi x8 x10 10

        """

        if rdExecuteBuffer in [rs1, rs2]:
            return [True, "EE", 2] #2 stall

        """
        F D E M W         addi x10 x9 1
          F D E M W       random instruction #doesn't cause hazards, confirmed from above cases
            F D   E M W   addi x8 x10 10

        """

        if rdMemoryBuffer in [rs1, rs2]:
            return [True, "ME", 1] #1 stalls

        return [False, "NO", 0]

    
    def getDataFromBuffer(self, i, bufferobj):
        return bufferobj.get(i)

if __name__ == "__main__":
    # Buffer=Buffer()
    # register = RegisterFile()
    # HDU = HDU(Buffer,register)
    
    df_control = pd.read_csv("controls.csv")
    df_control = df_control.dropna(axis=0, how='any')
    buf = Buffer()
    hdu = HDU(df_control)
    #Test case 1:
    #     addi x10,x11,1 #  F D E M W
    #     addi x10,x10,1 #    F D E M W
    # buf.executeB(9, "0"*7+"1", 10, "0"*8, 11, 0)
    # l = hdu.detectHazard(buf, 9, 3, 10, 0)
    # print(l)
    
    #Test case 2: No hazard
    #     sw x10,0(x10) # F D E M W
    #     sw x11,0(x10)     F D E M W

    #called right before execute of instruction 2
    # buf.executeB(17, "0"*7+"1", 0, "0"*8, 10, 10)
    # l = hdu.detectHazard(buf, 17, 3, 0, 11)
    # l2 = hdu.detectHazard(buf, 17, 3, 10, 0)
    # print(l, "\n", l2)
    
    #Test case 4: M->E
    #   lw x10,0(x9)  F D E M W
    #   sw x11,0(x10)   F D   E M W 1 stall
    # rdprev1 = x10= rs1 so hazard # 15 <= id <= 17 
    # buf.executeB(14, "0"*7+"1", 10, "0"*8, 9, 0)
    # l = hdu.detectHazard(buf, 17, 3, 10, 0)
    # l2 = hdu.detectHazard(buf, 17, 3, 0, 11)
    # print(l, "\n", l2)

    #Test case 5: M->M
    #   lw x10,0(x9)  F D E M W
    #   sw x10,0(x11)   F D E M W
    # rdprev1 = x10= rs1 so hazard # 15 <= id <= 17 
    buf.memoryB(14, "0"*7+"1", 10)
    l = hdu.detectHazard(buf, 17, 4, 11, 0)
    l2 = hdu.detectHazard(buf, 17, 4, 0, 10)
    print(l, "\n", l2)
    
    #Test case 5: M->E and 1 stall
    #    lw x10,0(x9) # 15 <= id <= 17 
    #    add x11,x10,x10 
    # rdprev1 = x10= rs1 so hazard # 15 <= id <= 17 
    # buf.executeB(14, "0"*7+"1", 10, "0"*8)
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
