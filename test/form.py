# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(700, 550)
        self.load_mp4 = QtWidgets.QPushButton(Form)
        self.load_mp4.setGeometry(QtCore.QRect(20, 510, 100, 30))
        self.load_mp4.setObjectName("load_mp4")
        self.yolov5 = QtWidgets.QPushButton(Form)
        self.yolov5.setGeometry(QtCore.QRect(180, 510, 100, 30))
        self.yolov5.setObjectName("yolov5")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(350, 510, 91, 31))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        self.load_mp4.clicked.connect(Form.pushButton_click) # type: ignore
        self.yolov5.clicked.connect(Form.yoloButton_click) # type: ignore
        self.pushButton.clicked.connect(Form.stop_click) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "PyQt-Yolov5"))
        self.load_mp4.setText(_translate("Form", "载入视频"))
        self.yolov5.setText(_translate("Form", "开始识别"))
        self.pushButton.setText(_translate("Form", "停止播放"))
