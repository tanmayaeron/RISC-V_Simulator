file = open('temp2.txt', 'r')
out = open('temp3.txt', 'w')
address = 0x10000000
for i in file:
    for j in i.split():
        j = int(j)
        out.write(hex(address)+" "+hex(j)+"\n")
        address += 4
