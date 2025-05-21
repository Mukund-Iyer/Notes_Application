from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys
from PyQt5.QtWidgets import QFileDialog

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi("Main_Window.ui", self)  # Load the .ui file
        self.setWindowTitle("Notes v1")
        self.actionExit.triggered.connect(self.exit_application)

    def exit_application(self):
        # Define what happens when ExitMenuItem is triggered
        sys.exit()

app = QtWidgets.QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec_())
