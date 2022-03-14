from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys 


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(100, 100, 1920, 1080)
    win.setWindowTitle("GUI")

    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    window()
    