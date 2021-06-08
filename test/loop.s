addi x10,x0,1000
addi x11,x0,0
loop:
beq x11,x10,exit
addi x11,x11,1
beq x0,x0,loop
exit: