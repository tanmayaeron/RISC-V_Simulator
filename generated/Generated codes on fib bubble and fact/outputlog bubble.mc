Fetch stage:
The value of PC is : 00000000
The instruction in IR is : 10000597
Decode stage:
code : {'neumonic': 'auipc', 'opcode': '0b0010111', 'immediate': '00010000000000000000000000000000', 'rd': '01011', 'format': 'U', 'id': 25}
rd is : 11
imm is : 10000000
Execute stage:
operand1 is 00000000 operand2 is: 10000000
RZ is : 10000000
Memory Access stage:
Register Update Stage:
RD: RY: 11 10000000
cycle is : 1
Fetch stage:
The value of PC is : 00000004
The instruction in IR is : 00058593
Decode stage:
code : {'neumonic': 'addi', 'opcode': '0b0010011', 'funct3': '0b000', 'rs1': '01011', 'rd': '01011', 'immediate': '000000000000', 'format': 'I', 'id': 9}
RA is : 10000000
rd is : 11
imm is : 00000000
Execute stage:
operand1 is 10000000 operand2 is: 00000000
RZ is : 10000000
Memory Access stage:
Register Update Stage:
RD: RY: 11 10000000
cycle is : 2
Fetch stage:
The value of PC is : 00000008
The instruction in IR is : 00A00613
Decode stage:
code : {'neumonic': 'addi', 'opcode': '0b0010011', 'funct3': '0b000', 'rs1': '00000', 'rd': '01100', 'immediate': '000000001010', 'format': 'I', 'id': 9}
RA is : 00000000
rd is : 12
imm is : 0000000a
Execute stage:
operand1 is 00000000 operand2 is: 0000000a
RZ is : 0000000a
Memory Access stage:
Register Update Stage:
RD: RY: 12 0000000a
cycle is : 3
Fetch stage:
The value of PC is : 0000000c
The instruction in IR is : 00200F93
Decode stage:
code : {'neumonic': 'addi', 'opcode': '0b0010011', 'funct3': '0b000', 'rs1': '00000', 'rd': '11111', 'immediate': '000000000010', 'format': 'I', 'id': 9}
RA is : 00000000
rd is : 31
imm is : 00000002
Execute stage:
operand1 is 00000000 operand2 is: 00000002
RZ is : 00000002
Memory Access stage:
Register Update Stage:
RD: RY: 31 00000002
cycle is : 4
Fetch stage:
The value of PC is : 00000010
The instruction in IR is : FFF60613
Decode stage:
code : {'neumonic': 'addi', 'opcode': '0b0010011', 'funct3': '0b000', 'rs1': '01100', 'rd': '01100', 'immediate': '111111111111', 'format': 'I', 'id': 9}
RA is : 0000000a
rd is : 12
imm is : ffffffff
Execute stage:
operand1 is 0000000a operand2 is: ffffffff
RZ is : 00000009
Memory Access stage:
Register Update Stage:
RD: RY: 12 00000009
cycle is : 5
Fetch stage:
The value of PC is : 00000014
The instruction in IR is : 02060C63
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01100', 'rs2': '00000', 'immediate': '0000000111000', 'format': 'SB', 'id': 18}
RA is : 00000009
RB is : 00000000
imm is : 00000038
Execute stage:
operand1 is 00000009 operand2 is: 00000000
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 12 00000000
cycle is : 6
Fetch stage:
The value of PC is : 00000018
The instruction in IR is : 00000693
Decode stage:
code : {'neumonic': 'addi', 'opcode': '0b0010011', 'funct3': '0b000', 'rs1': '00000', 'rd': '01101', 'immediate': '000000000000', 'format': 'I', 'id': 9}
RA is : 00000000
rd is : 13
imm is : 00000000
Execute stage:
operand1 is 00000000 operand2 is: 00000000
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 7
Fetch stage:
The value of PC is : 0000001c
The instruction in IR is : 02C68663
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01101', 'rs2': '01100', 'immediate': '0000000101100', 'format': 'SB', 'id': 18}
RA is : 00000000
RB is : 00000009
imm is : 0000002c
Execute stage:
operand1 is 00000000 operand2 is: 00000009
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 8
Fetch stage:
The value of PC is : 00000020
The instruction in IR is : 01F69733
Decode stage:
code : {'neumonic': 'sll', 'opcode': '0b0110011', 'funct3': '0b001', 'funct7': '0b0000000', 'rs1': '01101', 'rs2': '11111', 'rd': '01110', 'format': 'R', 'id': 5}
RA is : 00000000
RB is : 00000002
rd is : 14
Execute stage:
operand1 is 00000000 operand2 is: 00000002
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 14 00000000
cycle is : 9
Fetch stage:
The value of PC is : 00000024
The instruction in IR is : 00B70733
Decode stage:
code : {'neumonic': 'add', 'opcode': '0b0110011', 'funct3': '0b000', 'funct7': '0b0000000', 'rs1': '01110', 'rs2': '01011', 'rd': '01110', 'format': 'R', 'id': 0}
RA is : 00000000
RB is : 10000000
rd is : 14
Execute stage:
operand1 is 00000000 operand2 is: 10000000
RZ is : 10000000
Memory Access stage:
Register Update Stage:
RD: RY: 14 10000000
cycle is : 10
Fetch stage:
The value of PC is : 00000028
The instruction in IR is : 00072783
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '01111', 'immediate': '000000000000', 'format': 'I', 'id': 14}
RA is : 10000000
rd is : 15
imm is : 00000000
Execute stage:
operand1 is 10000000 operand2 is: 00000000
RZ is : 10000000
Memory Access stage:
Register Update Stage:
RD: RY: 15 00000064
cycle is : 11
Fetch stage:
The value of PC is : 0000002c
The instruction in IR is : 00472803
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '10000', 'immediate': '000000000100', 'format': 'I', 'id': 14}
RA is : 10000000
rd is : 16
imm is : 00000004
Execute stage:
operand1 is 10000000 operand2 is: 00000004
RZ is : 10000004
Memory Access stage:
Register Update Stage:
RD: RY: 16 0000005A
cycle is : 12
Fetch stage:
The value of PC is : 00000030
The instruction in IR is : 00168693
Decode stage:
code : {'neumonic': 'addi', 'opcode': '0b0010011', 'funct3': '0b000', 'rs1': '01101', 'rd': '01101', 'immediate': '000000000001', 'format': 'I', 'id': 9}
RA is : 00000000
rd is : 13
imm is : 00000001
Execute stage:
operand1 is 00000000 operand2 is: 00000001
RZ is : 00000001
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000001
cycle is : 13
Fetch stage:
The value of PC is : 00000034
The instruction in IR is : FF07C4E3
Decode stage:
code : {'neumonic': 'blt', 'opcode': '0b1100011', 'funct3': '0b100', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111101000', 'format': 'SB', 'id': 20}
RA is : 00000064
RB is : 0000005A
imm is : ffffffe8
Execute stage:
operand1 is 00000064 operand2 is: 0000005A
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 14
Fetch stage:
The value of PC is : 00000038
The instruction in IR is : FF0782E3
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111100100', 'format': 'SB', 'id': 18}
RA is : 00000064
RB is : 0000005A
imm is : ffffffe4
Execute stage:
operand1 is 00000064 operand2 is: 0000005A
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 15
Fetch stage:
The value of PC is : 0000003c
The instruction in IR is : 01072023
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '10000', 'immediate': '000000000000', 'format': 'S', 'id': 17}
RA is : 10000000
RB is : 0000005A
imm is : 00000000
Execute stage:
operand1 is 10000000 operand2 is: 00000000
RZ is : 10000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 10000000
cycle is : 16
Fetch stage:
The value of PC is : 00000040
The instruction in IR is : 00F72223
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '01111', 'immediate': '000000000100', 'format': 'S', 'id': 17}
RA is : 10000000
RB is : 00000064
imm is : 00000004
Execute stage:
operand1 is 10000000 operand2 is: 00000004
RZ is : 10000004
Memory Access stage:
Register Update Stage:
RD: RY: 13 10000004
cycle is : 17
Fetch stage:
The value of PC is : 00000044
The instruction in IR is : FD9FF06F
Decode stage:
code : {'neumonic': 'jal', 'opcode': '0b1101111', 'immediate': '111111111111111011000', 'rd': '00000', 'format': 'UJ', 'id': 22}
rd is : 0
imm is : ffffffd8
Execute stage:
operand1 is 10000000 operand2 is: 00000064
RZ is : 10000064
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000048
cycle is : 18
Fetch stage:
The value of PC is : 0000001c
The instruction in IR is : 02C68663
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01101', 'rs2': '01100', 'immediate': '0000000101100', 'format': 'SB', 'id': 18}
RA is : 00000001
RB is : 00000009
imm is : 0000002c
Execute stage:
operand1 is 00000001 operand2 is: 00000009
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000000
cycle is : 19
Fetch stage:
The value of PC is : 00000020
The instruction in IR is : 01F69733
Decode stage:
code : {'neumonic': 'sll', 'opcode': '0b0110011', 'funct3': '0b001', 'funct7': '0b0000000', 'rs1': '01101', 'rs2': '11111', 'rd': '01110', 'format': 'R', 'id': 5}
RA is : 00000001
RB is : 00000002
rd is : 14
Execute stage:
operand1 is 00000001 operand2 is: 00000002
RZ is : 00000004
Memory Access stage:
Register Update Stage:
RD: RY: 14 00000004
cycle is : 20
Fetch stage:
The value of PC is : 00000024
The instruction in IR is : 00B70733
Decode stage:
code : {'neumonic': 'add', 'opcode': '0b0110011', 'funct3': '0b000', 'funct7': '0b0000000', 'rs1': '01110', 'rs2': '01011', 'rd': '01110', 'format': 'R', 'id': 0}
RA is : 00000004
RB is : 10000000
rd is : 14
Execute stage:
operand1 is 00000004 operand2 is: 10000000
RZ is : 10000004
Memory Access stage:
Register Update Stage:
RD: RY: 14 10000004
cycle is : 21
Fetch stage:
The value of PC is : 00000028
The instruction in IR is : 00072783
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '01111', 'immediate': '000000000000', 'format': 'I', 'id': 14}
RA is : 10000004
rd is : 15
imm is : 00000000
Execute stage:
operand1 is 10000004 operand2 is: 00000000
RZ is : 10000004
Memory Access stage:
Register Update Stage:
RD: RY: 15 00000064
cycle is : 22
Fetch stage:
The value of PC is : 0000002c
The instruction in IR is : 00472803
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '10000', 'immediate': '000000000100', 'format': 'I', 'id': 14}
RA is : 10000004
rd is : 16
imm is : 00000004
Execute stage:
operand1 is 10000004 operand2 is: 00000004
RZ is : 10000008
Memory Access stage:
Register Update Stage:
RD: RY: 16 00000050
cycle is : 23
Fetch stage:
The value of PC is : 00000030
The instruction in IR is : 00168693
Decode stage:
code : {'neumonic': 'addi', 'opcode': '0b0010011', 'funct3': '0b000', 'rs1': '01101', 'rd': '01101', 'immediate': '000000000001', 'format': 'I', 'id': 9}
RA is : 00000001
rd is : 13
imm is : 00000001
Execute stage:
operand1 is 00000001 operand2 is: 00000001
RZ is : 00000002
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000002
cycle is : 24
Fetch stage:
The value of PC is : 00000034
The instruction in IR is : FF07C4E3
Decode stage:
code : {'neumonic': 'blt', 'opcode': '0b1100011', 'funct3': '0b100', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111101000', 'format': 'SB', 'id': 20}
RA is : 00000064
RB is : 00000050
imm is : ffffffe8
Execute stage:
operand1 is 00000064 operand2 is: 00000050
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 25
Fetch stage:
The value of PC is : 00000038
The instruction in IR is : FF0782E3
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111100100', 'format': 'SB', 'id': 18}
RA is : 00000064
RB is : 00000050
imm is : ffffffe4
Execute stage:
operand1 is 00000064 operand2 is: 00000050
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 26
Fetch stage:
The value of PC is : 0000003c
The instruction in IR is : 01072023
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '10000', 'immediate': '000000000000', 'format': 'S', 'id': 17}
RA is : 10000004
RB is : 00000050
imm is : 00000000
Execute stage:
operand1 is 10000004 operand2 is: 00000000
RZ is : 10000004
Memory Access stage:
Register Update Stage:
RD: RY: 13 10000004
cycle is : 27
Fetch stage:
The value of PC is : 00000040
The instruction in IR is : 00F72223
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '01111', 'immediate': '000000000100', 'format': 'S', 'id': 17}
RA is : 10000004
RB is : 00000064
imm is : 00000004
Execute stage:
operand1 is 10000004 operand2 is: 00000004
RZ is : 10000008
Memory Access stage:
Register Update Stage:
RD: RY: 13 10000008
cycle is : 28
Fetch stage:
The value of PC is : 00000044
The instruction in IR is : FD9FF06F
Decode stage:
code : {'neumonic': 'jal', 'opcode': '0b1101111', 'immediate': '111111111111111011000', 'rd': '00000', 'format': 'UJ', 'id': 22}
rd is : 0
imm is : ffffffd8
Execute stage:
operand1 is 10000004 operand2 is: 00000064
RZ is : 10000068
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000048
cycle is : 29
Fetch stage:
The value of PC is : 0000001c
The instruction in IR is : 02C68663
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01101', 'rs2': '01100', 'immediate': '0000000101100', 'format': 'SB', 'id': 18}
RA is : 00000002
RB is : 00000009
imm is : 0000002c
Execute stage:
operand1 is 00000002 operand2 is: 00000009
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000000
cycle is : 30
Fetch stage:
The value of PC is : 00000020
The instruction in IR is : 01F69733
Decode stage:
code : {'neumonic': 'sll', 'opcode': '0b0110011', 'funct3': '0b001', 'funct7': '0b0000000', 'rs1': '01101', 'rs2': '11111', 'rd': '01110', 'format': 'R', 'id': 5}
RA is : 00000002
RB is : 00000002
rd is : 14
Execute stage:
operand1 is 00000002 operand2 is: 00000002
RZ is : 00000008
Memory Access stage:
Register Update Stage:
RD: RY: 14 00000008
cycle is : 31
Fetch stage:
The value of PC is : 00000024
The instruction in IR is : 00B70733
Decode stage:
code : {'neumonic': 'add', 'opcode': '0b0110011', 'funct3': '0b000', 'funct7': '0b0000000', 'rs1': '01110', 'rs2': '01011', 'rd': '01110', 'format': 'R', 'id': 0}
RA is : 00000008
RB is : 10000000
rd is : 14
Execute stage:
operand1 is 00000008 operand2 is: 10000000
RZ is : 10000008
Memory Access stage:
Register Update Stage:
RD: RY: 14 10000008
cycle is : 32
Fetch stage:
The value of PC is : 00000028
The instruction in IR is : 00072783
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '01111', 'immediate': '000000000000', 'format': 'I', 'id': 14}
RA is : 10000008
rd is : 15
imm is : 00000000
Execute stage:
operand1 is 10000008 operand2 is: 00000000
RZ is : 10000008
Memory Access stage:
Register Update Stage:
RD: RY: 15 00000064
cycle is : 33
Fetch stage:
The value of PC is : 0000002c
The instruction in IR is : 00472803
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '10000', 'immediate': '000000000100', 'format': 'I', 'id': 14}
RA is : 10000008
rd is : 16
imm is : 00000004
Execute stage:
operand1 is 10000008 operand2 is: 00000004
RZ is : 1000000c
Memory Access stage:
Register Update Stage:
RD: RY: 16 00000046
cycle is : 34
Fetch stage:
The value of PC is : 00000030
The instruction in IR is : 00168693
Decode stage:
code : {'neumonic': 'addi', 'opcode': '0b0010011', 'funct3': '0b000', 'rs1': '01101', 'rd': '01101', 'immediate': '000000000001', 'format': 'I', 'id': 9}
RA is : 00000002
rd is : 13
imm is : 00000001
Execute stage:
operand1 is 00000002 operand2 is: 00000001
RZ is : 00000003
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000003
cycle is : 35
Fetch stage:
The value of PC is : 00000034
The instruction in IR is : FF07C4E3
Decode stage:
code : {'neumonic': 'blt', 'opcode': '0b1100011', 'funct3': '0b100', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111101000', 'format': 'SB', 'id': 20}
RA is : 00000064
RB is : 00000046
imm is : ffffffe8
Execute stage:
operand1 is 00000064 operand2 is: 00000046
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 36
Fetch stage:
The value of PC is : 00000038
The instruction in IR is : FF0782E3
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111100100', 'format': 'SB', 'id': 18}
RA is : 00000064
RB is : 00000046
imm is : ffffffe4
Execute stage:
operand1 is 00000064 operand2 is: 00000046
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 37
Fetch stage:
The value of PC is : 0000003c
The instruction in IR is : 01072023
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '10000', 'immediate': '000000000000', 'format': 'S', 'id': 17}
RA is : 10000008
RB is : 00000046
imm is : 00000000
Execute stage:
operand1 is 10000008 operand2 is: 00000000
RZ is : 10000008
Memory Access stage:
Register Update Stage:
RD: RY: 13 10000008
cycle is : 38
Fetch stage:
The value of PC is : 00000040
The instruction in IR is : 00F72223
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '01111', 'immediate': '000000000100', 'format': 'S', 'id': 17}
RA is : 10000008
RB is : 00000064
imm is : 00000004
Execute stage:
operand1 is 10000008 operand2 is: 00000004
RZ is : 1000000c
Memory Access stage:
Register Update Stage:
RD: RY: 13 1000000c
cycle is : 39
Fetch stage:
The value of PC is : 00000044
The instruction in IR is : FD9FF06F
Decode stage:
code : {'neumonic': 'jal', 'opcode': '0b1101111', 'immediate': '111111111111111011000', 'rd': '00000', 'format': 'UJ', 'id': 22}
rd is : 0
imm is : ffffffd8
Execute stage:
operand1 is 10000008 operand2 is: 00000064
RZ is : 1000006c
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000048
cycle is : 40
Fetch stage:
The value of PC is : 0000001c
The instruction in IR is : 02C68663
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01101', 'rs2': '01100', 'immediate': '0000000101100', 'format': 'SB', 'id': 18}
RA is : 00000003
RB is : 00000009
imm is : 0000002c
Execute stage:
operand1 is 00000003 operand2 is: 00000009
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000000
cycle is : 41
Fetch stage:
The value of PC is : 00000020
The instruction in IR is : 01F69733
Decode stage:
code : {'neumonic': 'sll', 'opcode': '0b0110011', 'funct3': '0b001', 'funct7': '0b0000000', 'rs1': '01101', 'rs2': '11111', 'rd': '01110', 'format': 'R', 'id': 5}
RA is : 00000003
RB is : 00000002
rd is : 14
Execute stage:
operand1 is 00000003 operand2 is: 00000002
RZ is : 0000000c
Memory Access stage:
Register Update Stage:
RD: RY: 14 0000000c
cycle is : 42
Fetch stage:
The value of PC is : 00000024
The instruction in IR is : 00B70733
Decode stage:
code : {'neumonic': 'add', 'opcode': '0b0110011', 'funct3': '0b000', 'funct7': '0b0000000', 'rs1': '01110', 'rs2': '01011', 'rd': '01110', 'format': 'R', 'id': 0}
RA is : 0000000c
RB is : 10000000
rd is : 14
Execute stage:
operand1 is 0000000c operand2 is: 10000000
RZ is : 1000000c
Memory Access stage:
Register Update Stage:
RD: RY: 14 1000000c
cycle is : 43
Fetch stage:
The value of PC is : 00000028
The instruction in IR is : 00072783
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '01111', 'immediate': '000000000000', 'format': 'I', 'id': 14}
RA is : 1000000c
rd is : 15
imm is : 00000000
Execute stage:
operand1 is 1000000c operand2 is: 00000000
RZ is : 1000000c
Memory Access stage:
Register Update Stage:
RD: RY: 15 00000064
cycle is : 44
Fetch stage:
The value of PC is : 0000002c
The instruction in IR is : 00472803
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '10000', 'immediate': '000000000100', 'format': 'I', 'id': 14}
RA is : 1000000c
rd is : 16
imm is : 00000004
Execute stage:
operand1 is 1000000c operand2 is: 00000004
RZ is : 10000010
Memory Access stage:
Register Update Stage:
RD: RY: 16 0000003C
cycle is : 45
Fetch stage:
The value of PC is : 00000030
The instruction in IR is : 00168693
Decode stage:
code : {'neumonic': 'addi', 'opcode': '0b0010011', 'funct3': '0b000', 'rs1': '01101', 'rd': '01101', 'immediate': '000000000001', 'format': 'I', 'id': 9}
RA is : 00000003
rd is : 13
imm is : 00000001
Execute stage:
operand1 is 00000003 operand2 is: 00000001
RZ is : 00000004
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000004
cycle is : 46
Fetch stage:
The value of PC is : 00000034
The instruction in IR is : FF07C4E3
Decode stage:
code : {'neumonic': 'blt', 'opcode': '0b1100011', 'funct3': '0b100', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111101000', 'format': 'SB', 'id': 20}
RA is : 00000064
RB is : 0000003C
imm is : ffffffe8
Execute stage:
operand1 is 00000064 operand2 is: 0000003C
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 47
Fetch stage:
The value of PC is : 00000038
The instruction in IR is : FF0782E3
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111100100', 'format': 'SB', 'id': 18}
RA is : 00000064
RB is : 0000003C
imm is : ffffffe4
Execute stage:
operand1 is 00000064 operand2 is: 0000003C
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 48
Fetch stage:
The value of PC is : 0000003c
The instruction in IR is : 01072023
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '10000', 'immediate': '000000000000', 'format': 'S', 'id': 17}
RA is : 1000000c
RB is : 0000003C
imm is : 00000000
Execute stage:
operand1 is 1000000c operand2 is: 00000000
RZ is : 1000000c
Memory Access stage:
Register Update Stage:
RD: RY: 13 1000000c
cycle is : 49
Fetch stage:
The value of PC is : 00000040
The instruction in IR is : 00F72223
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '01111', 'immediate': '000000000100', 'format': 'S', 'id': 17}
RA is : 1000000c
RB is : 00000064
imm is : 00000004
Execute stage:
operand1 is 1000000c operand2 is: 00000004
RZ is : 10000010
Memory Access stage:
Register Update Stage:
RD: RY: 13 10000010
cycle is : 50
Fetch stage:
The value of PC is : 00000044
The instruction in IR is : FD9FF06F
Decode stage:
code : {'neumonic': 'jal', 'opcode': '0b1101111', 'immediate': '111111111111111011000', 'rd': '00000', 'format': 'UJ', 'id': 22}
rd is : 0
imm is : ffffffd8
Execute stage:
operand1 is 1000000c operand2 is: 00000064
RZ is : 10000070
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000048
cycle is : 51
Fetch stage:
The value of PC is : 0000001c
The instruction in IR is : 02C68663
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01101', 'rs2': '01100', 'immediate': '0000000101100', 'format': 'SB', 'id': 18}
RA is : 00000004
RB is : 00000009
imm is : 0000002c
Execute stage:
operand1 is 00000004 operand2 is: 00000009
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000000
cycle is : 52
Fetch stage:
The value of PC is : 00000020
The instruction in IR is : 01F69733
Decode stage:
code : {'neumonic': 'sll', 'opcode': '0b0110011', 'funct3': '0b001', 'funct7': '0b0000000', 'rs1': '01101', 'rs2': '11111', 'rd': '01110', 'format': 'R', 'id': 5}
RA is : 00000004
RB is : 00000002
rd is : 14
Execute stage:
operand1 is 00000004 operand2 is: 00000002
RZ is : 00000010
Memory Access stage:
Register Update Stage:
RD: RY: 14 00000010
cycle is : 53
Fetch stage:
The value of PC is : 00000024
The instruction in IR is : 00B70733
Decode stage:
code : {'neumonic': 'add', 'opcode': '0b0110011', 'funct3': '0b000', 'funct7': '0b0000000', 'rs1': '01110', 'rs2': '01011', 'rd': '01110', 'format': 'R', 'id': 0}
RA is : 00000010
RB is : 10000000
rd is : 14
Execute stage:
operand1 is 00000010 operand2 is: 10000000
RZ is : 10000010
Memory Access stage:
Register Update Stage:
RD: RY: 14 10000010
cycle is : 54
Fetch stage:
The value of PC is : 00000028
The instruction in IR is : 00072783
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '01111', 'immediate': '000000000000', 'format': 'I', 'id': 14}
RA is : 10000010
rd is : 15
imm is : 00000000
Execute stage:
operand1 is 10000010 operand2 is: 00000000
RZ is : 10000010
Memory Access stage:
Register Update Stage:
RD: RY: 15 00000064
cycle is : 55
Fetch stage:
The value of PC is : 0000002c
The instruction in IR is : 00472803
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '10000', 'immediate': '000000000100', 'format': 'I', 'id': 14}
RA is : 10000010
rd is : 16
imm is : 00000004
Execute stage:
operand1 is 10000010 operand2 is: 00000004
RZ is : 10000014
Memory Access stage:
Register Update Stage:
RD: RY: 16 00000032
cycle is : 56
Fetch stage:
The value of PC is : 00000030
The instruction in IR is : 00168693
Decode stage:
code : {'neumonic': 'addi', 'opcode': '0b0010011', 'funct3': '0b000', 'rs1': '01101', 'rd': '01101', 'immediate': '000000000001', 'format': 'I', 'id': 9}
RA is : 00000004
rd is : 13
imm is : 00000001
Execute stage:
operand1 is 00000004 operand2 is: 00000001
RZ is : 00000005
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000005
cycle is : 57
Fetch stage:
The value of PC is : 00000034
The instruction in IR is : FF07C4E3
Decode stage:
code : {'neumonic': 'blt', 'opcode': '0b1100011', 'funct3': '0b100', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111101000', 'format': 'SB', 'id': 20}
RA is : 00000064
RB is : 00000032
imm is : ffffffe8
Execute stage:
operand1 is 00000064 operand2 is: 00000032
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 58
Fetch stage:
The value of PC is : 00000038
The instruction in IR is : FF0782E3
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111100100', 'format': 'SB', 'id': 18}
RA is : 00000064
RB is : 00000032
imm is : ffffffe4
Execute stage:
operand1 is 00000064 operand2 is: 00000032
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 59
Fetch stage:
The value of PC is : 0000003c
The instruction in IR is : 01072023
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '10000', 'immediate': '000000000000', 'format': 'S', 'id': 17}
RA is : 10000010
RB is : 00000032
imm is : 00000000
Execute stage:
operand1 is 10000010 operand2 is: 00000000
RZ is : 10000010
Memory Access stage:
Register Update Stage:
RD: RY: 13 10000010
cycle is : 60
Fetch stage:
The value of PC is : 00000040
The instruction in IR is : 00F72223
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '01111', 'immediate': '000000000100', 'format': 'S', 'id': 17}
RA is : 10000010
RB is : 00000064
imm is : 00000004
Execute stage:
operand1 is 10000010 operand2 is: 00000004
RZ is : 10000014
Memory Access stage:
Register Update Stage:
RD: RY: 13 10000014
cycle is : 61
Fetch stage:
The value of PC is : 00000044
The instruction in IR is : FD9FF06F
Decode stage:
code : {'neumonic': 'jal', 'opcode': '0b1101111', 'immediate': '111111111111111011000', 'rd': '00000', 'format': 'UJ', 'id': 22}
rd is : 0
imm is : ffffffd8
Execute stage:
operand1 is 10000010 operand2 is: 00000064
RZ is : 10000074
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000048
cycle is : 62
Fetch stage:
The value of PC is : 0000001c
The instruction in IR is : 02C68663
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01101', 'rs2': '01100', 'immediate': '0000000101100', 'format': 'SB', 'id': 18}
RA is : 00000005
RB is : 00000009
imm is : 0000002c
Execute stage:
operand1 is 00000005 operand2 is: 00000009
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000000
cycle is : 63
Fetch stage:
The value of PC is : 00000020
The instruction in IR is : 01F69733
Decode stage:
code : {'neumonic': 'sll', 'opcode': '0b0110011', 'funct3': '0b001', 'funct7': '0b0000000', 'rs1': '01101', 'rs2': '11111', 'rd': '01110', 'format': 'R', 'id': 5}
RA is : 00000005
RB is : 00000002
rd is : 14
Execute stage:
operand1 is 00000005 operand2 is: 00000002
RZ is : 00000014
Memory Access stage:
Register Update Stage:
RD: RY: 14 00000014
cycle is : 64
Fetch stage:
The value of PC is : 00000024
The instruction in IR is : 00B70733
Decode stage:
code : {'neumonic': 'add', 'opcode': '0b0110011', 'funct3': '0b000', 'funct7': '0b0000000', 'rs1': '01110', 'rs2': '01011', 'rd': '01110', 'format': 'R', 'id': 0}
RA is : 00000014
RB is : 10000000
rd is : 14
Execute stage:
operand1 is 00000014 operand2 is: 10000000
RZ is : 10000014
Memory Access stage:
Register Update Stage:
RD: RY: 14 10000014
cycle is : 65
Fetch stage:
The value of PC is : 00000028
The instruction in IR is : 00072783
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '01111', 'immediate': '000000000000', 'format': 'I', 'id': 14}
RA is : 10000014
rd is : 15
imm is : 00000000
Execute stage:
operand1 is 10000014 operand2 is: 00000000
RZ is : 10000014
Memory Access stage:
Register Update Stage:
RD: RY: 15 00000064
cycle is : 66
Fetch stage:
The value of PC is : 0000002c
The instruction in IR is : 00472803
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '10000', 'immediate': '000000000100', 'format': 'I', 'id': 14}
RA is : 10000014
rd is : 16
imm is : 00000004
Execute stage:
operand1 is 10000014 operand2 is: 00000004
RZ is : 10000018
Memory Access stage:
Register Update Stage:
RD: RY: 16 00000028
cycle is : 67
Fetch stage:
The value of PC is : 00000030
The instruction in IR is : 00168693
Decode stage:
code : {'neumonic': 'addi', 'opcode': '0b0010011', 'funct3': '0b000', 'rs1': '01101', 'rd': '01101', 'immediate': '000000000001', 'format': 'I', 'id': 9}
RA is : 00000005
rd is : 13
imm is : 00000001
Execute stage:
operand1 is 00000005 operand2 is: 00000001
RZ is : 00000006
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000006
cycle is : 68
Fetch stage:
The value of PC is : 00000034
The instruction in IR is : FF07C4E3
Decode stage:
code : {'neumonic': 'blt', 'opcode': '0b1100011', 'funct3': '0b100', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111101000', 'format': 'SB', 'id': 20}
RA is : 00000064
RB is : 00000028
imm is : ffffffe8
Execute stage:
operand1 is 00000064 operand2 is: 00000028
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 69
Fetch stage:
The value of PC is : 00000038
The instruction in IR is : FF0782E3
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111100100', 'format': 'SB', 'id': 18}
RA is : 00000064
RB is : 00000028
imm is : ffffffe4
Execute stage:
operand1 is 00000064 operand2 is: 00000028
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 70
Fetch stage:
The value of PC is : 0000003c
The instruction in IR is : 01072023
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '10000', 'immediate': '000000000000', 'format': 'S', 'id': 17}
RA is : 10000014
RB is : 00000028
imm is : 00000000
Execute stage:
operand1 is 10000014 operand2 is: 00000000
RZ is : 10000014
Memory Access stage:
Register Update Stage:
RD: RY: 13 10000014
cycle is : 71
Fetch stage:
The value of PC is : 00000040
The instruction in IR is : 00F72223
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '01111', 'immediate': '000000000100', 'format': 'S', 'id': 17}
RA is : 10000014
RB is : 00000064
imm is : 00000004
Execute stage:
operand1 is 10000014 operand2 is: 00000004
RZ is : 10000018
Memory Access stage:
Register Update Stage:
RD: RY: 13 10000018
cycle is : 72
Fetch stage:
The value of PC is : 00000044
The instruction in IR is : FD9FF06F
Decode stage:
code : {'neumonic': 'jal', 'opcode': '0b1101111', 'immediate': '111111111111111011000', 'rd': '00000', 'format': 'UJ', 'id': 22}
rd is : 0
imm is : ffffffd8
Execute stage:
operand1 is 10000014 operand2 is: 00000064
RZ is : 10000078
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000048
cycle is : 73
Fetch stage:
The value of PC is : 0000001c
The instruction in IR is : 02C68663
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01101', 'rs2': '01100', 'immediate': '0000000101100', 'format': 'SB', 'id': 18}
RA is : 00000006
RB is : 00000009
imm is : 0000002c
Execute stage:
operand1 is 00000006 operand2 is: 00000009
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000000
cycle is : 74
Fetch stage:
The value of PC is : 00000020
The instruction in IR is : 01F69733
Decode stage:
code : {'neumonic': 'sll', 'opcode': '0b0110011', 'funct3': '0b001', 'funct7': '0b0000000', 'rs1': '01101', 'rs2': '11111', 'rd': '01110', 'format': 'R', 'id': 5}
RA is : 00000006
RB is : 00000002
rd is : 14
Execute stage:
operand1 is 00000006 operand2 is: 00000002
RZ is : 00000018
Memory Access stage:
Register Update Stage:
RD: RY: 14 00000018
cycle is : 75
Fetch stage:
The value of PC is : 00000024
The instruction in IR is : 00B70733
Decode stage:
code : {'neumonic': 'add', 'opcode': '0b0110011', 'funct3': '0b000', 'funct7': '0b0000000', 'rs1': '01110', 'rs2': '01011', 'rd': '01110', 'format': 'R', 'id': 0}
RA is : 00000018
RB is : 10000000
rd is : 14
Execute stage:
operand1 is 00000018 operand2 is: 10000000
RZ is : 10000018
Memory Access stage:
Register Update Stage:
RD: RY: 14 10000018
cycle is : 76
Fetch stage:
The value of PC is : 00000028
The instruction in IR is : 00072783
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '01111', 'immediate': '000000000000', 'format': 'I', 'id': 14}
RA is : 10000018
rd is : 15
imm is : 00000000
Execute stage:
operand1 is 10000018 operand2 is: 00000000
RZ is : 10000018
Memory Access stage:
Register Update Stage:
RD: RY: 15 00000064
cycle is : 77
Fetch stage:
The value of PC is : 0000002c
The instruction in IR is : 00472803
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '10000', 'immediate': '000000000100', 'format': 'I', 'id': 14}
RA is : 10000018
rd is : 16
imm is : 00000004
Execute stage:
operand1 is 10000018 operand2 is: 00000004
RZ is : 1000001c
Memory Access stage:
Register Update Stage:
RD: RY: 16 0000001E
cycle is : 78
Fetch stage:
The value of PC is : 00000030
The instruction in IR is : 00168693
Decode stage:
code : {'neumonic': 'addi', 'opcode': '0b0010011', 'funct3': '0b000', 'rs1': '01101', 'rd': '01101', 'immediate': '000000000001', 'format': 'I', 'id': 9}
RA is : 00000006
rd is : 13
imm is : 00000001
Execute stage:
operand1 is 00000006 operand2 is: 00000001
RZ is : 00000007
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000007
cycle is : 79
Fetch stage:
The value of PC is : 00000034
The instruction in IR is : FF07C4E3
Decode stage:
code : {'neumonic': 'blt', 'opcode': '0b1100011', 'funct3': '0b100', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111101000', 'format': 'SB', 'id': 20}
RA is : 00000064
RB is : 0000001E
imm is : ffffffe8
Execute stage:
operand1 is 00000064 operand2 is: 0000001E
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 80
Fetch stage:
The value of PC is : 00000038
The instruction in IR is : FF0782E3
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111100100', 'format': 'SB', 'id': 18}
RA is : 00000064
RB is : 0000001E
imm is : ffffffe4
Execute stage:
operand1 is 00000064 operand2 is: 0000001E
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 81
Fetch stage:
The value of PC is : 0000003c
The instruction in IR is : 01072023
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '10000', 'immediate': '000000000000', 'format': 'S', 'id': 17}
RA is : 10000018
RB is : 0000001E
imm is : 00000000
Execute stage:
operand1 is 10000018 operand2 is: 00000000
RZ is : 10000018
Memory Access stage:
Register Update Stage:
RD: RY: 13 10000018
cycle is : 82
Fetch stage:
The value of PC is : 00000040
The instruction in IR is : 00F72223
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '01111', 'immediate': '000000000100', 'format': 'S', 'id': 17}
RA is : 10000018
RB is : 00000064
imm is : 00000004
Execute stage:
operand1 is 10000018 operand2 is: 00000004
RZ is : 1000001c
Memory Access stage:
Register Update Stage:
RD: RY: 13 1000001c
cycle is : 83
Fetch stage:
The value of PC is : 00000044
The instruction in IR is : FD9FF06F
Decode stage:
code : {'neumonic': 'jal', 'opcode': '0b1101111', 'immediate': '111111111111111011000', 'rd': '00000', 'format': 'UJ', 'id': 22}
rd is : 0
imm is : ffffffd8
Execute stage:
operand1 is 10000018 operand2 is: 00000064
RZ is : 1000007c
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000048
cycle is : 84
Fetch stage:
The value of PC is : 0000001c
The instruction in IR is : 02C68663
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01101', 'rs2': '01100', 'immediate': '0000000101100', 'format': 'SB', 'id': 18}
RA is : 00000007
RB is : 00000009
imm is : 0000002c
Execute stage:
operand1 is 00000007 operand2 is: 00000009
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000000
cycle is : 85
Fetch stage:
The value of PC is : 00000020
The instruction in IR is : 01F69733
Decode stage:
code : {'neumonic': 'sll', 'opcode': '0b0110011', 'funct3': '0b001', 'funct7': '0b0000000', 'rs1': '01101', 'rs2': '11111', 'rd': '01110', 'format': 'R', 'id': 5}
RA is : 00000007
RB is : 00000002
rd is : 14
Execute stage:
operand1 is 00000007 operand2 is: 00000002
RZ is : 0000001c
Memory Access stage:
Register Update Stage:
RD: RY: 14 0000001c
cycle is : 86
Fetch stage:
The value of PC is : 00000024
The instruction in IR is : 00B70733
Decode stage:
code : {'neumonic': 'add', 'opcode': '0b0110011', 'funct3': '0b000', 'funct7': '0b0000000', 'rs1': '01110', 'rs2': '01011', 'rd': '01110', 'format': 'R', 'id': 0}
RA is : 0000001c
RB is : 10000000
rd is : 14
Execute stage:
operand1 is 0000001c operand2 is: 10000000
RZ is : 1000001c
Memory Access stage:
Register Update Stage:
RD: RY: 14 1000001c
cycle is : 87
Fetch stage:
The value of PC is : 00000028
The instruction in IR is : 00072783
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '01111', 'immediate': '000000000000', 'format': 'I', 'id': 14}
RA is : 1000001c
rd is : 15
imm is : 00000000
Execute stage:
operand1 is 1000001c operand2 is: 00000000
RZ is : 1000001c
Memory Access stage:
Register Update Stage:
RD: RY: 15 00000064
cycle is : 88
Fetch stage:
The value of PC is : 0000002c
The instruction in IR is : 00472803
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '10000', 'immediate': '000000000100', 'format': 'I', 'id': 14}
RA is : 1000001c
rd is : 16
imm is : 00000004
Execute stage:
operand1 is 1000001c operand2 is: 00000004
RZ is : 10000020
Memory Access stage:
Register Update Stage:
RD: RY: 16 00000014
cycle is : 89
Fetch stage:
The value of PC is : 00000030
The instruction in IR is : 00168693
Decode stage:
code : {'neumonic': 'addi', 'opcode': '0b0010011', 'funct3': '0b000', 'rs1': '01101', 'rd': '01101', 'immediate': '000000000001', 'format': 'I', 'id': 9}
RA is : 00000007
rd is : 13
imm is : 00000001
Execute stage:
operand1 is 00000007 operand2 is: 00000001
RZ is : 00000008
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000008
cycle is : 90
Fetch stage:
The value of PC is : 00000034
The instruction in IR is : FF07C4E3
Decode stage:
code : {'neumonic': 'blt', 'opcode': '0b1100011', 'funct3': '0b100', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111101000', 'format': 'SB', 'id': 20}
RA is : 00000064
RB is : 00000014
imm is : ffffffe8
Execute stage:
operand1 is 00000064 operand2 is: 00000014
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 91
Fetch stage:
The value of PC is : 00000038
The instruction in IR is : FF0782E3
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111100100', 'format': 'SB', 'id': 18}
RA is : 00000064
RB is : 00000014
imm is : ffffffe4
Execute stage:
operand1 is 00000064 operand2 is: 00000014
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 92
Fetch stage:
The value of PC is : 0000003c
The instruction in IR is : 01072023
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '10000', 'immediate': '000000000000', 'format': 'S', 'id': 17}
RA is : 1000001c
RB is : 00000014
imm is : 00000000
Execute stage:
operand1 is 1000001c operand2 is: 00000000
RZ is : 1000001c
Memory Access stage:
Register Update Stage:
RD: RY: 13 1000001c
cycle is : 93
Fetch stage:
The value of PC is : 00000040
The instruction in IR is : 00F72223
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '01111', 'immediate': '000000000100', 'format': 'S', 'id': 17}
RA is : 1000001c
RB is : 00000064
imm is : 00000004
Execute stage:
operand1 is 1000001c operand2 is: 00000004
RZ is : 10000020
Memory Access stage:
Register Update Stage:
RD: RY: 13 10000020
cycle is : 94
Fetch stage:
The value of PC is : 00000044
The instruction in IR is : FD9FF06F
Decode stage:
code : {'neumonic': 'jal', 'opcode': '0b1101111', 'immediate': '111111111111111011000', 'rd': '00000', 'format': 'UJ', 'id': 22}
rd is : 0
imm is : ffffffd8
Execute stage:
operand1 is 1000001c operand2 is: 00000064
RZ is : 10000080
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000048
cycle is : 95
Fetch stage:
The value of PC is : 0000001c
The instruction in IR is : 02C68663
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01101', 'rs2': '01100', 'immediate': '0000000101100', 'format': 'SB', 'id': 18}
RA is : 00000008
RB is : 00000009
imm is : 0000002c
Execute stage:
operand1 is 00000008 operand2 is: 00000009
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000000
cycle is : 96
Fetch stage:
The value of PC is : 00000020
The instruction in IR is : 01F69733
Decode stage:
code : {'neumonic': 'sll', 'opcode': '0b0110011', 'funct3': '0b001', 'funct7': '0b0000000', 'rs1': '01101', 'rs2': '11111', 'rd': '01110', 'format': 'R', 'id': 5}
RA is : 00000008
RB is : 00000002
rd is : 14
Execute stage:
operand1 is 00000008 operand2 is: 00000002
RZ is : 00000020
Memory Access stage:
Register Update Stage:
RD: RY: 14 00000020
cycle is : 97
Fetch stage:
The value of PC is : 00000024
The instruction in IR is : 00B70733
Decode stage:
code : {'neumonic': 'add', 'opcode': '0b0110011', 'funct3': '0b000', 'funct7': '0b0000000', 'rs1': '01110', 'rs2': '01011', 'rd': '01110', 'format': 'R', 'id': 0}
RA is : 00000020
RB is : 10000000
rd is : 14
Execute stage:
operand1 is 00000020 operand2 is: 10000000
RZ is : 10000020
Memory Access stage:
Register Update Stage:
RD: RY: 14 10000020
cycle is : 98
Fetch stage:
The value of PC is : 00000028
The instruction in IR is : 00072783
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '01111', 'immediate': '000000000000', 'format': 'I', 'id': 14}
RA is : 10000020
rd is : 15
imm is : 00000000
Execute stage:
operand1 is 10000020 operand2 is: 00000000
RZ is : 10000020
Memory Access stage:
Register Update Stage:
RD: RY: 15 00000064
cycle is : 99
Fetch stage:
The value of PC is : 0000002c
The instruction in IR is : 00472803
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '10000', 'immediate': '000000000100', 'format': 'I', 'id': 14}
RA is : 10000020
rd is : 16
imm is : 00000004
Execute stage:
operand1 is 10000020 operand2 is: 00000004
RZ is : 10000024
Memory Access stage:
Register Update Stage:
RD: RY: 16 0000000a
cycle is : 100
Fetch stage:
The value of PC is : 00000030
The instruction in IR is : 00168693
Decode stage:
code : {'neumonic': 'addi', 'opcode': '0b0010011', 'funct3': '0b000', 'rs1': '01101', 'rd': '01101', 'immediate': '000000000001', 'format': 'I', 'id': 9}
RA is : 00000008
rd is : 13
imm is : 00000001
Execute stage:
operand1 is 00000008 operand2 is: 00000001
RZ is : 00000009
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000009
cycle is : 101
Fetch stage:
The value of PC is : 00000034
The instruction in IR is : FF07C4E3
Decode stage:
code : {'neumonic': 'blt', 'opcode': '0b1100011', 'funct3': '0b100', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111101000', 'format': 'SB', 'id': 20}
RA is : 00000064
RB is : 0000000a
imm is : ffffffe8
Execute stage:
operand1 is 00000064 operand2 is: 0000000a
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 102
Fetch stage:
The value of PC is : 00000038
The instruction in IR is : FF0782E3
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111100100', 'format': 'SB', 'id': 18}
RA is : 00000064
RB is : 0000000a
imm is : ffffffe4
Execute stage:
operand1 is 00000064 operand2 is: 0000000a
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 103
Fetch stage:
The value of PC is : 0000003c
The instruction in IR is : 01072023
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '10000', 'immediate': '000000000000', 'format': 'S', 'id': 17}
RA is : 10000020
RB is : 0000000a
imm is : 00000000
Execute stage:
operand1 is 10000020 operand2 is: 00000000
RZ is : 10000020
Memory Access stage:
Register Update Stage:
RD: RY: 13 10000020
cycle is : 104
Fetch stage:
The value of PC is : 00000040
The instruction in IR is : 00F72223
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '01111', 'immediate': '000000000100', 'format': 'S', 'id': 17}
RA is : 10000020
RB is : 00000064
imm is : 00000004
Execute stage:
operand1 is 10000020 operand2 is: 00000004
RZ is : 10000024
Memory Access stage:
Register Update Stage:
RD: RY: 13 10000024
cycle is : 105
Fetch stage:
The value of PC is : 00000044
The instruction in IR is : FD9FF06F
Decode stage:
code : {'neumonic': 'jal', 'opcode': '0b1101111', 'immediate': '111111111111111011000', 'rd': '00000', 'format': 'UJ', 'id': 22}
rd is : 0
imm is : ffffffd8
Execute stage:
operand1 is 10000020 operand2 is: 00000064
RZ is : 10000084
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000048
cycle is : 106
Fetch stage:
The value of PC is : 0000001c
The instruction in IR is : 02C68663
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01101', 'rs2': '01100', 'immediate': '0000000101100', 'format': 'SB', 'id': 18}
RA is : 00000009
RB is : 00000009
imm is : 0000002c
Execute stage:
operand1 is 00000009 operand2 is: 00000009
RZ is : 00000001
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000001
cycle is : 107
Fetch stage:
The value of PC is : 00000048
The instruction in IR is : FC9FF06F
Decode stage:
code : {'neumonic': 'jal', 'opcode': '0b1101111', 'immediate': '111111111111111001000', 'rd': '00000', 'format': 'UJ', 'id': 22}
rd is : 0
imm is : ffffffc8
Execute stage:
operand1 is 00000009 operand2 is: 00000009
RZ is : 00000012
Memory Access stage:
Register Update Stage:
RD: RY: 0 0000004c
cycle is : 108
Fetch stage:
The value of PC is : 00000010
The instruction in IR is : FFF60613
Decode stage:
code : {'neumonic': 'addi', 'opcode': '0b0010011', 'funct3': '0b000', 'rs1': '01100', 'rd': '01100', 'immediate': '111111111111', 'format': 'I', 'id': 9}
RA is : 00000009
rd is : 12
imm is : ffffffff
Execute stage:
operand1 is 00000009 operand2 is: ffffffff
RZ is : 00000008
Memory Access stage:
Register Update Stage:
RD: RY: 12 00000008
cycle is : 109
Fetch stage:
The value of PC is : 00000014
The instruction in IR is : 02060C63
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01100', 'rs2': '00000', 'immediate': '0000000111000', 'format': 'SB', 'id': 18}
RA is : 00000008
RB is : 00000000
imm is : 00000038
Execute stage:
operand1 is 00000008 operand2 is: 00000000
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 12 00000000
cycle is : 110
Fetch stage:
The value of PC is : 00000018
The instruction in IR is : 00000693
Decode stage:
code : {'neumonic': 'addi', 'opcode': '0b0010011', 'funct3': '0b000', 'rs1': '00000', 'rd': '01101', 'immediate': '000000000000', 'format': 'I', 'id': 9}
RA is : 00000000
rd is : 13
imm is : 00000000
Execute stage:
operand1 is 00000000 operand2 is: 00000000
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 111
Fetch stage:
The value of PC is : 0000001c
The instruction in IR is : 02C68663
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01101', 'rs2': '01100', 'immediate': '0000000101100', 'format': 'SB', 'id': 18}
RA is : 00000000
RB is : 00000008
imm is : 0000002c
Execute stage:
operand1 is 00000000 operand2 is: 00000008
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 112
Fetch stage:
The value of PC is : 00000020
The instruction in IR is : 01F69733
Decode stage:
code : {'neumonic': 'sll', 'opcode': '0b0110011', 'funct3': '0b001', 'funct7': '0b0000000', 'rs1': '01101', 'rs2': '11111', 'rd': '01110', 'format': 'R', 'id': 5}
RA is : 00000000
RB is : 00000002
rd is : 14
Execute stage:
operand1 is 00000000 operand2 is: 00000002
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 14 00000000
cycle is : 113
Fetch stage:
The value of PC is : 00000024
The instruction in IR is : 00B70733
Decode stage:
code : {'neumonic': 'add', 'opcode': '0b0110011', 'funct3': '0b000', 'funct7': '0b0000000', 'rs1': '01110', 'rs2': '01011', 'rd': '01110', 'format': 'R', 'id': 0}
RA is : 00000000
RB is : 10000000
rd is : 14
Execute stage:
operand1 is 00000000 operand2 is: 10000000
RZ is : 10000000
Memory Access stage:
Register Update Stage:
RD: RY: 14 10000000
cycle is : 114
Fetch stage:
The value of PC is : 00000028
The instruction in IR is : 00072783
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '01111', 'immediate': '000000000000', 'format': 'I', 'id': 14}
RA is : 10000000
rd is : 15
imm is : 00000000
Execute stage:
operand1 is 10000000 operand2 is: 00000000
RZ is : 10000000
Memory Access stage:
Register Update Stage:
RD: RY: 15 0000005A
cycle is : 115
Fetch stage:
The value of PC is : 0000002c
The instruction in IR is : 00472803
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '10000', 'immediate': '000000000100', 'format': 'I', 'id': 14}
RA is : 10000000
rd is : 16
imm is : 00000004
Execute stage:
operand1 is 10000000 operand2 is: 00000004
RZ is : 10000004
Memory Access stage:
Register Update Stage:
RD: RY: 16 00000050
cycle is : 116
Fetch stage:
The value of PC is : 00000030
The instruction in IR is : 00168693
Decode stage:
code : {'neumonic': 'addi', 'opcode': '0b0010011', 'funct3': '0b000', 'rs1': '01101', 'rd': '01101', 'immediate': '000000000001', 'format': 'I', 'id': 9}
RA is : 00000000
rd is : 13
imm is : 00000001
Execute stage:
operand1 is 00000000 operand2 is: 00000001
RZ is : 00000001
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000001
cycle is : 117
Fetch stage:
The value of PC is : 00000034
The instruction in IR is : FF07C4E3
Decode stage:
code : {'neumonic': 'blt', 'opcode': '0b1100011', 'funct3': '0b100', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111101000', 'format': 'SB', 'id': 20}
RA is : 0000005A
RB is : 00000050
imm is : ffffffe8
Execute stage:
operand1 is 0000005A operand2 is: 00000050
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 118
Fetch stage:
The value of PC is : 00000038
The instruction in IR is : FF0782E3
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111100100', 'format': 'SB', 'id': 18}
RA is : 0000005A
RB is : 00000050
imm is : ffffffe4
Execute stage:
operand1 is 0000005A operand2 is: 00000050
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 119
Fetch stage:
The value of PC is : 0000003c
The instruction in IR is : 01072023
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '10000', 'immediate': '000000000000', 'format': 'S', 'id': 17}
RA is : 10000000
RB is : 00000050
imm is : 00000000
Execute stage:
operand1 is 10000000 operand2 is: 00000000
RZ is : 10000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 10000000
cycle is : 120
Fetch stage:
The value of PC is : 00000040
The instruction in IR is : 00F72223
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '01111', 'immediate': '000000000100', 'format': 'S', 'id': 17}
RA is : 10000000
RB is : 0000005A
imm is : 00000004
Execute stage:
operand1 is 10000000 operand2 is: 00000004
RZ is : 10000004
Memory Access stage:
Register Update Stage:
RD: RY: 13 10000004
cycle is : 121
Fetch stage:
The value of PC is : 00000044
The instruction in IR is : FD9FF06F
Decode stage:
code : {'neumonic': 'jal', 'opcode': '0b1101111', 'immediate': '111111111111111011000', 'rd': '00000', 'format': 'UJ', 'id': 22}
rd is : 0
imm is : ffffffd8
Execute stage:
operand1 is 10000000 operand2 is: 0000005A
RZ is : 1000005a
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000048
cycle is : 122
Fetch stage:
The value of PC is : 0000001c
The instruction in IR is : 02C68663
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01101', 'rs2': '01100', 'immediate': '0000000101100', 'format': 'SB', 'id': 18}
RA is : 00000001
RB is : 00000008
imm is : 0000002c
Execute stage:
operand1 is 00000001 operand2 is: 00000008
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000000
cycle is : 123
Fetch stage:
The value of PC is : 00000020
The instruction in IR is : 01F69733
Decode stage:
code : {'neumonic': 'sll', 'opcode': '0b0110011', 'funct3': '0b001', 'funct7': '0b0000000', 'rs1': '01101', 'rs2': '11111', 'rd': '01110', 'format': 'R', 'id': 5}
RA is : 00000001
RB is : 00000002
rd is : 14
Execute stage:
operand1 is 00000001 operand2 is: 00000002
RZ is : 00000004
Memory Access stage:
Register Update Stage:
RD: RY: 14 00000004
cycle is : 124
Fetch stage:
The value of PC is : 00000024
The instruction in IR is : 00B70733
Decode stage:
code : {'neumonic': 'add', 'opcode': '0b0110011', 'funct3': '0b000', 'funct7': '0b0000000', 'rs1': '01110', 'rs2': '01011', 'rd': '01110', 'format': 'R', 'id': 0}
RA is : 00000004
RB is : 10000000
rd is : 14
Execute stage:
operand1 is 00000004 operand2 is: 10000000
RZ is : 10000004
Memory Access stage:
Register Update Stage:
RD: RY: 14 10000004
cycle is : 125
Fetch stage:
The value of PC is : 00000028
The instruction in IR is : 00072783
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '01111', 'immediate': '000000000000', 'format': 'I', 'id': 14}
RA is : 10000004
rd is : 15
imm is : 00000000
Execute stage:
operand1 is 10000004 operand2 is: 00000000
RZ is : 10000004
Memory Access stage:
Register Update Stage:
RD: RY: 15 0000005A
cycle is : 126
Fetch stage:
The value of PC is : 0000002c
The instruction in IR is : 00472803
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '10000', 'immediate': '000000000100', 'format': 'I', 'id': 14}
RA is : 10000004
rd is : 16
imm is : 00000004
Execute stage:
operand1 is 10000004 operand2 is: 00000004
RZ is : 10000008
Memory Access stage:
Register Update Stage:
RD: RY: 16 00000046
cycle is : 127
Fetch stage:
The value of PC is : 00000030
The instruction in IR is : 00168693
Decode stage:
code : {'neumonic': 'addi', 'opcode': '0b0010011', 'funct3': '0b000', 'rs1': '01101', 'rd': '01101', 'immediate': '000000000001', 'format': 'I', 'id': 9}
RA is : 00000001
rd is : 13
imm is : 00000001
Execute stage:
operand1 is 00000001 operand2 is: 00000001
RZ is : 00000002
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000002
cycle is : 128
Fetch stage:
The value of PC is : 00000034
The instruction in IR is : FF07C4E3
Decode stage:
code : {'neumonic': 'blt', 'opcode': '0b1100011', 'funct3': '0b100', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111101000', 'format': 'SB', 'id': 20}
RA is : 0000005A
RB is : 00000046
imm is : ffffffe8
Execute stage:
operand1 is 0000005A operand2 is: 00000046
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 129
Fetch stage:
The value of PC is : 00000038
The instruction in IR is : FF0782E3
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111100100', 'format': 'SB', 'id': 18}
RA is : 0000005A
RB is : 00000046
imm is : ffffffe4
Execute stage:
operand1 is 0000005A operand2 is: 00000046
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 130
Fetch stage:
The value of PC is : 0000003c
The instruction in IR is : 01072023
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '10000', 'immediate': '000000000000', 'format': 'S', 'id': 17}
RA is : 10000004
RB is : 00000046
imm is : 00000000
Execute stage:
operand1 is 10000004 operand2 is: 00000000
RZ is : 10000004
Memory Access stage:
Register Update Stage:
RD: RY: 13 10000004
cycle is : 131
Fetch stage:
The value of PC is : 00000040
The instruction in IR is : 00F72223
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '01111', 'immediate': '000000000100', 'format': 'S', 'id': 17}
RA is : 10000004
RB is : 0000005A
imm is : 00000004
Execute stage:
operand1 is 10000004 operand2 is: 00000004
RZ is : 10000008
Memory Access stage:
Register Update Stage:
RD: RY: 13 10000008
cycle is : 132
Fetch stage:
The value of PC is : 00000044
The instruction in IR is : FD9FF06F
Decode stage:
code : {'neumonic': 'jal', 'opcode': '0b1101111', 'immediate': '111111111111111011000', 'rd': '00000', 'format': 'UJ', 'id': 22}
rd is : 0
imm is : ffffffd8
Execute stage:
operand1 is 10000004 operand2 is: 0000005A
RZ is : 1000005e
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000048
cycle is : 133
Fetch stage:
The value of PC is : 0000001c
The instruction in IR is : 02C68663
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01101', 'rs2': '01100', 'immediate': '0000000101100', 'format': 'SB', 'id': 18}
RA is : 00000002
RB is : 00000008
imm is : 0000002c
Execute stage:
operand1 is 00000002 operand2 is: 00000008
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000000
cycle is : 134
Fetch stage:
The value of PC is : 00000020
The instruction in IR is : 01F69733
Decode stage:
code : {'neumonic': 'sll', 'opcode': '0b0110011', 'funct3': '0b001', 'funct7': '0b0000000', 'rs1': '01101', 'rs2': '11111', 'rd': '01110', 'format': 'R', 'id': 5}
RA is : 00000002
RB is : 00000002
rd is : 14
Execute stage:
operand1 is 00000002 operand2 is: 00000002
RZ is : 00000008
Memory Access stage:
Register Update Stage:
RD: RY: 14 00000008
cycle is : 135
Fetch stage:
The value of PC is : 00000024
The instruction in IR is : 00B70733
Decode stage:
code : {'neumonic': 'add', 'opcode': '0b0110011', 'funct3': '0b000', 'funct7': '0b0000000', 'rs1': '01110', 'rs2': '01011', 'rd': '01110', 'format': 'R', 'id': 0}
RA is : 00000008
RB is : 10000000
rd is : 14
Execute stage:
operand1 is 00000008 operand2 is: 10000000
RZ is : 10000008
Memory Access stage:
Register Update Stage:
RD: RY: 14 10000008
cycle is : 136
Fetch stage:
The value of PC is : 00000028
The instruction in IR is : 00072783
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '01111', 'immediate': '000000000000', 'format': 'I', 'id': 14}
RA is : 10000008
rd is : 15
imm is : 00000000
Execute stage:
operand1 is 10000008 operand2 is: 00000000
RZ is : 10000008
Memory Access stage:
Register Update Stage:
RD: RY: 15 0000005A
cycle is : 137
Fetch stage:
The value of PC is : 0000002c
The instruction in IR is : 00472803
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '10000', 'immediate': '000000000100', 'format': 'I', 'id': 14}
RA is : 10000008
rd is : 16
imm is : 00000004
Execute stage:
operand1 is 10000008 operand2 is: 00000004
RZ is : 1000000c
Memory Access stage:
Register Update Stage:
RD: RY: 16 0000003C
cycle is : 138
Fetch stage:
The value of PC is : 00000030
The instruction in IR is : 00168693
Decode stage:
code : {'neumonic': 'addi', 'opcode': '0b0010011', 'funct3': '0b000', 'rs1': '01101', 'rd': '01101', 'immediate': '000000000001', 'format': 'I', 'id': 9}
RA is : 00000002
rd is : 13
imm is : 00000001
Execute stage:
operand1 is 00000002 operand2 is: 00000001
RZ is : 00000003
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000003
cycle is : 139
Fetch stage:
The value of PC is : 00000034
The instruction in IR is : FF07C4E3
Decode stage:
code : {'neumonic': 'blt', 'opcode': '0b1100011', 'funct3': '0b100', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111101000', 'format': 'SB', 'id': 20}
RA is : 0000005A
RB is : 0000003C
imm is : ffffffe8
Execute stage:
operand1 is 0000005A operand2 is: 0000003C
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 140
Fetch stage:
The value of PC is : 00000038
The instruction in IR is : FF0782E3
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111100100', 'format': 'SB', 'id': 18}
RA is : 0000005A
RB is : 0000003C
imm is : ffffffe4
Execute stage:
operand1 is 0000005A operand2 is: 0000003C
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 141
Fetch stage:
The value of PC is : 0000003c
The instruction in IR is : 01072023
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '10000', 'immediate': '000000000000', 'format': 'S', 'id': 17}
RA is : 10000008
RB is : 0000003C
imm is : 00000000
Execute stage:
operand1 is 10000008 operand2 is: 00000000
RZ is : 10000008
Memory Access stage:
Register Update Stage:
RD: RY: 13 10000008
cycle is : 142
Fetch stage:
The value of PC is : 00000040
The instruction in IR is : 00F72223
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '01111', 'immediate': '000000000100', 'format': 'S', 'id': 17}
RA is : 10000008
RB is : 0000005A
imm is : 00000004
Execute stage:
operand1 is 10000008 operand2 is: 00000004
RZ is : 1000000c
Memory Access stage:
Register Update Stage:
RD: RY: 13 1000000c
cycle is : 143
Fetch stage:
The value of PC is : 00000044
The instruction in IR is : FD9FF06F
Decode stage:
code : {'neumonic': 'jal', 'opcode': '0b1101111', 'immediate': '111111111111111011000', 'rd': '00000', 'format': 'UJ', 'id': 22}
rd is : 0
imm is : ffffffd8
Execute stage:
operand1 is 10000008 operand2 is: 0000005A
RZ is : 10000062
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000048
cycle is : 144
Fetch stage:
The value of PC is : 0000001c
The instruction in IR is : 02C68663
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01101', 'rs2': '01100', 'immediate': '0000000101100', 'format': 'SB', 'id': 18}
RA is : 00000003
RB is : 00000008
imm is : 0000002c
Execute stage:
operand1 is 00000003 operand2 is: 00000008
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000000
cycle is : 145
Fetch stage:
The value of PC is : 00000020
The instruction in IR is : 01F69733
Decode stage:
code : {'neumonic': 'sll', 'opcode': '0b0110011', 'funct3': '0b001', 'funct7': '0b0000000', 'rs1': '01101', 'rs2': '11111', 'rd': '01110', 'format': 'R', 'id': 5}
RA is : 00000003
RB is : 00000002
rd is : 14
Execute stage:
operand1 is 00000003 operand2 is: 00000002
RZ is : 0000000c
Memory Access stage:
Register Update Stage:
RD: RY: 14 0000000c
cycle is : 146
Fetch stage:
The value of PC is : 00000024
The instruction in IR is : 00B70733
Decode stage:
code : {'neumonic': 'add', 'opcode': '0b0110011', 'funct3': '0b000', 'funct7': '0b0000000', 'rs1': '01110', 'rs2': '01011', 'rd': '01110', 'format': 'R', 'id': 0}
RA is : 0000000c
RB is : 10000000
rd is : 14
Execute stage:
operand1 is 0000000c operand2 is: 10000000
RZ is : 1000000c
Memory Access stage:
Register Update Stage:
RD: RY: 14 1000000c
cycle is : 147
Fetch stage:
The value of PC is : 00000028
The instruction in IR is : 00072783
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '01111', 'immediate': '000000000000', 'format': 'I', 'id': 14}
RA is : 1000000c
rd is : 15
imm is : 00000000
Execute stage:
operand1 is 1000000c operand2 is: 00000000
RZ is : 1000000c
Memory Access stage:
Register Update Stage:
RD: RY: 15 0000005A
cycle is : 148
Fetch stage:
The value of PC is : 0000002c
The instruction in IR is : 00472803
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '10000', 'immediate': '000000000100', 'format': 'I', 'id': 14}
RA is : 1000000c
rd is : 16
imm is : 00000004
Execute stage:
operand1 is 1000000c operand2 is: 00000004
RZ is : 10000010
Memory Access stage:
Register Update Stage:
RD: RY: 16 00000032
cycle is : 149
Fetch stage:
The value of PC is : 00000030
The instruction in IR is : 00168693
Decode stage:
code : {'neumonic': 'addi', 'opcode': '0b0010011', 'funct3': '0b000', 'rs1': '01101', 'rd': '01101', 'immediate': '000000000001', 'format': 'I', 'id': 9}
RA is : 00000003
rd is : 13
imm is : 00000001
Execute stage:
operand1 is 00000003 operand2 is: 00000001
RZ is : 00000004
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000004
cycle is : 150
Fetch stage:
The value of PC is : 00000034
The instruction in IR is : FF07C4E3
Decode stage:
code : {'neumonic': 'blt', 'opcode': '0b1100011', 'funct3': '0b100', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111101000', 'format': 'SB', 'id': 20}
RA is : 0000005A
RB is : 00000032
imm is : ffffffe8
Execute stage:
operand1 is 0000005A operand2 is: 00000032
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 151
Fetch stage:
The value of PC is : 00000038
The instruction in IR is : FF0782E3
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111100100', 'format': 'SB', 'id': 18}
RA is : 0000005A
RB is : 00000032
imm is : ffffffe4
Execute stage:
operand1 is 0000005A operand2 is: 00000032
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 152
Fetch stage:
The value of PC is : 0000003c
The instruction in IR is : 01072023
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '10000', 'immediate': '000000000000', 'format': 'S', 'id': 17}
RA is : 1000000c
RB is : 00000032
imm is : 00000000
Execute stage:
operand1 is 1000000c operand2 is: 00000000
RZ is : 1000000c
Memory Access stage:
Register Update Stage:
RD: RY: 13 1000000c
cycle is : 153
Fetch stage:
The value of PC is : 00000040
The instruction in IR is : 00F72223
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '01111', 'immediate': '000000000100', 'format': 'S', 'id': 17}
RA is : 1000000c
RB is : 0000005A
imm is : 00000004
Execute stage:
operand1 is 1000000c operand2 is: 00000004
RZ is : 10000010
Memory Access stage:
Register Update Stage:
RD: RY: 13 10000010
cycle is : 154
Fetch stage:
The value of PC is : 00000044
The instruction in IR is : FD9FF06F
Decode stage:
code : {'neumonic': 'jal', 'opcode': '0b1101111', 'immediate': '111111111111111011000', 'rd': '00000', 'format': 'UJ', 'id': 22}
rd is : 0
imm is : ffffffd8
Execute stage:
operand1 is 1000000c operand2 is: 0000005A
RZ is : 10000066
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000048
cycle is : 155
Fetch stage:
The value of PC is : 0000001c
The instruction in IR is : 02C68663
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01101', 'rs2': '01100', 'immediate': '0000000101100', 'format': 'SB', 'id': 18}
RA is : 00000004
RB is : 00000008
imm is : 0000002c
Execute stage:
operand1 is 00000004 operand2 is: 00000008
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000000
cycle is : 156
Fetch stage:
The value of PC is : 00000020
The instruction in IR is : 01F69733
Decode stage:
code : {'neumonic': 'sll', 'opcode': '0b0110011', 'funct3': '0b001', 'funct7': '0b0000000', 'rs1': '01101', 'rs2': '11111', 'rd': '01110', 'format': 'R', 'id': 5}
RA is : 00000004
RB is : 00000002
rd is : 14
Execute stage:
operand1 is 00000004 operand2 is: 00000002
RZ is : 00000010
Memory Access stage:
Register Update Stage:
RD: RY: 14 00000010
cycle is : 157
Fetch stage:
The value of PC is : 00000024
The instruction in IR is : 00B70733
Decode stage:
code : {'neumonic': 'add', 'opcode': '0b0110011', 'funct3': '0b000', 'funct7': '0b0000000', 'rs1': '01110', 'rs2': '01011', 'rd': '01110', 'format': 'R', 'id': 0}
RA is : 00000010
RB is : 10000000
rd is : 14
Execute stage:
operand1 is 00000010 operand2 is: 10000000
RZ is : 10000010
Memory Access stage:
Register Update Stage:
RD: RY: 14 10000010
cycle is : 158
Fetch stage:
The value of PC is : 00000028
The instruction in IR is : 00072783
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '01111', 'immediate': '000000000000', 'format': 'I', 'id': 14}
RA is : 10000010
rd is : 15
imm is : 00000000
Execute stage:
operand1 is 10000010 operand2 is: 00000000
RZ is : 10000010
Memory Access stage:
Register Update Stage:
RD: RY: 15 0000005A
cycle is : 159
Fetch stage:
The value of PC is : 0000002c
The instruction in IR is : 00472803
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '10000', 'immediate': '000000000100', 'format': 'I', 'id': 14}
RA is : 10000010
rd is : 16
imm is : 00000004
Execute stage:
operand1 is 10000010 operand2 is: 00000004
RZ is : 10000014
Memory Access stage:
Register Update Stage:
RD: RY: 16 00000028
cycle is : 160
Fetch stage:
The value of PC is : 00000030
The instruction in IR is : 00168693
Decode stage:
code : {'neumonic': 'addi', 'opcode': '0b0010011', 'funct3': '0b000', 'rs1': '01101', 'rd': '01101', 'immediate': '000000000001', 'format': 'I', 'id': 9}
RA is : 00000004
rd is : 13
imm is : 00000001
Execute stage:
operand1 is 00000004 operand2 is: 00000001
RZ is : 00000005
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000005
cycle is : 161
Fetch stage:
The value of PC is : 00000034
The instruction in IR is : FF07C4E3
Decode stage:
code : {'neumonic': 'blt', 'opcode': '0b1100011', 'funct3': '0b100', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111101000', 'format': 'SB', 'id': 20}
RA is : 0000005A
RB is : 00000028
imm is : ffffffe8
Execute stage:
operand1 is 0000005A operand2 is: 00000028
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 162
Fetch stage:
The value of PC is : 00000038
The instruction in IR is : FF0782E3
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111100100', 'format': 'SB', 'id': 18}
RA is : 0000005A
RB is : 00000028
imm is : ffffffe4
Execute stage:
operand1 is 0000005A operand2 is: 00000028
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 163
Fetch stage:
The value of PC is : 0000003c
The instruction in IR is : 01072023
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '10000', 'immediate': '000000000000', 'format': 'S', 'id': 17}
RA is : 10000010
RB is : 00000028
imm is : 00000000
Execute stage:
operand1 is 10000010 operand2 is: 00000000
RZ is : 10000010
Memory Access stage:
Register Update Stage:
RD: RY: 13 10000010
cycle is : 164
Fetch stage:
The value of PC is : 00000040
The instruction in IR is : 00F72223
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '01111', 'immediate': '000000000100', 'format': 'S', 'id': 17}
RA is : 10000010
RB is : 0000005A
imm is : 00000004
Execute stage:
operand1 is 10000010 operand2 is: 00000004
RZ is : 10000014
Memory Access stage:
Register Update Stage:
RD: RY: 13 10000014
cycle is : 165
Fetch stage:
The value of PC is : 00000044
The instruction in IR is : FD9FF06F
Decode stage:
code : {'neumonic': 'jal', 'opcode': '0b1101111', 'immediate': '111111111111111011000', 'rd': '00000', 'format': 'UJ', 'id': 22}
rd is : 0
imm is : ffffffd8
Execute stage:
operand1 is 10000010 operand2 is: 0000005A
RZ is : 1000006a
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000048
cycle is : 166
Fetch stage:
The value of PC is : 0000001c
The instruction in IR is : 02C68663
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01101', 'rs2': '01100', 'immediate': '0000000101100', 'format': 'SB', 'id': 18}
RA is : 00000005
RB is : 00000008
imm is : 0000002c
Execute stage:
operand1 is 00000005 operand2 is: 00000008
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000000
cycle is : 167
Fetch stage:
The value of PC is : 00000020
The instruction in IR is : 01F69733
Decode stage:
code : {'neumonic': 'sll', 'opcode': '0b0110011', 'funct3': '0b001', 'funct7': '0b0000000', 'rs1': '01101', 'rs2': '11111', 'rd': '01110', 'format': 'R', 'id': 5}
RA is : 00000005
RB is : 00000002
rd is : 14
Execute stage:
operand1 is 00000005 operand2 is: 00000002
RZ is : 00000014
Memory Access stage:
Register Update Stage:
RD: RY: 14 00000014
cycle is : 168
Fetch stage:
The value of PC is : 00000024
The instruction in IR is : 00B70733
Decode stage:
code : {'neumonic': 'add', 'opcode': '0b0110011', 'funct3': '0b000', 'funct7': '0b0000000', 'rs1': '01110', 'rs2': '01011', 'rd': '01110', 'format': 'R', 'id': 0}
RA is : 00000014
RB is : 10000000
rd is : 14
Execute stage:
operand1 is 00000014 operand2 is: 10000000
RZ is : 10000014
Memory Access stage:
Register Update Stage:
RD: RY: 14 10000014
cycle is : 169
Fetch stage:
The value of PC is : 00000028
The instruction in IR is : 00072783
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '01111', 'immediate': '000000000000', 'format': 'I', 'id': 14}
RA is : 10000014
rd is : 15
imm is : 00000000
Execute stage:
operand1 is 10000014 operand2 is: 00000000
RZ is : 10000014
Memory Access stage:
Register Update Stage:
RD: RY: 15 0000005A
cycle is : 170
Fetch stage:
The value of PC is : 0000002c
The instruction in IR is : 00472803
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '10000', 'immediate': '000000000100', 'format': 'I', 'id': 14}
RA is : 10000014
rd is : 16
imm is : 00000004
Execute stage:
operand1 is 10000014 operand2 is: 00000004
RZ is : 10000018
Memory Access stage:
Register Update Stage:
RD: RY: 16 0000001E
cycle is : 171
Fetch stage:
The value of PC is : 00000030
The instruction in IR is : 00168693
Decode stage:
code : {'neumonic': 'addi', 'opcode': '0b0010011', 'funct3': '0b000', 'rs1': '01101', 'rd': '01101', 'immediate': '000000000001', 'format': 'I', 'id': 9}
RA is : 00000005
rd is : 13
imm is : 00000001
Execute stage:
operand1 is 00000005 operand2 is: 00000001
RZ is : 00000006
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000006
cycle is : 172
Fetch stage:
The value of PC is : 00000034
The instruction in IR is : FF07C4E3
Decode stage:
code : {'neumonic': 'blt', 'opcode': '0b1100011', 'funct3': '0b100', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111101000', 'format': 'SB', 'id': 20}
RA is : 0000005A
RB is : 0000001E
imm is : ffffffe8
Execute stage:
operand1 is 0000005A operand2 is: 0000001E
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 173
Fetch stage:
The value of PC is : 00000038
The instruction in IR is : FF0782E3
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111100100', 'format': 'SB', 'id': 18}
RA is : 0000005A
RB is : 0000001E
imm is : ffffffe4
Execute stage:
operand1 is 0000005A operand2 is: 0000001E
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 174
Fetch stage:
The value of PC is : 0000003c
The instruction in IR is : 01072023
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '10000', 'immediate': '000000000000', 'format': 'S', 'id': 17}
RA is : 10000014
RB is : 0000001E
imm is : 00000000
Execute stage:
operand1 is 10000014 operand2 is: 00000000
RZ is : 10000014
Memory Access stage:
Register Update Stage:
RD: RY: 13 10000014
cycle is : 175
Fetch stage:
The value of PC is : 00000040
The instruction in IR is : 00F72223
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '01111', 'immediate': '000000000100', 'format': 'S', 'id': 17}
RA is : 10000014
RB is : 0000005A
imm is : 00000004
Execute stage:
operand1 is 10000014 operand2 is: 00000004
RZ is : 10000018
Memory Access stage:
Register Update Stage:
RD: RY: 13 10000018
cycle is : 176
Fetch stage:
The value of PC is : 00000044
The instruction in IR is : FD9FF06F
Decode stage:
code : {'neumonic': 'jal', 'opcode': '0b1101111', 'immediate': '111111111111111011000', 'rd': '00000', 'format': 'UJ', 'id': 22}
rd is : 0
imm is : ffffffd8
Execute stage:
operand1 is 10000014 operand2 is: 0000005A
RZ is : 1000006e
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000048
cycle is : 177
Fetch stage:
The value of PC is : 0000001c
The instruction in IR is : 02C68663
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01101', 'rs2': '01100', 'immediate': '0000000101100', 'format': 'SB', 'id': 18}
RA is : 00000006
RB is : 00000008
imm is : 0000002c
Execute stage:
operand1 is 00000006 operand2 is: 00000008
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000000
cycle is : 178
Fetch stage:
The value of PC is : 00000020
The instruction in IR is : 01F69733
Decode stage:
code : {'neumonic': 'sll', 'opcode': '0b0110011', 'funct3': '0b001', 'funct7': '0b0000000', 'rs1': '01101', 'rs2': '11111', 'rd': '01110', 'format': 'R', 'id': 5}
RA is : 00000006
RB is : 00000002
rd is : 14
Execute stage:
operand1 is 00000006 operand2 is: 00000002
RZ is : 00000018
Memory Access stage:
Register Update Stage:
RD: RY: 14 00000018
cycle is : 179
Fetch stage:
The value of PC is : 00000024
The instruction in IR is : 00B70733
Decode stage:
code : {'neumonic': 'add', 'opcode': '0b0110011', 'funct3': '0b000', 'funct7': '0b0000000', 'rs1': '01110', 'rs2': '01011', 'rd': '01110', 'format': 'R', 'id': 0}
RA is : 00000018
RB is : 10000000
rd is : 14
Execute stage:
operand1 is 00000018 operand2 is: 10000000
RZ is : 10000018
Memory Access stage:
Register Update Stage:
RD: RY: 14 10000018
cycle is : 180
Fetch stage:
The value of PC is : 00000028
The instruction in IR is : 00072783
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '01111', 'immediate': '000000000000', 'format': 'I', 'id': 14}
RA is : 10000018
rd is : 15
imm is : 00000000
Execute stage:
operand1 is 10000018 operand2 is: 00000000
RZ is : 10000018
Memory Access stage:
Register Update Stage:
RD: RY: 15 0000005A
cycle is : 181
Fetch stage:
The value of PC is : 0000002c
The instruction in IR is : 00472803
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '10000', 'immediate': '000000000100', 'format': 'I', 'id': 14}
RA is : 10000018
rd is : 16
imm is : 00000004
Execute stage:
operand1 is 10000018 operand2 is: 00000004
RZ is : 1000001c
Memory Access stage:
Register Update Stage:
RD: RY: 16 00000014
cycle is : 182
Fetch stage:
The value of PC is : 00000030
The instruction in IR is : 00168693
Decode stage:
code : {'neumonic': 'addi', 'opcode': '0b0010011', 'funct3': '0b000', 'rs1': '01101', 'rd': '01101', 'immediate': '000000000001', 'format': 'I', 'id': 9}
RA is : 00000006
rd is : 13
imm is : 00000001
Execute stage:
operand1 is 00000006 operand2 is: 00000001
RZ is : 00000007
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000007
cycle is : 183
Fetch stage:
The value of PC is : 00000034
The instruction in IR is : FF07C4E3
Decode stage:
code : {'neumonic': 'blt', 'opcode': '0b1100011', 'funct3': '0b100', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111101000', 'format': 'SB', 'id': 20}
RA is : 0000005A
RB is : 00000014
imm is : ffffffe8
Execute stage:
operand1 is 0000005A operand2 is: 00000014
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 184
Fetch stage:
The value of PC is : 00000038
The instruction in IR is : FF0782E3
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111100100', 'format': 'SB', 'id': 18}
RA is : 0000005A
RB is : 00000014
imm is : ffffffe4
Execute stage:
operand1 is 0000005A operand2 is: 00000014
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 185
Fetch stage:
The value of PC is : 0000003c
The instruction in IR is : 01072023
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '10000', 'immediate': '000000000000', 'format': 'S', 'id': 17}
RA is : 10000018
RB is : 00000014
imm is : 00000000
Execute stage:
operand1 is 10000018 operand2 is: 00000000
RZ is : 10000018
Memory Access stage:
Register Update Stage:
RD: RY: 13 10000018
cycle is : 186
Fetch stage:
The value of PC is : 00000040
The instruction in IR is : 00F72223
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '01111', 'immediate': '000000000100', 'format': 'S', 'id': 17}
RA is : 10000018
RB is : 0000005A
imm is : 00000004
Execute stage:
operand1 is 10000018 operand2 is: 00000004
RZ is : 1000001c
Memory Access stage:
Register Update Stage:
RD: RY: 13 1000001c
cycle is : 187
Fetch stage:
The value of PC is : 00000044
The instruction in IR is : FD9FF06F
Decode stage:
code : {'neumonic': 'jal', 'opcode': '0b1101111', 'immediate': '111111111111111011000', 'rd': '00000', 'format': 'UJ', 'id': 22}
rd is : 0
imm is : ffffffd8
Execute stage:
operand1 is 10000018 operand2 is: 0000005A
RZ is : 10000072
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000048
cycle is : 188
Fetch stage:
The value of PC is : 0000001c
The instruction in IR is : 02C68663
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01101', 'rs2': '01100', 'immediate': '0000000101100', 'format': 'SB', 'id': 18}
RA is : 00000007
RB is : 00000008
imm is : 0000002c
Execute stage:
operand1 is 00000007 operand2 is: 00000008
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000000
cycle is : 189
Fetch stage:
The value of PC is : 00000020
The instruction in IR is : 01F69733
Decode stage:
code : {'neumonic': 'sll', 'opcode': '0b0110011', 'funct3': '0b001', 'funct7': '0b0000000', 'rs1': '01101', 'rs2': '11111', 'rd': '01110', 'format': 'R', 'id': 5}
RA is : 00000007
RB is : 00000002
rd is : 14
Execute stage:
operand1 is 00000007 operand2 is: 00000002
RZ is : 0000001c
Memory Access stage:
Register Update Stage:
RD: RY: 14 0000001c
cycle is : 190
Fetch stage:
The value of PC is : 00000024
The instruction in IR is : 00B70733
Decode stage:
code : {'neumonic': 'add', 'opcode': '0b0110011', 'funct3': '0b000', 'funct7': '0b0000000', 'rs1': '01110', 'rs2': '01011', 'rd': '01110', 'format': 'R', 'id': 0}
RA is : 0000001c
RB is : 10000000
rd is : 14
Execute stage:
operand1 is 0000001c operand2 is: 10000000
RZ is : 1000001c
Memory Access stage:
Register Update Stage:
RD: RY: 14 1000001c
cycle is : 191
Fetch stage:
The value of PC is : 00000028
The instruction in IR is : 00072783
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '01111', 'immediate': '000000000000', 'format': 'I', 'id': 14}
RA is : 1000001c
rd is : 15
imm is : 00000000
Execute stage:
operand1 is 1000001c operand2 is: 00000000
RZ is : 1000001c
Memory Access stage:
Register Update Stage:
RD: RY: 15 0000005A
cycle is : 192
Fetch stage:
The value of PC is : 0000002c
The instruction in IR is : 00472803
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '10000', 'immediate': '000000000100', 'format': 'I', 'id': 14}
RA is : 1000001c
rd is : 16
imm is : 00000004
Execute stage:
operand1 is 1000001c operand2 is: 00000004
RZ is : 10000020
Memory Access stage:
Register Update Stage:
RD: RY: 16 0000000a
cycle is : 193
Fetch stage:
The value of PC is : 00000030
The instruction in IR is : 00168693
Decode stage:
code : {'neumonic': 'addi', 'opcode': '0b0010011', 'funct3': '0b000', 'rs1': '01101', 'rd': '01101', 'immediate': '000000000001', 'format': 'I', 'id': 9}
RA is : 00000007
rd is : 13
imm is : 00000001
Execute stage:
operand1 is 00000007 operand2 is: 00000001
RZ is : 00000008
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000008
cycle is : 194
Fetch stage:
The value of PC is : 00000034
The instruction in IR is : FF07C4E3
Decode stage:
code : {'neumonic': 'blt', 'opcode': '0b1100011', 'funct3': '0b100', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111101000', 'format': 'SB', 'id': 20}
RA is : 0000005A
RB is : 0000000a
imm is : ffffffe8
Execute stage:
operand1 is 0000005A operand2 is: 0000000a
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 195
Fetch stage:
The value of PC is : 00000038
The instruction in IR is : FF0782E3
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111100100', 'format': 'SB', 'id': 18}
RA is : 0000005A
RB is : 0000000a
imm is : ffffffe4
Execute stage:
operand1 is 0000005A operand2 is: 0000000a
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 196
Fetch stage:
The value of PC is : 0000003c
The instruction in IR is : 01072023
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '10000', 'immediate': '000000000000', 'format': 'S', 'id': 17}
RA is : 1000001c
RB is : 0000000a
imm is : 00000000
Execute stage:
operand1 is 1000001c operand2 is: 00000000
RZ is : 1000001c
Memory Access stage:
Register Update Stage:
RD: RY: 13 1000001c
cycle is : 197
Fetch stage:
The value of PC is : 00000040
The instruction in IR is : 00F72223
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '01111', 'immediate': '000000000100', 'format': 'S', 'id': 17}
RA is : 1000001c
RB is : 0000005A
imm is : 00000004
Execute stage:
operand1 is 1000001c operand2 is: 00000004
RZ is : 10000020
Memory Access stage:
Register Update Stage:
RD: RY: 13 10000020
cycle is : 198
Fetch stage:
The value of PC is : 00000044
The instruction in IR is : FD9FF06F
Decode stage:
code : {'neumonic': 'jal', 'opcode': '0b1101111', 'immediate': '111111111111111011000', 'rd': '00000', 'format': 'UJ', 'id': 22}
rd is : 0
imm is : ffffffd8
Execute stage:
operand1 is 1000001c operand2 is: 0000005A
RZ is : 10000076
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000048
cycle is : 199
Fetch stage:
The value of PC is : 0000001c
The instruction in IR is : 02C68663
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01101', 'rs2': '01100', 'immediate': '0000000101100', 'format': 'SB', 'id': 18}
RA is : 00000008
RB is : 00000008
imm is : 0000002c
Execute stage:
operand1 is 00000008 operand2 is: 00000008
RZ is : 00000001
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000001
cycle is : 200
Fetch stage:
The value of PC is : 00000048
The instruction in IR is : FC9FF06F
Decode stage:
code : {'neumonic': 'jal', 'opcode': '0b1101111', 'immediate': '111111111111111001000', 'rd': '00000', 'format': 'UJ', 'id': 22}
rd is : 0
imm is : ffffffc8
Execute stage:
operand1 is 00000008 operand2 is: 00000008
RZ is : 00000010
Memory Access stage:
Register Update Stage:
RD: RY: 0 0000004c
cycle is : 201
Fetch stage:
The value of PC is : 00000010
The instruction in IR is : FFF60613
Decode stage:
code : {'neumonic': 'addi', 'opcode': '0b0010011', 'funct3': '0b000', 'rs1': '01100', 'rd': '01100', 'immediate': '111111111111', 'format': 'I', 'id': 9}
RA is : 00000008
rd is : 12
imm is : ffffffff
Execute stage:
operand1 is 00000008 operand2 is: ffffffff
RZ is : 00000007
Memory Access stage:
Register Update Stage:
RD: RY: 12 00000007
cycle is : 202
Fetch stage:
The value of PC is : 00000014
The instruction in IR is : 02060C63
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01100', 'rs2': '00000', 'immediate': '0000000111000', 'format': 'SB', 'id': 18}
RA is : 00000007
RB is : 00000000
imm is : 00000038
Execute stage:
operand1 is 00000007 operand2 is: 00000000
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 12 00000000
cycle is : 203
Fetch stage:
The value of PC is : 00000018
The instruction in IR is : 00000693
Decode stage:
code : {'neumonic': 'addi', 'opcode': '0b0010011', 'funct3': '0b000', 'rs1': '00000', 'rd': '01101', 'immediate': '000000000000', 'format': 'I', 'id': 9}
RA is : 00000000
rd is : 13
imm is : 00000000
Execute stage:
operand1 is 00000000 operand2 is: 00000000
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 204
Fetch stage:
The value of PC is : 0000001c
The instruction in IR is : 02C68663
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01101', 'rs2': '01100', 'immediate': '0000000101100', 'format': 'SB', 'id': 18}
RA is : 00000000
RB is : 00000007
imm is : 0000002c
Execute stage:
operand1 is 00000000 operand2 is: 00000007
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 205
Fetch stage:
The value of PC is : 00000020
The instruction in IR is : 01F69733
Decode stage:
code : {'neumonic': 'sll', 'opcode': '0b0110011', 'funct3': '0b001', 'funct7': '0b0000000', 'rs1': '01101', 'rs2': '11111', 'rd': '01110', 'format': 'R', 'id': 5}
RA is : 00000000
RB is : 00000002
rd is : 14
Execute stage:
operand1 is 00000000 operand2 is: 00000002
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 14 00000000
cycle is : 206
Fetch stage:
The value of PC is : 00000024
The instruction in IR is : 00B70733
Decode stage:
code : {'neumonic': 'add', 'opcode': '0b0110011', 'funct3': '0b000', 'funct7': '0b0000000', 'rs1': '01110', 'rs2': '01011', 'rd': '01110', 'format': 'R', 'id': 0}
RA is : 00000000
RB is : 10000000
rd is : 14
Execute stage:
operand1 is 00000000 operand2 is: 10000000
RZ is : 10000000
Memory Access stage:
Register Update Stage:
RD: RY: 14 10000000
cycle is : 207
Fetch stage:
The value of PC is : 00000028
The instruction in IR is : 00072783
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '01111', 'immediate': '000000000000', 'format': 'I', 'id': 14}
RA is : 10000000
rd is : 15
imm is : 00000000
Execute stage:
operand1 is 10000000 operand2 is: 00000000
RZ is : 10000000
Memory Access stage:
Register Update Stage:
RD: RY: 15 00000050
cycle is : 208
Fetch stage:
The value of PC is : 0000002c
The instruction in IR is : 00472803
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '10000', 'immediate': '000000000100', 'format': 'I', 'id': 14}
RA is : 10000000
rd is : 16
imm is : 00000004
Execute stage:
operand1 is 10000000 operand2 is: 00000004
RZ is : 10000004
Memory Access stage:
Register Update Stage:
RD: RY: 16 00000046
cycle is : 209
Fetch stage:
The value of PC is : 00000030
The instruction in IR is : 00168693
Decode stage:
code : {'neumonic': 'addi', 'opcode': '0b0010011', 'funct3': '0b000', 'rs1': '01101', 'rd': '01101', 'immediate': '000000000001', 'format': 'I', 'id': 9}
RA is : 00000000
rd is : 13
imm is : 00000001
Execute stage:
operand1 is 00000000 operand2 is: 00000001
RZ is : 00000001
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000001
cycle is : 210
Fetch stage:
The value of PC is : 00000034
The instruction in IR is : FF07C4E3
Decode stage:
code : {'neumonic': 'blt', 'opcode': '0b1100011', 'funct3': '0b100', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111101000', 'format': 'SB', 'id': 20}
RA is : 00000050
RB is : 00000046
imm is : ffffffe8
Execute stage:
operand1 is 00000050 operand2 is: 00000046
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 211
Fetch stage:
The value of PC is : 00000038
The instruction in IR is : FF0782E3
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111100100', 'format': 'SB', 'id': 18}
RA is : 00000050
RB is : 00000046
imm is : ffffffe4
Execute stage:
operand1 is 00000050 operand2 is: 00000046
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 212
Fetch stage:
The value of PC is : 0000003c
The instruction in IR is : 01072023
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '10000', 'immediate': '000000000000', 'format': 'S', 'id': 17}
RA is : 10000000
RB is : 00000046
imm is : 00000000
Execute stage:
operand1 is 10000000 operand2 is: 00000000
RZ is : 10000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 10000000
cycle is : 213
Fetch stage:
The value of PC is : 00000040
The instruction in IR is : 00F72223
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '01111', 'immediate': '000000000100', 'format': 'S', 'id': 17}
RA is : 10000000
RB is : 00000050
imm is : 00000004
Execute stage:
operand1 is 10000000 operand2 is: 00000004
RZ is : 10000004
Memory Access stage:
Register Update Stage:
RD: RY: 13 10000004
cycle is : 214
Fetch stage:
The value of PC is : 00000044
The instruction in IR is : FD9FF06F
Decode stage:
code : {'neumonic': 'jal', 'opcode': '0b1101111', 'immediate': '111111111111111011000', 'rd': '00000', 'format': 'UJ', 'id': 22}
rd is : 0
imm is : ffffffd8
Execute stage:
operand1 is 10000000 operand2 is: 00000050
RZ is : 10000050
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000048
cycle is : 215
Fetch stage:
The value of PC is : 0000001c
The instruction in IR is : 02C68663
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01101', 'rs2': '01100', 'immediate': '0000000101100', 'format': 'SB', 'id': 18}
RA is : 00000001
RB is : 00000007
imm is : 0000002c
Execute stage:
operand1 is 00000001 operand2 is: 00000007
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000000
cycle is : 216
Fetch stage:
The value of PC is : 00000020
The instruction in IR is : 01F69733
Decode stage:
code : {'neumonic': 'sll', 'opcode': '0b0110011', 'funct3': '0b001', 'funct7': '0b0000000', 'rs1': '01101', 'rs2': '11111', 'rd': '01110', 'format': 'R', 'id': 5}
RA is : 00000001
RB is : 00000002
rd is : 14
Execute stage:
operand1 is 00000001 operand2 is: 00000002
RZ is : 00000004
Memory Access stage:
Register Update Stage:
RD: RY: 14 00000004
cycle is : 217
Fetch stage:
The value of PC is : 00000024
The instruction in IR is : 00B70733
Decode stage:
code : {'neumonic': 'add', 'opcode': '0b0110011', 'funct3': '0b000', 'funct7': '0b0000000', 'rs1': '01110', 'rs2': '01011', 'rd': '01110', 'format': 'R', 'id': 0}
RA is : 00000004
RB is : 10000000
rd is : 14
Execute stage:
operand1 is 00000004 operand2 is: 10000000
RZ is : 10000004
Memory Access stage:
Register Update Stage:
RD: RY: 14 10000004
cycle is : 218
Fetch stage:
The value of PC is : 00000028
The instruction in IR is : 00072783
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '01111', 'immediate': '000000000000', 'format': 'I', 'id': 14}
RA is : 10000004
rd is : 15
imm is : 00000000
Execute stage:
operand1 is 10000004 operand2 is: 00000000
RZ is : 10000004
Memory Access stage:
Register Update Stage:
RD: RY: 15 00000050
cycle is : 219
Fetch stage:
The value of PC is : 0000002c
The instruction in IR is : 00472803
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '10000', 'immediate': '000000000100', 'format': 'I', 'id': 14}
RA is : 10000004
rd is : 16
imm is : 00000004
Execute stage:
operand1 is 10000004 operand2 is: 00000004
RZ is : 10000008
Memory Access stage:
Register Update Stage:
RD: RY: 16 0000003C
cycle is : 220
Fetch stage:
The value of PC is : 00000030
The instruction in IR is : 00168693
Decode stage:
code : {'neumonic': 'addi', 'opcode': '0b0010011', 'funct3': '0b000', 'rs1': '01101', 'rd': '01101', 'immediate': '000000000001', 'format': 'I', 'id': 9}
RA is : 00000001
rd is : 13
imm is : 00000001
Execute stage:
operand1 is 00000001 operand2 is: 00000001
RZ is : 00000002
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000002
cycle is : 221
Fetch stage:
The value of PC is : 00000034
The instruction in IR is : FF07C4E3
Decode stage:
code : {'neumonic': 'blt', 'opcode': '0b1100011', 'funct3': '0b100', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111101000', 'format': 'SB', 'id': 20}
RA is : 00000050
RB is : 0000003C
imm is : ffffffe8
Execute stage:
operand1 is 00000050 operand2 is: 0000003C
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 222
Fetch stage:
The value of PC is : 00000038
The instruction in IR is : FF0782E3
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111100100', 'format': 'SB', 'id': 18}
RA is : 00000050
RB is : 0000003C
imm is : ffffffe4
Execute stage:
operand1 is 00000050 operand2 is: 0000003C
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 223
Fetch stage:
The value of PC is : 0000003c
The instruction in IR is : 01072023
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '10000', 'immediate': '000000000000', 'format': 'S', 'id': 17}
RA is : 10000004
RB is : 0000003C
imm is : 00000000
Execute stage:
operand1 is 10000004 operand2 is: 00000000
RZ is : 10000004
Memory Access stage:
Register Update Stage:
RD: RY: 13 10000004
cycle is : 224
Fetch stage:
The value of PC is : 00000040
The instruction in IR is : 00F72223
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '01111', 'immediate': '000000000100', 'format': 'S', 'id': 17}
RA is : 10000004
RB is : 00000050
imm is : 00000004
Execute stage:
operand1 is 10000004 operand2 is: 00000004
RZ is : 10000008
Memory Access stage:
Register Update Stage:
RD: RY: 13 10000008
cycle is : 225
Fetch stage:
The value of PC is : 00000044
The instruction in IR is : FD9FF06F
Decode stage:
code : {'neumonic': 'jal', 'opcode': '0b1101111', 'immediate': '111111111111111011000', 'rd': '00000', 'format': 'UJ', 'id': 22}
rd is : 0
imm is : ffffffd8
Execute stage:
operand1 is 10000004 operand2 is: 00000050
RZ is : 10000054
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000048
cycle is : 226
Fetch stage:
The value of PC is : 0000001c
The instruction in IR is : 02C68663
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01101', 'rs2': '01100', 'immediate': '0000000101100', 'format': 'SB', 'id': 18}
RA is : 00000002
RB is : 00000007
imm is : 0000002c
Execute stage:
operand1 is 00000002 operand2 is: 00000007
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000000
cycle is : 227
Fetch stage:
The value of PC is : 00000020
The instruction in IR is : 01F69733
Decode stage:
code : {'neumonic': 'sll', 'opcode': '0b0110011', 'funct3': '0b001', 'funct7': '0b0000000', 'rs1': '01101', 'rs2': '11111', 'rd': '01110', 'format': 'R', 'id': 5}
RA is : 00000002
RB is : 00000002
rd is : 14
Execute stage:
operand1 is 00000002 operand2 is: 00000002
RZ is : 00000008
Memory Access stage:
Register Update Stage:
RD: RY: 14 00000008
cycle is : 228
Fetch stage:
The value of PC is : 00000024
The instruction in IR is : 00B70733
Decode stage:
code : {'neumonic': 'add', 'opcode': '0b0110011', 'funct3': '0b000', 'funct7': '0b0000000', 'rs1': '01110', 'rs2': '01011', 'rd': '01110', 'format': 'R', 'id': 0}
RA is : 00000008
RB is : 10000000
rd is : 14
Execute stage:
operand1 is 00000008 operand2 is: 10000000
RZ is : 10000008
Memory Access stage:
Register Update Stage:
RD: RY: 14 10000008
cycle is : 229
Fetch stage:
The value of PC is : 00000028
The instruction in IR is : 00072783
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '01111', 'immediate': '000000000000', 'format': 'I', 'id': 14}
RA is : 10000008
rd is : 15
imm is : 00000000
Execute stage:
operand1 is 10000008 operand2 is: 00000000
RZ is : 10000008
Memory Access stage:
Register Update Stage:
RD: RY: 15 00000050
cycle is : 230
Fetch stage:
The value of PC is : 0000002c
The instruction in IR is : 00472803
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '10000', 'immediate': '000000000100', 'format': 'I', 'id': 14}
RA is : 10000008
rd is : 16
imm is : 00000004
Execute stage:
operand1 is 10000008 operand2 is: 00000004
RZ is : 1000000c
Memory Access stage:
Register Update Stage:
RD: RY: 16 00000032
cycle is : 231
Fetch stage:
The value of PC is : 00000030
The instruction in IR is : 00168693
Decode stage:
code : {'neumonic': 'addi', 'opcode': '0b0010011', 'funct3': '0b000', 'rs1': '01101', 'rd': '01101', 'immediate': '000000000001', 'format': 'I', 'id': 9}
RA is : 00000002
rd is : 13
imm is : 00000001
Execute stage:
operand1 is 00000002 operand2 is: 00000001
RZ is : 00000003
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000003
cycle is : 232
Fetch stage:
The value of PC is : 00000034
The instruction in IR is : FF07C4E3
Decode stage:
code : {'neumonic': 'blt', 'opcode': '0b1100011', 'funct3': '0b100', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111101000', 'format': 'SB', 'id': 20}
RA is : 00000050
RB is : 00000032
imm is : ffffffe8
Execute stage:
operand1 is 00000050 operand2 is: 00000032
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 233
Fetch stage:
The value of PC is : 00000038
The instruction in IR is : FF0782E3
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111100100', 'format': 'SB', 'id': 18}
RA is : 00000050
RB is : 00000032
imm is : ffffffe4
Execute stage:
operand1 is 00000050 operand2 is: 00000032
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 234
Fetch stage:
The value of PC is : 0000003c
The instruction in IR is : 01072023
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '10000', 'immediate': '000000000000', 'format': 'S', 'id': 17}
RA is : 10000008
RB is : 00000032
imm is : 00000000
Execute stage:
operand1 is 10000008 operand2 is: 00000000
RZ is : 10000008
Memory Access stage:
Register Update Stage:
RD: RY: 13 10000008
cycle is : 235
Fetch stage:
The value of PC is : 00000040
The instruction in IR is : 00F72223
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '01111', 'immediate': '000000000100', 'format': 'S', 'id': 17}
RA is : 10000008
RB is : 00000050
imm is : 00000004
Execute stage:
operand1 is 10000008 operand2 is: 00000004
RZ is : 1000000c
Memory Access stage:
Register Update Stage:
RD: RY: 13 1000000c
cycle is : 236
Fetch stage:
The value of PC is : 00000044
The instruction in IR is : FD9FF06F
Decode stage:
code : {'neumonic': 'jal', 'opcode': '0b1101111', 'immediate': '111111111111111011000', 'rd': '00000', 'format': 'UJ', 'id': 22}
rd is : 0
imm is : ffffffd8
Execute stage:
operand1 is 10000008 operand2 is: 00000050
RZ is : 10000058
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000048
cycle is : 237
Fetch stage:
The value of PC is : 0000001c
The instruction in IR is : 02C68663
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01101', 'rs2': '01100', 'immediate': '0000000101100', 'format': 'SB', 'id': 18}
RA is : 00000003
RB is : 00000007
imm is : 0000002c
Execute stage:
operand1 is 00000003 operand2 is: 00000007
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000000
cycle is : 238
Fetch stage:
The value of PC is : 00000020
The instruction in IR is : 01F69733
Decode stage:
code : {'neumonic': 'sll', 'opcode': '0b0110011', 'funct3': '0b001', 'funct7': '0b0000000', 'rs1': '01101', 'rs2': '11111', 'rd': '01110', 'format': 'R', 'id': 5}
RA is : 00000003
RB is : 00000002
rd is : 14
Execute stage:
operand1 is 00000003 operand2 is: 00000002
RZ is : 0000000c
Memory Access stage:
Register Update Stage:
RD: RY: 14 0000000c
cycle is : 239
Fetch stage:
The value of PC is : 00000024
The instruction in IR is : 00B70733
Decode stage:
code : {'neumonic': 'add', 'opcode': '0b0110011', 'funct3': '0b000', 'funct7': '0b0000000', 'rs1': '01110', 'rs2': '01011', 'rd': '01110', 'format': 'R', 'id': 0}
RA is : 0000000c
RB is : 10000000
rd is : 14
Execute stage:
operand1 is 0000000c operand2 is: 10000000
RZ is : 1000000c
Memory Access stage:
Register Update Stage:
RD: RY: 14 1000000c
cycle is : 240
Fetch stage:
The value of PC is : 00000028
The instruction in IR is : 00072783
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '01111', 'immediate': '000000000000', 'format': 'I', 'id': 14}
RA is : 1000000c
rd is : 15
imm is : 00000000
Execute stage:
operand1 is 1000000c operand2 is: 00000000
RZ is : 1000000c
Memory Access stage:
Register Update Stage:
RD: RY: 15 00000050
cycle is : 241
Fetch stage:
The value of PC is : 0000002c
The instruction in IR is : 00472803
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '10000', 'immediate': '000000000100', 'format': 'I', 'id': 14}
RA is : 1000000c
rd is : 16
imm is : 00000004
Execute stage:
operand1 is 1000000c operand2 is: 00000004
RZ is : 10000010
Memory Access stage:
Register Update Stage:
RD: RY: 16 00000028
cycle is : 242
Fetch stage:
The value of PC is : 00000030
The instruction in IR is : 00168693
Decode stage:
code : {'neumonic': 'addi', 'opcode': '0b0010011', 'funct3': '0b000', 'rs1': '01101', 'rd': '01101', 'immediate': '000000000001', 'format': 'I', 'id': 9}
RA is : 00000003
rd is : 13
imm is : 00000001
Execute stage:
operand1 is 00000003 operand2 is: 00000001
RZ is : 00000004
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000004
cycle is : 243
Fetch stage:
The value of PC is : 00000034
The instruction in IR is : FF07C4E3
Decode stage:
code : {'neumonic': 'blt', 'opcode': '0b1100011', 'funct3': '0b100', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111101000', 'format': 'SB', 'id': 20}
RA is : 00000050
RB is : 00000028
imm is : ffffffe8
Execute stage:
operand1 is 00000050 operand2 is: 00000028
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 244
Fetch stage:
The value of PC is : 00000038
The instruction in IR is : FF0782E3
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111100100', 'format': 'SB', 'id': 18}
RA is : 00000050
RB is : 00000028
imm is : ffffffe4
Execute stage:
operand1 is 00000050 operand2 is: 00000028
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 245
Fetch stage:
The value of PC is : 0000003c
The instruction in IR is : 01072023
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '10000', 'immediate': '000000000000', 'format': 'S', 'id': 17}
RA is : 1000000c
RB is : 00000028
imm is : 00000000
Execute stage:
operand1 is 1000000c operand2 is: 00000000
RZ is : 1000000c
Memory Access stage:
Register Update Stage:
RD: RY: 13 1000000c
cycle is : 246
Fetch stage:
The value of PC is : 00000040
The instruction in IR is : 00F72223
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '01111', 'immediate': '000000000100', 'format': 'S', 'id': 17}
RA is : 1000000c
RB is : 00000050
imm is : 00000004
Execute stage:
operand1 is 1000000c operand2 is: 00000004
RZ is : 10000010
Memory Access stage:
Register Update Stage:
RD: RY: 13 10000010
cycle is : 247
Fetch stage:
The value of PC is : 00000044
The instruction in IR is : FD9FF06F
Decode stage:
code : {'neumonic': 'jal', 'opcode': '0b1101111', 'immediate': '111111111111111011000', 'rd': '00000', 'format': 'UJ', 'id': 22}
rd is : 0
imm is : ffffffd8
Execute stage:
operand1 is 1000000c operand2 is: 00000050
RZ is : 1000005c
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000048
cycle is : 248
Fetch stage:
The value of PC is : 0000001c
The instruction in IR is : 02C68663
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01101', 'rs2': '01100', 'immediate': '0000000101100', 'format': 'SB', 'id': 18}
RA is : 00000004
RB is : 00000007
imm is : 0000002c
Execute stage:
operand1 is 00000004 operand2 is: 00000007
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000000
cycle is : 249
Fetch stage:
The value of PC is : 00000020
The instruction in IR is : 01F69733
Decode stage:
code : {'neumonic': 'sll', 'opcode': '0b0110011', 'funct3': '0b001', 'funct7': '0b0000000', 'rs1': '01101', 'rs2': '11111', 'rd': '01110', 'format': 'R', 'id': 5}
RA is : 00000004
RB is : 00000002
rd is : 14
Execute stage:
operand1 is 00000004 operand2 is: 00000002
RZ is : 00000010
Memory Access stage:
Register Update Stage:
RD: RY: 14 00000010
cycle is : 250
Fetch stage:
The value of PC is : 00000024
The instruction in IR is : 00B70733
Decode stage:
code : {'neumonic': 'add', 'opcode': '0b0110011', 'funct3': '0b000', 'funct7': '0b0000000', 'rs1': '01110', 'rs2': '01011', 'rd': '01110', 'format': 'R', 'id': 0}
RA is : 00000010
RB is : 10000000
rd is : 14
Execute stage:
operand1 is 00000010 operand2 is: 10000000
RZ is : 10000010
Memory Access stage:
Register Update Stage:
RD: RY: 14 10000010
cycle is : 251
Fetch stage:
The value of PC is : 00000028
The instruction in IR is : 00072783
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '01111', 'immediate': '000000000000', 'format': 'I', 'id': 14}
RA is : 10000010
rd is : 15
imm is : 00000000
Execute stage:
operand1 is 10000010 operand2 is: 00000000
RZ is : 10000010
Memory Access stage:
Register Update Stage:
RD: RY: 15 00000050
cycle is : 252
Fetch stage:
The value of PC is : 0000002c
The instruction in IR is : 00472803
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '10000', 'immediate': '000000000100', 'format': 'I', 'id': 14}
RA is : 10000010
rd is : 16
imm is : 00000004
Execute stage:
operand1 is 10000010 operand2 is: 00000004
RZ is : 10000014
Memory Access stage:
Register Update Stage:
RD: RY: 16 0000001E
cycle is : 253
Fetch stage:
The value of PC is : 00000030
The instruction in IR is : 00168693
Decode stage:
code : {'neumonic': 'addi', 'opcode': '0b0010011', 'funct3': '0b000', 'rs1': '01101', 'rd': '01101', 'immediate': '000000000001', 'format': 'I', 'id': 9}
RA is : 00000004
rd is : 13
imm is : 00000001
Execute stage:
operand1 is 00000004 operand2 is: 00000001
RZ is : 00000005
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000005
cycle is : 254
Fetch stage:
The value of PC is : 00000034
The instruction in IR is : FF07C4E3
Decode stage:
code : {'neumonic': 'blt', 'opcode': '0b1100011', 'funct3': '0b100', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111101000', 'format': 'SB', 'id': 20}
RA is : 00000050
RB is : 0000001E
imm is : ffffffe8
Execute stage:
operand1 is 00000050 operand2 is: 0000001E
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 255
Fetch stage:
The value of PC is : 00000038
The instruction in IR is : FF0782E3
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111100100', 'format': 'SB', 'id': 18}
RA is : 00000050
RB is : 0000001E
imm is : ffffffe4
Execute stage:
operand1 is 00000050 operand2 is: 0000001E
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 256
Fetch stage:
The value of PC is : 0000003c
The instruction in IR is : 01072023
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '10000', 'immediate': '000000000000', 'format': 'S', 'id': 17}
RA is : 10000010
RB is : 0000001E
imm is : 00000000
Execute stage:
operand1 is 10000010 operand2 is: 00000000
RZ is : 10000010
Memory Access stage:
Register Update Stage:
RD: RY: 13 10000010
cycle is : 257
Fetch stage:
The value of PC is : 00000040
The instruction in IR is : 00F72223
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '01111', 'immediate': '000000000100', 'format': 'S', 'id': 17}
RA is : 10000010
RB is : 00000050
imm is : 00000004
Execute stage:
operand1 is 10000010 operand2 is: 00000004
RZ is : 10000014
Memory Access stage:
Register Update Stage:
RD: RY: 13 10000014
cycle is : 258
Fetch stage:
The value of PC is : 00000044
The instruction in IR is : FD9FF06F
Decode stage:
code : {'neumonic': 'jal', 'opcode': '0b1101111', 'immediate': '111111111111111011000', 'rd': '00000', 'format': 'UJ', 'id': 22}
rd is : 0
imm is : ffffffd8
Execute stage:
operand1 is 10000010 operand2 is: 00000050
RZ is : 10000060
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000048
cycle is : 259
Fetch stage:
The value of PC is : 0000001c
The instruction in IR is : 02C68663
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01101', 'rs2': '01100', 'immediate': '0000000101100', 'format': 'SB', 'id': 18}
RA is : 00000005
RB is : 00000007
imm is : 0000002c
Execute stage:
operand1 is 00000005 operand2 is: 00000007
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000000
cycle is : 260
Fetch stage:
The value of PC is : 00000020
The instruction in IR is : 01F69733
Decode stage:
code : {'neumonic': 'sll', 'opcode': '0b0110011', 'funct3': '0b001', 'funct7': '0b0000000', 'rs1': '01101', 'rs2': '11111', 'rd': '01110', 'format': 'R', 'id': 5}
RA is : 00000005
RB is : 00000002
rd is : 14
Execute stage:
operand1 is 00000005 operand2 is: 00000002
RZ is : 00000014
Memory Access stage:
Register Update Stage:
RD: RY: 14 00000014
cycle is : 261
Fetch stage:
The value of PC is : 00000024
The instruction in IR is : 00B70733
Decode stage:
code : {'neumonic': 'add', 'opcode': '0b0110011', 'funct3': '0b000', 'funct7': '0b0000000', 'rs1': '01110', 'rs2': '01011', 'rd': '01110', 'format': 'R', 'id': 0}
RA is : 00000014
RB is : 10000000
rd is : 14
Execute stage:
operand1 is 00000014 operand2 is: 10000000
RZ is : 10000014
Memory Access stage:
Register Update Stage:
RD: RY: 14 10000014
cycle is : 262
Fetch stage:
The value of PC is : 00000028
The instruction in IR is : 00072783
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '01111', 'immediate': '000000000000', 'format': 'I', 'id': 14}
RA is : 10000014
rd is : 15
imm is : 00000000
Execute stage:
operand1 is 10000014 operand2 is: 00000000
RZ is : 10000014
Memory Access stage:
Register Update Stage:
RD: RY: 15 00000050
cycle is : 263
Fetch stage:
The value of PC is : 0000002c
The instruction in IR is : 00472803
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '10000', 'immediate': '000000000100', 'format': 'I', 'id': 14}
RA is : 10000014
rd is : 16
imm is : 00000004
Execute stage:
operand1 is 10000014 operand2 is: 00000004
RZ is : 10000018
Memory Access stage:
Register Update Stage:
RD: RY: 16 00000014
cycle is : 264
Fetch stage:
The value of PC is : 00000030
The instruction in IR is : 00168693
Decode stage:
code : {'neumonic': 'addi', 'opcode': '0b0010011', 'funct3': '0b000', 'rs1': '01101', 'rd': '01101', 'immediate': '000000000001', 'format': 'I', 'id': 9}
RA is : 00000005
rd is : 13
imm is : 00000001
Execute stage:
operand1 is 00000005 operand2 is: 00000001
RZ is : 00000006
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000006
cycle is : 265
Fetch stage:
The value of PC is : 00000034
The instruction in IR is : FF07C4E3
Decode stage:
code : {'neumonic': 'blt', 'opcode': '0b1100011', 'funct3': '0b100', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111101000', 'format': 'SB', 'id': 20}
RA is : 00000050
RB is : 00000014
imm is : ffffffe8
Execute stage:
operand1 is 00000050 operand2 is: 00000014
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 266
Fetch stage:
The value of PC is : 00000038
The instruction in IR is : FF0782E3
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111100100', 'format': 'SB', 'id': 18}
RA is : 00000050
RB is : 00000014
imm is : ffffffe4
Execute stage:
operand1 is 00000050 operand2 is: 00000014
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 267
Fetch stage:
The value of PC is : 0000003c
The instruction in IR is : 01072023
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '10000', 'immediate': '000000000000', 'format': 'S', 'id': 17}
RA is : 10000014
RB is : 00000014
imm is : 00000000
Execute stage:
operand1 is 10000014 operand2 is: 00000000
RZ is : 10000014
Memory Access stage:
Register Update Stage:
RD: RY: 13 10000014
cycle is : 268
Fetch stage:
The value of PC is : 00000040
The instruction in IR is : 00F72223
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '01111', 'immediate': '000000000100', 'format': 'S', 'id': 17}
RA is : 10000014
RB is : 00000050
imm is : 00000004
Execute stage:
operand1 is 10000014 operand2 is: 00000004
RZ is : 10000018
Memory Access stage:
Register Update Stage:
RD: RY: 13 10000018
cycle is : 269
Fetch stage:
The value of PC is : 00000044
The instruction in IR is : FD9FF06F
Decode stage:
code : {'neumonic': 'jal', 'opcode': '0b1101111', 'immediate': '111111111111111011000', 'rd': '00000', 'format': 'UJ', 'id': 22}
rd is : 0
imm is : ffffffd8
Execute stage:
operand1 is 10000014 operand2 is: 00000050
RZ is : 10000064
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000048
cycle is : 270
Fetch stage:
The value of PC is : 0000001c
The instruction in IR is : 02C68663
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01101', 'rs2': '01100', 'immediate': '0000000101100', 'format': 'SB', 'id': 18}
RA is : 00000006
RB is : 00000007
imm is : 0000002c
Execute stage:
operand1 is 00000006 operand2 is: 00000007
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000000
cycle is : 271
Fetch stage:
The value of PC is : 00000020
The instruction in IR is : 01F69733
Decode stage:
code : {'neumonic': 'sll', 'opcode': '0b0110011', 'funct3': '0b001', 'funct7': '0b0000000', 'rs1': '01101', 'rs2': '11111', 'rd': '01110', 'format': 'R', 'id': 5}
RA is : 00000006
RB is : 00000002
rd is : 14
Execute stage:
operand1 is 00000006 operand2 is: 00000002
RZ is : 00000018
Memory Access stage:
Register Update Stage:
RD: RY: 14 00000018
cycle is : 272
Fetch stage:
The value of PC is : 00000024
The instruction in IR is : 00B70733
Decode stage:
code : {'neumonic': 'add', 'opcode': '0b0110011', 'funct3': '0b000', 'funct7': '0b0000000', 'rs1': '01110', 'rs2': '01011', 'rd': '01110', 'format': 'R', 'id': 0}
RA is : 00000018
RB is : 10000000
rd is : 14
Execute stage:
operand1 is 00000018 operand2 is: 10000000
RZ is : 10000018
Memory Access stage:
Register Update Stage:
RD: RY: 14 10000018
cycle is : 273
Fetch stage:
The value of PC is : 00000028
The instruction in IR is : 00072783
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '01111', 'immediate': '000000000000', 'format': 'I', 'id': 14}
RA is : 10000018
rd is : 15
imm is : 00000000
Execute stage:
operand1 is 10000018 operand2 is: 00000000
RZ is : 10000018
Memory Access stage:
Register Update Stage:
RD: RY: 15 00000050
cycle is : 274
Fetch stage:
The value of PC is : 0000002c
The instruction in IR is : 00472803
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '10000', 'immediate': '000000000100', 'format': 'I', 'id': 14}
RA is : 10000018
rd is : 16
imm is : 00000004
Execute stage:
operand1 is 10000018 operand2 is: 00000004
RZ is : 1000001c
Memory Access stage:
Register Update Stage:
RD: RY: 16 0000000a
cycle is : 275
Fetch stage:
The value of PC is : 00000030
The instruction in IR is : 00168693
Decode stage:
code : {'neumonic': 'addi', 'opcode': '0b0010011', 'funct3': '0b000', 'rs1': '01101', 'rd': '01101', 'immediate': '000000000001', 'format': 'I', 'id': 9}
RA is : 00000006
rd is : 13
imm is : 00000001
Execute stage:
operand1 is 00000006 operand2 is: 00000001
RZ is : 00000007
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000007
cycle is : 276
Fetch stage:
The value of PC is : 00000034
The instruction in IR is : FF07C4E3
Decode stage:
code : {'neumonic': 'blt', 'opcode': '0b1100011', 'funct3': '0b100', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111101000', 'format': 'SB', 'id': 20}
RA is : 00000050
RB is : 0000000a
imm is : ffffffe8
Execute stage:
operand1 is 00000050 operand2 is: 0000000a
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 277
Fetch stage:
The value of PC is : 00000038
The instruction in IR is : FF0782E3
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111100100', 'format': 'SB', 'id': 18}
RA is : 00000050
RB is : 0000000a
imm is : ffffffe4
Execute stage:
operand1 is 00000050 operand2 is: 0000000a
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 278
Fetch stage:
The value of PC is : 0000003c
The instruction in IR is : 01072023
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '10000', 'immediate': '000000000000', 'format': 'S', 'id': 17}
RA is : 10000018
RB is : 0000000a
imm is : 00000000
Execute stage:
operand1 is 10000018 operand2 is: 00000000
RZ is : 10000018
Memory Access stage:
Register Update Stage:
RD: RY: 13 10000018
cycle is : 279
Fetch stage:
The value of PC is : 00000040
The instruction in IR is : 00F72223
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '01111', 'immediate': '000000000100', 'format': 'S', 'id': 17}
RA is : 10000018
RB is : 00000050
imm is : 00000004
Execute stage:
operand1 is 10000018 operand2 is: 00000004
RZ is : 1000001c
Memory Access stage:
Register Update Stage:
RD: RY: 13 1000001c
cycle is : 280
Fetch stage:
The value of PC is : 00000044
The instruction in IR is : FD9FF06F
Decode stage:
code : {'neumonic': 'jal', 'opcode': '0b1101111', 'immediate': '111111111111111011000', 'rd': '00000', 'format': 'UJ', 'id': 22}
rd is : 0
imm is : ffffffd8
Execute stage:
operand1 is 10000018 operand2 is: 00000050
RZ is : 10000068
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000048
cycle is : 281
Fetch stage:
The value of PC is : 0000001c
The instruction in IR is : 02C68663
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01101', 'rs2': '01100', 'immediate': '0000000101100', 'format': 'SB', 'id': 18}
RA is : 00000007
RB is : 00000007
imm is : 0000002c
Execute stage:
operand1 is 00000007 operand2 is: 00000007
RZ is : 00000001
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000001
cycle is : 282
Fetch stage:
The value of PC is : 00000048
The instruction in IR is : FC9FF06F
Decode stage:
code : {'neumonic': 'jal', 'opcode': '0b1101111', 'immediate': '111111111111111001000', 'rd': '00000', 'format': 'UJ', 'id': 22}
rd is : 0
imm is : ffffffc8
Execute stage:
operand1 is 00000007 operand2 is: 00000007
RZ is : 0000000e
Memory Access stage:
Register Update Stage:
RD: RY: 0 0000004c
cycle is : 283
Fetch stage:
The value of PC is : 00000010
The instruction in IR is : FFF60613
Decode stage:
code : {'neumonic': 'addi', 'opcode': '0b0010011', 'funct3': '0b000', 'rs1': '01100', 'rd': '01100', 'immediate': '111111111111', 'format': 'I', 'id': 9}
RA is : 00000007
rd is : 12
imm is : ffffffff
Execute stage:
operand1 is 00000007 operand2 is: ffffffff
RZ is : 00000006
Memory Access stage:
Register Update Stage:
RD: RY: 12 00000006
cycle is : 284
Fetch stage:
The value of PC is : 00000014
The instruction in IR is : 02060C63
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01100', 'rs2': '00000', 'immediate': '0000000111000', 'format': 'SB', 'id': 18}
RA is : 00000006
RB is : 00000000
imm is : 00000038
Execute stage:
operand1 is 00000006 operand2 is: 00000000
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 12 00000000
cycle is : 285
Fetch stage:
The value of PC is : 00000018
The instruction in IR is : 00000693
Decode stage:
code : {'neumonic': 'addi', 'opcode': '0b0010011', 'funct3': '0b000', 'rs1': '00000', 'rd': '01101', 'immediate': '000000000000', 'format': 'I', 'id': 9}
RA is : 00000000
rd is : 13
imm is : 00000000
Execute stage:
operand1 is 00000000 operand2 is: 00000000
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 286
Fetch stage:
The value of PC is : 0000001c
The instruction in IR is : 02C68663
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01101', 'rs2': '01100', 'immediate': '0000000101100', 'format': 'SB', 'id': 18}
RA is : 00000000
RB is : 00000006
imm is : 0000002c
Execute stage:
operand1 is 00000000 operand2 is: 00000006
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 287
Fetch stage:
The value of PC is : 00000020
The instruction in IR is : 01F69733
Decode stage:
code : {'neumonic': 'sll', 'opcode': '0b0110011', 'funct3': '0b001', 'funct7': '0b0000000', 'rs1': '01101', 'rs2': '11111', 'rd': '01110', 'format': 'R', 'id': 5}
RA is : 00000000
RB is : 00000002
rd is : 14
Execute stage:
operand1 is 00000000 operand2 is: 00000002
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 14 00000000
cycle is : 288
Fetch stage:
The value of PC is : 00000024
The instruction in IR is : 00B70733
Decode stage:
code : {'neumonic': 'add', 'opcode': '0b0110011', 'funct3': '0b000', 'funct7': '0b0000000', 'rs1': '01110', 'rs2': '01011', 'rd': '01110', 'format': 'R', 'id': 0}
RA is : 00000000
RB is : 10000000
rd is : 14
Execute stage:
operand1 is 00000000 operand2 is: 10000000
RZ is : 10000000
Memory Access stage:
Register Update Stage:
RD: RY: 14 10000000
cycle is : 289
Fetch stage:
The value of PC is : 00000028
The instruction in IR is : 00072783
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '01111', 'immediate': '000000000000', 'format': 'I', 'id': 14}
RA is : 10000000
rd is : 15
imm is : 00000000
Execute stage:
operand1 is 10000000 operand2 is: 00000000
RZ is : 10000000
Memory Access stage:
Register Update Stage:
RD: RY: 15 00000046
cycle is : 290
Fetch stage:
The value of PC is : 0000002c
The instruction in IR is : 00472803
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '10000', 'immediate': '000000000100', 'format': 'I', 'id': 14}
RA is : 10000000
rd is : 16
imm is : 00000004
Execute stage:
operand1 is 10000000 operand2 is: 00000004
RZ is : 10000004
Memory Access stage:
Register Update Stage:
RD: RY: 16 0000003C
cycle is : 291
Fetch stage:
The value of PC is : 00000030
The instruction in IR is : 00168693
Decode stage:
code : {'neumonic': 'addi', 'opcode': '0b0010011', 'funct3': '0b000', 'rs1': '01101', 'rd': '01101', 'immediate': '000000000001', 'format': 'I', 'id': 9}
RA is : 00000000
rd is : 13
imm is : 00000001
Execute stage:
operand1 is 00000000 operand2 is: 00000001
RZ is : 00000001
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000001
cycle is : 292
Fetch stage:
The value of PC is : 00000034
The instruction in IR is : FF07C4E3
Decode stage:
code : {'neumonic': 'blt', 'opcode': '0b1100011', 'funct3': '0b100', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111101000', 'format': 'SB', 'id': 20}
RA is : 00000046
RB is : 0000003C
imm is : ffffffe8
Execute stage:
operand1 is 00000046 operand2 is: 0000003C
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 293
Fetch stage:
The value of PC is : 00000038
The instruction in IR is : FF0782E3
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111100100', 'format': 'SB', 'id': 18}
RA is : 00000046
RB is : 0000003C
imm is : ffffffe4
Execute stage:
operand1 is 00000046 operand2 is: 0000003C
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 294
Fetch stage:
The value of PC is : 0000003c
The instruction in IR is : 01072023
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '10000', 'immediate': '000000000000', 'format': 'S', 'id': 17}
RA is : 10000000
RB is : 0000003C
imm is : 00000000
Execute stage:
operand1 is 10000000 operand2 is: 00000000
RZ is : 10000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 10000000
cycle is : 295
Fetch stage:
The value of PC is : 00000040
The instruction in IR is : 00F72223
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '01111', 'immediate': '000000000100', 'format': 'S', 'id': 17}
RA is : 10000000
RB is : 00000046
imm is : 00000004
Execute stage:
operand1 is 10000000 operand2 is: 00000004
RZ is : 10000004
Memory Access stage:
Register Update Stage:
RD: RY: 13 10000004
cycle is : 296
Fetch stage:
The value of PC is : 00000044
The instruction in IR is : FD9FF06F
Decode stage:
code : {'neumonic': 'jal', 'opcode': '0b1101111', 'immediate': '111111111111111011000', 'rd': '00000', 'format': 'UJ', 'id': 22}
rd is : 0
imm is : ffffffd8
Execute stage:
operand1 is 10000000 operand2 is: 00000046
RZ is : 10000046
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000048
cycle is : 297
Fetch stage:
The value of PC is : 0000001c
The instruction in IR is : 02C68663
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01101', 'rs2': '01100', 'immediate': '0000000101100', 'format': 'SB', 'id': 18}
RA is : 00000001
RB is : 00000006
imm is : 0000002c
Execute stage:
operand1 is 00000001 operand2 is: 00000006
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000000
cycle is : 298
Fetch stage:
The value of PC is : 00000020
The instruction in IR is : 01F69733
Decode stage:
code : {'neumonic': 'sll', 'opcode': '0b0110011', 'funct3': '0b001', 'funct7': '0b0000000', 'rs1': '01101', 'rs2': '11111', 'rd': '01110', 'format': 'R', 'id': 5}
RA is : 00000001
RB is : 00000002
rd is : 14
Execute stage:
operand1 is 00000001 operand2 is: 00000002
RZ is : 00000004
Memory Access stage:
Register Update Stage:
RD: RY: 14 00000004
cycle is : 299
Fetch stage:
The value of PC is : 00000024
The instruction in IR is : 00B70733
Decode stage:
code : {'neumonic': 'add', 'opcode': '0b0110011', 'funct3': '0b000', 'funct7': '0b0000000', 'rs1': '01110', 'rs2': '01011', 'rd': '01110', 'format': 'R', 'id': 0}
RA is : 00000004
RB is : 10000000
rd is : 14
Execute stage:
operand1 is 00000004 operand2 is: 10000000
RZ is : 10000004
Memory Access stage:
Register Update Stage:
RD: RY: 14 10000004
cycle is : 300
Fetch stage:
The value of PC is : 00000028
The instruction in IR is : 00072783
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '01111', 'immediate': '000000000000', 'format': 'I', 'id': 14}
RA is : 10000004
rd is : 15
imm is : 00000000
Execute stage:
operand1 is 10000004 operand2 is: 00000000
RZ is : 10000004
Memory Access stage:
Register Update Stage:
RD: RY: 15 00000046
cycle is : 301
Fetch stage:
The value of PC is : 0000002c
The instruction in IR is : 00472803
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '10000', 'immediate': '000000000100', 'format': 'I', 'id': 14}
RA is : 10000004
rd is : 16
imm is : 00000004
Execute stage:
operand1 is 10000004 operand2 is: 00000004
RZ is : 10000008
Memory Access stage:
Register Update Stage:
RD: RY: 16 00000032
cycle is : 302
Fetch stage:
The value of PC is : 00000030
The instruction in IR is : 00168693
Decode stage:
code : {'neumonic': 'addi', 'opcode': '0b0010011', 'funct3': '0b000', 'rs1': '01101', 'rd': '01101', 'immediate': '000000000001', 'format': 'I', 'id': 9}
RA is : 00000001
rd is : 13
imm is : 00000001
Execute stage:
operand1 is 00000001 operand2 is: 00000001
RZ is : 00000002
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000002
cycle is : 303
Fetch stage:
The value of PC is : 00000034
The instruction in IR is : FF07C4E3
Decode stage:
code : {'neumonic': 'blt', 'opcode': '0b1100011', 'funct3': '0b100', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111101000', 'format': 'SB', 'id': 20}
RA is : 00000046
RB is : 00000032
imm is : ffffffe8
Execute stage:
operand1 is 00000046 operand2 is: 00000032
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 304
Fetch stage:
The value of PC is : 00000038
The instruction in IR is : FF0782E3
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111100100', 'format': 'SB', 'id': 18}
RA is : 00000046
RB is : 00000032
imm is : ffffffe4
Execute stage:
operand1 is 00000046 operand2 is: 00000032
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 305
Fetch stage:
The value of PC is : 0000003c
The instruction in IR is : 01072023
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '10000', 'immediate': '000000000000', 'format': 'S', 'id': 17}
RA is : 10000004
RB is : 00000032
imm is : 00000000
Execute stage:
operand1 is 10000004 operand2 is: 00000000
RZ is : 10000004
Memory Access stage:
Register Update Stage:
RD: RY: 13 10000004
cycle is : 306
Fetch stage:
The value of PC is : 00000040
The instruction in IR is : 00F72223
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '01111', 'immediate': '000000000100', 'format': 'S', 'id': 17}
RA is : 10000004
RB is : 00000046
imm is : 00000004
Execute stage:
operand1 is 10000004 operand2 is: 00000004
RZ is : 10000008
Memory Access stage:
Register Update Stage:
RD: RY: 13 10000008
cycle is : 307
Fetch stage:
The value of PC is : 00000044
The instruction in IR is : FD9FF06F
Decode stage:
code : {'neumonic': 'jal', 'opcode': '0b1101111', 'immediate': '111111111111111011000', 'rd': '00000', 'format': 'UJ', 'id': 22}
rd is : 0
imm is : ffffffd8
Execute stage:
operand1 is 10000004 operand2 is: 00000046
RZ is : 1000004a
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000048
cycle is : 308
Fetch stage:
The value of PC is : 0000001c
The instruction in IR is : 02C68663
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01101', 'rs2': '01100', 'immediate': '0000000101100', 'format': 'SB', 'id': 18}
RA is : 00000002
RB is : 00000006
imm is : 0000002c
Execute stage:
operand1 is 00000002 operand2 is: 00000006
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000000
cycle is : 309
Fetch stage:
The value of PC is : 00000020
The instruction in IR is : 01F69733
Decode stage:
code : {'neumonic': 'sll', 'opcode': '0b0110011', 'funct3': '0b001', 'funct7': '0b0000000', 'rs1': '01101', 'rs2': '11111', 'rd': '01110', 'format': 'R', 'id': 5}
RA is : 00000002
RB is : 00000002
rd is : 14
Execute stage:
operand1 is 00000002 operand2 is: 00000002
RZ is : 00000008
Memory Access stage:
Register Update Stage:
RD: RY: 14 00000008
cycle is : 310
Fetch stage:
The value of PC is : 00000024
The instruction in IR is : 00B70733
Decode stage:
code : {'neumonic': 'add', 'opcode': '0b0110011', 'funct3': '0b000', 'funct7': '0b0000000', 'rs1': '01110', 'rs2': '01011', 'rd': '01110', 'format': 'R', 'id': 0}
RA is : 00000008
RB is : 10000000
rd is : 14
Execute stage:
operand1 is 00000008 operand2 is: 10000000
RZ is : 10000008
Memory Access stage:
Register Update Stage:
RD: RY: 14 10000008
cycle is : 311
Fetch stage:
The value of PC is : 00000028
The instruction in IR is : 00072783
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '01111', 'immediate': '000000000000', 'format': 'I', 'id': 14}
RA is : 10000008
rd is : 15
imm is : 00000000
Execute stage:
operand1 is 10000008 operand2 is: 00000000
RZ is : 10000008
Memory Access stage:
Register Update Stage:
RD: RY: 15 00000046
cycle is : 312
Fetch stage:
The value of PC is : 0000002c
The instruction in IR is : 00472803
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '10000', 'immediate': '000000000100', 'format': 'I', 'id': 14}
RA is : 10000008
rd is : 16
imm is : 00000004
Execute stage:
operand1 is 10000008 operand2 is: 00000004
RZ is : 1000000c
Memory Access stage:
Register Update Stage:
RD: RY: 16 00000028
cycle is : 313
Fetch stage:
The value of PC is : 00000030
The instruction in IR is : 00168693
Decode stage:
code : {'neumonic': 'addi', 'opcode': '0b0010011', 'funct3': '0b000', 'rs1': '01101', 'rd': '01101', 'immediate': '000000000001', 'format': 'I', 'id': 9}
RA is : 00000002
rd is : 13
imm is : 00000001
Execute stage:
operand1 is 00000002 operand2 is: 00000001
RZ is : 00000003
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000003
cycle is : 314
Fetch stage:
The value of PC is : 00000034
The instruction in IR is : FF07C4E3
Decode stage:
code : {'neumonic': 'blt', 'opcode': '0b1100011', 'funct3': '0b100', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111101000', 'format': 'SB', 'id': 20}
RA is : 00000046
RB is : 00000028
imm is : ffffffe8
Execute stage:
operand1 is 00000046 operand2 is: 00000028
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 315
Fetch stage:
The value of PC is : 00000038
The instruction in IR is : FF0782E3
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111100100', 'format': 'SB', 'id': 18}
RA is : 00000046
RB is : 00000028
imm is : ffffffe4
Execute stage:
operand1 is 00000046 operand2 is: 00000028
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 316
Fetch stage:
The value of PC is : 0000003c
The instruction in IR is : 01072023
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '10000', 'immediate': '000000000000', 'format': 'S', 'id': 17}
RA is : 10000008
RB is : 00000028
imm is : 00000000
Execute stage:
operand1 is 10000008 operand2 is: 00000000
RZ is : 10000008
Memory Access stage:
Register Update Stage:
RD: RY: 13 10000008
cycle is : 317
Fetch stage:
The value of PC is : 00000040
The instruction in IR is : 00F72223
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '01111', 'immediate': '000000000100', 'format': 'S', 'id': 17}
RA is : 10000008
RB is : 00000046
imm is : 00000004
Execute stage:
operand1 is 10000008 operand2 is: 00000004
RZ is : 1000000c
Memory Access stage:
Register Update Stage:
RD: RY: 13 1000000c
cycle is : 318
Fetch stage:
The value of PC is : 00000044
The instruction in IR is : FD9FF06F
Decode stage:
code : {'neumonic': 'jal', 'opcode': '0b1101111', 'immediate': '111111111111111011000', 'rd': '00000', 'format': 'UJ', 'id': 22}
rd is : 0
imm is : ffffffd8
Execute stage:
operand1 is 10000008 operand2 is: 00000046
RZ is : 1000004e
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000048
cycle is : 319
Fetch stage:
The value of PC is : 0000001c
The instruction in IR is : 02C68663
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01101', 'rs2': '01100', 'immediate': '0000000101100', 'format': 'SB', 'id': 18}
RA is : 00000003
RB is : 00000006
imm is : 0000002c
Execute stage:
operand1 is 00000003 operand2 is: 00000006
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000000
cycle is : 320
Fetch stage:
The value of PC is : 00000020
The instruction in IR is : 01F69733
Decode stage:
code : {'neumonic': 'sll', 'opcode': '0b0110011', 'funct3': '0b001', 'funct7': '0b0000000', 'rs1': '01101', 'rs2': '11111', 'rd': '01110', 'format': 'R', 'id': 5}
RA is : 00000003
RB is : 00000002
rd is : 14
Execute stage:
operand1 is 00000003 operand2 is: 00000002
RZ is : 0000000c
Memory Access stage:
Register Update Stage:
RD: RY: 14 0000000c
cycle is : 321
Fetch stage:
The value of PC is : 00000024
The instruction in IR is : 00B70733
Decode stage:
code : {'neumonic': 'add', 'opcode': '0b0110011', 'funct3': '0b000', 'funct7': '0b0000000', 'rs1': '01110', 'rs2': '01011', 'rd': '01110', 'format': 'R', 'id': 0}
RA is : 0000000c
RB is : 10000000
rd is : 14
Execute stage:
operand1 is 0000000c operand2 is: 10000000
RZ is : 1000000c
Memory Access stage:
Register Update Stage:
RD: RY: 14 1000000c
cycle is : 322
Fetch stage:
The value of PC is : 00000028
The instruction in IR is : 00072783
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '01111', 'immediate': '000000000000', 'format': 'I', 'id': 14}
RA is : 1000000c
rd is : 15
imm is : 00000000
Execute stage:
operand1 is 1000000c operand2 is: 00000000
RZ is : 1000000c
Memory Access stage:
Register Update Stage:
RD: RY: 15 00000046
cycle is : 323
Fetch stage:
The value of PC is : 0000002c
The instruction in IR is : 00472803
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '10000', 'immediate': '000000000100', 'format': 'I', 'id': 14}
RA is : 1000000c
rd is : 16
imm is : 00000004
Execute stage:
operand1 is 1000000c operand2 is: 00000004
RZ is : 10000010
Memory Access stage:
Register Update Stage:
RD: RY: 16 0000001E
cycle is : 324
Fetch stage:
The value of PC is : 00000030
The instruction in IR is : 00168693
Decode stage:
code : {'neumonic': 'addi', 'opcode': '0b0010011', 'funct3': '0b000', 'rs1': '01101', 'rd': '01101', 'immediate': '000000000001', 'format': 'I', 'id': 9}
RA is : 00000003
rd is : 13
imm is : 00000001
Execute stage:
operand1 is 00000003 operand2 is: 00000001
RZ is : 00000004
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000004
cycle is : 325
Fetch stage:
The value of PC is : 00000034
The instruction in IR is : FF07C4E3
Decode stage:
code : {'neumonic': 'blt', 'opcode': '0b1100011', 'funct3': '0b100', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111101000', 'format': 'SB', 'id': 20}
RA is : 00000046
RB is : 0000001E
imm is : ffffffe8
Execute stage:
operand1 is 00000046 operand2 is: 0000001E
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 326
Fetch stage:
The value of PC is : 00000038
The instruction in IR is : FF0782E3
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111100100', 'format': 'SB', 'id': 18}
RA is : 00000046
RB is : 0000001E
imm is : ffffffe4
Execute stage:
operand1 is 00000046 operand2 is: 0000001E
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 327
Fetch stage:
The value of PC is : 0000003c
The instruction in IR is : 01072023
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '10000', 'immediate': '000000000000', 'format': 'S', 'id': 17}
RA is : 1000000c
RB is : 0000001E
imm is : 00000000
Execute stage:
operand1 is 1000000c operand2 is: 00000000
RZ is : 1000000c
Memory Access stage:
Register Update Stage:
RD: RY: 13 1000000c
cycle is : 328
Fetch stage:
The value of PC is : 00000040
The instruction in IR is : 00F72223
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '01111', 'immediate': '000000000100', 'format': 'S', 'id': 17}
RA is : 1000000c
RB is : 00000046
imm is : 00000004
Execute stage:
operand1 is 1000000c operand2 is: 00000004
RZ is : 10000010
Memory Access stage:
Register Update Stage:
RD: RY: 13 10000010
cycle is : 329
Fetch stage:
The value of PC is : 00000044
The instruction in IR is : FD9FF06F
Decode stage:
code : {'neumonic': 'jal', 'opcode': '0b1101111', 'immediate': '111111111111111011000', 'rd': '00000', 'format': 'UJ', 'id': 22}
rd is : 0
imm is : ffffffd8
Execute stage:
operand1 is 1000000c operand2 is: 00000046
RZ is : 10000052
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000048
cycle is : 330
Fetch stage:
The value of PC is : 0000001c
The instruction in IR is : 02C68663
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01101', 'rs2': '01100', 'immediate': '0000000101100', 'format': 'SB', 'id': 18}
RA is : 00000004
RB is : 00000006
imm is : 0000002c
Execute stage:
operand1 is 00000004 operand2 is: 00000006
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000000
cycle is : 331
Fetch stage:
The value of PC is : 00000020
The instruction in IR is : 01F69733
Decode stage:
code : {'neumonic': 'sll', 'opcode': '0b0110011', 'funct3': '0b001', 'funct7': '0b0000000', 'rs1': '01101', 'rs2': '11111', 'rd': '01110', 'format': 'R', 'id': 5}
RA is : 00000004
RB is : 00000002
rd is : 14
Execute stage:
operand1 is 00000004 operand2 is: 00000002
RZ is : 00000010
Memory Access stage:
Register Update Stage:
RD: RY: 14 00000010
cycle is : 332
Fetch stage:
The value of PC is : 00000024
The instruction in IR is : 00B70733
Decode stage:
code : {'neumonic': 'add', 'opcode': '0b0110011', 'funct3': '0b000', 'funct7': '0b0000000', 'rs1': '01110', 'rs2': '01011', 'rd': '01110', 'format': 'R', 'id': 0}
RA is : 00000010
RB is : 10000000
rd is : 14
Execute stage:
operand1 is 00000010 operand2 is: 10000000
RZ is : 10000010
Memory Access stage:
Register Update Stage:
RD: RY: 14 10000010
cycle is : 333
Fetch stage:
The value of PC is : 00000028
The instruction in IR is : 00072783
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '01111', 'immediate': '000000000000', 'format': 'I', 'id': 14}
RA is : 10000010
rd is : 15
imm is : 00000000
Execute stage:
operand1 is 10000010 operand2 is: 00000000
RZ is : 10000010
Memory Access stage:
Register Update Stage:
RD: RY: 15 00000046
cycle is : 334
Fetch stage:
The value of PC is : 0000002c
The instruction in IR is : 00472803
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '10000', 'immediate': '000000000100', 'format': 'I', 'id': 14}
RA is : 10000010
rd is : 16
imm is : 00000004
Execute stage:
operand1 is 10000010 operand2 is: 00000004
RZ is : 10000014
Memory Access stage:
Register Update Stage:
RD: RY: 16 00000014
cycle is : 335
Fetch stage:
The value of PC is : 00000030
The instruction in IR is : 00168693
Decode stage:
code : {'neumonic': 'addi', 'opcode': '0b0010011', 'funct3': '0b000', 'rs1': '01101', 'rd': '01101', 'immediate': '000000000001', 'format': 'I', 'id': 9}
RA is : 00000004
rd is : 13
imm is : 00000001
Execute stage:
operand1 is 00000004 operand2 is: 00000001
RZ is : 00000005
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000005
cycle is : 336
Fetch stage:
The value of PC is : 00000034
The instruction in IR is : FF07C4E3
Decode stage:
code : {'neumonic': 'blt', 'opcode': '0b1100011', 'funct3': '0b100', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111101000', 'format': 'SB', 'id': 20}
RA is : 00000046
RB is : 00000014
imm is : ffffffe8
Execute stage:
operand1 is 00000046 operand2 is: 00000014
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 337
Fetch stage:
The value of PC is : 00000038
The instruction in IR is : FF0782E3
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111100100', 'format': 'SB', 'id': 18}
RA is : 00000046
RB is : 00000014
imm is : ffffffe4
Execute stage:
operand1 is 00000046 operand2 is: 00000014
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 338
Fetch stage:
The value of PC is : 0000003c
The instruction in IR is : 01072023
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '10000', 'immediate': '000000000000', 'format': 'S', 'id': 17}
RA is : 10000010
RB is : 00000014
imm is : 00000000
Execute stage:
operand1 is 10000010 operand2 is: 00000000
RZ is : 10000010
Memory Access stage:
Register Update Stage:
RD: RY: 13 10000010
cycle is : 339
Fetch stage:
The value of PC is : 00000040
The instruction in IR is : 00F72223
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '01111', 'immediate': '000000000100', 'format': 'S', 'id': 17}
RA is : 10000010
RB is : 00000046
imm is : 00000004
Execute stage:
operand1 is 10000010 operand2 is: 00000004
RZ is : 10000014
Memory Access stage:
Register Update Stage:
RD: RY: 13 10000014
cycle is : 340
Fetch stage:
The value of PC is : 00000044
The instruction in IR is : FD9FF06F
Decode stage:
code : {'neumonic': 'jal', 'opcode': '0b1101111', 'immediate': '111111111111111011000', 'rd': '00000', 'format': 'UJ', 'id': 22}
rd is : 0
imm is : ffffffd8
Execute stage:
operand1 is 10000010 operand2 is: 00000046
RZ is : 10000056
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000048
cycle is : 341
Fetch stage:
The value of PC is : 0000001c
The instruction in IR is : 02C68663
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01101', 'rs2': '01100', 'immediate': '0000000101100', 'format': 'SB', 'id': 18}
RA is : 00000005
RB is : 00000006
imm is : 0000002c
Execute stage:
operand1 is 00000005 operand2 is: 00000006
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000000
cycle is : 342
Fetch stage:
The value of PC is : 00000020
The instruction in IR is : 01F69733
Decode stage:
code : {'neumonic': 'sll', 'opcode': '0b0110011', 'funct3': '0b001', 'funct7': '0b0000000', 'rs1': '01101', 'rs2': '11111', 'rd': '01110', 'format': 'R', 'id': 5}
RA is : 00000005
RB is : 00000002
rd is : 14
Execute stage:
operand1 is 00000005 operand2 is: 00000002
RZ is : 00000014
Memory Access stage:
Register Update Stage:
RD: RY: 14 00000014
cycle is : 343
Fetch stage:
The value of PC is : 00000024
The instruction in IR is : 00B70733
Decode stage:
code : {'neumonic': 'add', 'opcode': '0b0110011', 'funct3': '0b000', 'funct7': '0b0000000', 'rs1': '01110', 'rs2': '01011', 'rd': '01110', 'format': 'R', 'id': 0}
RA is : 00000014
RB is : 10000000
rd is : 14
Execute stage:
operand1 is 00000014 operand2 is: 10000000
RZ is : 10000014
Memory Access stage:
Register Update Stage:
RD: RY: 14 10000014
cycle is : 344
Fetch stage:
The value of PC is : 00000028
The instruction in IR is : 00072783
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '01111', 'immediate': '000000000000', 'format': 'I', 'id': 14}
RA is : 10000014
rd is : 15
imm is : 00000000
Execute stage:
operand1 is 10000014 operand2 is: 00000000
RZ is : 10000014
Memory Access stage:
Register Update Stage:
RD: RY: 15 00000046
cycle is : 345
Fetch stage:
The value of PC is : 0000002c
The instruction in IR is : 00472803
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '10000', 'immediate': '000000000100', 'format': 'I', 'id': 14}
RA is : 10000014
rd is : 16
imm is : 00000004
Execute stage:
operand1 is 10000014 operand2 is: 00000004
RZ is : 10000018
Memory Access stage:
Register Update Stage:
RD: RY: 16 0000000a
cycle is : 346
Fetch stage:
The value of PC is : 00000030
The instruction in IR is : 00168693
Decode stage:
code : {'neumonic': 'addi', 'opcode': '0b0010011', 'funct3': '0b000', 'rs1': '01101', 'rd': '01101', 'immediate': '000000000001', 'format': 'I', 'id': 9}
RA is : 00000005
rd is : 13
imm is : 00000001
Execute stage:
operand1 is 00000005 operand2 is: 00000001
RZ is : 00000006
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000006
cycle is : 347
Fetch stage:
The value of PC is : 00000034
The instruction in IR is : FF07C4E3
Decode stage:
code : {'neumonic': 'blt', 'opcode': '0b1100011', 'funct3': '0b100', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111101000', 'format': 'SB', 'id': 20}
RA is : 00000046
RB is : 0000000a
imm is : ffffffe8
Execute stage:
operand1 is 00000046 operand2 is: 0000000a
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 348
Fetch stage:
The value of PC is : 00000038
The instruction in IR is : FF0782E3
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111100100', 'format': 'SB', 'id': 18}
RA is : 00000046
RB is : 0000000a
imm is : ffffffe4
Execute stage:
operand1 is 00000046 operand2 is: 0000000a
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 349
Fetch stage:
The value of PC is : 0000003c
The instruction in IR is : 01072023
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '10000', 'immediate': '000000000000', 'format': 'S', 'id': 17}
RA is : 10000014
RB is : 0000000a
imm is : 00000000
Execute stage:
operand1 is 10000014 operand2 is: 00000000
RZ is : 10000014
Memory Access stage:
Register Update Stage:
RD: RY: 13 10000014
cycle is : 350
Fetch stage:
The value of PC is : 00000040
The instruction in IR is : 00F72223
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '01111', 'immediate': '000000000100', 'format': 'S', 'id': 17}
RA is : 10000014
RB is : 00000046
imm is : 00000004
Execute stage:
operand1 is 10000014 operand2 is: 00000004
RZ is : 10000018
Memory Access stage:
Register Update Stage:
RD: RY: 13 10000018
cycle is : 351
Fetch stage:
The value of PC is : 00000044
The instruction in IR is : FD9FF06F
Decode stage:
code : {'neumonic': 'jal', 'opcode': '0b1101111', 'immediate': '111111111111111011000', 'rd': '00000', 'format': 'UJ', 'id': 22}
rd is : 0
imm is : ffffffd8
Execute stage:
operand1 is 10000014 operand2 is: 00000046
RZ is : 1000005a
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000048
cycle is : 352
Fetch stage:
The value of PC is : 0000001c
The instruction in IR is : 02C68663
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01101', 'rs2': '01100', 'immediate': '0000000101100', 'format': 'SB', 'id': 18}
RA is : 00000006
RB is : 00000006
imm is : 0000002c
Execute stage:
operand1 is 00000006 operand2 is: 00000006
RZ is : 00000001
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000001
cycle is : 353
Fetch stage:
The value of PC is : 00000048
The instruction in IR is : FC9FF06F
Decode stage:
code : {'neumonic': 'jal', 'opcode': '0b1101111', 'immediate': '111111111111111001000', 'rd': '00000', 'format': 'UJ', 'id': 22}
rd is : 0
imm is : ffffffc8
Execute stage:
operand1 is 00000006 operand2 is: 00000006
RZ is : 0000000c
Memory Access stage:
Register Update Stage:
RD: RY: 0 0000004c
cycle is : 354
Fetch stage:
The value of PC is : 00000010
The instruction in IR is : FFF60613
Decode stage:
code : {'neumonic': 'addi', 'opcode': '0b0010011', 'funct3': '0b000', 'rs1': '01100', 'rd': '01100', 'immediate': '111111111111', 'format': 'I', 'id': 9}
RA is : 00000006
rd is : 12
imm is : ffffffff
Execute stage:
operand1 is 00000006 operand2 is: ffffffff
RZ is : 00000005
Memory Access stage:
Register Update Stage:
RD: RY: 12 00000005
cycle is : 355
Fetch stage:
The value of PC is : 00000014
The instruction in IR is : 02060C63
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01100', 'rs2': '00000', 'immediate': '0000000111000', 'format': 'SB', 'id': 18}
RA is : 00000005
RB is : 00000000
imm is : 00000038
Execute stage:
operand1 is 00000005 operand2 is: 00000000
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 12 00000000
cycle is : 356
Fetch stage:
The value of PC is : 00000018
The instruction in IR is : 00000693
Decode stage:
code : {'neumonic': 'addi', 'opcode': '0b0010011', 'funct3': '0b000', 'rs1': '00000', 'rd': '01101', 'immediate': '000000000000', 'format': 'I', 'id': 9}
RA is : 00000000
rd is : 13
imm is : 00000000
Execute stage:
operand1 is 00000000 operand2 is: 00000000
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 357
Fetch stage:
The value of PC is : 0000001c
The instruction in IR is : 02C68663
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01101', 'rs2': '01100', 'immediate': '0000000101100', 'format': 'SB', 'id': 18}
RA is : 00000000
RB is : 00000005
imm is : 0000002c
Execute stage:
operand1 is 00000000 operand2 is: 00000005
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 358
Fetch stage:
The value of PC is : 00000020
The instruction in IR is : 01F69733
Decode stage:
code : {'neumonic': 'sll', 'opcode': '0b0110011', 'funct3': '0b001', 'funct7': '0b0000000', 'rs1': '01101', 'rs2': '11111', 'rd': '01110', 'format': 'R', 'id': 5}
RA is : 00000000
RB is : 00000002
rd is : 14
Execute stage:
operand1 is 00000000 operand2 is: 00000002
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 14 00000000
cycle is : 359
Fetch stage:
The value of PC is : 00000024
The instruction in IR is : 00B70733
Decode stage:
code : {'neumonic': 'add', 'opcode': '0b0110011', 'funct3': '0b000', 'funct7': '0b0000000', 'rs1': '01110', 'rs2': '01011', 'rd': '01110', 'format': 'R', 'id': 0}
RA is : 00000000
RB is : 10000000
rd is : 14
Execute stage:
operand1 is 00000000 operand2 is: 10000000
RZ is : 10000000
Memory Access stage:
Register Update Stage:
RD: RY: 14 10000000
cycle is : 360
Fetch stage:
The value of PC is : 00000028
The instruction in IR is : 00072783
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '01111', 'immediate': '000000000000', 'format': 'I', 'id': 14}
RA is : 10000000
rd is : 15
imm is : 00000000
Execute stage:
operand1 is 10000000 operand2 is: 00000000
RZ is : 10000000
Memory Access stage:
Register Update Stage:
RD: RY: 15 0000003C
cycle is : 361
Fetch stage:
The value of PC is : 0000002c
The instruction in IR is : 00472803
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '10000', 'immediate': '000000000100', 'format': 'I', 'id': 14}
RA is : 10000000
rd is : 16
imm is : 00000004
Execute stage:
operand1 is 10000000 operand2 is: 00000004
RZ is : 10000004
Memory Access stage:
Register Update Stage:
RD: RY: 16 00000032
cycle is : 362
Fetch stage:
The value of PC is : 00000030
The instruction in IR is : 00168693
Decode stage:
code : {'neumonic': 'addi', 'opcode': '0b0010011', 'funct3': '0b000', 'rs1': '01101', 'rd': '01101', 'immediate': '000000000001', 'format': 'I', 'id': 9}
RA is : 00000000
rd is : 13
imm is : 00000001
Execute stage:
operand1 is 00000000 operand2 is: 00000001
RZ is : 00000001
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000001
cycle is : 363
Fetch stage:
The value of PC is : 00000034
The instruction in IR is : FF07C4E3
Decode stage:
code : {'neumonic': 'blt', 'opcode': '0b1100011', 'funct3': '0b100', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111101000', 'format': 'SB', 'id': 20}
RA is : 0000003C
RB is : 00000032
imm is : ffffffe8
Execute stage:
operand1 is 0000003C operand2 is: 00000032
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 364
Fetch stage:
The value of PC is : 00000038
The instruction in IR is : FF0782E3
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111100100', 'format': 'SB', 'id': 18}
RA is : 0000003C
RB is : 00000032
imm is : ffffffe4
Execute stage:
operand1 is 0000003C operand2 is: 00000032
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 365
Fetch stage:
The value of PC is : 0000003c
The instruction in IR is : 01072023
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '10000', 'immediate': '000000000000', 'format': 'S', 'id': 17}
RA is : 10000000
RB is : 00000032
imm is : 00000000
Execute stage:
operand1 is 10000000 operand2 is: 00000000
RZ is : 10000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 10000000
cycle is : 366
Fetch stage:
The value of PC is : 00000040
The instruction in IR is : 00F72223
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '01111', 'immediate': '000000000100', 'format': 'S', 'id': 17}
RA is : 10000000
RB is : 0000003C
imm is : 00000004
Execute stage:
operand1 is 10000000 operand2 is: 00000004
RZ is : 10000004
Memory Access stage:
Register Update Stage:
RD: RY: 13 10000004
cycle is : 367
Fetch stage:
The value of PC is : 00000044
The instruction in IR is : FD9FF06F
Decode stage:
code : {'neumonic': 'jal', 'opcode': '0b1101111', 'immediate': '111111111111111011000', 'rd': '00000', 'format': 'UJ', 'id': 22}
rd is : 0
imm is : ffffffd8
Execute stage:
operand1 is 10000000 operand2 is: 0000003C
RZ is : 1000003c
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000048
cycle is : 368
Fetch stage:
The value of PC is : 0000001c
The instruction in IR is : 02C68663
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01101', 'rs2': '01100', 'immediate': '0000000101100', 'format': 'SB', 'id': 18}
RA is : 00000001
RB is : 00000005
imm is : 0000002c
Execute stage:
operand1 is 00000001 operand2 is: 00000005
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000000
cycle is : 369
Fetch stage:
The value of PC is : 00000020
The instruction in IR is : 01F69733
Decode stage:
code : {'neumonic': 'sll', 'opcode': '0b0110011', 'funct3': '0b001', 'funct7': '0b0000000', 'rs1': '01101', 'rs2': '11111', 'rd': '01110', 'format': 'R', 'id': 5}
RA is : 00000001
RB is : 00000002
rd is : 14
Execute stage:
operand1 is 00000001 operand2 is: 00000002
RZ is : 00000004
Memory Access stage:
Register Update Stage:
RD: RY: 14 00000004
cycle is : 370
Fetch stage:
The value of PC is : 00000024
The instruction in IR is : 00B70733
Decode stage:
code : {'neumonic': 'add', 'opcode': '0b0110011', 'funct3': '0b000', 'funct7': '0b0000000', 'rs1': '01110', 'rs2': '01011', 'rd': '01110', 'format': 'R', 'id': 0}
RA is : 00000004
RB is : 10000000
rd is : 14
Execute stage:
operand1 is 00000004 operand2 is: 10000000
RZ is : 10000004
Memory Access stage:
Register Update Stage:
RD: RY: 14 10000004
cycle is : 371
Fetch stage:
The value of PC is : 00000028
The instruction in IR is : 00072783
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '01111', 'immediate': '000000000000', 'format': 'I', 'id': 14}
RA is : 10000004
rd is : 15
imm is : 00000000
Execute stage:
operand1 is 10000004 operand2 is: 00000000
RZ is : 10000004
Memory Access stage:
Register Update Stage:
RD: RY: 15 0000003C
cycle is : 372
Fetch stage:
The value of PC is : 0000002c
The instruction in IR is : 00472803
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '10000', 'immediate': '000000000100', 'format': 'I', 'id': 14}
RA is : 10000004
rd is : 16
imm is : 00000004
Execute stage:
operand1 is 10000004 operand2 is: 00000004
RZ is : 10000008
Memory Access stage:
Register Update Stage:
RD: RY: 16 00000028
cycle is : 373
Fetch stage:
The value of PC is : 00000030
The instruction in IR is : 00168693
Decode stage:
code : {'neumonic': 'addi', 'opcode': '0b0010011', 'funct3': '0b000', 'rs1': '01101', 'rd': '01101', 'immediate': '000000000001', 'format': 'I', 'id': 9}
RA is : 00000001
rd is : 13
imm is : 00000001
Execute stage:
operand1 is 00000001 operand2 is: 00000001
RZ is : 00000002
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000002
cycle is : 374
Fetch stage:
The value of PC is : 00000034
The instruction in IR is : FF07C4E3
Decode stage:
code : {'neumonic': 'blt', 'opcode': '0b1100011', 'funct3': '0b100', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111101000', 'format': 'SB', 'id': 20}
RA is : 0000003C
RB is : 00000028
imm is : ffffffe8
Execute stage:
operand1 is 0000003C operand2 is: 00000028
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 375
Fetch stage:
The value of PC is : 00000038
The instruction in IR is : FF0782E3
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111100100', 'format': 'SB', 'id': 18}
RA is : 0000003C
RB is : 00000028
imm is : ffffffe4
Execute stage:
operand1 is 0000003C operand2 is: 00000028
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 376
Fetch stage:
The value of PC is : 0000003c
The instruction in IR is : 01072023
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '10000', 'immediate': '000000000000', 'format': 'S', 'id': 17}
RA is : 10000004
RB is : 00000028
imm is : 00000000
Execute stage:
operand1 is 10000004 operand2 is: 00000000
RZ is : 10000004
Memory Access stage:
Register Update Stage:
RD: RY: 13 10000004
cycle is : 377
Fetch stage:
The value of PC is : 00000040
The instruction in IR is : 00F72223
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '01111', 'immediate': '000000000100', 'format': 'S', 'id': 17}
RA is : 10000004
RB is : 0000003C
imm is : 00000004
Execute stage:
operand1 is 10000004 operand2 is: 00000004
RZ is : 10000008
Memory Access stage:
Register Update Stage:
RD: RY: 13 10000008
cycle is : 378
Fetch stage:
The value of PC is : 00000044
The instruction in IR is : FD9FF06F
Decode stage:
code : {'neumonic': 'jal', 'opcode': '0b1101111', 'immediate': '111111111111111011000', 'rd': '00000', 'format': 'UJ', 'id': 22}
rd is : 0
imm is : ffffffd8
Execute stage:
operand1 is 10000004 operand2 is: 0000003C
RZ is : 10000040
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000048
cycle is : 379
Fetch stage:
The value of PC is : 0000001c
The instruction in IR is : 02C68663
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01101', 'rs2': '01100', 'immediate': '0000000101100', 'format': 'SB', 'id': 18}
RA is : 00000002
RB is : 00000005
imm is : 0000002c
Execute stage:
operand1 is 00000002 operand2 is: 00000005
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000000
cycle is : 380
Fetch stage:
The value of PC is : 00000020
The instruction in IR is : 01F69733
Decode stage:
code : {'neumonic': 'sll', 'opcode': '0b0110011', 'funct3': '0b001', 'funct7': '0b0000000', 'rs1': '01101', 'rs2': '11111', 'rd': '01110', 'format': 'R', 'id': 5}
RA is : 00000002
RB is : 00000002
rd is : 14
Execute stage:
operand1 is 00000002 operand2 is: 00000002
RZ is : 00000008
Memory Access stage:
Register Update Stage:
RD: RY: 14 00000008
cycle is : 381
Fetch stage:
The value of PC is : 00000024
The instruction in IR is : 00B70733
Decode stage:
code : {'neumonic': 'add', 'opcode': '0b0110011', 'funct3': '0b000', 'funct7': '0b0000000', 'rs1': '01110', 'rs2': '01011', 'rd': '01110', 'format': 'R', 'id': 0}
RA is : 00000008
RB is : 10000000
rd is : 14
Execute stage:
operand1 is 00000008 operand2 is: 10000000
RZ is : 10000008
Memory Access stage:
Register Update Stage:
RD: RY: 14 10000008
cycle is : 382
Fetch stage:
The value of PC is : 00000028
The instruction in IR is : 00072783
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '01111', 'immediate': '000000000000', 'format': 'I', 'id': 14}
RA is : 10000008
rd is : 15
imm is : 00000000
Execute stage:
operand1 is 10000008 operand2 is: 00000000
RZ is : 10000008
Memory Access stage:
Register Update Stage:
RD: RY: 15 0000003C
cycle is : 383
Fetch stage:
The value of PC is : 0000002c
The instruction in IR is : 00472803
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '10000', 'immediate': '000000000100', 'format': 'I', 'id': 14}
RA is : 10000008
rd is : 16
imm is : 00000004
Execute stage:
operand1 is 10000008 operand2 is: 00000004
RZ is : 1000000c
Memory Access stage:
Register Update Stage:
RD: RY: 16 0000001E
cycle is : 384
Fetch stage:
The value of PC is : 00000030
The instruction in IR is : 00168693
Decode stage:
code : {'neumonic': 'addi', 'opcode': '0b0010011', 'funct3': '0b000', 'rs1': '01101', 'rd': '01101', 'immediate': '000000000001', 'format': 'I', 'id': 9}
RA is : 00000002
rd is : 13
imm is : 00000001
Execute stage:
operand1 is 00000002 operand2 is: 00000001
RZ is : 00000003
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000003
cycle is : 385
Fetch stage:
The value of PC is : 00000034
The instruction in IR is : FF07C4E3
Decode stage:
code : {'neumonic': 'blt', 'opcode': '0b1100011', 'funct3': '0b100', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111101000', 'format': 'SB', 'id': 20}
RA is : 0000003C
RB is : 0000001E
imm is : ffffffe8
Execute stage:
operand1 is 0000003C operand2 is: 0000001E
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 386
Fetch stage:
The value of PC is : 00000038
The instruction in IR is : FF0782E3
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111100100', 'format': 'SB', 'id': 18}
RA is : 0000003C
RB is : 0000001E
imm is : ffffffe4
Execute stage:
operand1 is 0000003C operand2 is: 0000001E
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 387
Fetch stage:
The value of PC is : 0000003c
The instruction in IR is : 01072023
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '10000', 'immediate': '000000000000', 'format': 'S', 'id': 17}
RA is : 10000008
RB is : 0000001E
imm is : 00000000
Execute stage:
operand1 is 10000008 operand2 is: 00000000
RZ is : 10000008
Memory Access stage:
Register Update Stage:
RD: RY: 13 10000008
cycle is : 388
Fetch stage:
The value of PC is : 00000040
The instruction in IR is : 00F72223
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '01111', 'immediate': '000000000100', 'format': 'S', 'id': 17}
RA is : 10000008
RB is : 0000003C
imm is : 00000004
Execute stage:
operand1 is 10000008 operand2 is: 00000004
RZ is : 1000000c
Memory Access stage:
Register Update Stage:
RD: RY: 13 1000000c
cycle is : 389
Fetch stage:
The value of PC is : 00000044
The instruction in IR is : FD9FF06F
Decode stage:
code : {'neumonic': 'jal', 'opcode': '0b1101111', 'immediate': '111111111111111011000', 'rd': '00000', 'format': 'UJ', 'id': 22}
rd is : 0
imm is : ffffffd8
Execute stage:
operand1 is 10000008 operand2 is: 0000003C
RZ is : 10000044
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000048
cycle is : 390
Fetch stage:
The value of PC is : 0000001c
The instruction in IR is : 02C68663
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01101', 'rs2': '01100', 'immediate': '0000000101100', 'format': 'SB', 'id': 18}
RA is : 00000003
RB is : 00000005
imm is : 0000002c
Execute stage:
operand1 is 00000003 operand2 is: 00000005
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000000
cycle is : 391
Fetch stage:
The value of PC is : 00000020
The instruction in IR is : 01F69733
Decode stage:
code : {'neumonic': 'sll', 'opcode': '0b0110011', 'funct3': '0b001', 'funct7': '0b0000000', 'rs1': '01101', 'rs2': '11111', 'rd': '01110', 'format': 'R', 'id': 5}
RA is : 00000003
RB is : 00000002
rd is : 14
Execute stage:
operand1 is 00000003 operand2 is: 00000002
RZ is : 0000000c
Memory Access stage:
Register Update Stage:
RD: RY: 14 0000000c
cycle is : 392
Fetch stage:
The value of PC is : 00000024
The instruction in IR is : 00B70733
Decode stage:
code : {'neumonic': 'add', 'opcode': '0b0110011', 'funct3': '0b000', 'funct7': '0b0000000', 'rs1': '01110', 'rs2': '01011', 'rd': '01110', 'format': 'R', 'id': 0}
RA is : 0000000c
RB is : 10000000
rd is : 14
Execute stage:
operand1 is 0000000c operand2 is: 10000000
RZ is : 1000000c
Memory Access stage:
Register Update Stage:
RD: RY: 14 1000000c
cycle is : 393
Fetch stage:
The value of PC is : 00000028
The instruction in IR is : 00072783
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '01111', 'immediate': '000000000000', 'format': 'I', 'id': 14}
RA is : 1000000c
rd is : 15
imm is : 00000000
Execute stage:
operand1 is 1000000c operand2 is: 00000000
RZ is : 1000000c
Memory Access stage:
Register Update Stage:
RD: RY: 15 0000003C
cycle is : 394
Fetch stage:
The value of PC is : 0000002c
The instruction in IR is : 00472803
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '10000', 'immediate': '000000000100', 'format': 'I', 'id': 14}
RA is : 1000000c
rd is : 16
imm is : 00000004
Execute stage:
operand1 is 1000000c operand2 is: 00000004
RZ is : 10000010
Memory Access stage:
Register Update Stage:
RD: RY: 16 00000014
cycle is : 395
Fetch stage:
The value of PC is : 00000030
The instruction in IR is : 00168693
Decode stage:
code : {'neumonic': 'addi', 'opcode': '0b0010011', 'funct3': '0b000', 'rs1': '01101', 'rd': '01101', 'immediate': '000000000001', 'format': 'I', 'id': 9}
RA is : 00000003
rd is : 13
imm is : 00000001
Execute stage:
operand1 is 00000003 operand2 is: 00000001
RZ is : 00000004
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000004
cycle is : 396
Fetch stage:
The value of PC is : 00000034
The instruction in IR is : FF07C4E3
Decode stage:
code : {'neumonic': 'blt', 'opcode': '0b1100011', 'funct3': '0b100', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111101000', 'format': 'SB', 'id': 20}
RA is : 0000003C
RB is : 00000014
imm is : ffffffe8
Execute stage:
operand1 is 0000003C operand2 is: 00000014
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 397
Fetch stage:
The value of PC is : 00000038
The instruction in IR is : FF0782E3
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111100100', 'format': 'SB', 'id': 18}
RA is : 0000003C
RB is : 00000014
imm is : ffffffe4
Execute stage:
operand1 is 0000003C operand2 is: 00000014
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 398
Fetch stage:
The value of PC is : 0000003c
The instruction in IR is : 01072023
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '10000', 'immediate': '000000000000', 'format': 'S', 'id': 17}
RA is : 1000000c
RB is : 00000014
imm is : 00000000
Execute stage:
operand1 is 1000000c operand2 is: 00000000
RZ is : 1000000c
Memory Access stage:
Register Update Stage:
RD: RY: 13 1000000c
cycle is : 399
Fetch stage:
The value of PC is : 00000040
The instruction in IR is : 00F72223
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '01111', 'immediate': '000000000100', 'format': 'S', 'id': 17}
RA is : 1000000c
RB is : 0000003C
imm is : 00000004
Execute stage:
operand1 is 1000000c operand2 is: 00000004
RZ is : 10000010
Memory Access stage:
Register Update Stage:
RD: RY: 13 10000010
cycle is : 400
Fetch stage:
The value of PC is : 00000044
The instruction in IR is : FD9FF06F
Decode stage:
code : {'neumonic': 'jal', 'opcode': '0b1101111', 'immediate': '111111111111111011000', 'rd': '00000', 'format': 'UJ', 'id': 22}
rd is : 0
imm is : ffffffd8
Execute stage:
operand1 is 1000000c operand2 is: 0000003C
RZ is : 10000048
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000048
cycle is : 401
Fetch stage:
The value of PC is : 0000001c
The instruction in IR is : 02C68663
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01101', 'rs2': '01100', 'immediate': '0000000101100', 'format': 'SB', 'id': 18}
RA is : 00000004
RB is : 00000005
imm is : 0000002c
Execute stage:
operand1 is 00000004 operand2 is: 00000005
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000000
cycle is : 402
Fetch stage:
The value of PC is : 00000020
The instruction in IR is : 01F69733
Decode stage:
code : {'neumonic': 'sll', 'opcode': '0b0110011', 'funct3': '0b001', 'funct7': '0b0000000', 'rs1': '01101', 'rs2': '11111', 'rd': '01110', 'format': 'R', 'id': 5}
RA is : 00000004
RB is : 00000002
rd is : 14
Execute stage:
operand1 is 00000004 operand2 is: 00000002
RZ is : 00000010
Memory Access stage:
Register Update Stage:
RD: RY: 14 00000010
cycle is : 403
Fetch stage:
The value of PC is : 00000024
The instruction in IR is : 00B70733
Decode stage:
code : {'neumonic': 'add', 'opcode': '0b0110011', 'funct3': '0b000', 'funct7': '0b0000000', 'rs1': '01110', 'rs2': '01011', 'rd': '01110', 'format': 'R', 'id': 0}
RA is : 00000010
RB is : 10000000
rd is : 14
Execute stage:
operand1 is 00000010 operand2 is: 10000000
RZ is : 10000010
Memory Access stage:
Register Update Stage:
RD: RY: 14 10000010
cycle is : 404
Fetch stage:
The value of PC is : 00000028
The instruction in IR is : 00072783
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '01111', 'immediate': '000000000000', 'format': 'I', 'id': 14}
RA is : 10000010
rd is : 15
imm is : 00000000
Execute stage:
operand1 is 10000010 operand2 is: 00000000
RZ is : 10000010
Memory Access stage:
Register Update Stage:
RD: RY: 15 0000003C
cycle is : 405
Fetch stage:
The value of PC is : 0000002c
The instruction in IR is : 00472803
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '10000', 'immediate': '000000000100', 'format': 'I', 'id': 14}
RA is : 10000010
rd is : 16
imm is : 00000004
Execute stage:
operand1 is 10000010 operand2 is: 00000004
RZ is : 10000014
Memory Access stage:
Register Update Stage:
RD: RY: 16 0000000a
cycle is : 406
Fetch stage:
The value of PC is : 00000030
The instruction in IR is : 00168693
Decode stage:
code : {'neumonic': 'addi', 'opcode': '0b0010011', 'funct3': '0b000', 'rs1': '01101', 'rd': '01101', 'immediate': '000000000001', 'format': 'I', 'id': 9}
RA is : 00000004
rd is : 13
imm is : 00000001
Execute stage:
operand1 is 00000004 operand2 is: 00000001
RZ is : 00000005
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000005
cycle is : 407
Fetch stage:
The value of PC is : 00000034
The instruction in IR is : FF07C4E3
Decode stage:
code : {'neumonic': 'blt', 'opcode': '0b1100011', 'funct3': '0b100', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111101000', 'format': 'SB', 'id': 20}
RA is : 0000003C
RB is : 0000000a
imm is : ffffffe8
Execute stage:
operand1 is 0000003C operand2 is: 0000000a
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 408
Fetch stage:
The value of PC is : 00000038
The instruction in IR is : FF0782E3
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111100100', 'format': 'SB', 'id': 18}
RA is : 0000003C
RB is : 0000000a
imm is : ffffffe4
Execute stage:
operand1 is 0000003C operand2 is: 0000000a
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 409
Fetch stage:
The value of PC is : 0000003c
The instruction in IR is : 01072023
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '10000', 'immediate': '000000000000', 'format': 'S', 'id': 17}
RA is : 10000010
RB is : 0000000a
imm is : 00000000
Execute stage:
operand1 is 10000010 operand2 is: 00000000
RZ is : 10000010
Memory Access stage:
Register Update Stage:
RD: RY: 13 10000010
cycle is : 410
Fetch stage:
The value of PC is : 00000040
The instruction in IR is : 00F72223
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '01111', 'immediate': '000000000100', 'format': 'S', 'id': 17}
RA is : 10000010
RB is : 0000003C
imm is : 00000004
Execute stage:
operand1 is 10000010 operand2 is: 00000004
RZ is : 10000014
Memory Access stage:
Register Update Stage:
RD: RY: 13 10000014
cycle is : 411
Fetch stage:
The value of PC is : 00000044
The instruction in IR is : FD9FF06F
Decode stage:
code : {'neumonic': 'jal', 'opcode': '0b1101111', 'immediate': '111111111111111011000', 'rd': '00000', 'format': 'UJ', 'id': 22}
rd is : 0
imm is : ffffffd8
Execute stage:
operand1 is 10000010 operand2 is: 0000003C
RZ is : 1000004c
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000048
cycle is : 412
Fetch stage:
The value of PC is : 0000001c
The instruction in IR is : 02C68663
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01101', 'rs2': '01100', 'immediate': '0000000101100', 'format': 'SB', 'id': 18}
RA is : 00000005
RB is : 00000005
imm is : 0000002c
Execute stage:
operand1 is 00000005 operand2 is: 00000005
RZ is : 00000001
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000001
cycle is : 413
Fetch stage:
The value of PC is : 00000048
The instruction in IR is : FC9FF06F
Decode stage:
code : {'neumonic': 'jal', 'opcode': '0b1101111', 'immediate': '111111111111111001000', 'rd': '00000', 'format': 'UJ', 'id': 22}
rd is : 0
imm is : ffffffc8
Execute stage:
operand1 is 00000005 operand2 is: 00000005
RZ is : 0000000a
Memory Access stage:
Register Update Stage:
RD: RY: 0 0000004c
cycle is : 414
Fetch stage:
The value of PC is : 00000010
The instruction in IR is : FFF60613
Decode stage:
code : {'neumonic': 'addi', 'opcode': '0b0010011', 'funct3': '0b000', 'rs1': '01100', 'rd': '01100', 'immediate': '111111111111', 'format': 'I', 'id': 9}
RA is : 00000005
rd is : 12
imm is : ffffffff
Execute stage:
operand1 is 00000005 operand2 is: ffffffff
RZ is : 00000004
Memory Access stage:
Register Update Stage:
RD: RY: 12 00000004
cycle is : 415
Fetch stage:
The value of PC is : 00000014
The instruction in IR is : 02060C63
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01100', 'rs2': '00000', 'immediate': '0000000111000', 'format': 'SB', 'id': 18}
RA is : 00000004
RB is : 00000000
imm is : 00000038
Execute stage:
operand1 is 00000004 operand2 is: 00000000
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 12 00000000
cycle is : 416
Fetch stage:
The value of PC is : 00000018
The instruction in IR is : 00000693
Decode stage:
code : {'neumonic': 'addi', 'opcode': '0b0010011', 'funct3': '0b000', 'rs1': '00000', 'rd': '01101', 'immediate': '000000000000', 'format': 'I', 'id': 9}
RA is : 00000000
rd is : 13
imm is : 00000000
Execute stage:
operand1 is 00000000 operand2 is: 00000000
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 417
Fetch stage:
The value of PC is : 0000001c
The instruction in IR is : 02C68663
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01101', 'rs2': '01100', 'immediate': '0000000101100', 'format': 'SB', 'id': 18}
RA is : 00000000
RB is : 00000004
imm is : 0000002c
Execute stage:
operand1 is 00000000 operand2 is: 00000004
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 418
Fetch stage:
The value of PC is : 00000020
The instruction in IR is : 01F69733
Decode stage:
code : {'neumonic': 'sll', 'opcode': '0b0110011', 'funct3': '0b001', 'funct7': '0b0000000', 'rs1': '01101', 'rs2': '11111', 'rd': '01110', 'format': 'R', 'id': 5}
RA is : 00000000
RB is : 00000002
rd is : 14
Execute stage:
operand1 is 00000000 operand2 is: 00000002
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 14 00000000
cycle is : 419
Fetch stage:
The value of PC is : 00000024
The instruction in IR is : 00B70733
Decode stage:
code : {'neumonic': 'add', 'opcode': '0b0110011', 'funct3': '0b000', 'funct7': '0b0000000', 'rs1': '01110', 'rs2': '01011', 'rd': '01110', 'format': 'R', 'id': 0}
RA is : 00000000
RB is : 10000000
rd is : 14
Execute stage:
operand1 is 00000000 operand2 is: 10000000
RZ is : 10000000
Memory Access stage:
Register Update Stage:
RD: RY: 14 10000000
cycle is : 420
Fetch stage:
The value of PC is : 00000028
The instruction in IR is : 00072783
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '01111', 'immediate': '000000000000', 'format': 'I', 'id': 14}
RA is : 10000000
rd is : 15
imm is : 00000000
Execute stage:
operand1 is 10000000 operand2 is: 00000000
RZ is : 10000000
Memory Access stage:
Register Update Stage:
RD: RY: 15 00000032
cycle is : 421
Fetch stage:
The value of PC is : 0000002c
The instruction in IR is : 00472803
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '10000', 'immediate': '000000000100', 'format': 'I', 'id': 14}
RA is : 10000000
rd is : 16
imm is : 00000004
Execute stage:
operand1 is 10000000 operand2 is: 00000004
RZ is : 10000004
Memory Access stage:
Register Update Stage:
RD: RY: 16 00000028
cycle is : 422
Fetch stage:
The value of PC is : 00000030
The instruction in IR is : 00168693
Decode stage:
code : {'neumonic': 'addi', 'opcode': '0b0010011', 'funct3': '0b000', 'rs1': '01101', 'rd': '01101', 'immediate': '000000000001', 'format': 'I', 'id': 9}
RA is : 00000000
rd is : 13
imm is : 00000001
Execute stage:
operand1 is 00000000 operand2 is: 00000001
RZ is : 00000001
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000001
cycle is : 423
Fetch stage:
The value of PC is : 00000034
The instruction in IR is : FF07C4E3
Decode stage:
code : {'neumonic': 'blt', 'opcode': '0b1100011', 'funct3': '0b100', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111101000', 'format': 'SB', 'id': 20}
RA is : 00000032
RB is : 00000028
imm is : ffffffe8
Execute stage:
operand1 is 00000032 operand2 is: 00000028
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 424
Fetch stage:
The value of PC is : 00000038
The instruction in IR is : FF0782E3
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111100100', 'format': 'SB', 'id': 18}
RA is : 00000032
RB is : 00000028
imm is : ffffffe4
Execute stage:
operand1 is 00000032 operand2 is: 00000028
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 425
Fetch stage:
The value of PC is : 0000003c
The instruction in IR is : 01072023
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '10000', 'immediate': '000000000000', 'format': 'S', 'id': 17}
RA is : 10000000
RB is : 00000028
imm is : 00000000
Execute stage:
operand1 is 10000000 operand2 is: 00000000
RZ is : 10000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 10000000
cycle is : 426
Fetch stage:
The value of PC is : 00000040
The instruction in IR is : 00F72223
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '01111', 'immediate': '000000000100', 'format': 'S', 'id': 17}
RA is : 10000000
RB is : 00000032
imm is : 00000004
Execute stage:
operand1 is 10000000 operand2 is: 00000004
RZ is : 10000004
Memory Access stage:
Register Update Stage:
RD: RY: 13 10000004
cycle is : 427
Fetch stage:
The value of PC is : 00000044
The instruction in IR is : FD9FF06F
Decode stage:
code : {'neumonic': 'jal', 'opcode': '0b1101111', 'immediate': '111111111111111011000', 'rd': '00000', 'format': 'UJ', 'id': 22}
rd is : 0
imm is : ffffffd8
Execute stage:
operand1 is 10000000 operand2 is: 00000032
RZ is : 10000032
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000048
cycle is : 428
Fetch stage:
The value of PC is : 0000001c
The instruction in IR is : 02C68663
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01101', 'rs2': '01100', 'immediate': '0000000101100', 'format': 'SB', 'id': 18}
RA is : 00000001
RB is : 00000004
imm is : 0000002c
Execute stage:
operand1 is 00000001 operand2 is: 00000004
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000000
cycle is : 429
Fetch stage:
The value of PC is : 00000020
The instruction in IR is : 01F69733
Decode stage:
code : {'neumonic': 'sll', 'opcode': '0b0110011', 'funct3': '0b001', 'funct7': '0b0000000', 'rs1': '01101', 'rs2': '11111', 'rd': '01110', 'format': 'R', 'id': 5}
RA is : 00000001
RB is : 00000002
rd is : 14
Execute stage:
operand1 is 00000001 operand2 is: 00000002
RZ is : 00000004
Memory Access stage:
Register Update Stage:
RD: RY: 14 00000004
cycle is : 430
Fetch stage:
The value of PC is : 00000024
The instruction in IR is : 00B70733
Decode stage:
code : {'neumonic': 'add', 'opcode': '0b0110011', 'funct3': '0b000', 'funct7': '0b0000000', 'rs1': '01110', 'rs2': '01011', 'rd': '01110', 'format': 'R', 'id': 0}
RA is : 00000004
RB is : 10000000
rd is : 14
Execute stage:
operand1 is 00000004 operand2 is: 10000000
RZ is : 10000004
Memory Access stage:
Register Update Stage:
RD: RY: 14 10000004
cycle is : 431
Fetch stage:
The value of PC is : 00000028
The instruction in IR is : 00072783
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '01111', 'immediate': '000000000000', 'format': 'I', 'id': 14}
RA is : 10000004
rd is : 15
imm is : 00000000
Execute stage:
operand1 is 10000004 operand2 is: 00000000
RZ is : 10000004
Memory Access stage:
Register Update Stage:
RD: RY: 15 00000032
cycle is : 432
Fetch stage:
The value of PC is : 0000002c
The instruction in IR is : 00472803
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '10000', 'immediate': '000000000100', 'format': 'I', 'id': 14}
RA is : 10000004
rd is : 16
imm is : 00000004
Execute stage:
operand1 is 10000004 operand2 is: 00000004
RZ is : 10000008
Memory Access stage:
Register Update Stage:
RD: RY: 16 0000001E
cycle is : 433
Fetch stage:
The value of PC is : 00000030
The instruction in IR is : 00168693
Decode stage:
code : {'neumonic': 'addi', 'opcode': '0b0010011', 'funct3': '0b000', 'rs1': '01101', 'rd': '01101', 'immediate': '000000000001', 'format': 'I', 'id': 9}
RA is : 00000001
rd is : 13
imm is : 00000001
Execute stage:
operand1 is 00000001 operand2 is: 00000001
RZ is : 00000002
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000002
cycle is : 434
Fetch stage:
The value of PC is : 00000034
The instruction in IR is : FF07C4E3
Decode stage:
code : {'neumonic': 'blt', 'opcode': '0b1100011', 'funct3': '0b100', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111101000', 'format': 'SB', 'id': 20}
RA is : 00000032
RB is : 0000001E
imm is : ffffffe8
Execute stage:
operand1 is 00000032 operand2 is: 0000001E
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 435
Fetch stage:
The value of PC is : 00000038
The instruction in IR is : FF0782E3
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111100100', 'format': 'SB', 'id': 18}
RA is : 00000032
RB is : 0000001E
imm is : ffffffe4
Execute stage:
operand1 is 00000032 operand2 is: 0000001E
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 436
Fetch stage:
The value of PC is : 0000003c
The instruction in IR is : 01072023
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '10000', 'immediate': '000000000000', 'format': 'S', 'id': 17}
RA is : 10000004
RB is : 0000001E
imm is : 00000000
Execute stage:
operand1 is 10000004 operand2 is: 00000000
RZ is : 10000004
Memory Access stage:
Register Update Stage:
RD: RY: 13 10000004
cycle is : 437
Fetch stage:
The value of PC is : 00000040
The instruction in IR is : 00F72223
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '01111', 'immediate': '000000000100', 'format': 'S', 'id': 17}
RA is : 10000004
RB is : 00000032
imm is : 00000004
Execute stage:
operand1 is 10000004 operand2 is: 00000004
RZ is : 10000008
Memory Access stage:
Register Update Stage:
RD: RY: 13 10000008
cycle is : 438
Fetch stage:
The value of PC is : 00000044
The instruction in IR is : FD9FF06F
Decode stage:
code : {'neumonic': 'jal', 'opcode': '0b1101111', 'immediate': '111111111111111011000', 'rd': '00000', 'format': 'UJ', 'id': 22}
rd is : 0
imm is : ffffffd8
Execute stage:
operand1 is 10000004 operand2 is: 00000032
RZ is : 10000036
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000048
cycle is : 439
Fetch stage:
The value of PC is : 0000001c
The instruction in IR is : 02C68663
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01101', 'rs2': '01100', 'immediate': '0000000101100', 'format': 'SB', 'id': 18}
RA is : 00000002
RB is : 00000004
imm is : 0000002c
Execute stage:
operand1 is 00000002 operand2 is: 00000004
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000000
cycle is : 440
Fetch stage:
The value of PC is : 00000020
The instruction in IR is : 01F69733
Decode stage:
code : {'neumonic': 'sll', 'opcode': '0b0110011', 'funct3': '0b001', 'funct7': '0b0000000', 'rs1': '01101', 'rs2': '11111', 'rd': '01110', 'format': 'R', 'id': 5}
RA is : 00000002
RB is : 00000002
rd is : 14
Execute stage:
operand1 is 00000002 operand2 is: 00000002
RZ is : 00000008
Memory Access stage:
Register Update Stage:
RD: RY: 14 00000008
cycle is : 441
Fetch stage:
The value of PC is : 00000024
The instruction in IR is : 00B70733
Decode stage:
code : {'neumonic': 'add', 'opcode': '0b0110011', 'funct3': '0b000', 'funct7': '0b0000000', 'rs1': '01110', 'rs2': '01011', 'rd': '01110', 'format': 'R', 'id': 0}
RA is : 00000008
RB is : 10000000
rd is : 14
Execute stage:
operand1 is 00000008 operand2 is: 10000000
RZ is : 10000008
Memory Access stage:
Register Update Stage:
RD: RY: 14 10000008
cycle is : 442
Fetch stage:
The value of PC is : 00000028
The instruction in IR is : 00072783
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '01111', 'immediate': '000000000000', 'format': 'I', 'id': 14}
RA is : 10000008
rd is : 15
imm is : 00000000
Execute stage:
operand1 is 10000008 operand2 is: 00000000
RZ is : 10000008
Memory Access stage:
Register Update Stage:
RD: RY: 15 00000032
cycle is : 443
Fetch stage:
The value of PC is : 0000002c
The instruction in IR is : 00472803
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '10000', 'immediate': '000000000100', 'format': 'I', 'id': 14}
RA is : 10000008
rd is : 16
imm is : 00000004
Execute stage:
operand1 is 10000008 operand2 is: 00000004
RZ is : 1000000c
Memory Access stage:
Register Update Stage:
RD: RY: 16 00000014
cycle is : 444
Fetch stage:
The value of PC is : 00000030
The instruction in IR is : 00168693
Decode stage:
code : {'neumonic': 'addi', 'opcode': '0b0010011', 'funct3': '0b000', 'rs1': '01101', 'rd': '01101', 'immediate': '000000000001', 'format': 'I', 'id': 9}
RA is : 00000002
rd is : 13
imm is : 00000001
Execute stage:
operand1 is 00000002 operand2 is: 00000001
RZ is : 00000003
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000003
cycle is : 445
Fetch stage:
The value of PC is : 00000034
The instruction in IR is : FF07C4E3
Decode stage:
code : {'neumonic': 'blt', 'opcode': '0b1100011', 'funct3': '0b100', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111101000', 'format': 'SB', 'id': 20}
RA is : 00000032
RB is : 00000014
imm is : ffffffe8
Execute stage:
operand1 is 00000032 operand2 is: 00000014
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 446
Fetch stage:
The value of PC is : 00000038
The instruction in IR is : FF0782E3
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111100100', 'format': 'SB', 'id': 18}
RA is : 00000032
RB is : 00000014
imm is : ffffffe4
Execute stage:
operand1 is 00000032 operand2 is: 00000014
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 447
Fetch stage:
The value of PC is : 0000003c
The instruction in IR is : 01072023
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '10000', 'immediate': '000000000000', 'format': 'S', 'id': 17}
RA is : 10000008
RB is : 00000014
imm is : 00000000
Execute stage:
operand1 is 10000008 operand2 is: 00000000
RZ is : 10000008
Memory Access stage:
Register Update Stage:
RD: RY: 13 10000008
cycle is : 448
Fetch stage:
The value of PC is : 00000040
The instruction in IR is : 00F72223
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '01111', 'immediate': '000000000100', 'format': 'S', 'id': 17}
RA is : 10000008
RB is : 00000032
imm is : 00000004
Execute stage:
operand1 is 10000008 operand2 is: 00000004
RZ is : 1000000c
Memory Access stage:
Register Update Stage:
RD: RY: 13 1000000c
cycle is : 449
Fetch stage:
The value of PC is : 00000044
The instruction in IR is : FD9FF06F
Decode stage:
code : {'neumonic': 'jal', 'opcode': '0b1101111', 'immediate': '111111111111111011000', 'rd': '00000', 'format': 'UJ', 'id': 22}
rd is : 0
imm is : ffffffd8
Execute stage:
operand1 is 10000008 operand2 is: 00000032
RZ is : 1000003a
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000048
cycle is : 450
Fetch stage:
The value of PC is : 0000001c
The instruction in IR is : 02C68663
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01101', 'rs2': '01100', 'immediate': '0000000101100', 'format': 'SB', 'id': 18}
RA is : 00000003
RB is : 00000004
imm is : 0000002c
Execute stage:
operand1 is 00000003 operand2 is: 00000004
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000000
cycle is : 451
Fetch stage:
The value of PC is : 00000020
The instruction in IR is : 01F69733
Decode stage:
code : {'neumonic': 'sll', 'opcode': '0b0110011', 'funct3': '0b001', 'funct7': '0b0000000', 'rs1': '01101', 'rs2': '11111', 'rd': '01110', 'format': 'R', 'id': 5}
RA is : 00000003
RB is : 00000002
rd is : 14
Execute stage:
operand1 is 00000003 operand2 is: 00000002
RZ is : 0000000c
Memory Access stage:
Register Update Stage:
RD: RY: 14 0000000c
cycle is : 452
Fetch stage:
The value of PC is : 00000024
The instruction in IR is : 00B70733
Decode stage:
code : {'neumonic': 'add', 'opcode': '0b0110011', 'funct3': '0b000', 'funct7': '0b0000000', 'rs1': '01110', 'rs2': '01011', 'rd': '01110', 'format': 'R', 'id': 0}
RA is : 0000000c
RB is : 10000000
rd is : 14
Execute stage:
operand1 is 0000000c operand2 is: 10000000
RZ is : 1000000c
Memory Access stage:
Register Update Stage:
RD: RY: 14 1000000c
cycle is : 453
Fetch stage:
The value of PC is : 00000028
The instruction in IR is : 00072783
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '01111', 'immediate': '000000000000', 'format': 'I', 'id': 14}
RA is : 1000000c
rd is : 15
imm is : 00000000
Execute stage:
operand1 is 1000000c operand2 is: 00000000
RZ is : 1000000c
Memory Access stage:
Register Update Stage:
RD: RY: 15 00000032
cycle is : 454
Fetch stage:
The value of PC is : 0000002c
The instruction in IR is : 00472803
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '10000', 'immediate': '000000000100', 'format': 'I', 'id': 14}
RA is : 1000000c
rd is : 16
imm is : 00000004
Execute stage:
operand1 is 1000000c operand2 is: 00000004
RZ is : 10000010
Memory Access stage:
Register Update Stage:
RD: RY: 16 0000000a
cycle is : 455
Fetch stage:
The value of PC is : 00000030
The instruction in IR is : 00168693
Decode stage:
code : {'neumonic': 'addi', 'opcode': '0b0010011', 'funct3': '0b000', 'rs1': '01101', 'rd': '01101', 'immediate': '000000000001', 'format': 'I', 'id': 9}
RA is : 00000003
rd is : 13
imm is : 00000001
Execute stage:
operand1 is 00000003 operand2 is: 00000001
RZ is : 00000004
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000004
cycle is : 456
Fetch stage:
The value of PC is : 00000034
The instruction in IR is : FF07C4E3
Decode stage:
code : {'neumonic': 'blt', 'opcode': '0b1100011', 'funct3': '0b100', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111101000', 'format': 'SB', 'id': 20}
RA is : 00000032
RB is : 0000000a
imm is : ffffffe8
Execute stage:
operand1 is 00000032 operand2 is: 0000000a
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 457
Fetch stage:
The value of PC is : 00000038
The instruction in IR is : FF0782E3
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111100100', 'format': 'SB', 'id': 18}
RA is : 00000032
RB is : 0000000a
imm is : ffffffe4
Execute stage:
operand1 is 00000032 operand2 is: 0000000a
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 458
Fetch stage:
The value of PC is : 0000003c
The instruction in IR is : 01072023
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '10000', 'immediate': '000000000000', 'format': 'S', 'id': 17}
RA is : 1000000c
RB is : 0000000a
imm is : 00000000
Execute stage:
operand1 is 1000000c operand2 is: 00000000
RZ is : 1000000c
Memory Access stage:
Register Update Stage:
RD: RY: 13 1000000c
cycle is : 459
Fetch stage:
The value of PC is : 00000040
The instruction in IR is : 00F72223
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '01111', 'immediate': '000000000100', 'format': 'S', 'id': 17}
RA is : 1000000c
RB is : 00000032
imm is : 00000004
Execute stage:
operand1 is 1000000c operand2 is: 00000004
RZ is : 10000010
Memory Access stage:
Register Update Stage:
RD: RY: 13 10000010
cycle is : 460
Fetch stage:
The value of PC is : 00000044
The instruction in IR is : FD9FF06F
Decode stage:
code : {'neumonic': 'jal', 'opcode': '0b1101111', 'immediate': '111111111111111011000', 'rd': '00000', 'format': 'UJ', 'id': 22}
rd is : 0
imm is : ffffffd8
Execute stage:
operand1 is 1000000c operand2 is: 00000032
RZ is : 1000003e
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000048
cycle is : 461
Fetch stage:
The value of PC is : 0000001c
The instruction in IR is : 02C68663
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01101', 'rs2': '01100', 'immediate': '0000000101100', 'format': 'SB', 'id': 18}
RA is : 00000004
RB is : 00000004
imm is : 0000002c
Execute stage:
operand1 is 00000004 operand2 is: 00000004
RZ is : 00000001
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000001
cycle is : 462
Fetch stage:
The value of PC is : 00000048
The instruction in IR is : FC9FF06F
Decode stage:
code : {'neumonic': 'jal', 'opcode': '0b1101111', 'immediate': '111111111111111001000', 'rd': '00000', 'format': 'UJ', 'id': 22}
rd is : 0
imm is : ffffffc8
Execute stage:
operand1 is 00000004 operand2 is: 00000004
RZ is : 00000008
Memory Access stage:
Register Update Stage:
RD: RY: 0 0000004c
cycle is : 463
Fetch stage:
The value of PC is : 00000010
The instruction in IR is : FFF60613
Decode stage:
code : {'neumonic': 'addi', 'opcode': '0b0010011', 'funct3': '0b000', 'rs1': '01100', 'rd': '01100', 'immediate': '111111111111', 'format': 'I', 'id': 9}
RA is : 00000004
rd is : 12
imm is : ffffffff
Execute stage:
operand1 is 00000004 operand2 is: ffffffff
RZ is : 00000003
Memory Access stage:
Register Update Stage:
RD: RY: 12 00000003
cycle is : 464
Fetch stage:
The value of PC is : 00000014
The instruction in IR is : 02060C63
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01100', 'rs2': '00000', 'immediate': '0000000111000', 'format': 'SB', 'id': 18}
RA is : 00000003
RB is : 00000000
imm is : 00000038
Execute stage:
operand1 is 00000003 operand2 is: 00000000
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 12 00000000
cycle is : 465
Fetch stage:
The value of PC is : 00000018
The instruction in IR is : 00000693
Decode stage:
code : {'neumonic': 'addi', 'opcode': '0b0010011', 'funct3': '0b000', 'rs1': '00000', 'rd': '01101', 'immediate': '000000000000', 'format': 'I', 'id': 9}
RA is : 00000000
rd is : 13
imm is : 00000000
Execute stage:
operand1 is 00000000 operand2 is: 00000000
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 466
Fetch stage:
The value of PC is : 0000001c
The instruction in IR is : 02C68663
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01101', 'rs2': '01100', 'immediate': '0000000101100', 'format': 'SB', 'id': 18}
RA is : 00000000
RB is : 00000003
imm is : 0000002c
Execute stage:
operand1 is 00000000 operand2 is: 00000003
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 467
Fetch stage:
The value of PC is : 00000020
The instruction in IR is : 01F69733
Decode stage:
code : {'neumonic': 'sll', 'opcode': '0b0110011', 'funct3': '0b001', 'funct7': '0b0000000', 'rs1': '01101', 'rs2': '11111', 'rd': '01110', 'format': 'R', 'id': 5}
RA is : 00000000
RB is : 00000002
rd is : 14
Execute stage:
operand1 is 00000000 operand2 is: 00000002
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 14 00000000
cycle is : 468
Fetch stage:
The value of PC is : 00000024
The instruction in IR is : 00B70733
Decode stage:
code : {'neumonic': 'add', 'opcode': '0b0110011', 'funct3': '0b000', 'funct7': '0b0000000', 'rs1': '01110', 'rs2': '01011', 'rd': '01110', 'format': 'R', 'id': 0}
RA is : 00000000
RB is : 10000000
rd is : 14
Execute stage:
operand1 is 00000000 operand2 is: 10000000
RZ is : 10000000
Memory Access stage:
Register Update Stage:
RD: RY: 14 10000000
cycle is : 469
Fetch stage:
The value of PC is : 00000028
The instruction in IR is : 00072783
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '01111', 'immediate': '000000000000', 'format': 'I', 'id': 14}
RA is : 10000000
rd is : 15
imm is : 00000000
Execute stage:
operand1 is 10000000 operand2 is: 00000000
RZ is : 10000000
Memory Access stage:
Register Update Stage:
RD: RY: 15 00000028
cycle is : 470
Fetch stage:
The value of PC is : 0000002c
The instruction in IR is : 00472803
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '10000', 'immediate': '000000000100', 'format': 'I', 'id': 14}
RA is : 10000000
rd is : 16
imm is : 00000004
Execute stage:
operand1 is 10000000 operand2 is: 00000004
RZ is : 10000004
Memory Access stage:
Register Update Stage:
RD: RY: 16 0000001E
cycle is : 471
Fetch stage:
The value of PC is : 00000030
The instruction in IR is : 00168693
Decode stage:
code : {'neumonic': 'addi', 'opcode': '0b0010011', 'funct3': '0b000', 'rs1': '01101', 'rd': '01101', 'immediate': '000000000001', 'format': 'I', 'id': 9}
RA is : 00000000
rd is : 13
imm is : 00000001
Execute stage:
operand1 is 00000000 operand2 is: 00000001
RZ is : 00000001
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000001
cycle is : 472
Fetch stage:
The value of PC is : 00000034
The instruction in IR is : FF07C4E3
Decode stage:
code : {'neumonic': 'blt', 'opcode': '0b1100011', 'funct3': '0b100', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111101000', 'format': 'SB', 'id': 20}
RA is : 00000028
RB is : 0000001E
imm is : ffffffe8
Execute stage:
operand1 is 00000028 operand2 is: 0000001E
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 473
Fetch stage:
The value of PC is : 00000038
The instruction in IR is : FF0782E3
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111100100', 'format': 'SB', 'id': 18}
RA is : 00000028
RB is : 0000001E
imm is : ffffffe4
Execute stage:
operand1 is 00000028 operand2 is: 0000001E
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 474
Fetch stage:
The value of PC is : 0000003c
The instruction in IR is : 01072023
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '10000', 'immediate': '000000000000', 'format': 'S', 'id': 17}
RA is : 10000000
RB is : 0000001E
imm is : 00000000
Execute stage:
operand1 is 10000000 operand2 is: 00000000
RZ is : 10000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 10000000
cycle is : 475
Fetch stage:
The value of PC is : 00000040
The instruction in IR is : 00F72223
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '01111', 'immediate': '000000000100', 'format': 'S', 'id': 17}
RA is : 10000000
RB is : 00000028
imm is : 00000004
Execute stage:
operand1 is 10000000 operand2 is: 00000004
RZ is : 10000004
Memory Access stage:
Register Update Stage:
RD: RY: 13 10000004
cycle is : 476
Fetch stage:
The value of PC is : 00000044
The instruction in IR is : FD9FF06F
Decode stage:
code : {'neumonic': 'jal', 'opcode': '0b1101111', 'immediate': '111111111111111011000', 'rd': '00000', 'format': 'UJ', 'id': 22}
rd is : 0
imm is : ffffffd8
Execute stage:
operand1 is 10000000 operand2 is: 00000028
RZ is : 10000028
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000048
cycle is : 477
Fetch stage:
The value of PC is : 0000001c
The instruction in IR is : 02C68663
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01101', 'rs2': '01100', 'immediate': '0000000101100', 'format': 'SB', 'id': 18}
RA is : 00000001
RB is : 00000003
imm is : 0000002c
Execute stage:
operand1 is 00000001 operand2 is: 00000003
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000000
cycle is : 478
Fetch stage:
The value of PC is : 00000020
The instruction in IR is : 01F69733
Decode stage:
code : {'neumonic': 'sll', 'opcode': '0b0110011', 'funct3': '0b001', 'funct7': '0b0000000', 'rs1': '01101', 'rs2': '11111', 'rd': '01110', 'format': 'R', 'id': 5}
RA is : 00000001
RB is : 00000002
rd is : 14
Execute stage:
operand1 is 00000001 operand2 is: 00000002
RZ is : 00000004
Memory Access stage:
Register Update Stage:
RD: RY: 14 00000004
cycle is : 479
Fetch stage:
The value of PC is : 00000024
The instruction in IR is : 00B70733
Decode stage:
code : {'neumonic': 'add', 'opcode': '0b0110011', 'funct3': '0b000', 'funct7': '0b0000000', 'rs1': '01110', 'rs2': '01011', 'rd': '01110', 'format': 'R', 'id': 0}
RA is : 00000004
RB is : 10000000
rd is : 14
Execute stage:
operand1 is 00000004 operand2 is: 10000000
RZ is : 10000004
Memory Access stage:
Register Update Stage:
RD: RY: 14 10000004
cycle is : 480
Fetch stage:
The value of PC is : 00000028
The instruction in IR is : 00072783
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '01111', 'immediate': '000000000000', 'format': 'I', 'id': 14}
RA is : 10000004
rd is : 15
imm is : 00000000
Execute stage:
operand1 is 10000004 operand2 is: 00000000
RZ is : 10000004
Memory Access stage:
Register Update Stage:
RD: RY: 15 00000028
cycle is : 481
Fetch stage:
The value of PC is : 0000002c
The instruction in IR is : 00472803
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '10000', 'immediate': '000000000100', 'format': 'I', 'id': 14}
RA is : 10000004
rd is : 16
imm is : 00000004
Execute stage:
operand1 is 10000004 operand2 is: 00000004
RZ is : 10000008
Memory Access stage:
Register Update Stage:
RD: RY: 16 00000014
cycle is : 482
Fetch stage:
The value of PC is : 00000030
The instruction in IR is : 00168693
Decode stage:
code : {'neumonic': 'addi', 'opcode': '0b0010011', 'funct3': '0b000', 'rs1': '01101', 'rd': '01101', 'immediate': '000000000001', 'format': 'I', 'id': 9}
RA is : 00000001
rd is : 13
imm is : 00000001
Execute stage:
operand1 is 00000001 operand2 is: 00000001
RZ is : 00000002
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000002
cycle is : 483
Fetch stage:
The value of PC is : 00000034
The instruction in IR is : FF07C4E3
Decode stage:
code : {'neumonic': 'blt', 'opcode': '0b1100011', 'funct3': '0b100', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111101000', 'format': 'SB', 'id': 20}
RA is : 00000028
RB is : 00000014
imm is : ffffffe8
Execute stage:
operand1 is 00000028 operand2 is: 00000014
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 484
Fetch stage:
The value of PC is : 00000038
The instruction in IR is : FF0782E3
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111100100', 'format': 'SB', 'id': 18}
RA is : 00000028
RB is : 00000014
imm is : ffffffe4
Execute stage:
operand1 is 00000028 operand2 is: 00000014
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 485
Fetch stage:
The value of PC is : 0000003c
The instruction in IR is : 01072023
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '10000', 'immediate': '000000000000', 'format': 'S', 'id': 17}
RA is : 10000004
RB is : 00000014
imm is : 00000000
Execute stage:
operand1 is 10000004 operand2 is: 00000000
RZ is : 10000004
Memory Access stage:
Register Update Stage:
RD: RY: 13 10000004
cycle is : 486
Fetch stage:
The value of PC is : 00000040
The instruction in IR is : 00F72223
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '01111', 'immediate': '000000000100', 'format': 'S', 'id': 17}
RA is : 10000004
RB is : 00000028
imm is : 00000004
Execute stage:
operand1 is 10000004 operand2 is: 00000004
RZ is : 10000008
Memory Access stage:
Register Update Stage:
RD: RY: 13 10000008
cycle is : 487
Fetch stage:
The value of PC is : 00000044
The instruction in IR is : FD9FF06F
Decode stage:
code : {'neumonic': 'jal', 'opcode': '0b1101111', 'immediate': '111111111111111011000', 'rd': '00000', 'format': 'UJ', 'id': 22}
rd is : 0
imm is : ffffffd8
Execute stage:
operand1 is 10000004 operand2 is: 00000028
RZ is : 1000002c
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000048
cycle is : 488
Fetch stage:
The value of PC is : 0000001c
The instruction in IR is : 02C68663
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01101', 'rs2': '01100', 'immediate': '0000000101100', 'format': 'SB', 'id': 18}
RA is : 00000002
RB is : 00000003
imm is : 0000002c
Execute stage:
operand1 is 00000002 operand2 is: 00000003
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000000
cycle is : 489
Fetch stage:
The value of PC is : 00000020
The instruction in IR is : 01F69733
Decode stage:
code : {'neumonic': 'sll', 'opcode': '0b0110011', 'funct3': '0b001', 'funct7': '0b0000000', 'rs1': '01101', 'rs2': '11111', 'rd': '01110', 'format': 'R', 'id': 5}
RA is : 00000002
RB is : 00000002
rd is : 14
Execute stage:
operand1 is 00000002 operand2 is: 00000002
RZ is : 00000008
Memory Access stage:
Register Update Stage:
RD: RY: 14 00000008
cycle is : 490
Fetch stage:
The value of PC is : 00000024
The instruction in IR is : 00B70733
Decode stage:
code : {'neumonic': 'add', 'opcode': '0b0110011', 'funct3': '0b000', 'funct7': '0b0000000', 'rs1': '01110', 'rs2': '01011', 'rd': '01110', 'format': 'R', 'id': 0}
RA is : 00000008
RB is : 10000000
rd is : 14
Execute stage:
operand1 is 00000008 operand2 is: 10000000
RZ is : 10000008
Memory Access stage:
Register Update Stage:
RD: RY: 14 10000008
cycle is : 491
Fetch stage:
The value of PC is : 00000028
The instruction in IR is : 00072783
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '01111', 'immediate': '000000000000', 'format': 'I', 'id': 14}
RA is : 10000008
rd is : 15
imm is : 00000000
Execute stage:
operand1 is 10000008 operand2 is: 00000000
RZ is : 10000008
Memory Access stage:
Register Update Stage:
RD: RY: 15 00000028
cycle is : 492
Fetch stage:
The value of PC is : 0000002c
The instruction in IR is : 00472803
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '10000', 'immediate': '000000000100', 'format': 'I', 'id': 14}
RA is : 10000008
rd is : 16
imm is : 00000004
Execute stage:
operand1 is 10000008 operand2 is: 00000004
RZ is : 1000000c
Memory Access stage:
Register Update Stage:
RD: RY: 16 0000000a
cycle is : 493
Fetch stage:
The value of PC is : 00000030
The instruction in IR is : 00168693
Decode stage:
code : {'neumonic': 'addi', 'opcode': '0b0010011', 'funct3': '0b000', 'rs1': '01101', 'rd': '01101', 'immediate': '000000000001', 'format': 'I', 'id': 9}
RA is : 00000002
rd is : 13
imm is : 00000001
Execute stage:
operand1 is 00000002 operand2 is: 00000001
RZ is : 00000003
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000003
cycle is : 494
Fetch stage:
The value of PC is : 00000034
The instruction in IR is : FF07C4E3
Decode stage:
code : {'neumonic': 'blt', 'opcode': '0b1100011', 'funct3': '0b100', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111101000', 'format': 'SB', 'id': 20}
RA is : 00000028
RB is : 0000000a
imm is : ffffffe8
Execute stage:
operand1 is 00000028 operand2 is: 0000000a
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 495
Fetch stage:
The value of PC is : 00000038
The instruction in IR is : FF0782E3
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111100100', 'format': 'SB', 'id': 18}
RA is : 00000028
RB is : 0000000a
imm is : ffffffe4
Execute stage:
operand1 is 00000028 operand2 is: 0000000a
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 496
Fetch stage:
The value of PC is : 0000003c
The instruction in IR is : 01072023
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '10000', 'immediate': '000000000000', 'format': 'S', 'id': 17}
RA is : 10000008
RB is : 0000000a
imm is : 00000000
Execute stage:
operand1 is 10000008 operand2 is: 00000000
RZ is : 10000008
Memory Access stage:
Register Update Stage:
RD: RY: 13 10000008
cycle is : 497
Fetch stage:
The value of PC is : 00000040
The instruction in IR is : 00F72223
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '01111', 'immediate': '000000000100', 'format': 'S', 'id': 17}
RA is : 10000008
RB is : 00000028
imm is : 00000004
Execute stage:
operand1 is 10000008 operand2 is: 00000004
RZ is : 1000000c
Memory Access stage:
Register Update Stage:
RD: RY: 13 1000000c
cycle is : 498
Fetch stage:
The value of PC is : 00000044
The instruction in IR is : FD9FF06F
Decode stage:
code : {'neumonic': 'jal', 'opcode': '0b1101111', 'immediate': '111111111111111011000', 'rd': '00000', 'format': 'UJ', 'id': 22}
rd is : 0
imm is : ffffffd8
Execute stage:
operand1 is 10000008 operand2 is: 00000028
RZ is : 10000030
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000048
cycle is : 499
Fetch stage:
The value of PC is : 0000001c
The instruction in IR is : 02C68663
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01101', 'rs2': '01100', 'immediate': '0000000101100', 'format': 'SB', 'id': 18}
RA is : 00000003
RB is : 00000003
imm is : 0000002c
Execute stage:
operand1 is 00000003 operand2 is: 00000003
RZ is : 00000001
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000001
cycle is : 500
Fetch stage:
The value of PC is : 00000048
The instruction in IR is : FC9FF06F
Decode stage:
code : {'neumonic': 'jal', 'opcode': '0b1101111', 'immediate': '111111111111111001000', 'rd': '00000', 'format': 'UJ', 'id': 22}
rd is : 0
imm is : ffffffc8
Execute stage:
operand1 is 00000003 operand2 is: 00000003
RZ is : 00000006
Memory Access stage:
Register Update Stage:
RD: RY: 0 0000004c
cycle is : 501
Fetch stage:
The value of PC is : 00000010
The instruction in IR is : FFF60613
Decode stage:
code : {'neumonic': 'addi', 'opcode': '0b0010011', 'funct3': '0b000', 'rs1': '01100', 'rd': '01100', 'immediate': '111111111111', 'format': 'I', 'id': 9}
RA is : 00000003
rd is : 12
imm is : ffffffff
Execute stage:
operand1 is 00000003 operand2 is: ffffffff
RZ is : 00000002
Memory Access stage:
Register Update Stage:
RD: RY: 12 00000002
cycle is : 502
Fetch stage:
The value of PC is : 00000014
The instruction in IR is : 02060C63
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01100', 'rs2': '00000', 'immediate': '0000000111000', 'format': 'SB', 'id': 18}
RA is : 00000002
RB is : 00000000
imm is : 00000038
Execute stage:
operand1 is 00000002 operand2 is: 00000000
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 12 00000000
cycle is : 503
Fetch stage:
The value of PC is : 00000018
The instruction in IR is : 00000693
Decode stage:
code : {'neumonic': 'addi', 'opcode': '0b0010011', 'funct3': '0b000', 'rs1': '00000', 'rd': '01101', 'immediate': '000000000000', 'format': 'I', 'id': 9}
RA is : 00000000
rd is : 13
imm is : 00000000
Execute stage:
operand1 is 00000000 operand2 is: 00000000
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 504
Fetch stage:
The value of PC is : 0000001c
The instruction in IR is : 02C68663
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01101', 'rs2': '01100', 'immediate': '0000000101100', 'format': 'SB', 'id': 18}
RA is : 00000000
RB is : 00000002
imm is : 0000002c
Execute stage:
operand1 is 00000000 operand2 is: 00000002
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 505
Fetch stage:
The value of PC is : 00000020
The instruction in IR is : 01F69733
Decode stage:
code : {'neumonic': 'sll', 'opcode': '0b0110011', 'funct3': '0b001', 'funct7': '0b0000000', 'rs1': '01101', 'rs2': '11111', 'rd': '01110', 'format': 'R', 'id': 5}
RA is : 00000000
RB is : 00000002
rd is : 14
Execute stage:
operand1 is 00000000 operand2 is: 00000002
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 14 00000000
cycle is : 506
Fetch stage:
The value of PC is : 00000024
The instruction in IR is : 00B70733
Decode stage:
code : {'neumonic': 'add', 'opcode': '0b0110011', 'funct3': '0b000', 'funct7': '0b0000000', 'rs1': '01110', 'rs2': '01011', 'rd': '01110', 'format': 'R', 'id': 0}
RA is : 00000000
RB is : 10000000
rd is : 14
Execute stage:
operand1 is 00000000 operand2 is: 10000000
RZ is : 10000000
Memory Access stage:
Register Update Stage:
RD: RY: 14 10000000
cycle is : 507
Fetch stage:
The value of PC is : 00000028
The instruction in IR is : 00072783
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '01111', 'immediate': '000000000000', 'format': 'I', 'id': 14}
RA is : 10000000
rd is : 15
imm is : 00000000
Execute stage:
operand1 is 10000000 operand2 is: 00000000
RZ is : 10000000
Memory Access stage:
Register Update Stage:
RD: RY: 15 0000001E
cycle is : 508
Fetch stage:
The value of PC is : 0000002c
The instruction in IR is : 00472803
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '10000', 'immediate': '000000000100', 'format': 'I', 'id': 14}
RA is : 10000000
rd is : 16
imm is : 00000004
Execute stage:
operand1 is 10000000 operand2 is: 00000004
RZ is : 10000004
Memory Access stage:
Register Update Stage:
RD: RY: 16 00000014
cycle is : 509
Fetch stage:
The value of PC is : 00000030
The instruction in IR is : 00168693
Decode stage:
code : {'neumonic': 'addi', 'opcode': '0b0010011', 'funct3': '0b000', 'rs1': '01101', 'rd': '01101', 'immediate': '000000000001', 'format': 'I', 'id': 9}
RA is : 00000000
rd is : 13
imm is : 00000001
Execute stage:
operand1 is 00000000 operand2 is: 00000001
RZ is : 00000001
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000001
cycle is : 510
Fetch stage:
The value of PC is : 00000034
The instruction in IR is : FF07C4E3
Decode stage:
code : {'neumonic': 'blt', 'opcode': '0b1100011', 'funct3': '0b100', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111101000', 'format': 'SB', 'id': 20}
RA is : 0000001E
RB is : 00000014
imm is : ffffffe8
Execute stage:
operand1 is 0000001E operand2 is: 00000014
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 511
Fetch stage:
The value of PC is : 00000038
The instruction in IR is : FF0782E3
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111100100', 'format': 'SB', 'id': 18}
RA is : 0000001E
RB is : 00000014
imm is : ffffffe4
Execute stage:
operand1 is 0000001E operand2 is: 00000014
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 512
Fetch stage:
The value of PC is : 0000003c
The instruction in IR is : 01072023
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '10000', 'immediate': '000000000000', 'format': 'S', 'id': 17}
RA is : 10000000
RB is : 00000014
imm is : 00000000
Execute stage:
operand1 is 10000000 operand2 is: 00000000
RZ is : 10000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 10000000
cycle is : 513
Fetch stage:
The value of PC is : 00000040
The instruction in IR is : 00F72223
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '01111', 'immediate': '000000000100', 'format': 'S', 'id': 17}
RA is : 10000000
RB is : 0000001E
imm is : 00000004
Execute stage:
operand1 is 10000000 operand2 is: 00000004
RZ is : 10000004
Memory Access stage:
Register Update Stage:
RD: RY: 13 10000004
cycle is : 514
Fetch stage:
The value of PC is : 00000044
The instruction in IR is : FD9FF06F
Decode stage:
code : {'neumonic': 'jal', 'opcode': '0b1101111', 'immediate': '111111111111111011000', 'rd': '00000', 'format': 'UJ', 'id': 22}
rd is : 0
imm is : ffffffd8
Execute stage:
operand1 is 10000000 operand2 is: 0000001E
RZ is : 1000001e
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000048
cycle is : 515
Fetch stage:
The value of PC is : 0000001c
The instruction in IR is : 02C68663
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01101', 'rs2': '01100', 'immediate': '0000000101100', 'format': 'SB', 'id': 18}
RA is : 00000001
RB is : 00000002
imm is : 0000002c
Execute stage:
operand1 is 00000001 operand2 is: 00000002
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000000
cycle is : 516
Fetch stage:
The value of PC is : 00000020
The instruction in IR is : 01F69733
Decode stage:
code : {'neumonic': 'sll', 'opcode': '0b0110011', 'funct3': '0b001', 'funct7': '0b0000000', 'rs1': '01101', 'rs2': '11111', 'rd': '01110', 'format': 'R', 'id': 5}
RA is : 00000001
RB is : 00000002
rd is : 14
Execute stage:
operand1 is 00000001 operand2 is: 00000002
RZ is : 00000004
Memory Access stage:
Register Update Stage:
RD: RY: 14 00000004
cycle is : 517
Fetch stage:
The value of PC is : 00000024
The instruction in IR is : 00B70733
Decode stage:
code : {'neumonic': 'add', 'opcode': '0b0110011', 'funct3': '0b000', 'funct7': '0b0000000', 'rs1': '01110', 'rs2': '01011', 'rd': '01110', 'format': 'R', 'id': 0}
RA is : 00000004
RB is : 10000000
rd is : 14
Execute stage:
operand1 is 00000004 operand2 is: 10000000
RZ is : 10000004
Memory Access stage:
Register Update Stage:
RD: RY: 14 10000004
cycle is : 518
Fetch stage:
The value of PC is : 00000028
The instruction in IR is : 00072783
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '01111', 'immediate': '000000000000', 'format': 'I', 'id': 14}
RA is : 10000004
rd is : 15
imm is : 00000000
Execute stage:
operand1 is 10000004 operand2 is: 00000000
RZ is : 10000004
Memory Access stage:
Register Update Stage:
RD: RY: 15 0000001E
cycle is : 519
Fetch stage:
The value of PC is : 0000002c
The instruction in IR is : 00472803
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '10000', 'immediate': '000000000100', 'format': 'I', 'id': 14}
RA is : 10000004
rd is : 16
imm is : 00000004
Execute stage:
operand1 is 10000004 operand2 is: 00000004
RZ is : 10000008
Memory Access stage:
Register Update Stage:
RD: RY: 16 0000000a
cycle is : 520
Fetch stage:
The value of PC is : 00000030
The instruction in IR is : 00168693
Decode stage:
code : {'neumonic': 'addi', 'opcode': '0b0010011', 'funct3': '0b000', 'rs1': '01101', 'rd': '01101', 'immediate': '000000000001', 'format': 'I', 'id': 9}
RA is : 00000001
rd is : 13
imm is : 00000001
Execute stage:
operand1 is 00000001 operand2 is: 00000001
RZ is : 00000002
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000002
cycle is : 521
Fetch stage:
The value of PC is : 00000034
The instruction in IR is : FF07C4E3
Decode stage:
code : {'neumonic': 'blt', 'opcode': '0b1100011', 'funct3': '0b100', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111101000', 'format': 'SB', 'id': 20}
RA is : 0000001E
RB is : 0000000a
imm is : ffffffe8
Execute stage:
operand1 is 0000001E operand2 is: 0000000a
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 522
Fetch stage:
The value of PC is : 00000038
The instruction in IR is : FF0782E3
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111100100', 'format': 'SB', 'id': 18}
RA is : 0000001E
RB is : 0000000a
imm is : ffffffe4
Execute stage:
operand1 is 0000001E operand2 is: 0000000a
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 523
Fetch stage:
The value of PC is : 0000003c
The instruction in IR is : 01072023
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '10000', 'immediate': '000000000000', 'format': 'S', 'id': 17}
RA is : 10000004
RB is : 0000000a
imm is : 00000000
Execute stage:
operand1 is 10000004 operand2 is: 00000000
RZ is : 10000004
Memory Access stage:
Register Update Stage:
RD: RY: 13 10000004
cycle is : 524
Fetch stage:
The value of PC is : 00000040
The instruction in IR is : 00F72223
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '01111', 'immediate': '000000000100', 'format': 'S', 'id': 17}
RA is : 10000004
RB is : 0000001E
imm is : 00000004
Execute stage:
operand1 is 10000004 operand2 is: 00000004
RZ is : 10000008
Memory Access stage:
Register Update Stage:
RD: RY: 13 10000008
cycle is : 525
Fetch stage:
The value of PC is : 00000044
The instruction in IR is : FD9FF06F
Decode stage:
code : {'neumonic': 'jal', 'opcode': '0b1101111', 'immediate': '111111111111111011000', 'rd': '00000', 'format': 'UJ', 'id': 22}
rd is : 0
imm is : ffffffd8
Execute stage:
operand1 is 10000004 operand2 is: 0000001E
RZ is : 10000022
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000048
cycle is : 526
Fetch stage:
The value of PC is : 0000001c
The instruction in IR is : 02C68663
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01101', 'rs2': '01100', 'immediate': '0000000101100', 'format': 'SB', 'id': 18}
RA is : 00000002
RB is : 00000002
imm is : 0000002c
Execute stage:
operand1 is 00000002 operand2 is: 00000002
RZ is : 00000001
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000001
cycle is : 527
Fetch stage:
The value of PC is : 00000048
The instruction in IR is : FC9FF06F
Decode stage:
code : {'neumonic': 'jal', 'opcode': '0b1101111', 'immediate': '111111111111111001000', 'rd': '00000', 'format': 'UJ', 'id': 22}
rd is : 0
imm is : ffffffc8
Execute stage:
operand1 is 00000002 operand2 is: 00000002
RZ is : 00000004
Memory Access stage:
Register Update Stage:
RD: RY: 0 0000004c
cycle is : 528
Fetch stage:
The value of PC is : 00000010
The instruction in IR is : FFF60613
Decode stage:
code : {'neumonic': 'addi', 'opcode': '0b0010011', 'funct3': '0b000', 'rs1': '01100', 'rd': '01100', 'immediate': '111111111111', 'format': 'I', 'id': 9}
RA is : 00000002
rd is : 12
imm is : ffffffff
Execute stage:
operand1 is 00000002 operand2 is: ffffffff
RZ is : 00000001
Memory Access stage:
Register Update Stage:
RD: RY: 12 00000001
cycle is : 529
Fetch stage:
The value of PC is : 00000014
The instruction in IR is : 02060C63
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01100', 'rs2': '00000', 'immediate': '0000000111000', 'format': 'SB', 'id': 18}
RA is : 00000001
RB is : 00000000
imm is : 00000038
Execute stage:
operand1 is 00000001 operand2 is: 00000000
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 12 00000000
cycle is : 530
Fetch stage:
The value of PC is : 00000018
The instruction in IR is : 00000693
Decode stage:
code : {'neumonic': 'addi', 'opcode': '0b0010011', 'funct3': '0b000', 'rs1': '00000', 'rd': '01101', 'immediate': '000000000000', 'format': 'I', 'id': 9}
RA is : 00000000
rd is : 13
imm is : 00000000
Execute stage:
operand1 is 00000000 operand2 is: 00000000
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 531
Fetch stage:
The value of PC is : 0000001c
The instruction in IR is : 02C68663
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01101', 'rs2': '01100', 'immediate': '0000000101100', 'format': 'SB', 'id': 18}
RA is : 00000000
RB is : 00000001
imm is : 0000002c
Execute stage:
operand1 is 00000000 operand2 is: 00000001
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 532
Fetch stage:
The value of PC is : 00000020
The instruction in IR is : 01F69733
Decode stage:
code : {'neumonic': 'sll', 'opcode': '0b0110011', 'funct3': '0b001', 'funct7': '0b0000000', 'rs1': '01101', 'rs2': '11111', 'rd': '01110', 'format': 'R', 'id': 5}
RA is : 00000000
RB is : 00000002
rd is : 14
Execute stage:
operand1 is 00000000 operand2 is: 00000002
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 14 00000000
cycle is : 533
Fetch stage:
The value of PC is : 00000024
The instruction in IR is : 00B70733
Decode stage:
code : {'neumonic': 'add', 'opcode': '0b0110011', 'funct3': '0b000', 'funct7': '0b0000000', 'rs1': '01110', 'rs2': '01011', 'rd': '01110', 'format': 'R', 'id': 0}
RA is : 00000000
RB is : 10000000
rd is : 14
Execute stage:
operand1 is 00000000 operand2 is: 10000000
RZ is : 10000000
Memory Access stage:
Register Update Stage:
RD: RY: 14 10000000
cycle is : 534
Fetch stage:
The value of PC is : 00000028
The instruction in IR is : 00072783
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '01111', 'immediate': '000000000000', 'format': 'I', 'id': 14}
RA is : 10000000
rd is : 15
imm is : 00000000
Execute stage:
operand1 is 10000000 operand2 is: 00000000
RZ is : 10000000
Memory Access stage:
Register Update Stage:
RD: RY: 15 00000014
cycle is : 535
Fetch stage:
The value of PC is : 0000002c
The instruction in IR is : 00472803
Decode stage:
code : {'neumonic': 'lw', 'opcode': '0b0000011', 'funct3': '0b010', 'rs1': '01110', 'rd': '10000', 'immediate': '000000000100', 'format': 'I', 'id': 14}
RA is : 10000000
rd is : 16
imm is : 00000004
Execute stage:
operand1 is 10000000 operand2 is: 00000004
RZ is : 10000004
Memory Access stage:
Register Update Stage:
RD: RY: 16 0000000a
cycle is : 536
Fetch stage:
The value of PC is : 00000030
The instruction in IR is : 00168693
Decode stage:
code : {'neumonic': 'addi', 'opcode': '0b0010011', 'funct3': '0b000', 'rs1': '01101', 'rd': '01101', 'immediate': '000000000001', 'format': 'I', 'id': 9}
RA is : 00000000
rd is : 13
imm is : 00000001
Execute stage:
operand1 is 00000000 operand2 is: 00000001
RZ is : 00000001
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000001
cycle is : 537
Fetch stage:
The value of PC is : 00000034
The instruction in IR is : FF07C4E3
Decode stage:
code : {'neumonic': 'blt', 'opcode': '0b1100011', 'funct3': '0b100', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111101000', 'format': 'SB', 'id': 20}
RA is : 00000014
RB is : 0000000a
imm is : ffffffe8
Execute stage:
operand1 is 00000014 operand2 is: 0000000a
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 538
Fetch stage:
The value of PC is : 00000038
The instruction in IR is : FF0782E3
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01111', 'rs2': '10000', 'immediate': '1111111100100', 'format': 'SB', 'id': 18}
RA is : 00000014
RB is : 0000000a
imm is : ffffffe4
Execute stage:
operand1 is 00000014 operand2 is: 0000000a
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 00000000
cycle is : 539
Fetch stage:
The value of PC is : 0000003c
The instruction in IR is : 01072023
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '10000', 'immediate': '000000000000', 'format': 'S', 'id': 17}
RA is : 10000000
RB is : 0000000a
imm is : 00000000
Execute stage:
operand1 is 10000000 operand2 is: 00000000
RZ is : 10000000
Memory Access stage:
Register Update Stage:
RD: RY: 13 10000000
cycle is : 540
Fetch stage:
The value of PC is : 00000040
The instruction in IR is : 00F72223
Decode stage:
code : {'neumonic': 'sw', 'opcode': '0b0100011', 'funct3': '0b010', 'rs1': '01110', 'rs2': '01111', 'immediate': '000000000100', 'format': 'S', 'id': 17}
RA is : 10000000
RB is : 00000014
imm is : 00000004
Execute stage:
operand1 is 10000000 operand2 is: 00000004
RZ is : 10000004
Memory Access stage:
Register Update Stage:
RD: RY: 13 10000004
cycle is : 541
Fetch stage:
The value of PC is : 00000044
The instruction in IR is : FD9FF06F
Decode stage:
code : {'neumonic': 'jal', 'opcode': '0b1101111', 'immediate': '111111111111111011000', 'rd': '00000', 'format': 'UJ', 'id': 22}
rd is : 0
imm is : ffffffd8
Execute stage:
operand1 is 10000000 operand2 is: 00000014
RZ is : 10000014
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000048
cycle is : 542
Fetch stage:
The value of PC is : 0000001c
The instruction in IR is : 02C68663
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01101', 'rs2': '01100', 'immediate': '0000000101100', 'format': 'SB', 'id': 18}
RA is : 00000001
RB is : 00000001
imm is : 0000002c
Execute stage:
operand1 is 00000001 operand2 is: 00000001
RZ is : 00000001
Memory Access stage:
Register Update Stage:
RD: RY: 0 00000001
cycle is : 543
Fetch stage:
The value of PC is : 00000048
The instruction in IR is : FC9FF06F
Decode stage:
code : {'neumonic': 'jal', 'opcode': '0b1101111', 'immediate': '111111111111111001000', 'rd': '00000', 'format': 'UJ', 'id': 22}
rd is : 0
imm is : ffffffc8
Execute stage:
operand1 is 00000001 operand2 is: 00000001
RZ is : 00000002
Memory Access stage:
Register Update Stage:
RD: RY: 0 0000004c
cycle is : 544
Fetch stage:
The value of PC is : 00000010
The instruction in IR is : FFF60613
Decode stage:
code : {'neumonic': 'addi', 'opcode': '0b0010011', 'funct3': '0b000', 'rs1': '01100', 'rd': '01100', 'immediate': '111111111111', 'format': 'I', 'id': 9}
RA is : 00000001
rd is : 12
imm is : ffffffff
Execute stage:
operand1 is 00000001 operand2 is: ffffffff
RZ is : 00000000
Memory Access stage:
Register Update Stage:
RD: RY: 12 00000000
cycle is : 545
Fetch stage:
The value of PC is : 00000014
The instruction in IR is : 02060C63
Decode stage:
code : {'neumonic': 'beq', 'opcode': '0b1100011', 'funct3': '0b000', 'rs1': '01100', 'rs2': '00000', 'immediate': '0000000111000', 'format': 'SB', 'id': 18}
RA is : 00000000
RB is : 00000000
imm is : 00000038
Execute stage:
operand1 is 00000000 operand2 is: 00000000
RZ is : 00000001
Memory Access stage:
Register Update Stage:
RD: RY: 12 00000001
cycle is : 546
Fetch stage:
The value of PC is : 0000004c
The instruction in IR is : 00000000
