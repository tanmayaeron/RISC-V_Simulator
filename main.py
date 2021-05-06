from GUI.mainPage import *
from frontBack import frontBackEndInteraction
#commented top line and added above for now
import argparse

import os

if __name__ == '__main__':

    my_parser = argparse.ArgumentParser(description='RISC-V simulator')
    my_parser.add_argument('-g', '-gui', action='store_true', help='enable GUI')
    my_parser.add_argument('-f', '-filename', action='store', type=str, required=False, help = 'specify file which is to be run for non-GUI version')

    my_parser.add_argument('-k1', '-knob1', action='store_true', help='enable Pipelining')
    my_parser.add_argument('-k2', '-knob2', action='store_true', help='enable Data Forwarding')
    my_parser.add_argument('-k3', '-knob3', action='store_true', help='show value in registerFile at end of each cycle')
    my_parser.add_argument('-k4', '-knob4', action='store_true', help='show value in Pipeline Registers at end of each cycle')
    my_parser.add_argument('-k5', '-knob5', action='store',type=int,required=False, help='show value in Pipeline Registers at end of each cycle for particular instruction')
    my_parser.add_argument('-ICache', '-instruction cache', action='store',type=int,nargs='+',help='configure input cache in format cache size block size number of ways')
    my_parser.add_argument('-DCache', '-data cache', action='store', type=int, nargs='+',help='configure data cache in format cache size block size number of ways')
    args = my_parser.parse_args()

    ifGUI = args.g
    fileName = args.f
    knob1 = args.k1
    knob2 = args.k2
    knob3 = args.k3
    knob4 = args.k4
    ICache = args.ICache
    DCache = args.DCache

    #print(ICache)
    #print(DCache)

    print("Compiling!!!!")
    print("Check generated folder for details.")

    ins_num = 0
    if args.k5 is None:
        knob5 = False
    else:
        knob5 = True
        ins_num = args.k5

    knobsL = [knob1, knob2, knob3, knob4, knob5, ins_num]
    
    if ifGUI:
        App = QApplication(sys.argv)
        App.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))
        window = mainScreen(App)
        sys.exit(App.exec_())

    elif(fileName is None):
        directoryPath = os.getcwd()
        currFilePath = os.path.join(directoryPath, "test", "main.mc")
        startDetails = [directoryPath, [64, 64], [4, 4], [2, 2]]
        link = frontBackEndInteraction(startDetails)
        link.runProgram(currFilePath, knobsL)
        # link.reset()
        
    else:
        directoryPath = os.getcwd()
        currFilePath = os.path.join(directoryPath, "test", fileName)
        startDetails = [directoryPath, [64, 64], [4, 4], [2, 2]]
        if ICache is not None:
            startDetails[1][0] = ICache[0]
            startDetails[2][0] = ICache[1]
            startDetails[3][0] = ICache[2]
        if DCache is not None:
            startDetails[1][1] = DCache[0]
            startDetails[2][1] = DCache[1]
            startDetails[3][1] = DCache[2]
        link = frontBackEndInteraction(startDetails)
        link.runProgram(currFilePath, knobsL)
        # link.reset()
        

