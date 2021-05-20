import re
import pandas as pd

df_control = pd.read_csv(os.path.join(currFolderPath, 'repository', "controls.csv"))
def_neu = list(df_control['neumonic'].astype(int))
df      = list(df_control['parts'].astype(int))
df_1    = list(df_control['part1'].astype(int))
df_2    = list(df_control['part2'].astype(int))
df_3    = list(df_control['part3'].astype(int))
            
def dump(file):
    f = open(file, 'r')
    f = f.readlines()
    for i in f:
        processInstruction(i)

def processInstruction(instruction):
    l = split(instruction)
    instructionIndex = 0
    try:
        instructionIndex = df_neu.index(l[0])
    except:
        return "Unknown instruction"
    if(len(l) != df[instructionIndex]):
        return "Insufficient/Excess parameters"
    
    else:
        if(check(l[1], df_1[instructionIndex]) == None):
            return "Incorrect syntax"
        if(check(l[2], df_2[instructionIndex]) == None):
            return "Incorrect syntax"
        else:
            l[2] = int(string, 2)
        try:
            if(check(l[3], df_3[instructionIndex]) == None):
                return "Incorrect syntax"
        except:
            pass
        '''
        l = [neumonic, part1, part2, part3]
        '''
        
        
        
        
    
    
def check(string, type):
    if(type == 0):
        if(re.search(r'^x(([0-9])|([1-2][0-9])|(3[0-1]))$', string)):
            return 1
        else:
            return None
    elif(type == 1):
        try:
            number = int(string, 0)
            return number
        except:
            return None
        
    elif(type == -1):
        return 1
        


def split(string):
    # splits the string at commas,spaces(tabs and \n), (,)
    # used to extract 12 and x16 from 12(x16)
    # also extracts lw x11 12 x12 from lw x11,12(x12)
    l=re.findall(r'[^,\s()]+',string)
    return l;

if __name__=='__main__':
    print(int("21", 0))
    print(int("0x21", 0))
    print(int("0b11", 0))
    print(int("0b21", 0))
    # string = "x21"
    # if(re.search(r'^x(([0-9])|([1-2][0-9])|(3[0-1]))$', string)):
    #     print(2)
    # string = "x211"
    # print(re.search(r'^x(([0-9])|([1-2][0-9])|(3[0-1]))$', string))
    # string = "1x21"
    # print(re.search(r'^x(([0-9])|([1-2][0-9])|(3[0-1]))$', string))
  
    
    
    
#     def stringsplit(string):
#         # this function splits according to space and comma only
#     l=[]
#     for i in string.split():
#         j=i.split(",")
#         l+=[k for k in j if k!=""]


#     return l;


# def stringsplit2(string,splitarray=" ,\n"):
#     # this function splits the string and arguments are all the elements in the splitarray
#     l=[]
#     splitarray=frozenset(splitarray)
#     # as the query is search frozenset performs faster over list
#     for i in string:
#         if i in splitarray:
#             if len(l)==0 or l[-1]!="":
#                 # we have to split here
#                 l.append("")
#         else:
#             if len(l)==0:
#                 l.append(i)
#             else:
#                 l[-1]+=i
#     if l and l[-1]=="":
#         l.pop()
#     return l;

# def splitstringregex(string):
#     # splits the string at commas and spaces(spaces tabs and \n)
#     l=re.findall(r'[^,\s]+',string)
#     return l;
