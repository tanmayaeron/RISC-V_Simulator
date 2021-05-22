auipc x11,0x10000 
addi x11 x11 0
addi x12 x0,10 
addi x31,    x0,2
bubble_sort: 
addi x12,x12,-1  
beq x12,x0,exit 
addi x13, x0,0 
loop:
beq x13,x12,break 
sll x14,x13,x31 
add x14,x14,x11 
lw x15,0(x14) 
lw x16,4(x14) 
addi x13,x13,1 
blt x15,x16,loop
beq x15,x16,loop
sw x16,0(x14) 
sw x15,4(x14) 
jal x0 loop
break:
jal x0 bubble_sort
exit:
