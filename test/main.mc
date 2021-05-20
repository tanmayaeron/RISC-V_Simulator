addi x10 x0 5
jal x1,fact
j exit
fact:
addi sp,sp,-8
sw x1,4(sp)
sw x10,0(sp)
li x11,1
blt x11,x10,l1
li x10,1
addi sp,sp,8
jalr x0,x1,0
l1:
addi x10,x10,-1
jal x1,fact
addi x6,x10,0
lw x10,0(sp)
lw x1,4(sp)
mul x10,x10,x6
addi sp,sp,8
jalr x0,x1,0
exit:
