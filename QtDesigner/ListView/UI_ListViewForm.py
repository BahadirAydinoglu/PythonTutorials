# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/bahadira/Desktop/Workspace/PythonTutorials/QtDesigner/ListView/ListViewForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ListItems = QtWidgets.QListWidget(self.centralwidget)
        self.ListItems.setGeometry(QtCore.QRect(60, 40, 281, 341))
        self.ListItems.setObjectName("ListItems")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(430, 40, 91, 341))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.BtnAdd = QtWidgets.QPushButton(self.widget)
        self.BtnAdd.setObjectName("BtnAdd")
        self.verticalLayout.addWidget(self.BtnAdd)
        self.BtnEdit = QtWidgets.QPushButton(self.widget)
        self.BtnEdit.setObjectName("BtnEdit")
        self.verticalLayout.addWidget(self.BtnEdit)
        self.BtnRemove = QtWidgets.QPushButton(self.widget)
        self.BtnRemove.setObjectName("BtnRemove")
        self.verticalLayout.addWidget(self.BtnRemove)
        self.BtnUp = QtWidgets.QPushButton(self.widget)
        self.BtnUp.setObjectName("BtnUp")
        self.verticalLayout.addWidget(self.BtnUp)
        self.BtnDown = QtWidgets.QPushButton(self.widget)
        self.BtnDown.setObjectName("BtnDown")
        self.verticalLayout.addWidget(self.BtnDown)
        self.BtnSort = QtWidgets.QPushButton(self.widget)
        self.BtnSort.setObjectName("BtnSort")
        self.verticalLayout.addWidget(self.BtnSort)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.BtnExit = QtWidgets.QPushButton(self.widget)
        self.BtnExit.setObjectName("BtnExit")
        self.verticalLayout.addWidget(self.BtnExit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.BtnAdd.setText(_translate("MainWindow", "Add"))
        self.BtnEdit.setText(_translate("MainWindow", "Edit"))
        self.BtnRemove.setText(_translate("MainWindow", "Remove"))
        self.BtnUp.setText(_translate("MainWindow", "Up"))
        self.BtnDown.setText(_translate("MainWindow", "Down"))
        self.BtnSort.setText(_translate("MainWindow", "Sort"))
        self.BtnExit.setText(_translate("MainWindow", "Exit"))
