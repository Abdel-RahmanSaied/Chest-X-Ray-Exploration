from PyQt5 import QtWidgets, QtCore, QtGui
from views import login_view
from PyQt5.QtCore import pyqtSignal



class LoginManager(QtWidgets.QWidget, login_view.Ui_Form):
    loginAcceptedSignal = pyqtSignal()
    def __init__(self):
        super(LoginManager, self).__init__()
        self.setupUi(self)
        # self.setFixedSize(720, 401)
        self.login_button.clicked.connect(self.run)
        self.msg = QtWidgets.QMessageBox()

    def get_data(self):
        with open("database/users_db.json", "r") as f:
            data = f.read()
        return data
    def run(self):
        username = self.username_lin.text()
        password = self.password_lin.text()
        data = self.get_data()
        if username == "" or password == "":
            self.msg.setText("Please fill all the fields")
            self.msg.exec_()
        else:
            if username in data:
                if password in data:
                    self.loginAcceptedSignal.emit()
                else:
                    self.msg.setText("Wrong password")
                    self.msg.exec_()
            else:
                self.msg.setText("Wrong username")
                self.msg.exec_()

    def clear(self):
        self.username_lin.setText("")
        self.password_lin.setText("")

if __name__ == "__main__":
    import qdarkstyle
    app = QtWidgets.QApplication([])
    w = LoginManager()
    w.show()
    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()