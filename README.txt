About The Project
The aim of this project is to simulate the machine level execution of RISC V 32-bit instructions using a high level language. The Project also aims to give updates to the user regarding each step of the execution of the program.
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

# Front-end - Python3
    * PyQT5: for the Graphic User Interface.
    * qdarkstyle: for dark theme

Installation
    1. Unzip the zip file and locate the folder directory using cmd

    2. Install required libraries using
        pip install -r requirements.txt
    3. To run the GUI version enter
        python main.py

    4. To run the non-GUI version on the default file
        python main.py 2
    
    5. To run the non-GUI version on a specific file
        python main.py 2 filename.mc
        Note:- file should be present in the test directory

    5. Check the generated folder for details of compilation. It contains:
        * memory.txt   :  details of memory
        * register.txt :  details of registers
        * outputLog.txt:  details of changes in temporary registers for each cycle


Instructions to use GUI:
1. Write the code you wish to run in the editor window. You may copy it from any other location as well.
2. You may save the file using save button.
3. Set the required knobs according to the documentation
4. To run the file, press compile button. Once the code completes execution, a tick sign will be visible on the button.
5. In case you run the pipelined version the datapath can visualised using the "datapath" and "info" tab
6. Look for the generated files

Contributors:
* Aditya Agarwal - 2019CSB1064
* Aneeket Mangal - 2019CSB1071
* Fadia Het Rakeshkumar - 2019CSB1084
* Shikhar Soni - 2019CSB1119
* Tanmay Aeron - 2019CSB1124
    
     
Input Format
* In text segment, data is word by word while in data segment it is byte by byte.
* Text segment followed by data segment demarcated by '$', each line is of format: "address data".
* Example:
    0x0 0x00500513
    0x4 0x008000EF
    0x8 0x0440006F
    $
    0x10000000 0x64

Output Format
Check the generated folder for details of compilation. It contains:
        * memory.txt   :  details of memory
        * register.txt :  details of registers
        * outputLog.txt:  details of changes in temporary registers for each cycle

Work split among team members:-
:) Overall it was a very successful team efforts. Each members coordinated others well.
:) It became really difficult for us to decide each other's contribution.
* Aditya Agarwal - Documentation, simulator.py, readme, testing
* Aneeket Mangal - FrontBack.py, UiComponents.py, MainPage.py, simulator.py
* Fadia Het Rakeshkumar - BTB.py, simulator.py, documentation, testing
* Shikhar Soni - Hazards.py, simulator.py, pipeline buffer, testing
* Tanmay Aeron - Hazards.py, simulator.py, IAG.py, memory.py
