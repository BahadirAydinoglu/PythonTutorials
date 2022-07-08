import sys
from PyQt5  import QtWidgets
from UI_ListViewForm   import Ui_MainWindow
from PyQt5.QtWidgets import QInputDialog,QLineEdit,QMessageBox


class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyApp,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #Load Students
        self.LoadStudents()
        #Add New Student
        self.ui.BtnAdd.clicked.connect(self.AddStudent)
        #Edit Student
        self.ui.BtnEdit.clicked.connect(self.EditStudent)
        #Delete Student
        self.ui.BtnRemove.clicked.connect(self.RemoveStudent)
        #Up Student
        self.ui.BtnUp.clicked.connect(self.UpStudent)
        #Down Student
        self.ui.BtnDown.clicked.connect(self.DownStudent)
        #Sort Student
        self.ui.BtnSort.clicked.connect(self.SortStudent)
        #Close UI
        self.ui.BtnExit.clicked.connect(self.CloseUI)

    def LoadStudents(self):
        self.ui.ListItems.addItems(["Bahadir","Irem","Ruya"])
        self.ui.ListItems.setCurrentRow(0) # İlk eleman otomatik seçili

    def AddStudent(self):
        text, ok = QInputDialog.getText(self,"New Student", "Student Name")      #getInt ile sayı değeri de alabiliriz
        if ok and text is not None:
            self.ui.ListItems.insertItem(0,text)    #Girilen ismi en üste ekledik

    def EditStudent(self):
        CurrentIndex = self.ui.ListItems.currentRow()  #Seçili index numarasını aldık
        item = self.ui.ListItems.item(CurrentIndex)    #Listitemin seçili index numarasının textini aldık
        if item is not None:
            text, ok =QInputDialog.getText(self,"Edit Student", "Student Name", QLineEdit.Normal,item.text()) #Texti ekrana yazdırdık
            if text and ok is not None:
                item.setText(text) # Eğer boş değil ise değiştirdik

    def RemoveStudent(self):
        CurrentIndex = self.ui.ListItems.currentRow()  #Seçili index numarasını aldık
        item = self.ui.ListItems.item(CurrentIndex)    #Listitemin seçili index numarasının textini aldık
        if item is None:
            return

        q = QMessageBox.question(self, "Remove Student","Do you want remove student?"+str(item.text()),QMessageBox.No | QMessageBox.Yes)
        if q == QMessageBox.Yes:
            item = self.ui.ListItems.takeItem(CurrentIndex)
            del item

    def UpStudent(self):
        index = self.ui.ListItems.currentRow()
        if index>0:
            item = self.ui.ListItems.takeItem(index)
            self.ui.ListItems.insertItem(index-1,item)
            self.ui.ListItems.setCurrentItem(item)


    def DownStudent(self):
        index = self.ui.ListItems.currentRow()
        if index<self.ui.ListItems.count()-1:
            item = self.ui.ListItems.takeItem(index)
            self.ui.ListItems.insertItem(index+1,item)
            self.ui.ListItems.setCurrentItem(item)

    def SortStudent(self):
        self.ui.ListItems.sortItems()

    def CloseUI(self):
        quit()

def App():
    app = QtWidgets.QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())

App()