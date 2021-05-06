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

class UiComponents():
    def __init__(self):
        self.fixedfont = QFontDatabase.systemFont(QFontDatabase.FixedFont)
        self.fixedfont.setPointSize(16)

    def operationTile(self, name):
        button = QPushButton()
        button.setText(name)
        button.setFont(QFont('Times', 30))
        
        button.setFixedHeight(40)
        button.setFixedWidth(40)
        return button
        
    def buttonTile(self, name, height, width):
        button = QPushButton()
        button.setText(name)
        button.setFont(QFont('Times', 30))
        # bto.setStyleSheet("background-color :red;")
        button.setFixedHeight(height)
        button.setFixedWidth(width)
        return button
    # def labelTile2(self, name, height, width)

    def labelTile(self, labelName, height, width, isBorder):
        temp = QLabel()
        temp.setText(labelName)
        temp.setFont(self.fixedfont)
        temp.setFixedHeight(height)
        temp.setFixedWidth(width)
        if (isBorder):
            temp.setStyleSheet("border :1px solid white;")
        temp.setAlignment(QtCore.Qt.AlignCenter)
        # temp.setStyleSheet("color: black;");
        return temp
    
    def labelTile2(self, labelName, height, width, color):
        temp = QLabel()
        temp.setText(labelName)
        temp.setFont(self.fixedfont)
        temp.setFixedHeight(height)
        temp.setFixedWidth(width)
        
        temp.setStyleSheet("background-color:" +color+";")
        temp.setAlignment(QtCore.Qt.AlignCenter)
        return temp
    def buttonTile2(self, labelName, height, width, color):
        temp = QPushButton()
        temp.setText(labelName)
        temp.setFont(self.fixedfont)
        temp.setFixedHeight(height)
        temp.setFixedWidth(width)
        temp.setStyleSheet("background-color:" +color+";")
        return temp

    def info(self):
        self.infoScroll = QScrollArea()
        self.displayWidget3 = QGroupBox()
        self.info_grid = QGridLayout()
        count = 0
        self.infoTable = []
        for i in range(30):
            temp = self.labelTile("",100,120,False)
            temp.setAlignment(QtCore.Qt.AlignLeft)
            temp.setWordWrap(True)
            self.info_grid.addWidget(temp,count,0)
            tempp = self.labelTile("",100,800,False)
            tempp.setAlignment(QtCore.Qt.AlignLeft)
            tempp.setWordWrap(True)
            self.info_grid.addWidget(tempp,count, 1)
            self.infoTable.append([temp, tempp])
            count+=1
            
        self.displayWidget3.setLayout(self.info_grid)
        self.infoScroll.setWidget(self.displayWidget3)
        self.infoScroll.setWidgetResizable(True)



    def ICache(self):
        self.scroll6 = QScrollArea()
        self.displayWidget6 = QGroupBox()
        self.ICachegrid = QGridLayout()
        self.ICacheTable = []
        for i in range(4):
            temp = self.labelTile("",100,120,0)
            temp.setAlignment(QtCore.Qt.AlignLeft)
            temp.setWordWrap(True)
            self.ICachegrid.addWidget(temp,i,0)
            tempp = self.labelTile("",100,800,False)
            tempp.setAlignment(QtCore.Qt.AlignLeft)
            tempp.setWordWrap(True)
            self.ICachegrid.addWidget(tempp,i, 1)
            self.ICacheTable.append([temp, tempp])
            
        self.displayWidget6.setLayout(self.ICachegrid)
        self.scroll6.setWidget(self.displayWidget6)
        self.scroll6.setWidgetResizable(True)
        
    def DCache(self):
        self.scroll7 = QScrollArea()
        self.displayWidget7 = QGroupBox()
        self.DCachegrid = QGridLayout()
        count = 0
        self.DCacheTable = []
        for i in range(4):
            temp = self.labelTile("",100,120,0)
            temp.setAlignment(QtCore.Qt.AlignLeft)
            temp.setWordWrap(True)
            self.DCachegrid.addWidget(temp,i,0)
            tempp = self.labelTile("",100,800,False)
            tempp.setAlignment(QtCore.Qt.AlignLeft)
            tempp.setWordWrap(True)
            self.DCachegrid.addWidget(tempp,i, 1)
            self.DCacheTable.append([temp, tempp])
            count+=1
            
        self.displayWidget7.setLayout(self.DCachegrid)
        self.scroll7.setWidget(self.displayWidget7)
        self.scroll7.setWidgetResizable(True)
        
    def lineEditTile(self):
        temp = QLineEdit("")
        temp.setValidator(QIntValidator())
        temp.setFixedHeight(40)
        temp.setFixedWidth(80)
        temp.setStyleSheet("border :1px solid white;")
        temp.setAlignment(QtCore.Qt.AlignCenter)
        return temp
    
    def checkBoxTile(self):
        temp = QCheckBox("")
        
        temp.setStyleSheet("QCheckBox::indicator"
                               "{"
                               "width :80px;"
                               "height : 40px;"
                               "}")
        
        return temp
        
    def controlBox(self):
        self.runMode()
        self.controlScroll = QScrollArea()
        self.displayWidget4 = QGroupBox()
        self.controlGrid = QGridLayout()
        self.controlTable = []
        
        controlsD = ["Cache(I$)", "Cache(D$)", "Block(I$)", "Block(D$)", "Way(I$)", "Way(D$)", "Compile", "Save","Theme", "K1", "K2", "K3", "K4", "K5", "K6"]
        for i in range(len(controlsD)):
            temp = self.labelTile(controlsD[i], 40, 130, 0)
            self.controlGrid.addWidget(temp, i+1, 0)
        
            
        for i in range(6):
            temp = self.lineEditTile()
            self.controlGrid.addWidget(temp, i+1 , 1)
            self.controlTable.append(temp)
        
        self.save_button = self.buttonTile("\U0001F4BE", 50, 40)
        self.compile_button = self.buttonTile("\U00002699", 50, 40)
        self.currentTheme = "Dark Theme"
        self.theme_button = self.buttonTile("\U0001F4A1", 50, 40)
        self.controlGrid.addWidget(self.compile_button, 7, 1)
        self.controlGrid.addWidget(self.save_button, 8, 1)
        self.controlGrid.addWidget(self.theme_button, 9, 1)
        
        
        self.controlGrid.addWidget(self.k1, 10, 1)
        self.controlGrid.addWidget(self.k2, 11, 1)
        self.controlGrid.addWidget(self.k3, 12, 1)
        self.controlGrid.addWidget(self.k4, 13, 1)
        self.controlGrid.addWidget(self.k5, 14, 1)
        self.controlGrid.addWidget(self.k6, 15, 1)
            
        self.controlTable[0].setText("64")
        self.controlTable[1].setText("64")
        self.controlTable[2].setText("4")
        self.controlTable[3].setText("4")
        self.controlTable[4].setText("2")
        self.controlTable[5].setText("2")
            
        self.displayWidget4.setLayout(self.controlGrid)
        self.controlScroll.setWidget(self.displayWidget4)
        self.controlScroll.setWidgetResizable(True)
        
    def mainLabel(self):
        
        
        main_label_image = QLabel()
        main_label_image_pixmap = QPixmap("GUI/Images/logo.png")
        main_label_image_pixmap = main_label_image_pixmap.scaled(300, 80)
        main_label_image.setPixmap(main_label_image_pixmap)
        main_label_hBox = QHBoxLayout()
        main_label_hBox.addWidget(main_label_image, 9)
        main_label_hBox.setContentsMargins(10, 10, 20, 10)
        
        return main_label_hBox
    
    def runMode(self):
        self.k1 = self.checkBoxTile()
        self.k2 = self.checkBoxTile()
        self.k3 = self.checkBoxTile()
        self.k4 = self.checkBoxTile()
        self.k5 = self.checkBoxTile()
        self.k6 = self.lineEditTile()
        self.k6.setValidator(QIntValidator())

        

    def editor(self, filePath):
        self.editorScroll = QScrollArea()
        self.editorlayout = QVBoxLayout()
        self.editorScreen = QPlainTextEdit()
        
        self.editorScreen.setFont(self.fixedfont)
        self.path = filePath
        self.editorlayout.addWidget(self.editorScreen)
        self.container = QGroupBox()
        
        self.container.setLayout(self.editorlayout)
        self.fileOpen()
        self.editorScreen.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.editorScroll.setWidget(self.container)
        self.editorScroll.setWidgetResizable(True)
        self.editorScroll.setFrameStyle(QFrame.NoFrame)
        self.container.setStyleSheet("border:none")
        self.editorScreen.setFrameStyle(QFrame.NoFrame)
        # self.container.setFrameStyle(QFrame.NoFrame)

    def datapath(self):
        self.displayWidget2 = QGroupBox()
        self.countDisplay = 1
        self.infoOfInstruction = self.labelTile("", 400, 100, 1)
        gridbox = QGridLayout()
        self.l1 = []
        l2 = []
        tt = 0
        name = ['F', 'D', 'E', 'MA', 'WB']
        color = ["Purple", "Orange", "Yellow", "Blue", "Pink"]
        for i in range(5):
            temp = self.buttonTile2(name[i], 140, 80, color[i])
            gridbox.addWidget(temp, 1, tt)
            
            self.l1.append(temp)
            tt+=1

        tempp = self.operationTile("\U00002212")
        gridbox.addWidget(tempp, 2, 1)
        self.l1.append(tempp)
        tempp = self.operationTile("\U00000031")
        gridbox.addWidget(tempp, 2, 2)
        self.l1.append(tempp)
        tempp = self.operationTile("\U0000002B")
        gridbox.addWidget(tempp, 2, 3)
        self.l1.append(tempp)
        tempp = self.labelTile("EE rs1", 40, 100,False)
        temp = self.labelTile("F", 40, 40,True)
        gridbox.addWidget(tempp, 3, 1)
        gridbox.addWidget(temp, 3, 3)
        self.l1.append(temp)
        tempp = self.labelTile("EE rs2", 40, 100,False)
        temp = self.labelTile("F", 40, 40,True)
        gridbox.addWidget(tempp, 4, 1)
        gridbox.addWidget(temp, 4, 3)
        self.l1.append(temp)
        tempp = self.labelTile("ME rs1", 40, 100,False)
        temp = self.labelTile("F", 40, 40,True)
        gridbox.addWidget(tempp, 5, 1)
        gridbox.addWidget(temp, 5, 3)
        self.l1.append(temp)
        tempp = self.labelTile("ME rs2", 40, 100,False)
        temp = self.labelTile("F", 40, 40,True)
        gridbox.addWidget(tempp, 6, 1)
        gridbox.addWidget(temp, 6, 3)
        self.l1.append(temp)
        tempp = self.labelTile("MM", 40, 100,False)
        temp = self.labelTile("F", 40, 40,True)
        gridbox.addWidget(tempp, 7, 1)
        gridbox.addWidget(temp, 7, 3)
        self.l1.append(temp)
        self.displayWidget2.setLayout(gridbox)
             
    def memoryDisplay(self):
        self.scroll = QScrollArea()
        self.displayWidget = QGroupBox()
        self.memoryArray = [[] for i in range(10)]
        gridbox = QGridLayout()
        tempA = self.labelTile("Address", 40, 160, 0)
        gridbox.addWidget(tempA, 0, 0)
        for i in range(4):
            tempB = self.labelTile("+"+str(i), 40, 40, 0)
            gridbox.addWidget(tempB, 0, i+1)
        
        
        for i in range(10):
            label = self.labelTile("0x", 40, 160, 0)
            self.memoryArray[i].append(label)
            gridbox.addWidget(self.memoryArray[i][0], i+1, 0)
            for j in range(4):
                temp = self.labelTile("", 40, 40, 1)
                self.memoryArray[i].append(temp)
                gridbox.addWidget(self.memoryArray[i][j + 1], i+1, j + 1)
                
        self.memoryArray.append([])
        self.tempLineEdit = QLineEdit()
        self.tempLineEdit.setFont(self.fixedfont)
        self.tempLineEdit.setFixedHeight(40)
        self.tempLineEdit.setFixedWidth(200)
        self.tempLineEdit.setStyleSheet("border :1px solid white;")
        self.tempLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.tempLineEdit.setMaxLength(8)
        self.tempLineEdit.setFixedWidth(300)
        self.jump_button =  self.buttonTile("Jump to", 30, 116)
        self.jump_button.setFont(self.fixedfont)
        self.memoryArray[-1].append(self.tempLineEdit)
        self.memoryArray[-1].append(self.jump_button)
        gridbox.addWidget(self.memoryArray[-1][0], 11, 0, 1, 16)
        gridbox.addWidget(self.memoryArray[-1][1], 11,3, 1, 20)

        gridbox.setVerticalSpacing(20)
        gridbox.setHorizontalSpacing(30)
        self.displayWidget.setLayout(gridbox)
        self.scroll.setWidget(self.displayWidget)
        # self.displayWidget.move(self.scroll.rect().center() - self.displayWidget.rect().center())
        
        self.scroll.setWidgetResizable(True)
        self.scroll.setFrameStyle(QFrame.NoFrame)
        self.displayWidget.setStyleSheet("border:none")
        
    def tabbedView1(self):
        self.tabs1 = QTabWidget()
        self.tabs1.setStyleSheet("border:none")
        self.tab1 = self.scroll1
        self.tab2 = self.scroll
        self.tab3 = self.infoScroll
        self.tab4 = self.controlScroll
        self.tab5 = self.scroll5
        self.tab6 = self.scroll6
        self.tab7 = self.scroll7
        self.tabs1.addTab(self.tab4, "Controls")
        self.tabs1.addTab(self.tab1, "Registers")
        self.tabs1.addTab(self.tab2, "Memory")
        self.tabs1.addTab(self.tab3, "Info")
        
        self.tabs1.addTab(self.tab5, "Cache Details")
        self.tabs1.addTab(self.tab7, "Data Cache")
        self.tabs1.addTab(self.tab6, "Instruction Cache")
        

    def tabbedView2(self):
        self.tabs2 = QTabWidget()
        self.tabs2.setStyleSheet("border:none")
        self.tabMain2 = self.editorScroll
        self.tabMain3 = self.displayWidget2
        
        
        self.tabs2.addTab(self.tabMain2, "Editor")
        self.tabs2.addTab(self.tabMain3, "Datapath")
        # self.tabs2.addTab(self.tabMain4, "Cache Control")

        


    def registerDisplay(self):
        self.scroll1 = QScrollArea()
        self.displayWidget = QGroupBox()
        gridbox = QGridLayout()
        self.registerArray = [[] for i in range(32)]
        
        for i in range(32):
            label1 = self.labelTile("x" + str(i), 40, 60, 0)
            label2 = self.labelTile("()", 40, 80, 0)
            temp = self.labelTile("", 40, 200, 1)
            self.registerArray[i] = [label1, label2, temp]
            gridbox.addWidget(self.registerArray[i][0], i+1, 0)
            gridbox.addWidget(self.registerArray[i][1], i+1, 1)
            gridbox.addWidget(self.registerArray[i][2], i+1, 2)

        
        # gridbox.setAlignment(QtCore.Qt.AlignCenter)
        self.displayWidget.setLayout(gridbox)
        self.scroll1.setWidget(self.displayWidget)
        self.scroll1.setWidgetResizable(True)
        
        
    def cacheDisplay(self):
        self.scroll5 = QScrollArea()
        self.displayWidget5 = QGroupBox()
        gridbox2 = QGridLayout()
        
        
        contents = ["Index", "Set", "isMiss", "Victim", "Access", "Hit", "Miss"]
        self.cacheArray = [[] for i in range(len(contents))]  
        self.cacheArray2 = []
        name = ["F", "L", "S"]
        color = ["Red", "Blue", "Green"]
        for i in range(3):
            temp = self.buttonTile2(name[i], 40, 40, color[i])
            gridbox2.addWidget(temp, 0, i) 
            self.cacheArray2.append(temp) 
                
        name = ["-", "1", "+"]
        for i in range(3):
            temp = self.buttonTile(name[i], 40, 40)
            gridbox2.addWidget(temp, 1, i)  
            self.cacheArray2.append(temp)     
        
        
        for i in range(len(contents)):
            label1 = self.labelTile(contents[i], 40, 100, 0)
            label2 = self.labelTile("-", 40, 100, 0)
            label2.setAlignment(QtCore.Qt.AlignLeft)
            label2.setWordWrap(True)
            
            self.cacheArray[i] = [label1, label2]
            gridbox2.addWidget(self.cacheArray[i][0], i+2, 0)
            gridbox2.addWidget(self.cacheArray[i][1], i+2, 1)
           
        # gridbox.setAlignment(QtCore.Qt.AlignCenter)
        self.displayWidget5.setLayout(gridbox2)
        self.scroll5.setWidget(self.displayWidget5)
        self.scroll5.setWidgetResizable(True)
