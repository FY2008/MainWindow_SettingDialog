# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_Setting(object):
    def setupUi(self, Dialog_Setting):
        Dialog_Setting.setObjectName("Dialog_Setting")
        Dialog_Setting.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog_Setting.resize(835, 616)
        self.gridLayout = QtWidgets.QGridLayout(Dialog_Setting)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(Dialog_Setting)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_routine = QtWidgets.QWidget()
        self.tab_routine.setObjectName("tab_routine")
        self.checkBoxStatus = QtWidgets.QCheckBox(self.tab_routine)
        self.checkBoxStatus.setGeometry(QtCore.QRect(30, 70, 121, 19))
        self.checkBoxStatus.setObjectName("checkBoxStatus")
        self.tabWidget.addTab(self.tab_routine, "")
        self.tab_Show = QtWidgets.QWidget()
        self.tab_Show.setObjectName("tab_Show")
        self.tabWidget.addTab(self.tab_Show, "")
        self.tab_about = QtWidgets.QWidget()
        self.tab_about.setObjectName("tab_about")
        self.tabWidget.addTab(self.tab_about, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_Ok = QtWidgets.QPushButton(Dialog_Setting)
        self.pushButton_Ok.setObjectName("pushButton_Ok")
        self.horizontalLayout.addWidget(self.pushButton_Ok)
        self.pushButton_Cancel = QtWidgets.QPushButton(Dialog_Setting)
        self.pushButton_Cancel.setObjectName("pushButton_Cancel")
        self.horizontalLayout.addWidget(self.pushButton_Cancel)
        self.pushButton_Apply = QtWidgets.QPushButton(Dialog_Setting)
        self.pushButton_Apply.setObjectName("pushButton_Apply")
        self.horizontalLayout.addWidget(self.pushButton_Apply)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 1)

        self.retranslateUi(Dialog_Setting)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Setting)

    def retranslateUi(self, Dialog_Setting):
        _translate = QtCore.QCoreApplication.translate
        Dialog_Setting.setWindowTitle(_translate("Dialog_Setting", "设置"))
        self.checkBoxStatus.setText(_translate("Dialog_Setting", "状态栏"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_routine), _translate("Dialog_Setting", "常规"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Show), _translate("Dialog_Setting", "显示"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_about), _translate("Dialog_Setting", "关于"))
        self.pushButton_Ok.setText(_translate("Dialog_Setting", "确认"))
        self.pushButton_Cancel.setText(_translate("Dialog_Setting", "取消"))
        self.pushButton_Apply.setText(_translate("Dialog_Setting", "应用"))
