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

    def buttonTile(self, name, height, width):
        button = QPushButton()
        button.setText(name)
        button.setFont(self.fixedfont)
        button.setFixedHeight(height)
        button.setFixedWidth(width)
        return button

    def labelTile(self, labelName, height, width, isBorder):
        temp = QLabel()
        temp.setText(labelName)
        temp.setFont(self.fixedfont)
        temp.setFixedHeight(height)
        temp.setFixedWidth(width)
        if (isBorder):
            temp.setStyleSheet("border :1px solid white;")
        temp.setAlignment(QtCore.Qt.AlignCenter)
        return temp

    def mainLabel(self, top, left, height, width):
        self.save_button = self.buttonTile("Save", 50, 100)
        self.compile_button = self.buttonTile("Compile", 50, 100)
        self.currentTheme = "Dark Theme"
        self.theme_button = self.buttonTile("Change\nTheme", 50, 100)
        self.theme_button.setContentsMargins(10,10,20,10)
        self.save_button.setContentsMargins(10, 10, 20, 10)
        self.compile_button.setContentsMargins(10, 10, 20, 10)
        main_label_image = QLabel()
        main_label_image_pixmap = QPixmap("GUI/Images/logo.png")
        main_label_image_pixmap = main_label_image_pixmap.scaled(300, 80)
        main_label_image.setPixmap(main_label_image_pixmap)
        main_label_hBox = QHBoxLayout()
        main_label_hBox.addWidget(main_label_image)
        main_label_hBox.addWidget(self.save_button)
        main_label_hBox.addWidget(self.compile_button)
        main_label_hBox.addWidget(self.theme_button)
        main_label_hBox.setContentsMargins(10, 10, 10, 10)
        return main_label_hBox

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


    def memoryDisplay(self):
        self.scroll = QScrollArea()
        self.displayWidget = QGroupBox()
        self.memoryArray = [[] for i in range(10)]
        gridbox = QGridLayout()
        tempA = self.labelTile("Address", 40, 160, 0)
        gridbox.addWidget(tempA, 0, 0)
        for i in range(4):
            tempB = self.labelTile("+"+str(i+1), 40, 40, 0)
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
        self.memoryArray[-1].append(self.tempLineEdit)
        self.memoryArray[-1].append(self.jump_button)
        gridbox.addWidget(self.memoryArray[-1][0], 11, 0, 1, 16)
        gridbox.addWidget(self.memoryArray[-1][1], 11,3, 1, 20)

        gridbox.setVerticalSpacing(20)
        gridbox.setHorizontalSpacing(30)
        self.displayWidget.setLayout(gridbox)
        self.scroll.setWidget(self.displayWidget)
        self.scroll.setWidgetResizable(True)

    def tabbedView1(self):
        self.tabs = QTabWidget()
        self.tab1 = self.scroll1
        self.tab2 = self.scroll
        self.tabs.addTab(self.tab1, "Registers")
        self.tabs.addTab(self.tab2, "Memory")

    def tabbedView2(self):
        self.tabsMain = QTabWidget()
        self.tabMain1 = self.editorScroll
        self.tabsMain.addTab(self.tabMain1, "Editor")

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


class mainScreen(QWidget, UiComponents):
    def __init__(self, App):
        super().__init__()
        self.App = App
        self.title = "RISC-V Simulator"
        self.directoryPath = os.getcwd()
        self.currFilePath = os.path.join(self.directoryPath, "test", "main.mc")
        self.link = frontBackEndInteraction(self.directoryPath)
        self.iconName = os.path.join(self.directoryPath, "GUI", "Images", "logo.png")
        self.splash = QSplashScreen(QPixmap(self.iconName), Qt.WindowStaysOnTopHint)
        QTimer.singleShot(3000, self.initWindow)
        self.splash.show()

    def updateRegisterView(self):
        alt = getAltNameOfRegister()
        val = self.link.getRegisterSnapshot()
        for i in range(32):
            self.registerArray[i][1].setText(str(alt[i]))
            self.registerArray[i][2].setText("0x" + str(val[i]))

    def updateMemoryView(self, address):
        l = self.link.getMemorySnapshot(address)
        for i in range(10):
            for j in range(5):
                self.memoryArray[i][j].setText(l[i][j])

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
        self.link.runProgram(self.currFilePath)
        self.compile_button.setText("\U00002705")
        self.updateRegisterView()
        self.updateMemoryView("10000000")
        
    def jumpAddress(self):
        a = self.tempLineEdit.text()
        if(len(a) == 8):
            self.updateMemoryView(a)
        
    def changeTheme(self):
        if self.currentTheme == "Dark Theme":
            self.currentTheme = "Light Theme"
            self.App.setStyleSheet("")
        else:
            self.currentTheme = "Dark Theme"
            self.App.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5', palette=DarkPalette))

    def initWindow(self):
        self.splash.close()
        self.setWindowTitle(self.title)
        logo_label = self.mainLabel(top=100, left=100, width=200, height=50)

        self.editor(self.currFilePath)
        self.memoryDisplay()
        self.registerDisplay()
        self.save_button.clicked.connect(lambda: self.fileSave())
        self.compile_button.clicked.connect(lambda: self.fileCompile())
        self.theme_button.clicked.connect(lambda: self.changeTheme())
        self.jump_button.clicked.connect(lambda: self.jumpAddress())

        self.updateMemoryView("10000000")
        self.updateRegisterView()

        self.tabbedView1()
        self.tabbedView2()

        memoryDisplay = self.tabs
        feed = self.tabsMain

        hbox = QHBoxLayout()
        hbox.addWidget(feed, 10)
        hbox.addWidget(memoryDisplay, 4)
        hbox.setContentsMargins(10, 10, 10, 10)
        vbox = QVBoxLayout()
        vbox.addLayout(logo_label)
        vbox.addLayout(hbox)
        vbox.setContentsMargins(10, 10, 10, 10)
        self.setLayout(vbox)
        self.showMaximized()



