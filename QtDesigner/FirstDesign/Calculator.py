from email.mime import application
from PyQt5 import QtWidgets
import sys
from Ui_MainWindow import Ui_MainWindow

class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btncarp.clicked.connect(self.hesapla)
        self.ui.btntopla.clicked.connect(self.hesapla)
        self.ui.btnbol.clicked.connect(self.hesapla)
        self.ui.btncikar.clicked.connect(self.hesapla)

    def hesapla(self):
        sender = self.sender().text()
        result=0

        if sender == "Toplama":
            result = int(self.ui.txtsayi1.text())+int(self.ui.txtsayi2.text())
        elif sender == "Çıkarma":
            result = int(self.ui.txtsayi1.text())-int(self.ui.txtsayi2.text())
        elif sender == "Çarpma":
            result = int(self.ui.txtsayi1.text())*int(self.ui.txtsayi2.text())
        elif sender == "Bölme":
            result = int(self.ui.txtsayi1.text())/int(self.ui.txtsayi2.text())

        self.ui.sonuc.setText("Sonuç: "+str(result))     



def app():
    app = QtWidgets.QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())

app()