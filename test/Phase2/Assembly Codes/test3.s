# if 12<=prevtype1<=14 and 15 <= id <= 17 and rdprev1 in [rs1, rs2]: #load then store
# load then store
.data
store: .word 0x10000010

.text

addi x11,x11,2
la x9,store
lw x10,0(x9) # 15 <= id <= 17 
add x11,x10,x10

0x0 0x00258593
0x4 0x10000497
0x8 0xFFC48493
0xc 0x0004A503
0x10 0x00A505B3
$
0x10000000 0x10000010
