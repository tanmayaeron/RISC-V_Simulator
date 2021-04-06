#void fib(n){
#	if(n<=1){return n;}
#    else return fib(n-1)+fib(n-2);
#}

li x10,7
jal x1,fib
j exit
fib:
addi sp,sp,-8
sw x10,0(sp)
sw x1,4(sp)
li x11,1
bgt x10,x11,l1
addi sp,sp,8
jalr x0,x1,0



l1:
addi x10,x10,-1
jal x1,fib
add x6,x10,x0
lw x10,0(sp)
addi x10,x10,-2
addi sp,sp,-4
sw x6,0(sp)
jal x1,fib
lw x6,0(sp)
addi sp,sp,4
lw x1,4(sp)
addi sp,sp,8
add x10,x10,x6
jalr x0,x1,0
exit:
