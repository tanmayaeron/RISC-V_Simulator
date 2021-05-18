
def stringsplit(string):
    # this function splits according to space and comma only
    l=[]
    for i in string.split():
        j=i.split(",")
        l+=[k for k in j if k!=""]


    return l;


def stringsplit2(string,splitarray=" ,\n"):
    # this function splits the string and arguments are all the elements in the splitarray
    l=[]
    
    for i in string:
        if i in splitarray:
            if len(l)==0 or l[-1]!="":
                # we have to split here
                l.append("")
        else:
            if len(l)==0:
                l.append(i)
            else:
                l[-1]+=i
    if l and l[-1]=="":
        l.pop()
    return l;

if __name__=='__main__':
    my_string="addi x11,x12, x13"
    string=stringsplit(my_string)
    print(string)

    
    string =stringsplit2(my_string)
    print(string)

    my_string="lw x11,12(x11)\n"
    string =stringsplit2(my_string)
    print(string)

    my_string="lw x11,12(x11)\n"
    string =stringsplit2(my_string," ,()\n")
    print(string)
    