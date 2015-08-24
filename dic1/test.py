__author__ = 'Rancho'
import sys
import numpy as np
import pyqtgraph as pg
from PySide.QtCore import *
from PySide.QtGui import *
from sklearn import *

iris = datasets.load_iris()
digits = datasets.load_digits()

print(iris.data)
'''
dt = np.array([[1, 0, 0, 0, 0],
               [1, 1, 1, 0, 0],
               [1, 0, 0, 0, 0],
               [1, 1, 1, 1, 0],
               [1, 0, 1, 1, 1]], dtype=int)
k_means = cluster.KMeans(n_clusters=3)
k_means.fit(dt)

'''
k_means = cluster.KMeans(n_clusters=4)
k_means.fit(iris.data)
print(len(k_means.labels_))
#每个点所属的中心的index
print(k_means.labels_)
print(iris.target)
#每个簇在n维空间中的簇中心坐标
print(k_means.cluster_centers_)
#暂时理解为每个点到质心的平方距离的平均值
print(k_means.inertia_)

