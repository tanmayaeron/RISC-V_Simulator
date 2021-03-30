
import pandas as pd
from ALU_re import alu_interface
from register import RegisterFile
from bitstring import BitArray
from bitstring import Bits
# we will use register objects here

df_main = pd.read_csv('instructions.csv')


class Execute:
    def __init__(self):
        self.PC = 0
        self.cycle = 0
        self.IR = 0
        self.registers = RegisterFile()
        self.obj = alu_interface()

    def int_to_hex(self, a):
        b = 0x100000000
        if a >= 0:
            a = '{:08x}'.format(a)[-8:]
        else:
            a += b
            a = hex(a)
        return a

    def fetch(self):

        self.PC += 4
        self.cycle += 1
        self.IR = "00B62323"  # we have to reload next instruction here
        self.obj.PC = self.PC  # temporary copying self.pc to obj.pc to be removed in future
        self.alu_caller(self.IR)
        self.PC = self.obj.PC  # copying back the changes to obj.pc in pc to be removed in future

    def decode(self, code):
        # code must be of the form "0x00D60593"
        """

        :param code:32 bit machine code in hex(without 0x32)
        :return: dictionary of all data
        """

        fields = {}

        # print(df)
        machine_code = '0' * 32 + bin(int(code, 16))[2:]
        machine_code = machine_code[-32:]
        opcode = '0b'+machine_code[-7:]
        df = df_main[df_main.opcode == opcode]
        # print(df)
        if len(df['id']) == 0:
            return 0
        else:
            format = list(df['format'])[0]

            if format == 'R':
                funct3 = '0b'+machine_code[-15:-12]
                funct7 = '0b'+machine_code[:7]
                df = df[(df.funct3 == funct3) & (df.funct7 == funct7)]
                # print(df)
                if len(df['id']) == 0:
                    return 0
                else:
                    fields['neumonic'] = list(df['neumonic'])[0]
                    fields['opcode'] = list(df['opcode'])[0]
                    fields['funct3'] = list(df['funct3'])[0]
                    fields['funct7'] = list(df['funct7'])[0]
                    fields['rs1'] = machine_code[-20:-15]
                    fields['rs2'] = machine_code[-25:-20]
                    fields['rd'] = machine_code[-12:-7]
                    fields['format'] = 'R'

            elif format == 'I':
                funct3 = '0b'+machine_code[-15:-12]
                df = df[df.funct3 == funct3]
                if len(df['id']) == 0:
                    return 0
                else:
                    fields['neumonic'] = list(df['neumonic'])[0]
                    fields['opcode'] = list(df['opcode'])[0]
                    fields['funct3'] = list(df['funct3'])[0]
                    fields['rs1'] = machine_code[-20:-15]
                    fields['rd'] = machine_code[-12:-7]
                    fields['immediate'] = machine_code[0:12]
                    fields['format'] = 'I'

            elif format == 'S':
                funct3 = '0b'+machine_code[-15:-12]
                df = df[df.funct3 == funct3]
                if len(df['id']) == 0:
                    return 0
                else:
                    fields['neumonic'] = list(df['neumonic'])[0]
                    fields['opcode'] = list(df['opcode'])[0]
                    fields['funct3'] = list(df['funct3'])[0]
                    fields['rs1'] = machine_code[-20:-15]
                    fields['rs2'] = machine_code[-25:-20]
                    fields['immediate'] = machine_code[0:7] + \
                        machine_code[-12:-7]
                    fields["format"] = 'S'

            elif format == 'SB':
                funct3 = '0b'+machine_code[-15:-12]
                df = df[df.funct3 == funct3]
                if len(df['id']) == 0:
                    return 0
                else:
                    fields['neumonic'] = list(df['neumonic'])[0]
                    fields['opcode'] = list(df['opcode'])[0]
                    fields['funct3'] = list(df['funct3'])[0]
                    fields['rs1'] = machine_code[-20:-15]
                    fields['rs2'] = machine_code[-25:-20]
                    fields['immediate'] = machine_code[0]+machine_code[-8] + \
                        machine_code[1:7]+machine_code[-12:-
                                                       8]  # 0 not added in the end
                    fields["format"] = 'SB'

            elif format == 'U':
                fields['neumonic'] = list(df['neumonic'])[0]
                fields['opcode'] = opcode
                fields['immediate'] = machine_code[0:20]
                fields['rd'] = machine_code[-12:-7]
                fields["format"] = 'U'

            elif format == 'UJ':
                fields['neumonic'] = list(df['neumonic'])[0]
                fields['opcode'] = opcode
                fields['immediate'] = machine_code[0]+machine_code[-20:-12] + \
                    machine_code[-21] + \
                    machine_code[1:11]  # not shifted 12 bits see later
                fields['rd'] = machine_code[-12:-7]
                fields["format"] = 'UJ'
            return fields

    def twos_complement(self, a):

        return Bits(bin=a).int

    def R_format(self, fields):

        instruction = fields['neumonic']
        rs1 = int(fields['rs1'], 2)
        rs2 = int(fields['rs2'], 2)
        rd = int(fields['rd'], 2)
        self.obj.RA = self.registers.get_register(rs1)
        self.obj.RB = self.registers.get_register(rs2)
        self.obj.muxB = 0
        if instruction == "add":
            self.obj.add()
        elif instruction == "and":
            self.obj._and()
        elif instruction == "or":
            self.obj._or()
        elif instruction == "sll":
            self.obj.sll()
        elif instruction == "slt":
            self.obj.slt()
        elif instruction == "sra":
            self.obj.sra()
        elif instruction == "srl":
            self.obj.srl()
        elif instruction == "sub":
            self.obj.sub()
        elif instruction == "xor":
            self.obj.xor()
        elif instruction == "mul":
            self.obj.mul()
        elif instruction == "div":
            self.obj.div()
        elif instruction == "rem":
            self.obj.rem()

    def I_format(self, fields):
        instruction = fields['neumonic']
        rs1 = int(fields['rs1'], 2)

        imm = self.twos_complement(fields['immediate'])

        rd = int(fields['rd'], 2)
        self.obj.RA = self.registers.get_register(rs1)

        self.obj.imm = imm
        self.obj.imm = self.int_to_hex(imm)
        self.obj.muxB = 1

        if instruction == "addi":
            # mux value is 1
            self.obj.add()
            print(self.obj.RZ)
        elif instruction == "ori":
            # mux value is 1
            self.obj._or()
            print(self.obj.RZ)
        elif instruction == "andi":
            # mux value is 1
            self.obj._andi()
            print(self.obj.RZ)
        elif instruction == "lb":
            # mux value is 1
            self.obj.lbhw()
            print(self.obj.RZ)
        elif instruction == "jalr":
            # mux value is 1
            # works fine
            self.obj.jalr()
            print(self.obj.PC)

    def S_format(self, fields):
        # not checked
        # to be checked later
        #######################################
        instruction = fields['neumonic']
        rs1 = int(fields['rs1'], 2)
        rs2 = int(fields['rs2'], 2)
        self.obj.RA = self.registers.get_register(rs1)
        self.obj.RB = self.registers.get_register(rs2)
        imm = self.twos_complement(fields['immediate'])
        self.obj.imm = self.int_to_hex(imm)
        self.obj.muxB = 1
        if instruction == "sb":
            self.obj.sbhw()
        elif instruction == "sh":
            self.obj.sbhw()
        elif instruction == "sw":
            self.obj.sbhw()

        print("location is:", self.obj.RZ)
        print("the value is : ", self.obj.RM)

    def SB_format(self, fields):
        instruction = fields['neumonic']
        rs1 = int(fields['rs1'], 2)
        rs2 = int(fields['rs2'], 2)
        imm = self.twos_complement(fields['immediate'])
        imm *= 2  # to left shift as imm[0] is 0
        self.obj.RA = self.registers.get_register(rs1)
        self.obj.RB = self.registers.get_register(rs2)
        self.obj.imm = self.int_to_hex(imm)
        print(self.obj.RA, self.obj.RB, self.obj.imm, self.obj.PC)
        self.obj.muxB = 0
        if instruction == "beq":
            self.obj.beq()
            print(self.obj.PC)
        elif instruction == "bne":
            self.obj.bne()
            print(self.obj.PC)
        elif instruction == "bge":
            self.obj.bge()
            print(self.obj.PC)
        elif instruction == "blt":
            self.obj.blt()
            print(self.obj.PC)

    def U_format(self, fields):
        instruction = fields['neumonic']
        rd = int(fields['rd'], 2)
        imm = self.twos_complement(fields['immediate'])
        imm = imm*2**12  # left shifting 12 bits
        self.obj.imm = self.int_to_hex(imm)
        self.obj.muxB = 0
        if instruction == "lui":
            self.obj.lui()
        elif instruction == "auipc":
            self.obj.auipc()
            print(self.obj.RZ)

    def UJ_format(self, fields):
        instruction = fields['neumonic']
        rd = int(fields['rd'], 2)
        imm = self.twos_complement(fields['immediate'])
        imm *= 2  # to left shift as imm[0] is 0
        self.obj.imm = self.int_to_hex(imm)
        self.obj.muxB = 0
        if instruction == "jal":
            self.obj.jal()
            print(self.obj.PC_temp)
            print(self.obj.PC)

    def alu_caller(self, machine_code):

        fields = self.decode(machine_code)

        format = fields['format']
        print(fields)
        if format == 0:
            print("not found")
            return
        if format == 'R':
            self.R_format(fields)
        elif format == 'I':
            self.I_format(fields)
        elif format == "S":
            self.S_format(fields)
        elif format == "SB":
            self.SB_format(fields)
        elif format == "U":
            self.U_format(fields)
        else:
            self.UJ_format(fields)


execute_obj = Execute()
execute_obj.fetch()
