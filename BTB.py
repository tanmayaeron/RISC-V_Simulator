class BTB:

    def __init__(self):
        self.lookup = {}
        self.maxlimit = 32

    # prediction - 1 -> Taken
    # prediction - 0 -> Not Taken
    # type_ins - 0-> jump
    #            1 -> branch
    def add_ins(self,PC,target,type_ins,sign):
        num_instructions = len(self.lookup)
        prediction = sign
        if num_instructions < self.maxlimit:
            self.lookup[PC]=[type_ins,target,prediction]

    def check_ins(self,PC):
        if PC in self.lookup:
            return self.lookup[PC]
        else:
            return [-1]*3