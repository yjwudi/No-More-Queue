# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/nmq_second_cluster.ui'
#
# Created: Sun Mar 15 11:16:26 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class clu_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(901, 600)
        MainWindow.setMinimumSize(QtCore.QSize(901, 600))
        MainWindow.setMaximumSize(QtCore.QSize(901, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(QtCore.QDir().currentPath()+"/logo/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 180, 361, 381))
        self.groupBox_3.setObjectName("groupBox_3")
        self.res_browser = QtGui.QTextBrowser(self.groupBox_3)
        self.res_browser.setGeometry(QtCore.QRect(10, 20, 341, 351))
        self.res_browser.setObjectName("res_browser")
        self.groupBox_4 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(380, 10, 511, 551))
        self.groupBox_4.setObjectName("groupBox_4")
        self.res_graph = PlotWidget(self.groupBox_4)
        self.res_graph.setGeometry(QtCore.QRect(10, 20, 491, 521))
        self.res_graph.setObjectName("res_graph")
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 361, 161))
        self.groupBox.setObjectName("groupBox")
        self.seg_browser = QtGui.QTextBrowser(self.groupBox)
        self.seg_browser.setGeometry(QtCore.QRect(10, 20, 341, 131))
        self.seg_browser.setObjectName("seg_browser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 901, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "关联分析", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("MainWindow", "聚类结果", None, QtGui.QApplication.UnicodeUTF8))
        self.res_browser.setHtml(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("MainWindow", "图形展示", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "建议", None, QtGui.QApplication.UnicodeUTF8))

from pyqtgraph import PlotWidget
