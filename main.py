from GUI.mainPage import *

if __name__ == '__main__':
    App = QApplication(sys.argv)
    App.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))
    window = mainScreen(App)
    sys.exit(App.exec_())
        
