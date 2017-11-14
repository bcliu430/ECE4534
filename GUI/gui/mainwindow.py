import sys, os
import threading
import json
from PyQt5 import QtGui,QtCore, QtWidgets
from start import *

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.main_box  = QtWidgets.QVBoxLayout()
        self.start_box = QtWidgets.QVBoxLayout()
        self.debug_box = QtWidgets.QVBoxLayout()
        self.us_box = QtWidgets.QGridLayout()

        vbox = QtWidgets.QVBoxLayout()
        vbox.addLayout(self.main_box)
        vbox.addLayout(self.start_box)
        vbox.addLayout(self.debug_box)
        vbox.addLayout(self.us_box)
        self.setLayout(vbox)

        self.main()

    def main(self):
        w = QtWidgets.QWidget()
        width = 100
        pic = QtWidgets.QLabel(w)
        pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/Tron_Lightcycles.jpg"))
        pic.resize(597,297) 

        self.start = QtWidgets.QPushButton("Start") #first box
        self.start.setMaximumWidth(width)

        self.debug = QtWidgets.QPushButton("Debug")
        self.debug.setMaximumWidth(width)

        self.us = QtWidgets.QPushButton("About us")
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
        self.start_widget = Start()
##        self.start_widget.update_grid([0.0,10], [ 100,0] )
        self.back = QtWidgets.QPushButton("Back")
        self.back.setMaximumWidth(100)
        self.start_box.addWidget(self.start_widget)
        self.start_box.addWidget(self.back)

        self.back.clicked.connect(self.back_to_main_start)

    def back_to_main_start(self):
        self.remove_second_view()
        self.main()

    def Debug(self):
        width = 100
        self.tableWidget = QtWidgets.QTableWidget()
        self.tableWidget.setRowCount(11)
        self.tableWidget.setColumnCount(2) 
        self.tableWidget.setItem(0,0, QtWidgets.QTableWidgetItem("User"))
        self.tableWidget.setItem(0,1, QtWidgets.QTableWidgetItem("AI"))
    
        self.start = QtWidgets.QPushButton("Start")
        self.stop = QtWidgets.QPushButton("Stop")
        self.back = QtWidgets.QPushButton("Back")

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

    @pyqtSlot(list)
    def update_user(self, data):
            for i in range (1,11):
                self.tableWidget.setItem(i,0, QtWidgets.QTableWidgetItem(data[i]))

    @pyqtSlot(list)
    def update_AI(self, data):
            for i in range (1,11):
                self.tableWidget.setItem(i,1, QtWidgets.QTableWidgetItem(data[i]))


    def Debug_func(self,enable):
        print (enable)
        global thread1, server1
        global thread2, server2
        sgnStop = QtCore.pyqtSignal()

        if enable:
            thread1 = None   
            thread2 = None                            
            if not thread1:
                thread1 =QtCore.QThread()

            if not thread2:
                thread2 =QtCore.QThread() 
           
            server1 = Server(None)
#            server2 = Server(None)
            server1.moveToThread(thread1)
#            server2.moveToThread(thread2)
            thread1.started.connect(server1.run())
#            thread2.started.connect(server2.run(20002))
### how to start two thread?
            thread1.start()
#            thread2.start()
            print (thread1.isRunning())
            self.update_table()
        else:
            print (thread1)
            server.stop()
            thread1.terminate()
            print('thread stop')

    def back_to_main_debug(self):
        self.remove_fourth_view()
        self.main()

    def Us(self):
        gu = QtWidgets.QLabel()
        gu.setPixmap(QtGui.QPixmap(os.getcwd() + "/sample.jpg"))
        Hao = QtWidgets.QLabel('Hao Gu\nAI Algorithm\nLine Following Sensor') 

        liang = QtWidgets.QLabel()
        liang.setPixmap(QtGui.QPixmap(os.getcwd() + "/sample.jpg"))
        Yuqiao = QtWidgets.QLabel('Yuqiao Liang\nmotor') 

        liu = QtWidgets.QLabel()
        liu.setPixmap(QtGui.QPixmap(os.getcwd() + "/sample.jpg"))
        Beichen = QtWidgets.QLabel('Beichen Liu\nGUI Interface\nWi-Fly Communication') 

        tsongalis = QtWidgets.QLabel()
        tsongalis.setPixmap(QtGui.QPixmap(os.getcwd() + "/sample.jpg"))
        Peter = QtWidgets.QLabel('Peter Tsongalis\nCommunication\nIR sensor') 
    

        self.back = QtWidgets.QPushButton("Back")
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



