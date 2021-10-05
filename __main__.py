# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/train_view.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtWidgets , QtGui , QtCore
from views_mangers.login_manger import LoginManager
from views_mangers.main_manger import MainManager
from views_mangers.predict_manger import PredictManager



class Chest_xray_exploration(QtWidgets.QStackedWidget):
    def __init__(self):
        super(Chest_xray_exploration, self).__init__()
        self.login_manager = LoginManager()
        self.main_manager = MainManager()
        self.predict_manager = PredictManager()

        # add widgets to the stack
        self.addWidget(self.login_manager)
        self.addWidget(self.main_manager)
        self.addWidget(self.predict_manager)


        # install signals
        self.login_manager.loginAcceptedSignal.connect(self.handle_login_accepted)
        self.main_manager.loginout_btn.clicked.connect(self.handle_logout_process)
        self.main_manager.predict_btn.clicked.connect(self.handle_predict_selected)

        self.predict_manager.upload_photo_btn.clicked.connect(self.handle_upload_btn_selected)
        self.predict_manager.predict_btn.clicked.connect(self.handle_predict_btn)
        self.predict_manager.clear_btn.clicked.connect(self.handle_clear_btn)


        self.predict_manager.back_btn.clicked.connect(lambda : self.setCurrentIndex(1))


    def handle_login_accepted(self):
        self.setCurrentIndex(1)

    def handle_logout_process(self):
        self.login_manager.clear()
        self.setCurrentIndex(0)

    def handle_predict_selected(self):
        self.predict_manager.clear()
        self.setCurrentIndex(2)

    def handle_upload_btn_selected(self):
        self.predict_manager.clear()
        self.predict_manager.getfiles()
        self.predict_manager.clear_warning()

    def handle_predict_btn(self):
        self.predict_manager.predict()

    def handle_clear_btn(self):
        self.predict_manager.clear_File_path()
        self.predict_manager.clear()
        self.predict_manager.clear_warning()


if __name__ == "__main__":
    #import qdarkstyle
    app = QtWidgets.QApplication([])
    w = Chest_xray_exploration()
    w.show()
    #app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()










