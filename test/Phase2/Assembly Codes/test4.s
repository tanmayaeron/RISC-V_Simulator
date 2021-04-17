# 12<=prevtype2<=14 and rdprev2 in [rs1, rs2]: #if the previous of previous were load then M->E beginning
.data
store: .word 0x10000010

.text
addi x11,x11,2
la x9,store
lw x10,0(x9) # 12<=prevtype2<=14
add x0,x0,x0
add x11,x10,x10 # rs1= rs2 = rdprev2 and prev2  is load instruction

# 0x0 0x00258593
# 0x4 0x10000497
# 0x8 0xFFC48493
# 0xc 0x0004A503
# 0x10 0x00000033
# 0x14 0x00A505B3
# $
# 0x10000000 0x10000010
