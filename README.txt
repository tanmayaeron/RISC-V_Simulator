About The Project
The aim of this project is to simulate the machine level execution of RISC V as well as the RISC-V 32-bit instructions using a high level language. The Project also aims to give updates to the user regarding each step of the execution of the program.
The user can also choose the Inst and Data Replacement policy, Data and Inst Cache size. The project can also be executed using step functionality for debugging purposes.
It also returns the final status of the memory and registers as output for the user to analyse the working of their programs thoroughly. The Project currently allows the user to use 29 different instructions and can be extended to allow the use of any number of instructions by editing the .csv files as long as the instructions are supported by 32-bit RISC V ISA.
For each instruction the program gives various updates like IR, PC, decoded instruction, temporary registers like RA, RB, RZ, RY, etc. during each cycle and prints the number of cycles.
The program executes each instruction using five stages as described in the RISC V architecture.

Prerequisites
    * python (>=3.7)
    * pip (>=21.0.3)

Libraries Used
# Back-end - Python3
    * pandas: for reading .csv files.
    * os: for getting and adding path to certain file locations.
    * defaultdict: to make a hash map for memory.
    * sys: for reading and editing files with ease.
    * json: for crunching generated data.
    * glob: for file management
    * regex: for making the cleaned file by splitting the RISC-V instructions and removing comments
    * random: for generating random number in Random Replacement Policy
# Front-end - Python3
    * PyQT5: for the Graphic User Interface.
    * qdarkstyle: for dark theme
    * QtAwesome: for beautifying the theme

Installation
    1. Unzip the zip file and locate the folder directory using cmd

    2. Install required libraries using
        pip install -r requirements.txt
    3. To run GUI version:
        python main.py -g
        After you run this command in terminal the GUI will pop up.
        Then you can enable each knob by ticking them.
        For the fifth knob you can add the instruction number by adding the instruction in the box.
        
        
    4. To run Non GUI version:
        python3 main.py
        add following knobs accordingly
        -h, --help            show this help message and exit
        -g, -gui              enable GUI
        -f F, -filename F     specify file which is to be run for non-GUI version
        -k1, -knob1           enable Pipelining
        -k2, -knob2           enable Data Forwarding
        -k3, -knob3           show value in registerFile at end of each cycle
        -k4, -knob4           show value in Pipeline Registers at end of each cycle
        -k5 K5, -knob5 K5     show value in Pipeline Registers at end of each cycle for particular instruction
        -ICache cacheSize blockSize noOfWays :- configure input cache in format cache size block size number of ways
        -DCache cacheSize blockSize noOfWays :- configure data cache in format cache size block size number of ways


Instructions to use GUI:
1. Write the code you wish to run in the editor window. You may copy it from any other location as well.
2. You may save the file using save button.
3. Set the required knobs according to the documentation
4. Set the details of cache in the control box.
5. Tick the isMC button if the file is in Machine level of RISC-V.
6. You may change the Inst Replacement Policy as well as the Data Replacement Policy by clicking on them. The Default is LRU.
7. You may set branch predictor and initial state of predictor. The Default is static Always Taken predictor.
8. To run the file using step function first load the file by pressing on the top right third (down arrow key) button and then click on the step button.
9. To run the file, press compile button. Once the code completes execution, a tick sign will be visible on the button.
10. In case you run the pipelined version the datapath can visualised using the "datapath" and "info" tab
11. You can get the info about data cache and instruction cache from respective tabs.
12. Look for the generated files

Contributors:
* Aditya Agarwal - 2019CSB1064
* Aneeket Mangal - 2019CSB1071
* Fadia Het Rakeshkumar - 2019CSB1084
* Shikhar Soni - 2019CSB1119
* Tanmay Aeron - 2019CSB1124
    
     
Input Format

Input format of the MC file instructions
* In text segment, data is word by word while in data segment it is byte by byte.
* Text segment followed by data segment demarcated by '$', each line is of format: "address data".
* Example:
    0x0 0x00500513
    0x4 0x008000EF
    0x8 0x0440006F
    $
    0x10000000 0x64

Input format of the RISC-V instructions
* The instructions are RISC-V 32 bit instructions.
* For these instructions keep the isMC unchecked
.data
array: .word 1 2 10 9 3 8 4 7 5 6

.text
auipc x11,0x10000 # x11=array.begin()
addi x11 x11 0
addi x12 x0,10 # x12=array.size()
addi x31,    x0,2
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
jal x0 loop
break:

jal x0 bubble_sort
exit:


Output Format
Check the generated folder for details of compilation. It contains:
        * memory.txt            :  details of memory
        * register.txt          :  details of registers
        * outputLog.txt         :  details of changes in temporary registers for each cycle
        * buffer.txt            :  details of buffer in a particular cycle provided in knob5 input box.
        * forwarding.txt        :  details of data forwarding paths taken in each cycle
        * stats.txt             :  contains general stats about the code compilation.
        * DataCache.txt         :  contains info of the data cache
        * InstructionCache.txt  :  contains info of the data cache
        * CacheInfo.txt         :  contains information about the cache
        * Buffer Snapshots      :  contains data of buffers in each cycle if knob4 is on.
        * Register Snapshots    :  contains details of register file in knob3 is on.


Work split among team members:-
:) Overall it was a very successful team efforts. Each members coordinated others well.
:) It became really difficult for us to decide each other's contribution.
* Aditya Agarwal        -   Cache.py, documentation, GUI
* Aneeket Mangal        -   Cache.py, documentation, GUI
* Fadia Het Rakeshkumar -   Cache.py, documentation, GUI
* Shikhar Soni          -   Cache.py, documentation, GUI
* Tanmay Aeron          -   Cache.py, documentation, GUI
