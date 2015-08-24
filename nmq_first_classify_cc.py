__author__ = 'Rancho'

import sys
import pyqtgraph as pg

from PySide.QtCore import *
from PySide.QtGui import *

from nmq_first_classify import classify_MainWindow

class classify_mainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)

        self.ui= classify_MainWindow()
        self.ui.setupUi(self)

    def info_label_show(self, instance_num, attribute_num):
        intent =  "<font size=5 face=\"楷体\" color=blue>类型<br>实例数:"+str(attribute_num)+"\t "+"属性数:"+str(instance_num)+"<\\font>"
       # self.ui.info_label.setWordWrap(self,1,1)
        #self.ui.info_label.setLineWidth(self,)
        self.ui.info_label.setText("<td align=\"left\">"+intent+"<\\td>")

    def attr_list_show(self,list_attr):
        self.ui.attr_list.addItems(list_attr)
#换成其它时间
    def pot_num_show(self, list_port):
        self.ui.pot_num.addItems(list_port)

    def weekday_show(self):
        list_weekday = ['周一','周二','周三','周四','周五','周六','周日']
        self.ui.weekday.addItems(list_weekday)
        list_time = ['0','1','2']
        self.ui.spe_time.addItems(list_time)
'''
    def say_hello(self):
        self.ui.label_3.setText("this is a test")
'''

def main():
    file_name = "test.nmq"
    file_read = open(file_name,'r',encoding= 'UTF-8')
    line = file_read.readline()
    list_attr = []
    list_data = []
    list_port = []
    data_flag = 0
    while line:
        line_split = line.split(" ", 1)
        if line_split[0] == "@ATTRIBUTE":
            list_attr.append(line_split[1])
        if data_flag == 1:
            list_data.append(line_split[0])
        if line_split[0] == "@DATA\n":
            data_flag = 1
        line = file_read.readline()
    print(list_attr)
    print(list_data)
    for item in list_data:
        temp_list = item.split(',')
        list_port.append(temp_list[0])

    file_read.close()

    app = QApplication(sys.argv)
    d = classify_mainWindow()
    d.info_label_show(len(list_data), len(list_attr))
    d.attr_list_show(list_attr)
    d.weekday_show()
    d.pot_num_show(list_port)
    #d.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()