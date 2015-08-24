__author__ = 'Rancho'

import sys
import numpy as np
import pyqtgraph as pg

from PySide import QtCore
from PySide.QtGui import *
from nmq_second_stc import stc_MainWindow

ave_list = []

class stc_mainWindow(QMainWindow):

    #new_show = QtCore.Signal(str)
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)

        self.ui= stc_MainWindow()
        self.ui.setupUi(self)
        #self.ui.new_show.connect(self, stc_mainWindow.ss)

    def plot_graphics(self, time, ave_list):
        #self.ui.curve_graphics.setBackground(background='default')
        self.ui.curve_graphics.setBackground(QBrush(QColor('default')))
        self.ui.curve_graphics.plot(time, ave_list[0])
        s = pg.ScatterPlotItem(pxMode=False)
        spots3 = []
        for i in time:
            spots3.append({'pos': (i, ave_list[0][i-1]), 'size': 0.5, 'pen': {'color': 'r', 'width': 1}})
        s.addPoints(spots3)
        self.ui.curve_graphics.addItem(s)
        #pg.plot(time, ave_list[0])

    def attr_list_show(self,list_attr):
        self.ui.attr_list.addItems(list_attr)

    def combox_show(self, list_port):
        self.ui.pot_num.addItems(list_port)
        list_weekday = ['周一','周二','周三','周四','周五','周六','周日']
        self.ui.weekday.addItems(list_weekday)
        list_time = ['早上','中午','晚上']
        self.ui.spe_time.addItems(list_time)

    def new_plot(self):
        time = np.arange(21)
        time += 1
        port =  self.ui.pot_num.currentIndex()
        self.ui.curve_graphics.plotItem.clearPlots()
        self.ui.curve_graphics.plot(time, ave_list[port], color=pg.intColor(port, 100))
        s = pg.ScatterPlotItem(pxMode=False)
        spots3 = []
        for i in time:
            spots3.append({'pos': (i, ave_list[port][i-1]), 'size': 0.5, 'pen': {'color': port, 'width': 1}})
        s.addPoints(spots3)
        self.ui.curve_graphics.addItem(s)

    def on_plot(self):
        port =  self.ui.pot_num.currentIndex()
        time = np.arange(21)
        time += 1
        self.ui.curve_graphics.plot(time, ave_list[port])
        s = pg.ScatterPlotItem(pxMode=False)
        spots3 = []
        for i in time:
            spots3.append({'pos': (i, ave_list[port][i-1]), 'size': 0.5, 'pen': {'color': port, 'width': 1}})
        s.addPoints(spots3)
        self.ui.curve_graphics.addItem(s)

    def show_money(self):
        port =  self.ui.pot_num.currentIndex()
        time_week = self.ui.weekday.currentIndex()
        time_spe = self.ui.spe_time.currentIndex()
        #print(time_week, time_spe)
        money = "金额: " + '%.2f'%ave_list[port][time_week*3+time_spe]
        self.ui.label_2.setText(money)

def data_process(list_port, list_data):
    all_data = []

    for i in range(0, len(list_port)):
        port_data = []
        for j in range(0, 21):
            port_data.append(np.array([], dtype=int))
        all_data.append(port_data)

    #print(all_data)
    for item in list_data:
        temp_item = item.split(',')
        index = list_port.index(temp_item[0])
        spe_index = (int(temp_item[1])-1)*3+int(temp_item[2])-1
        vec = np.append(all_data[index][spe_index],[int(temp_item[3])],axis=0)
        all_data[index][spe_index] = vec
        #print(all_data)
    #print(all_data)
    return all_data


#def nmq_stc(file_name):
def main():
    file_read = open(sys.argv[1],'r',encoding= 'UTF-8')
    #file_read = open(file_name,'r',encoding= 'UTF-8')
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
    file_read.close()


    for item in list_data:
        temp_list = item.split(',')
        if temp_list[0] not in list_port:
            list_port.append(temp_list[0])

    all_data = data_process(list_port, list_data)
    #print(all_data)
    #ave_list = []
    for i in range(0, len(list_port)):
        ave_list.append(np.array([], dtype=float))

    for index in range(0, len(all_data)):
        for j in range(0,21):
            if all_data[index][j].size:
                average = np.mean(all_data[index][j])
                vec2 = np.append(ave_list[index], [average], axis=0)
            else:
                vec2 = np.append(ave_list[index], [0], axis=0)
            ave_list[index] = vec2
    #print(ave_list)
    time = np.arange(21)
    time += 1
    app = QApplication(sys.argv)
    d = stc_mainWindow()
    d.ui.new_show.clicked.connect(d.new_plot)
    d.ui.on_show.clicked.connect(d.on_plot)
    d.ui.pushButton.clicked.connect(d.show_money)
    d.plot_graphics(time, ave_list)
    d.attr_list_show(list_attr)
    d.combox_show(list_port)
    d.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
