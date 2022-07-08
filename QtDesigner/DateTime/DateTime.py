import sys
from PyQt5 import QtWidgets
from UI_DateTimeForm import Ui_MainWindow
from PyQt5.QtCore   import QDate,QTime,QDateTime

class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyApp,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.BtnCalc.clicked.connect(self.Calculate)


    def Calculate(self):
        start = self.ui.dateStart.date()
        end   = self.ui.dateEnd.date()
        print(start,end)

        print("Days in Month: {0}".format(start.daysInMonth()))
        print("Days in Year: {0}".format(start.daysInYear()))   





def App():
    app = QtWidgets.QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())

App()