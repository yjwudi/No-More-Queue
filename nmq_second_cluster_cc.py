__author__ = 'Rancho'

import sys
import numpy as np
import pyqtgraph as pg
from PySide.QtCore import *
from PySide.QtGui import *
from sklearn.cluster import *
from nmq_second_cluster import clu_MainWindow

class clu_mainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)

        self.ui= clu_MainWindow()
        self.ui.setupUi(self)

    def cluster_res(self, window_num, cluster_num, aly_cluster):
        #a = QWidget()
        #self.ui.res_browser.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.ui.res_browser.setText("窗口\t\t分类")
        self.ui.res_browser.append("          1        2        3        4        5")
        self.ui.res_browser.append("=================================================\n")
        for i in range(0, window_num):
            win_num = '%d'%(i+1)
            for j in range(0, cluster_num):
                win_num += "  "+'%f'%aly_cluster[j][i]
            self.ui.res_browser.append(win_num+'\n')

    def res_sug(self, window_num, cluster_num, aly_cluster):
        self.ui.seg_browser.setText("具有关联性的窗口为:\n")
        for i in range(0, cluster_num):
            for j in range(0, window_num):
                if aly_cluster[i][j]>0.9:
                    first_index = j
                    for k in range(0, window_num):
                        if (aly_cluster[i][k]>0.1 and k!=j):
                            second_index = k
                            win_num = "窗口"+'%d'%(first_index+1)+"与窗口"+'%d'%(second_index+1)
                            self.ui.seg_browser.append('\t'+win_num+'\n')
                            break
                    continue
                if aly_cluster[i][j]>0.3:
                    first_index = j
                    for k in range(j+1, window_num):
                        if (aly_cluster[i][k]>0.3 and aly_cluster[i][k]<0.9 and k!=j):
                            second_index = k
                            win_num = "窗口"+'%d'%(first_index+1)+"与窗口"+'%d'%(second_index+1)
                            self.ui.seg_browser.append('\t'+win_num+'\n')

    def clu_draw(self, window_num, data_num, all_data):
        #x = np.arange(15)
        y = np.zeros(15)
        flag = np.zeros(15)
        #x += 1
        for i in range(0, data_num):
            for j in range(0, window_num):
                if all_data[i][j]==1:
                    for k in range(j+1, window_num):
                        if all_data[i][k]==1:
                            if flag[j]==0:
                                flag[j]=1
                            else:
                                y[j] = k+1
        s = pg.ScatterPlotItem(pxMode=False)
        spots3 = []
        for i in range(1, 16):
                if y[i-1] != 0:
                    spots3.append({'pos': (i, y[i-1]), 'size': 1, 'pen': {'color': 'w', 'width': 2}, 'brush':pg.intColor(i*10+y[i-1], 100)})
        s.addPoints(spots3)
        self.ui.res_graph.addItem(s)



def data_process(window_num, data_num, list_data):
    bool_data = np.arange(data_num*window_num).reshape(data_num, window_num)
    #print(bool_data)
    index = -1
    for item in list_data:
        index += 1
        item_data = item.split(',')
        for i in range(0,window_num):
            bool_data[index][i] = int(item_data[i])
    return bool_data


#def nmq_cluster(file_name):
def main():
    file_read = open(sys.argv[1],'r',encoding= 'UTF-8')
    line = file_read.readline()
    list_windows = []
    list_data = []
    data_flag = 0
    while line:
        line_split = line.split(' ')
        if line_split[0]== "@ATTRIBUTE":
            list_windows.append(line_split[1])
        if data_flag == 1:
            list_data.append(line_split[0])
        if line_split[0] == "@DATA\n":
            data_flag = 1
        line = file_read.readline()
    file_read.close()
    window_num = len(list_windows)
    data_num = len(list_data)
    all_data = data_process(window_num, data_num, list_data)

    '''
    print(list_data)
    print(list_windows)
    print(all_data)
    '''

    cluster_num = 5
    k_means = KMeans(n_clusters=cluster_num)
    k_means.fit(all_data)
    '''
    print("中心坐标")
    print(k_means.cluster_centers_)
    print("所属中心序号")
    print(k_means.labels_)
    '''
    res_cluster = []
    for i in range(0, cluster_num):
        part_cluster = []
        for j in range(0, data_num):
            if k_means.labels_[j]==i:
                part_cluster.append(all_data[j])
        res_cluster.append(part_cluster)
    #集群分布
    #print(res_cluster)
    aly_cluster = []
    for i in range(0, cluster_num):
        part_aly = np.zeros(15, dtype=float)
        for j in range(0, window_num):
            temp_list = []
            for k in range(0, len(res_cluster[i])):
                temp_list.append(res_cluster[i][k][j])
            ave_window = sum(temp_list)/len(res_cluster[i])
            part_aly[j] = ave_window
        aly_cluster.append(part_aly)
    '''
    for i in range(0, cluster_num):
        print(aly_cluster[i])
    '''
    app = QApplication(sys.argv)
    d = clu_mainWindow()
    d.cluster_res(window_num, cluster_num, aly_cluster)
    d.res_sug(window_num, cluster_num, aly_cluster)
    d.clu_draw(window_num, data_num, all_data)
    d.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
