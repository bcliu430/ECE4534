import sys, os
import json
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from start import start
from Controller import Controller

class MainWindow(QWidget):
    ctl = Controller()
    def __init__(self):
        super(MainWindow, self).__init__()
        self.main_box  = QVBoxLayout()
        self.start_box = QVBoxLayout()
        self.debug_box = QVBoxLayout()
        self.us_box = QGridLayout()

        vbox = QVBoxLayout()
        vbox.addLayout(self.main_box)
        vbox.addLayout(self.start_box)
        vbox.addLayout(self.debug_box)
        vbox.addLayout(self.us_box)
        self.setLayout(vbox)
#        self.ctl.user_coor_sig.connect(self.start_widget.view.update_grid)
        self.ctl.user_coor_sig.connect(self.new_coor_user)
        self.main()

    def main(self):
        w = QWidget()
        width = 100
        pic = QLabel(w)
        pic.setPixmap(QPixmap(os.getcwd() + "/Tron_Lightcycles.jpg"))
        pic.resize(597,297) 

        self.start = QPushButton("Start") #first box
        self.start.setMaximumWidth(width)

        self.debug = QPushButton("Debug")
        self.debug.setMaximumWidth(width)

        self.us = QPushButton("About us")
        self.us.setMaximumWidth(width)

        self.main_box.addWidget(w)
        self.main_box.addWidget(self.start)
        self.main_box.addWidget(self.debug)
        self.main_box.addWidget(self.us)
        pic.setScaledContents(True)
        pic.setMinimumSize(1,1)
        self.start.clicked.connect(self.main_start)
        self.debug.clicked.connect(self.main_debug)
        self.us.clicked.connect(self.main_us)

    def main_start(self):
        self.remove_first_view()
        self.Start()

    def main_help(self):
        self.remove_first_view()
        self.Help()

    def main_debug(self):
        self.remove_first_view()
        self.Debug()

    def main_us(self):
        self.remove_first_view()
        self.Us()

    def Start(self):
        self.start_widget = start(self.ctl)
#        self.ctl.user_coor_sig.connect(self.start_widget.view.update_grid)
        self.back = QPushButton("Back")
        self.back.setMaximumWidth(100)
        self.start_box.addWidget(self.start_widget)
        self.start_box.addWidget(self.back)

        self.back.clicked.connect(self.back_to_main_start)

    def back_to_main_start(self):
        self.remove_second_view()
        self.main()

    def Debug(self):
        width = 100
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(11)
        self.tableWidget.setColumnCount(2) 
        self.tableWidget.setItem(0,0, QTableWidgetItem("User"))
        self.tableWidget.setItem(0,1, QTableWidgetItem("AI"))
    
        self.start = QPushButton("Start")
        self.stop = QPushButton("Stop")
        self.back = QPushButton("Back")

        self.start.setMaximumWidth(width)
        self.stop.setMaximumWidth(width)
        self.back.setMaximumWidth(width)
        self.debug_box.addWidget(self.tableWidget)
        
        self.debug_box.addWidget(self.start)
        self.debug_box.addWidget(self.stop)
        self.debug_box.addWidget(self.back)

        print (self.start.clicked)

        self.start.clicked.connect(lambda: self.Debug_func(True))
        self.stop.clicked.connect(lambda: self.Debug_func(False))
        self.back.clicked.connect(self.back_to_main_debug)

    @pyqtSlot(str)
    def new_coor_user(self, data):
        print ("data: "+data)

    @pyqtSlot(list)
    def update_user(self, data):
        print ("called")
        for i in range (1,11):
            self.tableWidget.setItem(i,0, QTableWidgetItem(data[i]))

    @pyqtSlot(list)
    def update_AI(self, data):
            for i in range (1,11):
                self.tableWidget.setItem(i,1, QTableWidgetItem(data[i]))


    def Debug_func(self,enable):
            print('thread stop')

    def back_to_main_debug(self):
        self.remove_fourth_view()
        self.main()

    def Us(self):
        gu = QLabel()
        gu.setPixmap(QPixmap(os.getcwd() + "/sample.jpg"))
        Hao = QLabel('Hao Gu\nAI Algorithm\nLine Following Sensor') 

        liang = QLabel()
        liang.setPixmap(QPixmap(os.getcwd() + "/sample.jpg"))
        Yuqiao = QLabel('Yuqiao Liang\nmotor') 

        liu = QLabel()
        liu.setPixmap(QPixmap(os.getcwd() + "/sample.jpg"))
        Beichen = QLabel('Beichen Liu\nGUI Interface\nWi-Fly Communication') 

        tsongalis = QLabel()
        tsongalis.setPixmap(QPixmap(os.getcwd() + "/sample.jpg"))
        Peter = QLabel('Peter Tsongalis\nCommunication\nIR sensor') 
    

        self.back = QPushButton("Back")
        self.us_box.addWidget(gu, 0, 0)
        self.us_box.addWidget(Hao, 1, 0)
        self.us_box.addWidget(liang, 0 ,1)
        self.us_box.addWidget(Yuqiao, 1 ,1)
        self.us_box.addWidget(liu, 0 ,2)
        self.us_box.addWidget(Beichen, 1 ,2)
        self.us_box.addWidget(tsongalis, 0 ,3)
        self.us_box.addWidget(Peter, 1 ,3)
        self.us_box.addWidget(self.back, 2, 0)

        self.back.clicked.connect(self.back_to_main_us)

    def back_to_main_us(self):
        self.remove_fifth_view()
        self.main()

    def remove_first_view(self):
        for cnt in reversed(range(self.main_box.count())):
            # takeAt does both the jobs of itemAt and removeWidget
            # namely it removes an item and returns it
            widget = self.main_box.takeAt(cnt).widget()

            if widget is not None: 
                # widget will be None if the item is a layout
                widget.deleteLater()

    def remove_second_view(self):
        for cnt in reversed(range(self.start_box.count())):
            # takeAt does both the jobs of itemAt and removeWidget
            # namely it removes an item and returns it
            widget = self.start_box.takeAt(cnt).widget()

            if widget is not None: 
                # widget will be None if the item is a layout
                widget.deleteLater()

    def remove_fourth_view(self):
        for cnt in reversed(range(self.debug_box.count())):
            # takeAt does both the jobs of itemAt and removeWidget
            # namely it removes an item and returns it
            widget = self.debug_box.takeAt(cnt).widget()

            if widget is not None: 
                # widget will be None if the item is a layout
                widget.deleteLater()

    def remove_fifth_view(self):
        for cnt in reversed(range(self.us_box.count())):
            # takeAt does both the jobs of itemAt and removeWidget
            # namely it removes an item and returns it
            widget = self.us_box.takeAt(cnt).widget()

            if widget is not None: 
                # widget will be None if the item is a layout
                widget.deleteLater()
def run():

    app = QApplication(sys.argv)
    w = MainWindow()
    w.resize(1200, 450)
    w.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    run()
