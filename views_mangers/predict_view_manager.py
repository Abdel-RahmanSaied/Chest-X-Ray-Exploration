from PyQt5 import QtWidgets, QtCore, QtGui
from views import predict_view
from PyQt5.QtCore import pyqtSignal
import os
import cv2
import keras




class PredictManager(QtWidgets.QWidget, predict_view.Ui_lab):
    def __init__(self):
        super(PredictManager, self).__init__()
        self.setupUi(self)
        self.setFixedSize(720, 401)
        self.upload_photo_btn.clicked.connect(self.get_file_path)
        self.predict_btn.clicked.connect(self.run)
        self.clear_btn.clicked.connect(self.clear)
        self.msg = QtWidgets.QMessageBox()


    def get_file_path(self):
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open file", "Image files (*.jpg *.png)")
        if len(file_path) > 0:
            self.file_path_lbl.setText(file_path)
        else:
            self.file_path_lbl.setText("path to file.............")
        return file_path

    def run(self):
        if self.file_path_lbl.text() != "path to file.............":
            img_path = str(self.file_path_lbl.text())
            result = self.predict(img_path)
            self.msg.setWindowTitle("Result")
            self.msg.setIcon(QtWidgets.QMessageBox.Information)
            self.msg.setStyleSheet('''font: 12pt "Acumin Pro";''')
            self.msg.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
            self.msg.setText(result)
            self.msg.exec_()
        else:
            self.msg.setText("please select image to predict")
            self.msg.exec_()

    def predict(self, image_path):
        # os.path.join("model","chestExploration.hdf5")
        model_path = os.path.join("model", "chestExploration.hdf5")
        model = keras.models.load_model(model_path)
        gray_image = cv2.imread(image_path, 0)
        resized_image = cv2.resize(gray_image, (100, 100))
        scaled_image = resized_image.astype("float32") / 255.0
        sample_batch = scaled_image.reshape(1, 100, 100, 1)  # 1 image, 100, 100 dim , 1 no of chanels
        result = model.predict(sample_batch)
        result[result >= 0.5] = 1  # Normal
        result[result < 0.5] = 0  # Pneimonia
        if result[0][0] == 1:
            result = "Normal"
        else:
            result = "Pneimonia"
        return result

    def clear(self):
        self.file_path_lbl.setText("path to file.............")


if __name__ == "__main__":
    # import qdarkstyle
    app = QtWidgets.QApplication([])
    w = PredictManager()
    w.show()
    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()