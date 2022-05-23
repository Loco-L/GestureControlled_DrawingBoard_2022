# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InterfaceUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1241, 801)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("#frame\n"
"{\n"
"    background-color: rgb(49, 51, 53);\n"
"    border-radius:30px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, -1)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setStyleSheet("#frame_2\n"
"{\n"
"    background-color: rgb(83, 83, 83);\n"
"    border-top-left-radius:30px;\n"
"    border-top-right-radius:30px;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setGeometry(QtCore.QRect(1000, 0, 221, 61))
        self.frame_4.setStyleSheet("QPushButton\n"
"{\n"
"    border:none;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    padding-bottom:3px;\n"
"}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.frame_4)
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("GUI素材库/icons/最小化.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 20))
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("GUI素材库/icons/最大化.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("GUI素材库/icons/关闭.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setAutoRepeatDelay(300)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(12)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.Meau_WT = QtWidgets.QWidget(self.frame_3)
        self.Meau_WT.setGeometry(QtCore.QRect(0, 0, 150, 711))
        self.Meau_WT.setMaximumSize(QtCore.QSize(150, 16777215))
        self.Meau_WT.setStyleSheet("QWidget{\n"
"\n"
"    background-color: rgba(96, 204, 195, 255);\n"
"}\n"
"QPushButton{\n"
"    font: 17pt \"仿宋\";\n"
"    color:rgba(0, 255, 195, 255);\n"
"    border-left:3px solid rgba(0, 255, 195, 255);\n"
"    border-radius:9px;\n"
"}\n"
"QPushButton:hover{\n"
"    border-left:7px solid #ffd194;\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(255, 255, 255, 50), stop:1 rgba(255, 255, 255, 0))\n"
"    }\n"
"QPushButton:pressed{\n"
"    border-left:7px solid #ffd194;\n"
"    background-color:rgba(0,0,0,40);\n"
"    border-bottom-right-radius:0px;\n"
"    border-top-right-radius:0px;\n"
"    }")
        self.Meau_WT.setObjectName("Meau_WT")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Meau_WT)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.Meau_WT)
        self.pushButton_4.setMaximumSize(QtCore.QSize(150, 70))
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.Meau_WT)
        self.pushButton_5.setMaximumSize(QtCore.QSize(150, 70))
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_2.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.Meau_WT)
        self.pushButton_6.setMaximumSize(QtCore.QSize(150, 70))
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_2.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.Meau_WT)
        self.pushButton_7.setMaximumSize(QtCore.QSize(150, 70))
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_2.addWidget(self.pushButton_7)
        spacerItem = QtWidgets.QSpacerItem(20, 150, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(20, 150, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 150, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem2)
        self.pushButton_8 = QtWidgets.QPushButton(self.Meau_WT)
        self.pushButton_8.setMaximumSize(QtCore.QSize(150, 70))
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout_2.addWidget(self.pushButton_8)
        self.pushButton_9 = QtWidgets.QPushButton(self.Meau_WT)
        self.pushButton_9.setMaximumSize(QtCore.QSize(150, 70))
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout_2.addWidget(self.pushButton_9)
        self.verticalLayout.addWidget(self.frame_3)
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionxinjian = QtWidgets.QAction(MainWindow)
        self.actionxinjian.setObjectName("actionxinjian")
        self.actiona = QtWidgets.QAction(MainWindow)
        self.actiona.setObjectName("actiona")
        self.actionbaoqun = QtWidgets.QAction(MainWindow)
        self.actionbaoqun.setObjectName("actionbaoqun")
        self.actionx = QtWidgets.QAction(MainWindow)
        self.actionx.setObjectName("actionx")
        self.actionl = QtWidgets.QAction(MainWindow)
        self.actionl.setObjectName("actionl")
        self.actionbao = QtWidgets.QAction(MainWindow)
        self.actionbao.setObjectName("actionbao")
        self.actionda = QtWidgets.QAction(MainWindow)
        self.actionda.setObjectName("actionda")
        self.actionbao_2 = QtWidgets.QAction(MainWindow)
        self.actionbao_2.setObjectName("actionbao_2")
        self.actionb = QtWidgets.QAction(MainWindow)
        self.actionb.setObjectName("actionb")
        self.actiont = QtWidgets.QAction(MainWindow)
        self.actiont.setObjectName("actiont")
        self.actionshux = QtWidgets.QAction(MainWindow)
        self.actionshux.setObjectName("actionshux")
        self.actiong = QtWidgets.QAction(MainWindow)
        self.actiong.setObjectName("actiong")

        self.retranslateUi(MainWindow)
        self.pushButton_3.clicked.connect(MainWindow.close)
        self.pushButton_2.clicked.connect(MainWindow.showMaximized)
        self.pushButton.clicked.connect(MainWindow.showMinimized)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_4.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_5.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_6.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_7.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_8.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_9.setText(_translate("MainWindow", "PushButton"))
        self.actionxinjian.setText(_translate("MainWindow", "新建"))
        self.actiona.setText(_translate("MainWindow", "打开"))
        self.actionbaoqun.setText(_translate("MainWindow", "保存"))
        self.actionx.setText(_translate("MainWindow", "图形库"))
        self.actionl.setText(_translate("MainWindow", "另存为"))
        self.actionbao.setText(_translate("MainWindow", "保存全部"))
        self.actionda.setText(_translate("MainWindow", "打印"))
        self.actionbao_2.setText(_translate("MainWindow", "保存图像"))
        self.actionb.setText(_translate("MainWindow", "关闭"))
        self.actiont.setText(_translate("MainWindow", "退出"))
        self.actionshux.setText(_translate("MainWindow", "属性"))
        self.actiong.setText(_translate("MainWindow", "关于画板"))

