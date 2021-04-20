class Buffer:
  #  #
    def __init__(self):
    111  self.dict = {}
    
    """
        buffers are set after their repective stages, fetch after the fetch stage and so on
        set after each cycle
    """
    def fetchB(self, PC, IR):
        self.dict[1] = PC, IR

    def decodeB(self, id, PC , rs1, rs2, RA = "0"*8, RB = "0"*8, RM = "0"*8, rd = 0):
        self.dict[2] = id, PC, RA, RB, RM, rd, rs1, rs2 #RM contains the value of rs2 by default if it's not to be written then ME = 0
        #RA and RB may not be used and rejected by muxes

    def executeB(self, id, RZ, rd, RM, rs1, rs2):
        #included rs1, rs2 in the after execute buffer, this will be needed for X->M forwarding/stalling
        self.dict[3] = id, RZ, rd, RM, rs1, rs2 # RZ is the result

    def memoryB(self, id, RY, rd):
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

    def __init__(self, df_control):
        self.df_control = df_control #read csv and pass to HDU object
        self.initialiseControls()
    
    def initialiseControls(self):
        self.isExecuters1 = list(self.df_control['rs1E'].astype(int))
        self.isExecuters2 = list(self.df_control['rs2E'].astype(int))
        self.isMemoryrs1 = list(self.df_control['rs1M'].astype(int))
        self.isMemoryrs2 = list(self.df_control['rs2M'].astype(int))
        self.is_AE = list(self.df_control['isAE'].astype(int))
        self.WE = list(self.df_control['WE'].astype(int))

    def forwarding2(self, buffer_obj,id, rs1 = 0, rs2 = 0):
        
        result = [[],[]]
        is_rs1 = max(self.isExecuters1[id],self.isMemoryrs1[id])
        is_rs2 = max(self.isExecuters1[id],self.isMemoryrs1[id])
        
    
        if rs1 == 0:
            result[0] = [False,"NO",0]
        elif is_rs1 == 0:
            #[isHazard,Forwarding,stall]
            result[0] = [False,"NO",0]
        else:
            #id and rd
            prev_id, rd = buffer_obj.get(2)[0],buffer_obj.get(2)[5] #rs1 valid != 0
            currWE = self.WE[prev_id]
            if currWE == 0 or rd!=rs1:
                result[0]=[False,"NO",0]
            else: #
                curr_AE = self.is_AE[prev_id]
                if curr_AE:
                    result[0]=[True,"EE",0]
                else:
                    isrs1_E = self.isExecuters1[id]
                    if isrs1_E==0:
                        result[0]=[True,"MM",0]                                             #not required in execute
                    else:
                        result[0]=[True,"ME",1]
            if result[0][0] = False:
                prev_id, rd = buffer_obj.get(3)[0],buffer_obj.get(3)[2] 
                currWE = self.WE[prev_id]
                if currWE==1 and rs1==rd:
                   result[0]=[True,"ME",0]
            
        if rs2 == 0:
            result[1] = [False,"NO",0]
        elif is_rs2 == 0:
            #[isHazard,Forwarding,stall]
            result[1] = [False,"NO",0]
        else:
            #id and rd
            prev_id, rd = buffer_obj.get(2)[0],buffer_obj.get(2)[5] #rs1 valid != 0
            currWE = self.WE[prev_id]
            if currWE == 0 or rd!=rs2:
                result[1] = [False,"NO",0]
            else: #
                curr_AE = self.is_AE[prev_id]
                if curr_AE:
                    result[1]=[True,"EE",0]
                else:
                    isrs2_E = self.isExecuters2[id]
                    if isrs2_E==0:
                        result[1]=[True,"MM",0]                                             #not required in execute
                    else:
                        result[1]=[True,"ME",1]
            if result[1][0] = False:
                prev_id, rd = buffer_obj.get(3)[0],buffer_obj.get(3)[2] 

                currWE = self.WE[prev_id]
                if currWE==1 and rs1==rd:
                   result[1]=[True,"ME",0]

        stall = max(result[0][2],result[1][2])

        if stall:
            pass            
