file = open("temp2.txt", 'r')
out = open('temp3.txt', 'w')

for i in file:
    j = i.split()
    try:
        out.write(j[0]+" "+j[1]+"\n")
    except:
        pass
