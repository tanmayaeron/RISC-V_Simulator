import pandas as pd


def decode(code):
    """

    :param code:32 bit machine code in hex(without 0x32)
    :return: dictionary of all data
    """

    fields = {}
    df = pd.read_csv('instructions.csv')
    machine_code = '0' * 32 + bin(int(code, 16))[2:]
    machine_code = machine_code[-32:]
    opcode = '0b'+machine_code[-7:]
    df = df[df.opcode==opcode]
    if len(df['id'])==0:
        return 0
    else:
        format = df['format'][0]
        if format=='R':
            funct3 = '0b'+machine_code[-15:-12]
            funct7 = '0b'+machine_code[:7]
            df = df[(df.funct3==funct3) & (df.funct7==funct7)]
            if len(df['id']) == 0:
                return 0
            else:
                fields['neumonic']=df['neumonic'][0]
                fields['opcode']=df['opcode'][0]
                fields['funct3']=df['funct3'][0]
                fields['funct7']=df['funct7'][0]
                fields['rs1']=machine_code[-20:-15]
                fields['rs2']=machine_code[-25:-20]
                fields['rd']=machine_code[-12:-7]
        return fields

print(decode('00A48433'))
