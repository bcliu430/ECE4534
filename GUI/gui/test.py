from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import *
import sys

class Foo(QWidget):

    trigger = pyqtSignal()
    def __init__(self):
        super(Foo, self).__init__()

    def connect_and_emit_trigger(self):
        # Connect the trigger signal to a slot.
        self.trigger.connect(self.handle_trigger)

        # Emit the signal.
        self.trigger.emit()

    def handle_trigger(self):
        # Show that the slot has been called.

        print ("trigger signal received")

if __name__ == '__main__':
    app = QApplication(sys.argv)

    test = Foo()
    test.connect_and_emit_trigger()

    sys.exit(app.exec_())

