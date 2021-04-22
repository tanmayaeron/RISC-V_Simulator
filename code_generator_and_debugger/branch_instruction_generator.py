out=open('out.txt','w')

string="goto"

out.write('addi x10 x0 1')
out.write("\n")
for i in range(1,1000+1):
    gotoi=string+str(i)
    goto="beq x10,x11,"+gotoi
    out.write(goto)
    out.write("\n")
    out.write(gotoi+":")
    out.write("\n")
    