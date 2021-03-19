from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import qtawesome as iconPack
class UiComponents():
    def __init__(self):
        super().__init__()
        
        
    def buttonTile(self):
        button = QPushButton()
        button.setText("save")
        button.setFixedHeight(50)
        button.setFixedWidth(50)
        button.setStyleSheet("border-bottom :10px solid;"
                             "border-bottom-color : blue;")
        button.clicked.connect(lambda: self.fileSave())
        return button


    def mainLabel(self, top, left, height, width):
        main_label_text = self.buttonTile()
        main_label_text.setContentsMargins(10,10,20,10)
        main_label_image = QLabel()
        main_label_image_pixmap = QPixmap("GUI/Images/logo.png")
        main_label_image_pixmap = main_label_image_pixmap.scaled(400, 60)
        main_label_image.setPixmap(main_label_image_pixmap)
        main_label_hBox = QHBoxLayout()
        main_label_hBox.addWidget(main_label_image)
        main_label_hBox.addWidget(main_label_text)
        main_label_hBox.setContentsMargins(10, 10, 10, 10)
        return main_label_hBox

    


        
    def editor(self):
        self.editorlayout = QVBoxLayout()
        self.editorScreen = QPlainTextEdit()
        fixedfont = QFontDatabase.systemFont(QFontDatabase.FixedFont)
        fixedfont.setPointSize(14)
        self.editorScreen.setFont(fixedfont)
        self.path = 'test/test1.mc'
        self.editorlayout.addWidget(self.editorScreen)
        self.container = QGroupBox("Editor")
        self.container.setLayout(self.editorlayout)
        self.fileOpen()
        self.editorScreen.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

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
        self.displayWidget = QGroupBox("Memory Lookup")
        vbox = QVBoxLayout()
        for i in range(10):
            label = QLabel("Ox"+str(i+1))
            label.setAlignment(Qt.AlignCenter)
            vbox.addWidget(label)
        self.displayWidget.setLayout(vbox)
        self.displayWidget.setContentsMargins(10,10,10,10)


class mainScreen(QWidget, UiComponents):
    def __init__(self):
        super().__init__()
        
        self.title = "RISC-V Simulator"
        self.subTitle = "Made by TAASH"
        self.top = 100
        self.left = 100
        self.width = 1400
        self.height = 900
        self.iconName = "GUI/Images/logo.png"
        
        self.initWindow()

    def initWindow(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        
  
        self.setGeometry(self.left, self.top, self.width, self.height)
        logo_label = self.mainLabel(top=100, left=100, width=200, height=50)
        
        self.editor()
        feed = self.container
        
        self.memoryDisplay()
        memoryDisplay = self.displayWidget
        hbox = QHBoxLayout()
        hbox.addWidget(feed,10)
        hbox.addWidget(memoryDisplay, 5)
        hbox.setContentsMargins(10,10,10,10)
        vbox = QVBoxLayout()
        vbox.addLayout(logo_label)
        vbox.addLayout(hbox)
        vbox.setContentsMargins(10,10,10,10)
        self.setLayout(vbox)
        
        self.show()

App = QApplication(sys.argv)
window = mainScreen()
sys.exit(App.exec_())