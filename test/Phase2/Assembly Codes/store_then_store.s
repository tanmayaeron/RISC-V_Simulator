# store after store so rdprev1 == rdprev2 == -1:

lui x10,0x10000
addi x11,x10,12
sw x10,0(x10)
sw x11,0(x11)
