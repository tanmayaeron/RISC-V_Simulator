import pandas as pd

# df_main = pd.read_csv('instructions.csv')

def identify(code, df_main):
    """

    :param code:32 bit machine code in hex(without 0x)
    :return: dictionary of all data
    """

    fields = {}
    machine_code = '0' * 32 + bin(int(code, 16))[2:]
    machine_code = machine_code[-32:]
    opcode = '0b'+machine_code[-7:]
    df = df_main[df_main.opcode == opcode]
    if len(df['id']) == 0:
        return 0
    else:
        format = list(df['format'])[0]

        if format == 'R':
            funct3 = '0b'+machine_code[-15:-12]
            funct7 = '0b'+machine_code[:7]
            df = df[(df.funct3 == funct3) & (df.funct7 == funct7)]
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
                                                   8]+'0'  # 0 not added in the end
                fields["format"] = 'SB'

        elif format == 'U':
            fields['neumonic'] = list(df['neumonic'])[0]
            fields['opcode'] = opcode
            fields['immediate'] = machine_code[0:20]+'0'*12
            fields['rd'] = machine_code[-12:-7]
            fields["format"] = 'U'

        elif format == 'UJ':
            fields['neumonic'] = list(df['neumonic'])[0]
            fields['opcode'] = opcode
            fields['immediate'] = machine_code[0]+machine_code[-20:-12] + \
                machine_code[-21] + \
                machine_code[1:11]+'0'  # not shifted 12 bits see later
            fields['rd'] = machine_code[-12:-7]
            fields["format"] = 'UJ'

        fields['id'] = list(df['id'])[0]
        return fields
