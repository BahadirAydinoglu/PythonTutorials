import sys
from PyQt5  import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from UI_TableViewForm   import Ui_MainWindow

class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyApp,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.LoadProducts()
        self.ui.BtnAdd.clicked.connect(self.AddData)


    def AddData(self):
        name = self.ui.CityLine.text()
        plate = self.ui.PlateLine.text()

        if name and plate is not None:
            rowCount = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(rowCount)
            self.ui.tableWidget.setItem(rowCount,0,QTableWidgetItem(name))
            self.ui.tableWidget.setItem(rowCount,1,QTableWidgetItem(plate))

    def LoadProducts(self):
        products = [
            {"name": "Antalya" , "Plaka": "07"},
            {"name": "Ordu"    , "Plaka": "52"},
            {"name": "Samsun"  , "Plaka": "55"},
        ]
        self.ui.tableWidget.setRowCount(len(products))
        self.ui.tableWidget.setColumnCount(2)

        rowindex=0
        for product in products:
            self.ui.tableWidget.setItem(rowindex,0,QTableWidgetItem(product["name"]))
            self.ui.tableWidget.setItem(rowindex,1,QTableWidgetItem(product["Plaka"]))
            rowindex+=1

        # self.ui.tableWidget.setColumnCount(2)
        # self.ui.tableWidget.setRowCount(3)
        # self.ui.tableWidget.setHorizontalHeaderLabels(("Şehir","Plaka"))
        # self.ui.tableWidget.setItem(0,0,QTableWidgetItem("Antalya"))
        # self.ui.tableWidget.setItem(0,1,QTableWidgetItem("07"))
        # self.ui.tableWidget.setItem(1,0,QTableWidgetItem("Ordu"))
        # self.ui.tableWidget.setItem(1,1,QTableWidgetItem("52"))
        # self.ui.tableWidget.setItem(2,0,QTableWidgetItem("Samsun"))
        # self.ui.tableWidget.setItem(2,1,QTableWidgetItem("55"))
        

def App():
    app = QtWidgets.QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())

App()