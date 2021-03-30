class RegisterFile:

    """
    data: hexadecimal string representing 32 bit number
    self._registers : list of 32 integers representing 32 registers
    methods:
    initialise_registers : initialise registers to default value
                           can be used to reset register file
    get_register: return content of register enquired
    set_register: set content of register
    """

    def __init__(self):
        self._registers = []
        self.initialise_registers()
        self.PC = 0
        self._alt_name = ["zero", "ra", "sp", "gp", "tp", "t0", "t1", "t2", "s0/fp", "s1", "a0", "a1", "a2", "a3",
                          "a4", "a5", "a6", "a7", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9", "s10", "s11", "t3", "t4", "t5", "t6"]

    def initialise_registers(self):
        self._registers = ["00000000"]*32
        self._registers[2] = "7FFFFFF0"  # sp
        self._registers[3] = "10000000" # gp

    def print_registers(self):
        print(self._registers)

    def get_register(self, index):
        return self._registers[index]

    def get_alt_name(self, index):
        return self._alt_name[index]

    def set_register(self, index, data):
        if index != 0:
            self._registers[index] = data[-8:]


if __name__ == '__main__':
    rf = RegisterFile()
    rf.initialise_registers()
    rf.print_registers()
