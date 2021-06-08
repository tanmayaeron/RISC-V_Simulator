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
from GUI.temp import PythonHighlighter
import qtawesome as qta

import syntax
class UiComponents():
    def __init__(self):
        font1 = QFontDatabase.applicationFontFamilies(0)[0]
        self.fixedfont = QFont(font1, 14)
        # self.fixedfont.setPointSize(16)
        self.fixedfont2 = QFontDatabase.systemFont(QFontDatabase.FixedFont)
        self.fixedfont2.setPointSize(16)
        

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
        button.setFixedHeight(height)
        button.setFixedWidth(width)
        return button
    # def labelTile2(self, name, height, width)

    def labelTile(self, labelName, height, width, isBorder, isCenter = 1):
        temp = QLabel()
        temp.setText(labelName)
        temp.setFont(self.fixedfont)
        temp.setFixedHeight(height)
        temp.setFixedWidth(width)
        if (isBorder):
            temp.setStyleSheet("border :1px solid white;")
        if(isCenter):
            temp.setAlignment(QtCore.Qt.AlignCenter)
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

    def buttonTile2(self, labelName, height, width, color = "black"):
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


    def IDCache(self):
        self.table1 = QTableWidget()
        self.table2 = QTableWidget()
        self.table1.setFont(self.fixedfont)
        self.table2.setFont(self.fixedfont)
        self.table1.horizontalHeader().setStretchLastSection(True)
        self.table1.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table2.horizontalHeader().setStretchLastSection(True)
        self.table2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
      
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
                               "width :40px;"
                               "height : 40px;"
                               "}")
        
        return temp
        
    def controlBox(self):
        self.runMode()
        self.controlScroll = QScrollArea()
        self.displayWidget4 = QGroupBox()
        self.controlGrid = QGridLayout()
        self.controlTable = []
        controlsD = ["Cache(I$)", "Cache(D$)", "Block(I$)", "Block(D$)", "Way(I$)", "Way(D$)", "Pipelined", "Forwarding", "Machine Code", "Replacement(I$)","Replacement(D$)", "Branch Pre.", "Initial State"]
        for i in range(len(controlsD)):
            temp = self.labelTile(controlsD[i], 40, 200, 0, 0)
            self.controlGrid.addWidget(temp, i+1, 0)
        
        
        
            
        for i in range(6):
            temp = self.lineEditTile()
            self.controlGrid.addWidget(temp, i+1 , 1)
            self.controlTable.append(temp)

        self.controlGrid.addWidget(self.k1, 7, 1)
        self.controlGrid.addWidget(self.k2, 8, 1)
        self.controlGrid.addWidget(self.k3, 9, 1)
        
        self.k7 = self.buttonTile2("LRU", 30, 100)
        # self.k7.addItems(["LRU", "FIFO", "Random", "NRU"])
        
        self.k8 = self.buttonTile2("LRU", 30, 100)
        self.k9 = self.buttonTile2("AT", 30, 100)
        
        self.k10 = self.buttonTile2("Taken", 30, 100)

        self.controlGrid.addWidget(self.k7, 10, 1)
        self.controlGrid.addWidget(self.k8, 11, 1)
        self.controlGrid.addWidget(self.k9, 12, 1)
        self.controlGrid.addWidget(self.k10, 13, 1)
        
            
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
        main_label_image_pixmap = main_label_image_pixmap.scaled(450, 140)
        self.save_button = self.buttonTile("\U0001F4BE", 50, 40)
        self.compile_button = self.buttonTile("\U00002699", 50, 40)
        self.load_button = self.buttonTile("\U000021E9", 50, 40)
        self.step_button = self.buttonTile("\U000000BB", 50, 40)
        
        main_label_image.setPixmap(main_label_image_pixmap)
        main_label_hBox = QHBoxLayout()
        main_label_hBox.addWidget(main_label_image)
        
        main_label_hBox.addWidget(self.compile_button)
        main_label_hBox.addWidget(self.save_button)
        main_label_hBox.addWidget(self.load_button)
        main_label_hBox.addWidget(self.step_button)
        main_label_hBox.addSpacing(40)
        # main_label_hBox.setAlignment(QtCore.Qt.AlignCenter)
        return main_label_hBox
    
    def runMode(self):
        self.k1 = self.checkBoxTile()
        self.k2 = self.checkBoxTile()
        self.k3 = self.checkBoxTile()
        self.k4 = self.checkBoxTile()
        self.k5 = self.checkBoxTile()
        self.k6 = self.lineEditTile()
        self.k6.setValidator(QIntValidator())


    def developerInfo(self):
        self.about = QMessageBox()
        self.about.setTitle("about RISC-V simulator")
        self.about.setText("assembly to machine code\n conversion of RISC-V ISA\n\npython simulation of\nmachine level execution of\nRISC-V 32 bit instructions.\n"+
                           "This project is developed by\nAneeket\nShikhar\nTanmay\nHet\nAditya\nSource code can be found at\nhttps://github.com/tanmayaeron/RISC-V_Simulator")
        self.about.exec_()
        
        
    def createMenuBar(self):
        self.menuBar =  QMenuBar(self)
        
        fileMenu = QMenu("&File", self)
        self.menuBar.addMenu(fileMenu)
        editMenu = self.menuBar.addMenu("&Edit")
        helpMenu = self.menuBar.addMenu("&Help")
        

    def editor(self, filePath):
        self.editorScroll = QScrollArea()
        self.editorlayout = QVBoxLayout()
        self.editorScreen = QPlainTextEdit()
        self.editorScreen.setStyleSheet("background-color: '#00171F'")
        self.editorScreen.setFont(self.fixedfont2)
        # self.editorScreen.setFont()s
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
        
    def statsDisplay(self):
        self.statsScroll = QScrollArea()
        self.statsWidget = QGroupBox()
        gridbox = QGridLayout()
        
        d = ["Cycles", "Instructions", "CPI", "Data instructions", "ALU instructions", "Control instructions", "Stall Count", "Data Hazard", "Control Hazard", "Mispredictions", "data stalls", "control stalls"]
        self.statsArray = []
        for i in range(len(d)):
            label = self.labelTile(d[i], 40, 260, 0, 0)
            gridbox.addWidget(label, i+1, 0)
            
            label = self.labelTile("0", 40, 60, 0)
            gridbox.addWidget(label, i+1, 1)
            self.statsArray.append(label)
      
        gridbox.setVerticalSpacing(20)
        gridbox.setHorizontalSpacing(30)
        self.statsWidget.setLayout(gridbox)
        self.statsScroll.setWidget(self.statsWidget)
        self.statsScroll.setWidgetResizable(True)
        self.statsScroll.setFrameStyle(QFrame.NoFrame)
        self.statsWidget.setStyleSheet("border:none")
        

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

        # self.text = self.labelTile("Display\nsettings",80,160,0)
        # self.selectMemoryFormat = QComboBox()
        # self.selectMemoryFormat.addItems(["Hex","Decimal","Unsigned","ASCII"])
        # self.selectMemoryFormat.setStyleSheet("border :1px solid white;")
        # self.selectMemoryFormat.setFont(self.fixedfont)
        # gridbox.addWidget(self.text,12,0)
        # gridbox.addWidget(self.selectMemoryFormat,12,2,1,3)

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
        self.tabs1.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabs1.setIconSize(QtCore.QSize(60, 60))
        self.tabs1.setStyleSheet("border:none")
        self.tab1 = self.scroll1
        self.tab2 = self.scroll
        self.tab3 = self.infoScroll
        self.tab4 = self.controlScroll
        self.tab5 = self.scroll5
        self.tab6 = self.table1
        self.tab7 = self.table2
        self.tab8 = self.statsScroll
        
        self.tabs1.addTab(self.tab4, QIcon("GUI/Images/controls.png"), "")
        self.tabs1.addTab(self.tab1, QIcon("GUI/Images/registers.png"), "")
        self.tabs1.addTab(self.tab2, QIcon("GUI/Images/memory.png"), "")
        self.tabs1.addTab(self.tab8, QIcon("GUI/Images/stats.png"), "")
        self.tabs1.addTab(self.tab3, QIcon("GUI/Images/cache.png"), "")
        
        # self.tabs1.addTab(self.tab5, "Cache Details")
        # self.tabs1.addTab(self.tab6, "D$ Cache")
        # self.tabs1.addTab(self.tab7, "I$ Cache")


    def tabbedView2(self):
        self.tabs2 = QTabWidget()
        self.tabs2.setStyleSheet("border:none")
        
        self.tabMain2 = self.editorScroll
        self.tabMain3 = self.displayWidget2
        # self.tabMain4 = 
        # self.tabs2.addTab(self.tab4, "Controls")
        self.tabs2.addTab(self.tabMain2, "Code")
        self.tabs2.addTab(self.tabMain3, "Visualise")


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
            gridbox.addWidget(self.registerArray[i][0], i, 0)
            gridbox.addWidget(self.registerArray[i][1], i, 1)
            gridbox.addWidget(self.registerArray[i][2], i, 2)

        # self.text = self.labelTile("Display\nsettings", 80, 160, 0)
        # self.selectMemoryFormat = QComboBox()
        # self.selectMemoryFormat.addItems(["Hex", "Decimal", "Unsigned", "ASCII"])
        # self.selectMemoryFormat.setStyleSheet("border :1px solid white;")
        # self.selectMemoryFormat.setFont(self.fixedfont)
        # gridbox.addWidget(self.text, 32, 0)
        # gridbox.addWidget(self.selectMemoryFormat, 32, 2)


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
            label1 = self.labelTile(contents[i], 100, 100, 0)
            label3  = self.labelTile("", 100, 100, 0)
            label2 = self.labelTile("-", 100, 600, 0)
            # label2.setAlignment(QtCore.Qt.AlignLeft)
            label2.setWordWrap(True)
            
            self.cacheArray[i] = [label1, label2]
            gridbox2.addWidget(self.cacheArray[i][0], i+2, 0)
            gridbox2.addWidget(label3, i+2, 1)
            
            gridbox2.addWidget(self.cacheArray[i][1], i+2, 2)
           
        # gridbox.setAlignment(QtCore.Qt.AlignCenter)
        self.displayWidget5.setLayout(gridbox2)
        self.scroll5.setWidget(self.displayWidget5)
        self.scroll5.setWidgetResizable(True)
