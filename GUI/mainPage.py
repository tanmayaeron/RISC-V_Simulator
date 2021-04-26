from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import qdarkstyle
from qdarkstyle.dark.palette import DarkPalette
import os
from helperFunctions import *
from frontBack import *
from GUI.UiComponents import UiComponents

class mainScreen(QWidget, UiComponents):
    def __init__(self, App):
        super().__init__()
        self.App = App
        self.title = "RISC-V Simulator"
        
        self.directoryPath = os.getcwd()
        self.countDisplay = 1
        self.currFilePath = os.path.join(self.directoryPath, "test", "main.mc")
        self.link = frontBackEndInteraction(self.directoryPath)
        self.iconName = os.path.join(self.directoryPath, "GUI", "Images", "logo.png")
        self.splash = QSplashScreen(QPixmap(self.iconName), Qt.WindowStaysOnTopHint)
        self.datapathO = self.link.parseData(os.path.join(self.directoryPath, "generated", "outputLog.txt"))
        self.datapathF = self.link.parseData(os.path.join(self.directoryPath, "generated", "forwarding.txt"))
        QTimer.singleShot(0, self.initWindow)
        self.splash.show()

    def updateRegisterView(self):
        alt = getAltNameOfRegister()
        val = self.link.getRegisterSnapshot()
        for i in range(32):
            self.registerArray[i][1].setText(str(alt[i]))
            self.registerArray[i][2].setText("0x" + str(val[i]))

    def updateMemoryView(self, address = "10000000"):
        l = self.link.getMemorySnapshot(address)
        for i in range(10):
            for j in range(5):
                self.memoryArray[i][j].setText(l[i][j])
    def updateInfoView(self, stage):
        dictionary = self.datapathO[self.countDisplay-1][str(stage)]
        count = 0
        for i in range(30):
            self.infoTable[i][0].setText("")
            self.infoTable[i][1].setText("")
        
        for i in dictionary.keys():
            self.infoTable[count][0].setText(i)
            self.infoTable[count][1].setText(str(dictionary[i]))
            count+=1
            # self.memoryArray[i][j].setText(l[i][j])

        
    def fileOpen(self):
        f = open(self.currFilePath, 'r')
        self.editorScreen.setPlainText(f.read())

    def fileSave(self):
        text = self.editorScreen.toPlainText()
        f = open(self.currFilePath, 'w')
        self.compile_button.setText("Compile")
        f.write(text)

    def fileCompile(self):
        self.fileSave()
        self.link.reset()
        self.link.runProgram(self.currFilePath, self.runModes.currentIndex())
        self.compile_button.setText("\U00002705")
        self.updateRegisterView()
        self.updateMemoryView("10000000")
        self.datapathO = self.link.parseData(os.path.join(self.directoryPath, "generated", "outputLog.txt"))
        self.datapathF = self.link.parseData(os.path.join(self.directoryPath, "generated", "forwarding.txt"))
        loop = QEventLoop()
        QTimer.singleShot(1000,loop.quit)
        loop.exec_()
        
        self.compile_button.setText("\U00002699")
        
    def datapathhelp(self, flag):
        self.countDisplay +=flag
        self.countDisplay = max(1, self.countDisplay)
        temp = self.datapathF[self.countDisplay]
        self.l1[6].setText(str(self.countDisplay))
        self.l1[7].setText(temp["ME"])
        self.l1[8].setText(temp["DE"])
        self.l1[9].setText(temp["EE"])
    

    def jumpAddress(self):
        a = self.tempLineEdit.text()
        a = a.lower()
        if(len(a) == 8):
            self.updateMemoryView(a)
        
    def changeTheme(self):
        if self.currentTheme == "Dark Theme":
            self.currentTheme = "Light Theme"
            self.App.setStyleSheet("")
        else:
            self.currentTheme = "Dark Theme"
            self.App.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5', palette=DarkPalette))
            
            
    def connections(self):
        self.save_button.clicked.connect(lambda: self.fileSave())
        self.compile_button.clicked.connect(lambda: self.fileCompile())
        self.theme_button.clicked.connect(lambda: self.changeTheme())
        self.jump_button.clicked.connect(lambda: self.jumpAddress())
        
        self.l1[0].clicked.connect(lambda: self.updateInfoView(0))
        self.l1[1].clicked.connect(lambda: self.updateInfoView(1))
        self.l1[2].clicked.connect(lambda: self.updateInfoView(2))
        self.l1[3].clicked.connect(lambda: self.updateInfoView(3))
        self.l1[4].clicked.connect(lambda: self.updateInfoView(4))
        self.l1[5].clicked.connect(lambda: self.datapathhelp(-1))
        self.l1[7].clicked.connect(lambda: self.datapathhelp(1))
        
            
    def window(self):
        self.editor(self.currFilePath)
        self.memoryDisplay()
        self.registerDisplay()
        self.updateRegisterView()
        self.updateMemoryView()
        self.datapath()
        self.info()
        self.tabbedView2()
        self.tabbedView1()
        self.help = self.tabs1
        self.feed = self.tabs2
   
    def initWindow(self):
        self.splash.close()
        logo_label = self.mainLabel()
        
        self.window()
        self.connections()
        hbox = QHBoxLayout()

        hbox.addWidget(self.feed, 10)
        hbox.addWidget(self.help, 4)
        vbox = QVBoxLayout()
        vbox.addLayout(logo_label)
        vbox.addLayout(hbox)
        self.setLayout(vbox)
        self.showMaximized()

App = QApplication(sys.argv)
App.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))
window = mainScreen(App)
sys.exit(App.exec_())
