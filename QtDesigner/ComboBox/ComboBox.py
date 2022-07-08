import sys
from PyQt5 import QtWidgets
from UI_ComboBox import Ui_MainWindow


class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyApp,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        Combo = self.ui.CBSehirler
        Combo.addItem("ANKARA")
        Combo.addItem("ANTALYA")
        Combo.addItem("ORDU")
        #self.addItems(["ADANA","IZMIR","EDIRNE"])

        self.ui.BTLoadItem.clicked.connect(self.LoadItems)
        self.ui.BTGetItem.clicked.connect(self.GetItem)

        self.ui.CBSehirler.currentIndexChanged.connect(self.Selected) 

    def LoadItems(self):
        Sehirler = ["ADANA","IZMIR","EDIRNE"]
        self.ui.CBSehirler.addItems(Sehirler)

    def GetItem(self):
        print(self.ui.CBSehirler.currentText())
        print(self.ui.CBSehirler.currentIndex())

    def Selected(self,text):
        print(text)
        



def App():
    app = QtWidgets.QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())

App()
