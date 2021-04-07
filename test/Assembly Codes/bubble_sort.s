.data
array: .word 1 2 10 9 3 8 4 7 5 6

.text
auipc x11,0x10000 # x11=array.begin()
addi x11 x11 0
li x12,10 # x12=array.size()
addi x31,x0,2
bubble_sort: 
addi x12,x12,-1  #n-=1
beq x12,x0,exit # if (n-1==0){break;}
addi x13, x0,0 # x13= counter
loop:
beq x13,x12,break # if (i==n-1){loop ends so break and continue with bubble_sort(n-1)}
sll x14,x13,x31 # x14= 4* i
add x14,x14,x11 # x14=&arr[i]
lw x15,0(x14) # x15=arr[i]
lw x16,4(x14) # x16=arr[i+1]
addi x13,x13,1 #i++
blt x15,x16,loop
beq x15,x16,loop
sw x16,0(x14) # arr[i]=arr[i+1]
sw x15,4(x14) # arr[i+1]=arr[i] # thus swapped
j loop
break:

j bubble_sort
exit:
