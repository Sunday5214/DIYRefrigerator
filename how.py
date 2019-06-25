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
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMessageBox

__author__ = "Deokyu Lim <hong18s@gmail.com>"

class PW_setting(QWidget):
    def __init__(self):
        QWidget.__init__(self)

class SerialConnect():
    def SendMessage(self, Message):
        self.ser = serial.Serial("/dev/ttyS0", 9600)
        self.ser.write(bytes(Message.encode()))
        self.ser.close()

    def ReadMessage(self):
        self.ser = serial.Serial("/dev/ttyS0", 9600)
        self.ser.read()
        self.ser.close()


class Password_Page(QWidget):
    # 계산 버튼이 눌러졌을때 값을 전달할 시그널
    #result_changed = pyqtSignal(int, name="resultChanged")

    def __init__(self):
        QWidget.__init__(self)
        # 사용될 위젯 생성
        self.tbx_pw = QLineEdit(self)
       # self.tbx_pw.setEchoMode(QLineEdit.Password)
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
        #
        # # 기본 값 생성
        # self.set_random_numbers()


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
                    ser = SerialConnect()
                    ser.SendMessage("10")
                    break




        #여기에 시리얼 관련코드 필요
    # 계산하여 값을 전송
    # @pyqtSlot()
    # def calculate(self):
    #     result = self.input_a + self.input_b
    #     self.result_changed.emit(result)
    #
    # @pyqtSlot()
    # def set_random_numbers(self):
    #     self.input_a = random.randrange(1, 100)
    #     self.input_b = random.randrange(1, 100)
    #     self.lb.setText("{0} + {1}".format(self.input_a, self.input_b))


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
    # 페이지 중앙 라벨에 값을 바꿀 수 있는 슬롯
    # @pyqtSlot(int, name="setValue")
    # def set_value(self, v: int):
    #     self.lb_result.setText(str(v))


class Form(QWidget):
    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)
        self.tbw = QTabWidget()
        self.init_widget()

    def init_widget(self):
        """
        현재 위젯의 모양등을 초기화
        """
        self.setWindowTitle("Tab Widget")
        form_lbx = QBoxLayout(QBoxLayout.TopToBottom, parent=self)
        self.setLayout(form_lbx)
        self.resize(800, 480)
        form_lbx.addWidget(self.tbw)

        # 페이지 생성e
        self.password_page = Password_Page()
        self.pw_setting = PW_setting()
        self.temperature_page = Temperature_Page()


        # 기본 탭 생성
        self.tbw.addTab(self.password_page, "잠금해제")
        self.tbw.addTab(self.pw_setting, "잠금설정")
        self.tbw.addTab(self.temperature_page, "온도설정")


        # # 시그널 슬롯 연결
        # # 입력 페이지의 값이 계산되면 즉시 결과 페이지에 반영됨
        # self.page_input.result_changed.connect(self.page_result.set_value)
        # # 탭을 결과 페이지로 강제 이동
        # self.page_input.result_changed.connect(
        #     lambda __: self.tbw.setCurrentIndex(1))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    exit(app.exec_())