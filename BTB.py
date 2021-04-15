from collections import defaultdict


class BTB:

    """
        0 -> Not Taken
        1 -> Taken
        PC is a String of HEX (without 0x)
        target is the target address if Taken
    """

    def __init__(self):
        self.lookup = defaultdict(str)
        pass

    def insert(self, PC, target):
        if PC not in self.lookup.keys():
            self.lookup[PC] = [0, target]

    def predict(self, PC):
        return self.lookup[PC][0]

    def getTarget(self, PC):
        return self.lookup[PC][1]
    
    def setTarget(self, PC, newTarget):
        self.lookup[PC][1] = newTarget
        
    def changeState(self, PC, Outcome):
        if Outcome != self.lookup[PC][0]:
            self.lookup[PC][0] = 1 - self.lookup[PC][0]
