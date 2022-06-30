import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QToolTip
from PyQt5.QtGui import QIcon

class MyWindow(QMainWindow):
    def __init__(this):
        super(MyWindow,this).__init__()
        this.setWindowTitle("Hello World Application") # Pencere Bar'a Yazı Gönderiyoruz
        this.setGeometry(200,200,640,480) # x,y, width,length
        this.setWindowIcon(QIcon('icon.png'))
        this.setToolTip("My Tool Tip") # İmleç uygulamanın üzerindeyken çıkacak yazı
        this.initUI()    
  
    def initUI(this):
        this.lbl_name = QtWidgets.QLabel(this)
        this.lbl_name.setText("ADINIZ: ")
        this.lbl_name.move(25,20)
        this.lbl_surname = QtWidgets.QLabel(this)
        this.lbl_surname.setText("SOYADINIZ: ")
        this.lbl_surname.move(25,60)

        this.result = QtWidgets.QLabel(this)
        this.result.move(250,20)
        this.result.resize(250,32)

        this.txt_name = QtWidgets.QLineEdit(this)
        this.txt_name.move(120,20)
        this.txt_surname = QtWidgets.QLineEdit(this)
        this.txt_surname.move(120,60)    

        this.btn_save = QtWidgets.QPushButton(this)
        this.btn_save.move(120,100)
        this.btn_save.setText("KAYDET")
        this.btn_save.clicked.connect(this.clicked)

    def clicked(this):
        #print("BUTONA TIKLANDI Isım: "+this.txt_name.text()+" Soyisim: "+this.txt_surname.text())
        this.result.setText("Isım: "+this.txt_name.text()+" Soyisim: "+this.txt_surname.text())



def window():
    app = QApplication(sys.argv)
    win = MyWindow() # Pencere oluşturduk
    win.show() # Pencereyi gösteriyoruz
    sys.exit(app.exec_())  # Çarpı ikonuna bastığımızda duracak
    
window()

