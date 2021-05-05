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
        self.knobsList = [0, 0, 0, 0 ,0, 0]
        self.currFilePath = os.path.join(self.directoryPath, "test", "main.mc")
        self.link = frontBackEndInteraction([self.directoryPath, [1024, 1024], [8, 8], [4, 4]])
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
        
    def getCacheFromInput(self):
        temp = []
        
        for i in range(3):
            temp.append([])
            for j in range(2):
                if(self.controlTable[i*2+j].text() == ""):
                    temp[-1].append(32)
                else:
                    temp[-1].append(int(self.controlTable[(i*2) + j].text()))
                    
                    
        return temp

    def updateknobsList(self):
        self.knobsList[0] = self.k1.isChecked()
        self.knobsList[1] = self.k2.isChecked()
        self.knobsList[2] = self.k3.isChecked()
        self.knobsList[3] = self.k4.isChecked()
        self.knobsList[4] = self.k5.isChecked()
        if(self.k6.text() == ""):
            self.knobsList[5] = 0
        else:
            self.knobsList[5] = int(self.k6.text())
        
    def fileCompile(self):
        self.fileSave()
        cacheDetails = self.getCacheFromInput()
        self.link.reset(cacheDetails)
        self.updateknobsList()
        self.link.runProgram(self.currFilePath, self.knobsList)
        self.compile_button.setText("\U00002705")
        self.updateRegisterView()
        self.updateMemoryView("10000000")
        self.datapathO = self.link.parseData(os.path.join(self.directoryPath, "generated", "outputLog.txt"))
        self.datapathF = self.link.parseData(os.path.join(self.directoryPath, "generated", "forwarding.txt"))
        # self.hitMissData = self.link.parseData(os.path.join(self.directoryPath, "miss.txt"))
        self.link.printCaches()
        loop = QEventLoop()
        QTimer.singleShot(1000,loop.quit)   
        loop.exec_()
        
        self.compile_button.setText("\U00002699")
        
    def datapathhelp(self, flag):
        self.countDisplay +=flag
        self.countDisplay = max(1, self.countDisplay)
        temp = self.datapathF[self.countDisplay]
        self.l1[6].setText(str(self.countDisplay))
        self.l1[8].setText(temp["EE1"])
        self.l1[9].setText(temp["EE2"])
        self.l1[10].setText(temp["ME1"])
        self.l1[11].setText(temp["ME2"])
        self.l1[12].setText(temp["MM"])
    

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
        self.controlBox()
        self.cacheDisplay()
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

        hbox.addWidget(self.feed, 2)
        hbox.addWidget(self.help, 1)
        vbox = QVBoxLayout()
        vbox.addLayout(logo_label)
        vbox.addLayout(hbox)
        self.setLayout(vbox)
        self.showMaximized()
