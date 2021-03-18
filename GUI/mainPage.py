from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import qtawesome as iconPack
class UiComponents():
    def __init__(self):
        super().__init__()


    def mainLabel(self, top, left, height, width):
        # main_label_text = QLabel()
        # main_label_text.setText("RISC-V Simulator")
        # main_label_text.setFont(QFont("Gotham", 39))
        # main_label_text.setContentsMargins(10,10,20,10)
        main_label_image = QLabel()
        main_label_image_pixmap = QPixmap("GUI/Images/logo.png")
        main_label_image_pixmap = main_label_image_pixmap.scaled(400, 60)
        main_label_image.setPixmap(main_label_image_pixmap)
        main_label_hBox = QHBoxLayout()
        main_label_hBox.addWidget(main_label_image)
        # main_label_hBox.addWidget(main_label_text)
        main_label_hBox.setContentsMargins(10, 10, 10, 10)
        return main_label_hBox

    def buttonTile(self, link):
        button = QPushButton()
        button.setFixedHeight(320)
        button.setFixedWidth(200)
        button.setStyleSheet("border-bottom :10px solid;"
                             "border-bottom-color : blue;")
        button.clicked.connect(lambda: self.openFile(link))
        return button

    def yourFeed(self):
        self.groupBox = QGroupBox("Editor")
        self.gridLayout = QGridLayout()
        self.scroller = QScrollArea()
        self.scroller.setWidget(self.groupBox)
        self.scroller.setWidgetResizable(True)

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
        self.yourFeed()
        feed = self.scroller
        
        self.memoryDisplay()
        memoryDisplay = self.displayWidget
        hbox = QHBoxLayout()
        hbox.addWidget(feed,11)
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