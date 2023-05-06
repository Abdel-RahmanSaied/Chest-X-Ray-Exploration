from PyQt5 import QtWidgets, QtCore, QtGui
from views import main_view
from PyQt5.QtCore import pyqtSignal

class MainManager(QtWidgets.QWidget, main_view.Ui_main_window):
    def __init__(self):
        super(MainManager, self).__init__()
        self.setupUi(self)
        self.setFixedSize(720, 401)



if __name__ == "__main__":
    # import qdarkstyle
    app = QtWidgets.QApplication([])
    w = MainManager()
    w.show()
    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()