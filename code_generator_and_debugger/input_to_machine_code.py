file = open("temp2.txt", 'r')
out = open('temp3.txt', 'w')
## converts 0x0 0x00200593 to 0x00200593
for i in file:
    j = i.split()
    try:
        out.write(j[1]+"\n")
    except:
        pass
