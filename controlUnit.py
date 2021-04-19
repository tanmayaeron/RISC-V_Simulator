 c
 cla= ss CU:
    def __init__(self, k1, k2):
        self.k1 = k1
        self.k2 = k2
        self.HDU = HDU()
        self.processor = Processor()
        
    def control(self):
        
        
    # FF non pipeline
    # TF pipeline w/0 forward
    # TT pipline w forward
    
    def one(self):
        self.processor.load_mc(filePath)
        while True:
            self.processor.fetch()
            if self.processor.getIR() == '0'*8:
                break
            self.processor.decode()
            self.processor.execute()
            self.processor.memoryAccess()
            self.processor.registerUpdate()
        self.processor.printRegisters()
        self.processor.printData()
        
    def PipeWithForward(self):
        isStall = [0, 0, 0, 0, 0]
        isLastFetched = 0
        watchArray = [1, 0, 0, 0, 0]
        while(1 in watchArray):
            i = 4
            while i >=0 :
                if isStall[i] > 0:
                    isStall[i]-=1
                    continue
                elif(watchArray[i] == 0):
                    continue
                elif i == 4:
                    self.processor.registerUpdate()
                elif i == 3:
                    id, rs1, rs2 = self.HDU.getDataFromBuffer(i-1)[0], self.HDU.getDataFromBuffer(i-1)[-2], self.HDU.getDataFromBuffer(i-1)[-1]
                    hazardDetails1 = self.HDU.detectHazard(id = id, rs1=rs1)
                    hazardDetails2 = self.HDU.detectHazard(id = id, rs2=rs2)
                    isStall[3] = max(hazardDetails1[2], hazardDetails2[2])
                    isStall[2] = isStall[1] = isStall[0]
                    if(not isStall[3]):
                        #forwarding
                        #call memory access
                elif i == 2:
                    id, rs1, rs2 = self.HDU.getDataFromBuffer(i-1)[0], self.HDU.getDataFromBuffer(i-1)[-2], self.HDU.getDataFromBuffer(i-1)[-1]
                    hazardDetails1 = self.HDU.detectHazard(id = id, rs1=rs1)
                    hazardDetails2 = self.HDU.detectHazard(id = id, rs2=rs2)
                    isStall[2] = max(hazardDetails1[2], hazardDetails2[2])
                    isStall[1] = isStall[0]
                    if(not isStall[2]):
                        #forwarding
                        
                        
                elif i == 1:
                    self.processor.decode()
                    rs1, rs2 = self.processor.rs1, self.processor.rs2
                    id = self.HDU.getDataFromBuffer(i-1)[0]
                    if(branch):
                        hazardDetails1 = self.HDU.detectHazard(id = id,rs1=rs1)
                        hazardDetails2 = self.HDU.detectHazard(id = id,rs2=rs2)
                        isStall[1] = max(hazardDetails1[2], hazardDetails2[2])
                        isStall[0] = isStall[1]
                        if(not isStall[1]):
                            if not hazardDetails1[0]:
                                select_mux1 = 0
                            elif hazardDetails1[1] == "ED":
                                select_mux1 = 1
                            elif hazardDetails1[1] == "MD":
                                select_mux1 = 2
                            
                            if not hazardDetails2[0]:
                                select_mux2 = 0
                            elif hazardDetails2[1] == "ED":
                                select_mux2 = 1
                            elif hazardDetails2[1] == "MD":
                                select_mux2 = 2
                            
                            result = self.processor.comparator(rs1, rs2, id-18, select_mux1, select_mux2)
                            ##handle branching use BTB
                            
                elif i == 0:
                    pass
                
                isStall[i] = max(0, isStall[i]-1) 
                i -=1
                        
            if self.processor.getIR() == '0'*8:
                isLastFetched = 1
            
                        
                        
            
            
                        
            
                        
                        
                    
                


            