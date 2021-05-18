import re

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
    splitarray=frozenset(splitarray)
    # as the query is search frozenset performs faster over list
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

def splitstringregex(string):
    # splits the string at commas and spaces(spaces tabs and \n)
    l=re.findall(r'[^,\s]+',string)
    return l;

def bracketsplit(string):
    # splits the string at commas,spaces(tabs and \n), (,)
    # used to extract 12 and x16 from 12(x16)
    # also extracts lw x11 12 x12 from lw x11,12(x12)
    l=re.findall(r'[^,\s()]+',string)
    return l;

if __name__=='__main__':
    my_string="addi                        x11,x12, x13"
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

    my_string="lw            x11,12(x11)\n"
    string =splitstringregex(my_string)
    print("regex output",string)

    my_string="12(x16)"
    string =bracketsplit(my_string)
    print("regex output",string)