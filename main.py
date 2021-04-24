from GUI.mainPage import *
from frontBack import frontBackEndInteraction
#commented top line and added above for now
import sys
import os
if __name__ == '__main__':
    n = len(sys.argv)
    print("Compiling!!!!")
    print("Check generated folder for details.")
    if(n == 2 and sys.argv[1] == '2'):
        directoryPath = os.getcwd()
        currFilePath = os.path.join(directoryPath, "test", "main.mc")
        link = frontBackEndInteraction(directoryPath)
        link.runProgram(currFilePath)
        
    elif(n == 3 and sys.argv[1] == '2'):
        directoryPath = os.getcwd()
        currFilePath = os.path.join(directoryPath, "test", sys.argv[2])
        link = frontBackEndInteraction(directoryPath)
        link.runProgram(currFilePath)
        
    else:
        App = QApplication(sys.argv)
        App.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))
        window = mainScreen(App)
        sys.exit(App.exec_())
        

