import sys
from PyQt5 import QtWidgets
from Ui_RadioButton import Ui_MainWindow

class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyApp,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.RBTurkiye.setChecked(True)
        self.ui.RBIlk.setChecked(True)

        
        self.ui.RBTurkiye.toggled.connect(self.OnClickedCountry)
        self.ui.RBAzerbaycan.toggled.connect(self.OnClickedCountry)
        self.ui.RBAlmanya.toggled.connect(self.OnClickedCountry)
        self.ui.RBIsvec.toggled.connect(self.OnClickedCountry)

        self.ui.RBIlk.toggled.connect(self.OnClickedEdu)
        self.ui.RBLise.toggled.connect(self.OnClickedEdu)
        self.ui.RBLisans.toggled.connect(self.OnClickedEdu)
        self.ui.RBYuksekLisans.toggled.connect(self.OnClickedEdu)

        self.ui.pushButton.clicked.connect(self.GetSelectedCountry)
        self.ui.pushButton_2.clicked.connect(self.GetSelectedEdu)


    def OnClickedCountry(self):
        RB = self.sender()
        if RB.isChecked():
            print(RB.text())

    def OnClickedEdu(self):
        RB=self.sender()
        if(RB.isChecked()):
            print(RB.text())

    def GetSelectedCountry(self):        
        items = self.ui.groupBox.findChildren(QtWidgets.QRadioButton)
        for rb in items:
            if (rb.isChecked()):
                self.ui.LBUlke.setText(rb.text())
                

    def GetSelectedEdu(self):
        items=self.ui.groupBox_2.findChildren(QtWidgets.QRadioButton)
        for rb in items:
            if(rb.isChecked()):
                self.ui.LBEgitim.setText(rb.text())

def App():
    app = QtWidgets.QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())

App()