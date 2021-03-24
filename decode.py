import pandas as pd
from ALU import ALU
from register import RegisterFile
from bitstring import BitArray
from bitstring import Bits
df_main = pd.read_csv('instructions.csv')


def decode(code):
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
                fields['immediate'] = machine_code[0:7]+machine_code[-12:-7]
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


obj = ALU()
registers = RegisterFile()


def twos_complement(a):

    return Bits(bin=a).int


def R_format(fields):

    instruction = fields['neumonic']
    rs1 = int(fields['rs1'], 2)
    rs2 = int(fields['rs2'], 2)
    rd = int(fields['rd'], 2)
    obj.RA = registers.get_register(rs1)
    obj.RB = registers.get_register(rs2)
    obj.muxB = 0
    if instruction == "add":
        obj.add()
    elif instruction == "and":
        obj._and()
    elif instruction == "or":
        obj._or()
    elif instruction == "sll":
        obj.sll()
    elif instruction == "slt":
        obj.slt()
    elif instruction == "sra":
        obj.sra()
    elif instruction == "srl":
        obj.srl()
    elif instruction == "sub":
        obj.sub()
    elif instruction == "xor":
        obj.xor()
    elif instruction == "mul":
        obj.mul()
    elif instruction == "div":
        obj.div()
    elif instruction == "rem":
        obj.rem()


def I_format(fields):
    instruction = fields['neumonic']
    rs1 = int(fields['rs1'], 2)
    imm = twos_complement(fields['immediate'])
    rd = int(fields['rd'], 2)
    obj.RA = registers.get_register(rs1)
    obj.imm = imm
    obj.muxB = 1
    if instruction == "addi":
        # mux value is 1
        obj.add()
        print(obj.RZ)
    elif instruction == "ori":
        # mux value is 1
        obj._or()
        print(obj.RZ)
    elif instruction == "andi":
        # mux value is 1
        obj._andi()
        print(obj.RZ)
    elif instruction == "lb":
        # mux value is 1
        obj.lbhw()
        print(obj.RZ)
    elif instruction == "jalr":
        # mux value is 1
        obj.jalr()
        print(obj.RZ)


def S_format(fields):
    pass


def SB_format(fields):
    pass


def U_format(fields):
    pass


def UJ_format(fields):
    pass


def alu_caller():
    machine_code = "43E58593"
    fields = decode(machine_code)

    format = fields['format']
    if format == 0:
        return
    if format == 'R':
        R_format(fields)
    elif format == 'I':
        I_format(fields)
    elif format == "S":
        S_format(fields)
    elif format == "SB":
        SB_format(fields)
    elif format == "U":
        U_format(fields)
    else:
        UJ_format(fields)


alu_caller()
