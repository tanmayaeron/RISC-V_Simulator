# if 12<=prevtype1<=14 and 15 <= id <= 17 and rdprev1 in [rs1, rs2]: #load then store
# load then store
.data
store: .word 0x10000010

.text
addi x10,x10,1
addi x11,x11,2
la x9,store
lw x10,0(x9) 
sw x11,0(x10) # rdprev1 = x10= rs1 so hazard # 15 <= id <= 17 



0x0 0x00150513
0x4 0x00258593
0x8 0x10000497
0xc 0xFF848493
0x10 0x0004A503
0x14 0x00B52023
$
0x10000000 0x10000010

