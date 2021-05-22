addi x10 x0 5
jal x1,fact
jal x0 exit
fact:
addi x2,x2,-8
sw x1,4(x2)
sw x10,0(x2)
addi x11 x0,1
blt x11,x10,l1
addi x10,x0 1
addi x2,x2,8
jalr x0,x1,0
l1:
addi x10,x10,-1
jal x1,fact
addi x6,x10,0
lw x10,0(x2)
lw x1,4(x2)
mul x10,x10,x6
addi x2,x2,8
jalr x0,x1,0
exit:
