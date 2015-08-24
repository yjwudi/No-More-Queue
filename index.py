__author__ = 'Rancho'

import os
from PySide.QtCore import *
from PySide.QtGui import *
from nmq_second_stc_cc import *
from nmq_second_cluster_cc import *
from nmq_index import in_MainWindow

class in_mainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)

        self.ui= in_MainWindow()
        self.ui.setupUi(self)
        self.file_name = ""

    def open_file(self):
        #fdialog = QFileDialog()
        file_full = QFileDialog().getOpenFileName()
        self.file_name = file_full[0]
        #print(file_location)
        list_name = self.file_name.split('/')
        for i in range(0, len(list_name)):
            if i != 0:
                self.ui.file_path.append("<font size=5>"+'\\'+list_name[i]+"<\\font>")
            else:
                self.ui.file_path.setText("<font size=5>"+list_name[0]+"<\\font>")

    def reg_data(self):
        if len(self.file_name) == 0:
            QMessageBox().information( self, "No File", "Please choose a file   " )#about( self, 'PyQt', "About" )

        else:
            os.popen("nmq_second_stc_cc.exe "+self.file_name)
            #nmq_stc(self.file_name)
            #os.system("nmq_second_stc_cc.py "+self.file_name)
        #if len(file_name) == 0:

    def clu_data(self):
        if len(self.file_name) == 0:
            warning = QMessageBox()
            warning.setText("Please choose a file   ")
            warning.setWindowTitle("No File")
            warning.show()

        else:
            os.popen("nmq_second_cluster_cc.exe "+self.file_name)
            #os.system("nmq_second_cluster_cc.py "+self.file_name)


def main():
    #print(qDir.currentPath())
    app = QApplication(sys.argv)
    d = in_mainWindow()
    d.ui.choose_file.clicked.connect(d.open_file)
    d.ui.reg_btn.clicked.connect(d.reg_data)
    d.ui.cluster_btn.clicked.connect(d.clu_data)
    d.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()