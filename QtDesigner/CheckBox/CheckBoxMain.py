import sys
from PyQt5 import QtWidgets
from Ui_CheckBox import Ui_MainWindow

class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyApp,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.CbSinema.stateChanged.connect(self.show_state)  # show_state metodu her seçimde çalışacak.
        self.ui.CbKitap.stateChanged.connect(self.show_state)  # show_state metodu her seçimde çalışacak.
        self.ui.CbSpor.stateChanged.connect(self.show_state)  # show_state metodu her seçimde çalışacak.

        self.ui.ButonSecim.clicked.connect(self.getinfo)

    def show_state(self,value):
        #print(value)
        #print(self.ui.CbSinema.isChecked()) # True ya da False Değeri Döndürür
        #print(self.ui.CbSinema.text())  # Text Değerini Döndürür
        cb=self.sender()
        print(cb.text())
        print(cb.isChecked())

    def getinfo(self):
        Result = ""
        items = self.ui.centralwidget.findChildren(QtWidgets.QCheckBox)  #QtWidgetsın altındaki QCheckboxların hepsini alıyor.
        for i in items:
            if(i.isChecked()):   # Sadece seçilenleri alıyoruz
                Result += i.text() +"\n" #Seçilenleri Resultun içine attık
        self.ui.LabelResult.setText(Result)


def App():
    app = QtWidgets.QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())

App()