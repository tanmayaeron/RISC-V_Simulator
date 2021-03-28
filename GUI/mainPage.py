from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import qtawesome as iconPack
import qdarkstyle
from register import RegisterFile
from memory import Memory

class UiComponents(RegisterFile, Memory):
    def __init__(self):
        super().__init__()
        self.fixedfont = QFontDatabase.systemFont(QFontDatabase.FixedFont)
        self.fixedfont.setPointSize(14)
        
        
    def buttonTile(self, name):
        button = QPushButton()
        button.setText(name)
        button.setFixedHeight(30)
        button.setFixedWidth(50)
        return button
    
    def updateRegisterView(self):
        for i in range(32):
            currValue = self.get_register(i)
            self.registerArray[i].setText("0x"+str(currValue))
            
    def updateMemoryView(self, address):
        l = self.getMemoryDisplay(address)
        for i in range(10):
            for j in range(4):
                print(l[i*4 + j])
                self.memoryArray[i][j].setText(l[i*4 + j])
             

    def mainLabel(self, top, left, height, width):
        save_button = self.buttonTile("Save")
        save_button.clicked.connect(lambda: self.fileSave())
        save_button.setContentsMargins(10,10,20,10)
        
        main_label_image = QLabel()
        main_label_image_pixmap = QPixmap("GUI/Images/logo.png")
        main_label_image_pixmap = main_label_image_pixmap.scaled(400, 60)
        main_label_image.setPixmap(main_label_image_pixmap)
        main_label_hBox = QHBoxLayout()
        main_label_hBox.addWidget(main_label_image)
        main_label_hBox.addWidget(save_button)
        main_label_hBox.setContentsMargins(10, 10, 10, 10)
        return main_label_hBox


    def editor(self):
        self.editorScroll = QScrollArea()
        self.editorlayout = QVBoxLayout()
        self.editorScreen = QPlainTextEdit()
        self.editorScreen.setFont(self.fixedfont)
        self.path = 'test/test1.mc'
        self.editorlayout.addWidget(self.editorScreen)
        self.container = QGroupBox()
        self.container.setLayout(self.editorlayout)
        self.fileOpen()
        self.editorScreen.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.editorScroll.setWidget(self.container)
        self.editorScroll.setWidgetResizable(True)
        
        
    def team(self):
        self.members = ["Aneeket", "Tanmay", "Shikhar", "Het", "Aditya"]
        pass
        
    def fileOpen(self):
        path = self.path
        f = open(path, 'r')
        text = f.read()
        self.path = path
        self.editorScreen.setPlainText(text)

    def fileSave(self):
        path = self.path
        text = self.editorScreen.toPlainText()
        f = open(path, 'w')
        f.write(text)
        self.path = path

    def memoryDisplay(self):
        self.scroll = QScrollArea()
        self.scroll.setFrameShape = None
        self.displayWidget = QGroupBox()
        self.memoryArray = []
        vbox = QGridLayout()
        for i in range(10):
            self.memoryArray.append([])
            label = QLabel("Ox"+'0'*7+str(i+1))
            label.setFont(self.fixedfont)
            self.memoryArray[-1].append(label)
            vbox.addWidget(self.memoryArray[-1][-1], i, 0)
            
            for j in range(4):
                temp = QLabel()
                temp.setText("a")
                temp.setFont(self.fixedfont)
                temp.setFixedHeight(40)
                temp.setFixedWidth(40)
                temp.setStyleSheet("border :1px solid white;")
                temp.setAlignment(QtCore.Qt.AlignCenter) 
                self.memoryArray[-1].append(temp)
                
                vbox.addWidget(self.memoryArray[-1][-1], i, j+1)
                   
        self.updateMemoryView("00000000")
        self.displayWidget.setLayout(vbox)
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
        self.scroll1.setFrameShape = None
        self.displayWidget = QGroupBox()
        vbox = QGridLayout()
        self.registerArray = []
        for i in range(32):
            label = QLabel("x"+str(i))
            vbox.addWidget(label, i, 0)
            label2 = QLabel("("+ self.get_alt_name(i)+")")
            label2.setFont(self.fixedfont)
            vbox.addWidget(label2, i, 1)
            label.setFont(self.fixedfont)
            
            temp = QLabel()
            self.registerArray.append(temp)
            self.registerArray[i].setFont(self.fixedfont)
            self.registerArray[i].setFixedHeight(40)
            self.registerArray[i].setFixedWidth(160)
            self.registerArray[i].setStyleSheet("border :1px solid white;")
            self.registerArray[i].setAlignment(QtCore.Qt.AlignCenter)
            vbox.addWidget(self.registerArray[i], i, 2)
            
        self.updateRegisterView()
        self.displayWidget.setLayout(vbox)
        self.scroll1.setWidget(self.displayWidget)
        self.scroll1.setWidgetResizable(True)

class mainScreen(QWidget, UiComponents):
    def __init__(self):
        super().__init__()
        self.title = "RISC-V Simulator"
        self.subTitle = "Made by SAATH"
        self.top = 200
        self.left = 100
        self.width = 1400
        self.height = 900
        self.iconName = "GUI/Images/logo.png"
    
        self.splash = QSplashScreen(QPixmap(self.iconName), Qt.WindowStaysOnTopHint)
        QTimer.singleShot(3000, self.initWindow)
        self.splash.show()
        
        

    def initWindow(self):
        self.splash.close()
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)
        logo_label = self.mainLabel(top=100, left=100, width=200, height=50)
        self.editor()
        
        self.memoryDisplay()
        self.registerDisplay()
        self.tabbedView1()
        self.tabbedView2()
        memoryDisplay = self.tabs
        feed = self.tabsMain
        hbox = QHBoxLayout()
        hbox.addWidget(feed,10)
        hbox.addWidget(memoryDisplay, 4)
        hbox.setContentsMargins(10,10,10,10)
        vbox = QVBoxLayout()
        vbox.addLayout(logo_label)
        vbox.addLayout(hbox)
        vbox.setContentsMargins(10,10,10,10)
        self.setLayout(vbox)

        self.show()

App = QApplication(sys.argv)

App.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))
window = mainScreen()
sys.exit(App.exec_())