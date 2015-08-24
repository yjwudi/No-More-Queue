# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/nmq_second_stc.ui'
#
# Created: Tue Feb 24 20:36:22 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class stc_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(916, 609)
        MainWindow.setMinimumSize(QtCore.QSize(916, 609))
        MainWindow.setMaximumSize(QtCore.QSize(916, 609))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(QtCore.QDir().currentPath()+"/logo/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 320, 211, 131))
        self.groupBox.setObjectName("groupBox")
        self.pot_label = QtGui.QLabel(self.groupBox)
        self.pot_label.setGeometry(QtCore.QRect(10, 30, 91, 31))
        self.pot_label.setObjectName("pot_label")
        self.pot_num = QtGui.QComboBox(self.groupBox)
        self.pot_num.setGeometry(QtCore.QRect(110, 40, 69, 22))
        self.pot_num.setObjectName("pot_num")
        self.new_show = QtGui.QPushButton(self.groupBox)
        self.new_show.setGeometry(QtCore.QRect(10, 80, 91, 31))
        self.new_show.setObjectName("new_show")
        self.on_show = QtGui.QPushButton(self.groupBox)
        self.on_show.setGeometry(QtCore.QRect(110, 80, 91, 31))
        self.on_show.setObjectName("on_show")
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 459, 211, 121))
        self.groupBox_2.setObjectName("groupBox_2")
        self.weekday = QtGui.QComboBox(self.groupBox_2)
        self.weekday.setGeometry(QtCore.QRect(10, 30, 69, 22))
        self.weekday.setObjectName("weekday")
        self.spe_time = QtGui.QComboBox(self.groupBox_2)
        self.spe_time.setGeometry(QtCore.QRect(110, 30, 69, 22))
        self.spe_time.setObjectName("spe_time")
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(60, 60, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 141, 31))
        self.label_2.setObjectName("label_2")
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 10, 211, 291))
        self.groupBox_3.setObjectName("groupBox_3")
        self.attr_list = QtGui.QListWidget(self.groupBox_3)
        self.attr_list.setGeometry(QtCore.QRect(0, 20, 201, 261))
        self.attr_list.setObjectName("attr_list")
        self.groupBox_4 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(230, 0, 681, 581))
        self.groupBox_4.setObjectName("groupBox_4")
        self.curve_graphics = PlotWidget(self.groupBox_4)
        self.curve_graphics.setGeometry(QtCore.QRect(10, 20, 661, 551))
        self.curve_graphics.setMinimumSize(QtCore.QSize(661, 551))
        self.curve_graphics.setMaximumSize(QtCore.QSize(661, 551))
        self.curve_graphics.setObjectName("curve_graphics")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 916, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "预测结果", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "展示其它窗口结果", None, QtGui.QApplication.UnicodeUTF8))
        self.pot_label.setText(QtGui.QApplication.translate("MainWindow", " 选择窗口号：", None, QtGui.QApplication.UnicodeUTF8))
        self.new_show.setText(QtGui.QApplication.translate("MainWindow", "单独显示", None, QtGui.QApplication.UnicodeUTF8))
        self.on_show.setText(QtGui.QApplication.translate("MainWindow", "原图显示", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("MainWindow", "所选窗口某段时间金额", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "显示金额", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "金额：", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("MainWindow", "数据属性列表", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("MainWindow", "预测结果图形化展示", None, QtGui.QApplication.UnicodeUTF8))

from pyqtgraph import PlotWidget
