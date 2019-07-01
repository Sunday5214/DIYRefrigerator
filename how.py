import sys
import serial
import os
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QTabWidget
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLCDNumber
from PyQt5.QtWidgets import QDial
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QDesktopWidget
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtCore import Qt

__author__ = "Deokyu Lim <hong18s@gmail.com>"


# class SerialConnect():
#     def SendMessage(self, Message):
#         self.ser = serial.Serial("/dev/ttyS0", 9600)
#         self.ser.write(bytes(Message.encode()))
#         self.ser.close()
#
#     def ReadMessage(self):
#         self.ser = serial.Serial("/dev/ttyS0", 9600)
#         self.ser.read()
#         self.ser.close()


class Password_Page(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        # 사용될 위젯 생성
        self.tbx_pw = QLineEdit(self)
        self.tbx_pw.setEchoMode(QLineEdit.Password)
        self.pb_0 = QPushButton("0", self)
        self.pb_1 = QPushButton("1", self)
        self.pb_2 = QPushButton("2", self)
        self.pb_3 = QPushButton("3", self)
        self.pb_4 = QPushButton("4", self)
        self.pb_5 = QPushButton("5", self)
        self.pb_6 = QPushButton("6", self)
        self.pb_7 = QPushButton("7", self)
        self.pb_8 = QPushButton("8", self)
        self.pb_9 = QPushButton("9", self)
        self.pb_clear = QPushButton("clear", self)
        self.pb_ok = QPushButton("해제", self)

        # 위젯 배치
        self.tbx_pw.resize(300, 30)
        self.tbx_pw.move(250, 10)

        #첫째줄
        self.pb_1.resize(70, 70)
        self.pb_1.move(250, 78)

        self.pb_2.resize(70, 70)
        self.pb_2.move(365, 78)

        self.pb_3.resize(70, 70)
        self.pb_3.move(480, 78)

        #둘째줄
        self.pb_4.resize(70, 70)
        self.pb_4.move(250, 170)

        self.pb_5.resize(70, 70)
        self.pb_5.move(365, 170)

        self.pb_6.resize(70, 70)
        self.pb_6.move(480, 170)

        #셋째줄
        self.pb_7.resize(70, 70)
        self.pb_7.move(250, 262)

        self.pb_8.resize(70, 70)
        self.pb_8.move(365, 262)

        self.pb_9.resize(70, 70)
        self.pb_9.move(480, 262)

        #넷째줄
        self.pb_0.resize(70, 70)
        self.pb_0.move(250, 354)

        self.pb_clear.resize(70, 70)
        self.pb_clear.move(365, 354)

        self.pb_ok.resize(70, 70)
        self.pb_ok.move(480, 354)

        # 시그널 슬롯 연결
        self.pb_1.clicked.connect(self.AddOne)
        self.pb_2.clicked.connect(self.AddTwo)
        self.pb_3.clicked.connect(self.AddThree)
        self.pb_4.clicked.connect(self.AddFour)
        self.pb_5.clicked.connect(self.AddFive)
        self.pb_6.clicked.connect(self.AddSix)
        self.pb_7.clicked.connect(self.AddSeven)
        self.pb_8.clicked.connect(self.AddEight)
        self.pb_9.clicked.connect(self.AddNine)
        self.pb_0.clicked.connect(self.AddZero)
        self.pb_clear.clicked.connect(self.Clear)
        self.pb_ok.clicked.connect(self.Unlock)


    @pyqtSlot()
    def AddOne(self):
        self.tbx_pw.setText("{}".format(self.tbx_pw.text() + "1"))

    @pyqtSlot()
    def AddTwo(self):
        self.tbx_pw.setText("{}".format(self.tbx_pw.text() + "2"))

    @pyqtSlot()
    def AddThree(self):
        self.tbx_pw.setText("{}".format(self.tbx_pw.text() + "3"))
       # self.tbx_pw.text += "3"

    @pyqtSlot()
    def AddFour(self):
        self.tbx_pw.setText("{}".format(self.tbx_pw.text() + "4"))

    @pyqtSlot()
    def AddFive(self):
        self.tbx_pw.setText("{}".format(self.tbx_pw.text() + "5"))

    @pyqtSlot()
    def AddSix(self):
        self.tbx_pw.setText("{}".format(self.tbx_pw.text() + "6"))

    @pyqtSlot()
    def AddSeven(self):
        self.tbx_pw.setText("{}".format(self.tbx_pw.text() + "7"))

    @pyqtSlot()
    def AddEight(self):
        self.tbx_pw.setText("{}".format(self.tbx_pw.text() + "8"))

    @pyqtSlot()
    def AddNine(self):
        self.tbx_pw.setText("{}".format(self.tbx_pw.text() + "9"))

    @pyqtSlot()
    def AddZero(self):
        self.tbx_pw.setText("{}".format(self.tbx_pw.text() + "0"))

    @pyqtSlot()
    def Clear(self):
        self.tbx_pw.clear()

    @pyqtSlot()
    def Unlock(self):
        file_on_off=os.path.isdir("login.txt")
        loginPW = self.tbx_pw.text()
        if(file_on_off):
            file = open("login.txt", "r")
            while True:
                line = file.readline()

                if not line:
                    reply = QMessageBox.question(self, "경고", "일치하는 비밀번호가 없습니다.", QMessageBox.Yes | QMessageBox.No,
                                                 QMessageBox.No)

                    if reply == QMessageBox.Yes:
                        break
                    else:
                        break
                elif(loginPW==line):
                    # ser = SerialConnect()
                    # ser.SendMessage("10")
                    break

class Setting_Page(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        PW_cb = QCheckBox("비밀번호 비활성화", self)


class Temperature_Page(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.NowTemperature = QLCDNumber(self);
        self.WantTemperature = QLCDNumber(self);
        self.SettingDial = QDial(self)
        self.lbNow = QLabel("현재 온도", self)
        self.lbWant = QLabel("희망 온도", self)
        self.NowFont = self.lbNow.font()
        self.NowFont.setPointSize(40)
        self.NowFont.setBold(True)

        self.lbNow.resize(300, 50)
        self.lbNow.move(50, 50)
        self.lbNow.setAlignment(Qt.AlignCenter)
        self.lbNow.setFont(self.NowFont)

        self.lbWant.resize(300, 50)
        self.lbWant.move(400, 50)
        self.lbWant.setAlignment(Qt.AlignCenter)
        self.lbWant.setFont(self.NowFont)

        self.NowTemperature.resize(300, 100)
        self.NowTemperature.move(50, 130)

        self.WantTemperature.resize(300, 100)
        self.WantTemperature.move(400, 130)

        self.SettingDial.resize(245, 245)
        self.SettingDial.move(430, 210)

        self.SettingDial.valueChanged.connect(self.WantTemperature.display)


class Form(QWidget):
    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)
        self.tbw = QTabWidget()
        self.init_ui()

    def init_ui(self):
        #현재 위젯의 모양등을 초기화
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        form_lbx = QBoxLayout(QBoxLayout.TopToBottom, parent=self)
        self.setLayout(form_lbx)
        self.resize(800, 480)
        self.center()
        form_lbx.addWidget(self.tbw)

        # 페이지 생성e
        self.password_page = Password_Page()
        self.setting_page = Setting_Page()
        self.temperature_page = Temperature_Page()


        # 기본 탭 생성
        self.tbw.addTab(self.password_page, "잠금해제")
        self.tbw.addTab(self.setting_page, "잠금설정")
        self.tbw.addTab(self.temperature_page, "온도설정")

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    exit(app.exec_())