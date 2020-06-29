#This file writed by alirezaahani :)
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtWidgets import QApplication,QFileDialog
from PyQt5.QtCore import pyqtSlot
import ui,pytesseract
def Image_to_text(file):
    output = pytesseract.image_to_string(file)
    if not output == "":
        return output
    else:
        return "I can't see anything"
class App(QtWidgets.QMainWindow, ui.Ui_MainWindow):
    def __init__(self,parent=None):
        super(App,self).__init__(parent)
        self.setupUi(self)

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options = QFileDialog.DontUseNativeDialog
        user_file, _ = QFileDialog.getOpenFileName(self,"Please select a file", "","Image Files (*.png *jpg *.jpeg)", options=options)
        if user_file:
            self.user_contect.setText(Image_to_text(user_file))

    @pyqtSlot()
    def go_button_pressed(self):
        self.openFileNameDialog()


def main():
    mainApp = QApplication(['Image to text'])
    mainwindow = App()
    mainwindow.show()
    mainApp.exec_()


if __name__ == "__main__":
    main()
