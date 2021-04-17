# rs1 = rdprev1 rs1=rdprev2 as well as rsprev1==rsprev2=rdprev2
.data
lab: .word 0x10000000
.text
lw x10,lab
addi x10,x10,10
add x10,x10,x10
addi x11,x10,5

# 0x0	0x10000517
# 0x4	0x00052503
# 0x8	0x00A50513
# 0xc	0x00A50533
# 0x10 0x00550593
# $
# 0x10000000 0x10000010
