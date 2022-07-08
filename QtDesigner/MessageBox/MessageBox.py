from email.message import Message
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from UI_MessageBoxForm import Ui_MainWindow

class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyApp,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.BtnExit.clicked.connect(self.ShowDialog)

    def ShowDialog(self):
        msg = QMessageBox()
        msg.setWindowTitle("Close Application") 
        msg.setText("Are you sure?")
        msg.setIcon(QMessageBox.Question) # Popup mesaja icon ekledik
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.setDefaultButton(QMessageBox.Ok)  # Default seçili
        msg.setDetailedText("Details...")
        msg.buttonClicked.connect(self.popup_button)
        x = msg.exec_()

    def popup_button(self,i):
        print(i.text())
        if(i.text() == "&OK"):
            print("OKEY")
            QtWidgets.qApp.quit()  #Formu kapatır
        elif i.text() =="&Cancel":
            print("Cancel")
        else:
            print("Ignore")


        

def App():
    app = QtWidgets.QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())

App()
