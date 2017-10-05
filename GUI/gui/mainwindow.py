import sys, os
from PyQt5 import QtGui,QtCore, QtWidgets


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.main_box  = QtWidgets.QVBoxLayout()
        self.start_box = QtWidgets.QVBoxLayout()
        self.help_box  = QtWidgets.QVBoxLayout()
        self.debug_box = QtWidgets.QVBoxLayout()
        self.us_box = QtWidgets.QVBoxLayout()

        self.zvbox = QtWidgets.QVBoxLayout()

        vbox = QtWidgets.QVBoxLayout()
        vbox.addLayout(self.main_box)
        vbox.addLayout(self.start_box)
        vbox.addLayout(self.help_box)
        vbox.addLayout(self.debug_box)
        vbox.addLayout(self.us_box)
        self.setLayout(vbox)

        self.main()

        self.setGeometry(300, 200, 600, 400)

    def main(self):
        w = QtWidgets.QWidget()
        self.pic = QtWidgets.QLabel(w)
        self.pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/Tron_Lightcycles.jpg"))
        self.start = QtWidgets.QPushButton("Start") #first box
        self.help = QtWidgets.QPushButton("Help")
        self.debug = QtWidgets.QPushButton("Debug")
        self.us = QtWidgets.QPushButton("About us")
        self.main_box.addWidget(w)
        self.main_box.addWidget(self.start)
        self.main_box.addWidget(self.help)
        self.main_box.addWidget(self.debug)
        self.main_box.addWidget(self.us)
        self.start.clicked.connect(self.main_start)
        self.help.clicked.connect(self.main_help)
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
        self.back = QtWidgets.QPushButton("Back")
        self.start_box.addWidget(self.back)

        self.back.clicked.connect(self.back_to_main_start)

    def back_to_main_start(self):
        self.remove_second_view()
        self.main()

    def Help(self):
        self.back = QtWidgets.QPushButton("Back")
        self.help_box.addWidget(self.back)

        self.back.clicked.connect(self.back_to_main_help)

    def back_to_main_help(self):
        self.remove_third_view()
        self.main()

    def Debug(self):
        self.back = QtWidgets.QPushButton("Back")
        self.debug_box.addWidget(self.back)

        self.back.clicked.connect(self.back_to_main_debug)

    def back_to_main_debug(self):
        self.remove_fourth_view()
        self.main()

    def Us(self):
        self.back = QtWidgets.QPushButton("Back")
        self.us_box.addWidget(self.back)

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

    def remove_third_view(self):
        for cnt in reversed(range(self.help_box.count())):
            # takeAt does both the jobs of itemAt and removeWidget
            # namely it removes an item and returns it
            widget = self.help_box.takeAt(cnt).widget()

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



