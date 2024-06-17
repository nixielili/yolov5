# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from PyQt5 import QtWidgets, QtGui, QtCore
from form import Ui_Form

from PyQt5.QtWidgets import QApplication
from python_trt import *

def cvImgtoQtImg(cvImg):  # 定义opencv图像转PyQt图像的函数
    QtImgBuf = cv2.cvtColor(cvImg, cv2.COLOR_BGR2BGRA)
    QtImg = QtGui.QImage(QtImgBuf.data, QtImgBuf.shape[1], QtImgBuf.shape[0], QtGui.QImage.Format_RGB32)
    return QtImg


class MyPyQT_Form(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(MyPyQT_Form, self).__init__()
        self.setupUi(self)
        self.ImgDisp = QtWidgets.QLabel(self)
        self.ImgDisp.setGeometry(QtCore.QRect(30, 10, 640, 480))
        self.ImgDisp.setObjectName("ImgDisp")
        self.bClose = False
        self.fps = 30

    def stop_click(self):
        self.bClose = True

    def pushButton_click(self):
        self.bClose = False
        cap = cv2.VideoCapture(r'C:\Users\李子珍\Desktop\test.mp4')  # 打开影片

        while not self.bClose:
            ret, frame = cap.read()  # 逐帧读取影片
            if not ret:
                break

            frame = cv2.resize(frame,[640,480])
            QtImg = cvImgtoQtImg(frame)  # 将帧数据转换为PyQt图像格式
            self.ImgDisp.setPixmap(QtGui.QPixmap.fromImage(QtImg))  # 在ImgDisp显示图像
            self.ImgDisp.show()  # 刷新界面
            cv2.waitKey(int(1000 / self.fps))  # 休眠一会，确保每秒播放fps帧

        # 完成所有操作后，释放捕获器
        cap.release()

    def yoloButton_click(self):
        self.bClose = False

        det = Detector(model_path=b'yolov5.engine', dll_path='yolov5.dll')
        with open('classes.txt') as f:
            classes = f.read().strip().split()
        color = getColor(classes)

        cap = cv2.VideoCapture(r'C:\Users\李子珍\Desktop\test.mp4')

        while not self.bClose:
            success, frame = cap.read()
            if success:
                frame = cv2.resize(frame, [640, 480])
                result = det.predict(frame)
                frame = visualize(frame, result, classes, color)
                QtImg = cvImgtoQtImg(frame)  # 将帧数据转换为PyQt图像格式
                self.ImgDisp.setPixmap(QtGui.QPixmap.fromImage(QtImg))  # 在ImgDisp显示图像
                self.ImgDisp.show()  # 刷新界面
                cv2.waitKey(int(1000 / self.fps))  # 休眠一会，确保每秒播放fps帧
            else:
                break

        det.free()
        cap.release()

if __name__ == '__main__':
    app = QApplication([])

    myqt =  MyPyQT_Form()
    myqt.show()

    app.exec_()
