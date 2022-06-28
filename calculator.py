from PyQt5 import QtCore, QtGui, QtWidgets
import re


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(360, 568)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.output_lable = QtWidgets.QLabel(self.centralwidget)
        self.output_lable.setGeometry(QtCore.QRect(10, 10, 341, 91))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.output_lable.setFont(font)
        self.output_lable.setFrameShape(QtWidgets.QFrame.Box)
        self.output_lable.setFrameShadow(QtWidgets.QFrame.Raised)
        self.output_lable.setLineWidth(2)
        self.output_lable.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.output_lable.setObjectName("output_lable")
        self.percent_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.percent_it())
        self.percent_button.setGeometry(QtCore.QRect(10, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.percent_button.setFont(font)
        self.percent_button.setObjectName("percent_button")

        self.c_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.clear_screen())
        self.c_button.setGeometry(QtCore.QRect(90, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.c_button.setFont(font)
        self.c_button.setObjectName("c_button")

        self.arrow_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.remove_it())
        self.arrow_button.setGeometry(QtCore.QRect(170, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.arrow_button.setFont(font)
        self.arrow_button.setObjectName("arrow_button")

        self.divide_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.pres_it("/"))
        self.divide_button.setGeometry(QtCore.QRect(275, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.divide_button.setFont(font)
        self.divide_button.setObjectName("divide_button")

        self.multiply_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.pres_it("*"))
        self.multiply_button.setGeometry(QtCore.QRect(275, 190, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.multiply_button.setFont(font)
        self.multiply_button.setObjectName("multiply_button")

        self.add_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.pres_it("+"))
        self.add_button.setGeometry(QtCore.QRect(275, 350, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.add_button.setFont(font)
        self.add_button.setObjectName("add_button")

        self.minus_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.pres_it("-"))
        self.minus_button.setGeometry(QtCore.QRect(275, 270, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.minus_button.setFont(font)
        self.minus_button.setObjectName("minus_button")

        self.button_9 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.pres_it("9"))
        self.button_9.setGeometry(QtCore.QRect(170, 190, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.button_9.setFont(font)
        self.button_9.setObjectName("button_9")

        self.button_8 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.pres_it("8"))
        self.button_8.setGeometry(QtCore.QRect(90, 190, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.button_8.setFont(font)
        self.button_8.setObjectName("button_8")

        self.button_7 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.pres_it("7"))
        self.button_7.setGeometry(QtCore.QRect(10, 190, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.button_7.setFont(font)
        self.button_7.setObjectName("button_7")

        self.button_6 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.pres_it("6"))
        self.button_6.setGeometry(QtCore.QRect(170, 270, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.button_6.setFont(font)
        self.button_6.setObjectName("button_6")

        self.button_5 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.pres_it("5"))
        self.button_5.setGeometry(QtCore.QRect(90, 270, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.button_5.setFont(font)
        self.button_5.setObjectName("button_5")

        self.button_4 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.pres_it("4"))
        self.button_4.setGeometry(QtCore.QRect(10, 270, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.button_4.setFont(font)
        self.button_4.setObjectName("button_4")

        self.button_3 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.pres_it("3"))
        self.button_3.setGeometry(QtCore.QRect(170, 350, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.button_3.setFont(font)
        self.button_3.setObjectName("button_3")

        self.button_2 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.pres_it("2"))
        self.button_2.setGeometry(QtCore.QRect(90, 350, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.button_2.setFont(font)
        self.button_2.setObjectName("button_2")

        self.button_1 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.pres_it("1"))
        self.button_1.setGeometry(QtCore.QRect(10, 350, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.button_1.setFont(font)
        self.button_1.setObjectName("button_1")

        self.button_0 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.pres_it("0"))
        self.button_0.setGeometry(QtCore.QRect(90, 430, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.button_0.setFont(font)
        self.button_0.setObjectName("button_0")

        self.decimal_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.dot_it())
        self.decimal_button.setGeometry(QtCore.QRect(170, 430, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.decimal_button.setFont(font)
        self.decimal_button.setObjectName("decimal_button")

        self.plus_minus_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.plus_minus_it())
        self.plus_minus_button.setGeometry(QtCore.QRect(10, 430, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.plus_minus_button.setFont(font)
        self.plus_minus_button.setObjectName("plus_minus_button")

        self.equal_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.math_it())
        self.equal_button.setGeometry(QtCore.QRect(275, 430, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.equal_button.setFont(font)
        self.equal_button.setObjectName("equal_button")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 360, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    sings = ["+", "-", "*", "/"]

    def percent_it(self):
        screen = self.output_lable.text()
        numbers = re.findall("[0-9.]+", screen)
        if len(numbers) == 1 and len(numbers[0]) == len(screen):
            screen = '0'
        else:
            number = numbers[-1]
            if len(numbers) > 1:
                number2 = numbers[-2]
            else:
                number2 = numbers[-1]
            if '.' in number:
                number = float(number)
            else:
                number = int(number)
            if '.' in number2:
                number2 = float(number2)
            else:
                number2 = int(number2)
            result = number2 * (number / 100)
            index = -(len(str(number)))
            print(result)
            print(index)
            screen = screen[:index] + str(result)
            print(screen[:index])
        self.output_lable.setText(screen)

    def math_it(self):
        screen = self.output_lable.text()
        answer = eval(screen)
        self.output_lable.setText(str(answer))

    def plus_minus_it(self):
        screen = self.output_lable.text()
        numbers = re.findall("[0-9.]+", screen)
        if len(numbers) == 1:
            if screen[0] == '-':
                screen = screen[1::]
            elif screen[0].isdigit():
                screen = '-' + screen
        else:
            last = numbers[-1]
            sing_index = -(len(last) + 1)
            sign = screen[sing_index]
            if sign == '+':
                screen = screen[:sing_index] + '-' + screen[sing_index + 1:]
            elif sign == '-':
                screen = screen[:sing_index] + '+' + screen[sing_index + 1:]

        self.output_lable.setText(screen)

    def remove_it(self):
        screen = self.output_lable.text()
        screen = screen[:-1]
        self.output_lable.setText(screen)

    def dot_it(self):
        screen = self.output_lable.text()
        numbers = re.findall("[^-+/*]+", screen)
        if '.' in numbers[-1]:
            pass
        else:
            self.output_lable.setText(f'{screen}.')

    def clear_screen(self):
        self.output_lable.setText('0')

    def pres_it(self, pressed):

        if self.output_lable.text() == '0':
            self.output_lable.setText('')
        self.output_lable.setText(f'{self.output_lable.text()}{pressed}')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.output_lable.setText(_translate("MainWindow", "0"))
        self.percent_button.setText(_translate("MainWindow", "%"))
        self.c_button.setText(_translate("MainWindow", "C"))
        self.arrow_button.setText(_translate("MainWindow", "<<"))
        self.divide_button.setText(_translate("MainWindow", "/"))
        self.button_9.setText(_translate("MainWindow", "9"))
        self.multiply_button.setText(_translate("MainWindow", "x"))
        self.button_7.setText(_translate("MainWindow", "7"))
        self.button_8.setText(_translate("MainWindow", "8"))
        self.button_6.setText(_translate("MainWindow", "6"))
        self.minus_button.setText(_translate("MainWindow", "-"))
        self.button_4.setText(_translate("MainWindow", "4"))
        self.button_5.setText(_translate("MainWindow", "5"))
        self.button_3.setText(_translate("MainWindow", "3"))
        self.add_button.setText(_translate("MainWindow", "+"))
        self.button_1.setText(_translate("MainWindow", "1"))
        self.button_2.setText(_translate("MainWindow", "2"))
        self.decimal_button.setText(_translate("MainWindow", "."))
        self.plus_minus_button.setText(_translate("MainWindow", "+/-"))
        self.equal_button.setText(_translate("MainWindow", "="))
        self.button_0.setText(_translate("MainWindow", "0"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
