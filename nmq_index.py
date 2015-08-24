# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/nmq_index.ui'
#
# Created: Thu Feb 26 17:22:44 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!
#import logo_rc
from PySide import QtCore, QtGui

class in_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(712, 510)
        MainWindow.setMinimumSize(QtCore.QSize(712, 510))
        MainWindow.setMaximumSize(QtCore.QSize(712, 510))
        '''
        file_out = open("out.txt",'w',encoding= 'UTF-8')
        file_out.write(QtCore.QDir().currentPath())
        QtCore.QDir().setPath(":/")
        file_out.write(QtCore.QDir().currentPath())
        '''
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(QtCore.QDir().currentPath()+"/logo/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.logo = QtGui.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(10, 10, 471, 491))
        self.logo.setFrameShape(QtGui.QFrame.Panel)
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap(QtCore.QDir().currentPath()+ '/logo/logo.png'))
        #self.logo.setPixmap(QtGui.QPixmap(QtCore.QDir().currentPath()+"/logo/logo.jpg"))
        self.logo.setScaledContents(False)
        self.logo.setObjectName("logo")
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(490, 10, 211, 171))
        self.groupBox.setObjectName("groupBox")
        self.choose_file = QtGui.QPushButton(self.groupBox)
        self.choose_file.setGeometry(QtCore.QRect(10, 20, 75, 23))
        self.choose_file.setObjectName("choose_file")
        self.file_path = QtGui.QTextEdit(self.groupBox)
        self.file_path.setGeometry(QtCore.QRect(0, 50, 191, 101))
        self.file_path.setObjectName("file_path")
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(490, 200, 201, 291))
        self.groupBox_2.setObjectName("groupBox_2")
        self.reg_btn = QtGui.QPushButton(self.groupBox_2)
        self.reg_btn.setGeometry(QtCore.QRect(40, 30, 131, 101))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.reg_btn.setFont(font)
        self.reg_btn.setObjectName("reg_btn")
        self.cluster_btn = QtGui.QPushButton(self.groupBox_2)
        self.cluster_btn.setGeometry(QtCore.QRect(40, 160, 131, 101))
        self.cluster_btn.setMinimumSize(QtCore.QSize(0, 0))
        self.cluster_btn.setMaximumSize(QtCore.QSize(99999, 99999))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.cluster_btn.setFont(font)
        self.cluster_btn.setObjectName("cluster_btn")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "No More Queue", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "打开文件", None, QtGui.QApplication.UnicodeUTF8))
        self.choose_file.setText(QtGui.QApplication.translate("MainWindow", "选择文件", None, QtGui.QApplication.UnicodeUTF8))
        self.file_path.setHtml(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("MainWindow", "选择功能", None, QtGui.QApplication.UnicodeUTF8))
        self.reg_btn.setText(QtGui.QApplication.translate("MainWindow", "预测结果", None, QtGui.QApplication.UnicodeUTF8))
        self.cluster_btn.setText(QtGui.QApplication.translate("MainWindow", "关联分析", None, QtGui.QApplication.UnicodeUTF8))

#import logo_rc
