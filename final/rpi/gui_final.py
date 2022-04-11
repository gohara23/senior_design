# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'final_senior_design_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import cv2 as cv

from PyQt5.QtWidgets import QWidget, QLabel, QApplication
from PyQt5.QtCore import QThread, Qt, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QImage, QPixmap


def list_ports():
    """
    Test the ports and returns a tuple with the available ports and the ones that are working.
    """
    non_working_ports = []
    dev_port = 0
    working_ports = []
    available_ports = []
    # if there are more than 5 non working ports stop the testing.
    while len(non_working_ports) < 5:
        camera = cv.VideoCapture(dev_port)
        if not camera.isOpened():
            non_working_ports.append(dev_port)
            print("Port %s is not working." % dev_port)
        else:
            is_reading, img = camera.read()
            w = camera.get(3)
            h = camera.get(4)
            if is_reading:
                print("Port %s is working and reads images (%s x %s)" %
                      (dev_port, h, w))
                working_ports.append(dev_port)
            else:
                print("Port %s for camera ( %s x %s) is present but does not reads." % (
                    dev_port, h, w))
                available_ports.append(dev_port)
        dev_port += 1
    return available_ports, working_ports, non_working_ports


class ImageSensingThread(QThread):
    change_pixmap_one = pyqtSignal(QImage)
#     _, ports, _ = list_ports()
    ports = [0, 2]

    def run(self):
        while True:
            cam_one = cv.VideoCapture(self.ports[0])
            ret_one, frame_one = cam_one.read()

            if not ret_one:
                print("Cam one error")

            cam_one.release()

            cam_two = cv.VideoCapture(self.ports[1])
            ret_two, frame_two = cam_two.read()

            if not ret_two:
                print("Cam two error")

            cam_two.release()

            v1 = frame_one[140:330, 50:140]
            v2 = frame_one[75:340, 290:395]
            v3 = frame_two[80:315, 30:110]
            v4 = frame_two[65:320, 250:360]
            v5 = frame_two[75:315, 500:605]

            vials = [v1, v2, v3, v4, v5]

            ix = 1

            resized_vials = [
                cv.resize(vial, (50, 120), interpolation=cv.INTER_AREA) for vial in vials]

            h, w, ch = resized_vials[0].shape
            bytesPerLine = ch*w
            convertToQtFormat = QImage(
                vials[0].data, w, h, bytesPerLine, QImage.Format_RGB888)
            # p = convertToQtFormat.scaled(50, 120, Qt.KeepAspectRatio)
            self.change_pixmap_one.emit(convertToQtFormat)

            # return resized_vials


class Ui_MainWindow(object):
    #     @pyqtSlot(QImage)
    def setImage(self, image):
        scene = QtWidgets.QGraphicsScene()
        scene.addPixmap(image)
        print(type(image))
        self.vial_cam_1.setScene(scene)
        # self.vial_cam_1.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.vial_cam_1 = QtWidgets.QGraphicsView(self.centralwidget)
        self.vial_cam_1.setGeometry(QtCore.QRect(10, 10, 50, 120))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.vial_cam_1.sizePolicy().hasHeightForWidth())
        self.vial_cam_1.setSizePolicy(sizePolicy)
        self.vial_cam_1.setMinimumSize(QtCore.QSize(50, 120))
        self.vial_cam_1.setMaximumSize(QtCore.QSize(50, 120))
        self.vial_cam_1.setObjectName("vial_cam_1")
        th = ImageSensingThread()
        th.change_pixmap_one.connect(self.setImage)

        self.vial_cam_2 = QtWidgets.QGraphicsView(self.centralwidget)
        self.vial_cam_2.setGeometry(QtCore.QRect(70, 10, 50, 120))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.vial_cam_2.sizePolicy().hasHeightForWidth())
        self.vial_cam_2.setSizePolicy(sizePolicy)
        self.vial_cam_2.setMinimumSize(QtCore.QSize(50, 120))
        self.vial_cam_2.setMaximumSize(QtCore.QSize(50, 120))
        self.vial_cam_2.setObjectName("vial_cam_2")
        self.vial_cam_3 = QtWidgets.QGraphicsView(self.centralwidget)
        self.vial_cam_3.setGeometry(QtCore.QRect(130, 10, 50, 120))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.vial_cam_3.sizePolicy().hasHeightForWidth())
        self.vial_cam_3.setSizePolicy(sizePolicy)
        self.vial_cam_3.setMinimumSize(QtCore.QSize(50, 120))
        self.vial_cam_3.setMaximumSize(QtCore.QSize(50, 120))
        self.vial_cam_3.setObjectName("vial_cam_3")
        self.vial_cam_4 = QtWidgets.QGraphicsView(self.centralwidget)
        self.vial_cam_4.setGeometry(QtCore.QRect(190, 10, 50, 120))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.vial_cam_4.sizePolicy().hasHeightForWidth())
        self.vial_cam_4.setSizePolicy(sizePolicy)
        self.vial_cam_4.setMinimumSize(QtCore.QSize(50, 120))
        self.vial_cam_4.setMaximumSize(QtCore.QSize(50, 120))
        self.vial_cam_4.setObjectName("vial_cam_4")
        self.vial_cam_5 = QtWidgets.QGraphicsView(self.centralwidget)
        self.vial_cam_5.setGeometry(QtCore.QRect(250, 10, 50, 120))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.vial_cam_5.sizePolicy().hasHeightForWidth())
        self.vial_cam_5.setSizePolicy(sizePolicy)
        self.vial_cam_5.setMinimumSize(QtCore.QSize(50, 120))
        self.vial_cam_5.setMaximumSize(QtCore.QSize(50, 120))
        self.vial_cam_5.setObjectName("vial_cam_5")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(30, 130, 21, 20))
        self.label_1.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 130, 21, 20))
        self.label_2.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 130, 21, 20))
        self.label_3.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(210, 130, 21, 20))
        self.label_4.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(270, 130, 21, 20))
        self.label_5.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.live_temp_1 = QtWidgets.QLCDNumber(self.centralwidget)
        self.live_temp_1.setGeometry(QtCore.QRect(0, 150, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setStrikeOut(False)
        self.live_temp_1.setFont(font)
        self.live_temp_1.setStyleSheet("QLCDNumber{\n"
                                       "    color: rgb(255, 255, 255);    \n"
                                       "    background-color: rgb(50, 50, 50);\n"
                                       "}")
        self.live_temp_1.setSmallDecimalPoint(False)
        self.live_temp_1.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.live_temp_1.setProperty("value", 35.78)
        self.live_temp_1.setObjectName("live_temp_1")
        self.live_temp_2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.live_temp_2.setGeometry(QtCore.QRect(60, 150, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setStrikeOut(False)
        self.live_temp_2.setFont(font)
        self.live_temp_2.setStyleSheet("QLCDNumber{\n"
                                       "    color: rgb(0, 255, 0);    \n"
                                       "    background-color: rgb(50, 50, 50);\n"
                                       "}")
        self.live_temp_2.setSmallDecimalPoint(False)
        self.live_temp_2.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.live_temp_2.setProperty("value", 35.78)
        self.live_temp_2.setObjectName("live_temp_2")
        self.live_temp_3 = QtWidgets.QLCDNumber(self.centralwidget)
        self.live_temp_3.setGeometry(QtCore.QRect(120, 150, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setStrikeOut(False)
        self.live_temp_3.setFont(font)
        self.live_temp_3.setStyleSheet("QLCDNumber{\n"
                                       "    color: rgb(255, 255, 255);    \n"
                                       "    background-color: rgb(50, 50, 50);\n"
                                       "}")
        self.live_temp_3.setSmallDecimalPoint(False)
        self.live_temp_3.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.live_temp_3.setProperty("value", 35.78)
        self.live_temp_3.setObjectName("live_temp_3")
        self.live_temp_4 = QtWidgets.QLCDNumber(self.centralwidget)
        self.live_temp_4.setGeometry(QtCore.QRect(180, 150, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setStrikeOut(False)
        self.live_temp_4.setFont(font)
        self.live_temp_4.setStyleSheet("QLCDNumber{\n"
                                       "    color: rgb(0, 255, 0);    \n"
                                       "    background-color: rgb(50, 50, 50);\n"
                                       "}")
        self.live_temp_4.setSmallDecimalPoint(False)
        self.live_temp_4.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.live_temp_4.setProperty("value", 35.78)
        self.live_temp_4.setObjectName("live_temp_4")
        self.live_temp_5 = QtWidgets.QLCDNumber(self.centralwidget)
        self.live_temp_5.setGeometry(QtCore.QRect(240, 150, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setStrikeOut(False)
        self.live_temp_5.setFont(font)
        self.live_temp_5.setStyleSheet("QLCDNumber{\n"
                                       "    color: rgb(255, 255, 255);    \n"
                                       "    background-color: rgb(50, 50, 50);\n"
                                       "}")
        self.live_temp_5.setSmallDecimalPoint(False)
        self.live_temp_5.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.live_temp_5.setProperty("value", 35.78)
        self.live_temp_5.setObjectName("live_temp_5")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(320, 10, 251, 251))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.tableWidget.setFont(font)
        self.tableWidget.setAutoFillBackground(True)
        self.tableWidget.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(13)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(35)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(36)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(17)
        self.tableWidget.verticalHeader().setMinimumSectionSize(10)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.pushButton_go = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_go.setGeometry(QtCore.QRect(345, 265, 60, 40))
        self.pushButton_go.setStyleSheet("QPushButton {\n"
                                         "    background-color: rgb(0, 255, 127);\n"
                                         "    border-style: outset;\n"
                                         "    border-width: 2px;\n"
                                         "    border-color: black;\n"
                                         "    font: 63 24pt \"Segoe UI Semibold\";\n"
                                         "}\n"
                                         "QPushButton:pressed {\n"
                                         "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                         "                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
                                         "}")
        self.pushButton_go.setObjectName("pushButton_go")
        self.plot_1 = QtWidgets.QGraphicsView(self.centralwidget)
        self.plot_1.setGeometry(QtCore.QRect(10, 170, 140, 140))
        self.plot_1.setObjectName("plot_1")
        self.plot_2 = QtWidgets.QGraphicsView(self.centralwidget)
        self.plot_2.setGeometry(QtCore.QRect(160, 170, 140, 140))
        self.plot_2.setObjectName("plot_2")
        self.plot_3 = QtWidgets.QGraphicsView(self.centralwidget)
        self.plot_3.setGeometry(QtCore.QRect(10, 310, 140, 140))
        self.plot_3.setObjectName("plot_3")
        self.plot_4 = QtWidgets.QGraphicsView(self.centralwidget)
        self.plot_4.setGeometry(QtCore.QRect(160, 310, 140, 140))
        self.plot_4.setObjectName("plot_4")
        self.plot_5 = QtWidgets.QGraphicsView(self.centralwidget)
        self.plot_5.setGeometry(QtCore.QRect(310, 310, 140, 140))
        self.plot_5.setObjectName("plot_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_1.setText(_translate("MainWindow", "1"))
        self.label_2.setText(_translate("MainWindow", "2"))
        self.label_3.setText(_translate("MainWindow", "3"))
        self.label_4.setText(_translate("MainWindow", "4"))
        self.label_5.setText(_translate("MainWindow", "5"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Ti [C]"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Tm [C]"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Tf [C]"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "tr [min]"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "td1 [min]"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "tf [min]"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "td2 [min]"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "Red [mL]"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "Red [min]"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "Blue [mL]"))
        item = self.tableWidget.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "Blue [min]"))
        item = self.tableWidget.verticalHeaderItem(11)
        item.setText(_translate("MainWindow", "Yellow [mL]"))
        item = self.tableWidget.verticalHeaderItem(12)
        item.setText(_translate("MainWindow", "Yellow [min]"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "VIAL 1"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "VIAL 2"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "VIAL 3"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "VIAL 4"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "VIAL 5"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton_go.setText(_translate("MainWindow", "GO"))


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
