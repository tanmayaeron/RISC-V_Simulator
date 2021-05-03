from math import log2

class cache:

    def __init__(self, cache_size, block_size, ways):
        self.cache_size = cache_size
        self.block_size = block_size
        self.ways = ways #number of ways
        self._cache = [] #list for now
        self._LRU = []
        self.index = int(math.log2(cache_size/block_size)) - int(math.log2(ways)) #index bits
        self.BO = int(math.log2(block_size)) #block offset bits
        self.tag = 32 - self.index - self.BO #tage bits
        self.miss = 0
        self.hits = 0
        self.total_accesses = 0
        self.modify_cache()
        self.initialise_LRU()

    def address_break(self, address): #takes the hex string
        #should return binary, returns decimal for now
        address = int(address, 16)
        tag = address[:self.tag]
        index = address[self.tag:self.tag+self.index]
        BO = address[-self.BO:]
        return tag, index, BO

    def modify_cache(self, address):
        #modify the dict for easy access
        """
            let there be a cache of 8 byte size
            and a block is of size 1 byte
            there will be 8 blocks i.e., 8 dicts, one for each block

            [[{},{}],[{},{}],[{},{}],[{},{}]]
        """
        
        for i in range(2**self.index):
            self._cache.append([]) #every list
            for j in range(self.ways):
                self._cache[i].append(["0"*8]*((self.block_size)//4)) #every dict will be a block, and there will be as many dict as ways
    
    def initialise_LRU(self):
        # [1/0, state, tag]
        for ind in range(2**self.index):
            self._LRU.append([])
            for blocks in range(self.ways):
                self._LRU[ind].append([0,0,0])
                
    def checkInCache(self ,tag, index):
        self._LRU
        
        
        

    def updateLRU(self, tag, index):
        
        for i in range(self.ways):
            if self._LRU[index][i][0] == 1 and self._LRU[index][i][2] == tag:
                self._LRU[index][i][1] = self.ways
                for j in range(self.ways):
                    self._LRU[index][j][1] = max(self._LRU[index][j][1]-1, 0)
                return
            
        for i in range(self.ways):
            if self._LRU[index][i][0] == 0:
                self._LRU[index][i][0] = 1
                self._LRU[index][i][1] = self.ways
                self._LRU[index][i][2] = tag
                for j in range(self.ways):
                    self._LRU[index][j][1] = max(self._LRU[index][j][1]-1, 0)
                return
            
        minS = 1e9
        victim = 0
        for i in range(self.ways):
            if(minS > self._LRU[index][i][1]):
                minS = self._LRU[index][i][1]
                victim = i
                  
        self._LRU[index][victim][0] = 1
        self._LRU[index][victim][1] = self.ways
        self._LRU[index][victim][2] = tag
        for j in range(self.ways):
            self._LRU[index][j][1] = max(self._LRU[index][j][1]-1, 0)
        return    

    def set_associative(self, address, memory_obj, Write = False, toWrite = "00"):
        self.total_accesses += 1
        tag, index, BO = self.address_break(address)
        #read
        checkInCache();
        # read
        # slightly incorrect
        # if not Write: #during read
        #     for block in self._cache[index]:
        #         if tag in block: #LRU update pending
        #             self.hits += 1
        #             return block[tag]
        #     #if code reaches here then it's a miss
        #     self.miss += 1
        #     #update_block using LRU and other stuff
        # else: #write
        #     for block in self._cache[index]:
        #         if tag in block: #LRU update pending
        #             self.hits += 1
        #             block[tag] = toWrite
        #             return
        #     #miss
        #     self.miss += 1
