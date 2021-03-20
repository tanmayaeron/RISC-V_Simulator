class RegisterFile:

    """
    data:
    self._registers : list storing content of 32 register in hex
                 each as a string of size 8(without 0x)

    methods:
    initialise_registers : initialise registers to default value
                           can be used to reset register file
    get_register: return content of register enquired
    set_register: set content of register
    """

    def __init__(self):
        self._registers = []

    def initialise_registers(self):
        self._registers = ["0" * 8] * 32
        self._registers[2] = "7ffffff0"
        self._registers[3] = "1" + "0" * 7

    def print_registers(self):
        print(self._registers)

    def get_register(self,index):
        return self._registers[index]

    def set_register(self,index,data):
        if index==0 and data!="0"*8:
            return 0   #x0 register can't be changed
        else:
            self._registers[index]=data
            return 1

if __name__ == '__main__':
    rf = RegisterFile()
    rf.initialise_registers()
    rf.print_registers()