import sys
import RPi.GPIO as gpio
import threading
import Adafruit_DHT
import os
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
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
from PyQt5.QtCore import Qt

__author__ = "Deokyu Lim <hong18s@gmail.com>"

numbertemp = 0
sensor = Adafruit_DHT.DHT11
pwtemp = ""
flag = 0
flag2 = 0
sensorValue = 0
gpio.setmode(gpio.BCM)
RelayIN1 = 3
RelayIN2 = 2
Magantic = 4
DHT11 = 17
gpio.setup(Magantic, gpio.OUT)
gpio.setup(RelayIN1, gpio.OUT)
gpio.setup(RelayIN2, gpio.OUT)


    
def goodsenser(self):
    self.cnt = 0
    
    while True:
        if self.cnt != sensorValue:
            sensorValue = self.cnt
            gpio.output(RelayIN1, False)
            gpio.output(RelayIN2, False)
        elif self.cnt == sensorValue:
            gpio.output(RelayIN1, True)
            gpio.output(RelayIN2, True)

        self.humidity, self.temperature = Adafruit_DHT.read_retry(sensor, DHT11)
        self.humidity = int(self.humidity)
        self.temperature = int(self.temperature)
        self.cnt = str(self.temperature)
    

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
class Fileio:
    def Wrtie(self, password):
        try:
            self.wfile = open("/home/pi/DIYRefrigerator/"+"password.txt", "a")
            password += "\n"
            self.wfile.write(password)
            self.wfile.close()
        except Exception as e:
            print(e)

    def ReWrite(self, data):
        try:
            self.refile = open("/home/pi/DIYRefrigerator/"+"password.txt", "r+t")
            self.refile.write(data)
        except Exception as e:
            print(e)

    def Read(self):
        try:
            self.rfile = open("/home/pi/DIYRefrigerator/"+"password.txt", "r")
            self.pwData = self.rfile.read()
            return self.pwData
        except Exception as e:
            print(e)

    def Find(self, wPassword):
        try:
            a = Fileio()
            self.data = a.Read()
            return self.data.find(wPassword)
        except Exception as e:
            print(e)

    def Update(self, wChangePW, wChangedPW):
        try:
            a = Fileio()
            self.data = a.Read()
            self.ChangeData = self.data.replace(wChangePW, wChangedPW)
            a.ReWrite(self.ChangeData)
        except Exception as e:
            print(e)


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
        self.changePW = QPushButton("비밀번호 교체", self)

        self.leftlocation = 250
        self.middlelocation = 365
        self.rightlocation = 480

        # 위젯 배치
        self.changePW.move(356, 50)
        self.tbx_pw.resize(300, 30)
        self.tbx_pw.move(self.leftlocation, 10)

        #첫째줄
        self.pb_1.resize(70, 70)
        self.pb_1.move(self.leftlocation, 78)

        self.pb_2.resize(70, 70)
        self.pb_2.move(self.middlelocation, 78)

        self.pb_3.resize(70, 70)
        self.pb_3.move(self.rightlocation, 78)

        #둘째줄
        self.pb_4.resize(70, 70)
        self.pb_4.move(self.leftlocation, 170)

        self.pb_5.resize(70, 70)
        self.pb_5.move(self.middlelocation, 170)

        self.pb_6.resize(70, 70)
        self.pb_6.move(self.rightlocation, 170)

        #셋째줄
        self.pb_7.resize(70, 70)
        self.pb_7.move(self.leftlocation, 262)

        self.pb_8.resize(70, 70)
        self.pb_8.move(self.middlelocation, 262)

        self.pb_9.resize(70, 70)
        self.pb_9.move(self.rightlocation, 262)

        #넷째줄
        self.pb_0.resize(70, 70)
        self.pb_0.move(self.leftlocation, 354)

        self.pb_clear.resize(70, 70)
        self.pb_clear.move(self.middlelocation, 354)

        self.pb_ok.resize(70, 70)
        self.pb_ok.move(self.rightlocation, 354)

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
        self.changePW.clicked.connect(self.PwChangeFunc)

    @pyqtSlot()
    def PwChangeFunc(self):
        global flag
        global flag2
        global pwtemp
        if flag2 == 0:
            self.res = QMessageBox.question(self, "알림", "비밀번호를 바꾸시겠습니까?",
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            if self.res == QMessageBox.Yes:
                pwtemp = self.tbx_pw.text()
                self.tbx_pw.clear()
                self.tbx_pw.setEchoMode(QLineEdit.Normal)
                self.tbx_pw.setText("{}".format("please Wirte now password and push button"))
                flag = 1
                flag2 = 1
        elif flag2 == 1:
            a = Fileio()
            self.enable = a.Find(self.tbx_pw.text())
            if self.enable > -1:
                a.Update(self.tbx_pw.text(), pwtemp)
                QMessageBox.question(self, "알림", "비밀번호를 바꾸었습니다.",
                                    QMessageBox.Yes, QMessageBox.Yes)
            else:
                QMessageBox.question(self, "알림", "입력한 비밀번호가 적합하지 않습니다.",
                                    QMessageBox.Yes, QMessageBox.Yes)




    @pyqtSlot()
    def AddOne(self):
        global numbertemp
        global flag
        numbertemp = 1
        self.loginPW = self.tbx_pw.text()
        if self.loginPW=="please Wirte now password and push button":
            if flag == 1:
                self.tbx_pw.setEchoMode(QLineEdit.Password)
                flag = 0
            self.tbx_pw.clear()
            self.tbx_pw.setText("{}".format(str(numbertemp)))
        else:
            self.tbx_pw.setText("{}".format(self.tbx_pw.text() + "1"))

    @pyqtSlot()
    def AddTwo(self):
        global numbertemp
        global flag
        numbertemp = 2
        self.loginPW = self.tbx_pw.text()
        if self.loginPW=="please Wirte now password and push button":
            if flag == 1:
                self.tbx_pw.setEchoMode(QLineEdit.Password)
                flag = 0
            self.tbx_pw.clear()
            self.tbx_pw.setText("{}".format(str(numbertemp)))
        else:
            self.tbx_pw.setText("{}".format(self.tbx_pw.text() + "2"))
    @pyqtSlot()
    def AddThree(self):
        global numbertemp
        global flag
        numbertemp = 3
        self.loginPW = self.tbx_pw.text()
        if self.loginPW == "please Wirte now password and push button":
            if flag == 1:
                self.tbx_pw.setEchoMode(QLineEdit.Password)
                flag = 0
            self.tbx_pw.clear()
            self.tbx_pw.setText("{}".format(str(numbertemp)))
        else:
            self.tbx_pw.setText("{}".format(self.tbx_pw.text() + "3"))
       # self.tbx_pw.text += "3"

    @pyqtSlot()
    def AddFour(self):
        global numbertemp
        global flag
        numbertemp = 4
        self.loginPW = self.tbx_pw.text()
        if self.loginPW == "please Wirte now password and push button":
            if flag == 1:
                self.tbx_pw.setEchoMode(QLineEdit.Password)
                flag = 0
            self.tbx_pw.clear()
            self.tbx_pw.setText("{}".format(str(numbertemp)))
        else:
            self.tbx_pw.setText("{}".format(self.tbx_pw.text() + "4"))

    @pyqtSlot()
    def AddFive(self):
        global numbertemp
        global flag
        numbertemp = 5
        self.loginPW = self.tbx_pw.text()
        if self.loginPW == "please Wirte now password and push button":
            if flag == 1:
                self.tbx_pw.setEchoMode(QLineEdit.Password)
                flag = 0
            self.tbx_pw.clear()
            self.tbx_pw.setText("{}".format(str(numbertemp)))
        else:
            self.tbx_pw.setText("{}".format(self.tbx_pw.text() + "5"))

    @pyqtSlot()
    def AddSix(self):
        global numbertemp
        global flag
        numbertemp = 6
        self.loginPW = self.tbx_pw.text()
        if self.loginPW == "please Wirte now password and push button":
            if flag == 1:
                self.tbx_pw.setEchoMode(QLineEdit.Password)
                flag = 0
            self.tbx_pw.clear()
            self.tbx_pw.setText("{}".format(str(numbertemp)))
        else:
            self.tbx_pw.setText("{}".format(self.tbx_pw.text() + "6"))

    @pyqtSlot()
    def AddSeven(self):
        global numbertemp
        global flag
        numbertemp = 7
        self.loginPW = self.tbx_pw.text()
        if self.loginPW == "please Wirte now password and push button":
            if flag == 1:
                self.tbx_pw.setEchoMode(QLineEdit.Password)
                flag = 0
            self.tbx_pw.clear()
            self.tbx_pw.setText("{}".format(str(numbertemp)))
        else:
            self.tbx_pw.setText("{}".format(self.tbx_pw.text() + "7"))
    @pyqtSlot()
    def AddEight(self):
        global numbertemp
        global flag
        numbertemp = 8
        self.loginPW = self.tbx_pw.text()
        if self.loginPW == "please Wirte now password and push button":
            if flag == 1:
                self.tbx_pw.setEchoMode(QLineEdit.Password)
                flag = 0
            self.tbx_pw.clear()
            self.tbx_pw.setText("{}".format(str(numbertemp)))
        else:
            self.tbx_pw.setText("{}".format(self.tbx_pw.text() + "8"))
    @pyqtSlot()
    def AddNine(self):
        global numbertemp
        global flag
        numbertemp = 9
        self.loginPW = self.tbx_pw.text()
        if self.loginPW == "please Wirte now password and push button":
            if flag == 1:
                self.tbx_pw.setEchoMode(QLineEdit.Password)
                flag = 0
            self.tbx_pw.clear()
            self.tbx_pw.setText("{}".format(str(numbertemp)))
        else:
            self.tbx_pw.setText("{}".format(self.tbx_pw.text() + "9"))
    @pyqtSlot()
    def AddZero(self):
        global numbertemp
        global flag
        numbertemp = 0
        self.loginPW = self.tbx_pw.text()
        if self.loginPW == "please Wirte now password and push button":
            if flag == 1:
                self.tbx_pw.setEchoMode(QLineEdit.Password)
                flag = 0
            self.tbx_pw.clear()
            self.tbx_pw.setText("{}".format(str(numbertemp)))
        else:
            self.tbx_pw.setText("{}".format(self.tbx_pw.text() + "0"))
    @pyqtSlot()
    def Clear(self):
        self.tbx_pw.clear()

    @pyqtSlot()
    def Unlock(self):
        self.loginPW = self.tbx_pw.text()
        a = Fileio()
        self.enablePw = a.Find(self.loginPW)
        if self.enablePw > -1 :
            self.replay = QMessageBox.question(self, "알림", "냉장고를 여시겠습니까?",
                                               QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            if self.replay == QMessageBox.Yes:
                gpio.output(Magantic, False)
                QMessageBox.question(self, "열림", "열림",  QMessageBox.Yes, QMessageBox.Yes)
            else:
                gpio.output(Magantic, True)
                QMessageBox.question(self, "닫힘", QMessageBox.Yes, QMessageBox.Yes)
        else:
            QMessageBox.question(self, "경고", "비밀번호가 일치하지 않습니다", QMessageBox.Yes, QMessageBox.Yes)


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

        self.SettingDial.resize(190, 190)
        self.SettingDial.setRange(-20, 20)
        self.SettingDial.setNotchesVisible(True)
        self.SettingDial.move(460, 250)
        self.NowTemperature.display(sensorValue)
        
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
        self.temperature_page = Temperature_Page()


        # 기본 탭 생성
        self.tbw.addTab(self.password_page, "잠금해제")
        self.tbw.addTab(self.temperature_page, "온도설정")

    def center(self):
        self.move(0, 0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    threading = threading.Thread(target=goodsenser)
    threading.daemon = True
    threading.start()
    gpio.OUTPUT(Magantic, True)
    gpio.OUTPUT(RelayIN1, True)
    gpio.OUTPUT(RelayIN2, True)
    exit(app.exec_())