import sys
from PyQt5 import QtWidgets, QtGui


class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("PyQt5 Demo")
        self.setGeometry(450, 100, 500, 500)

        exp1_btn = QtWidgets.QPushButton("Yazı, resim ve buton ekleme")
        exp2_btn = QtWidgets.QPushButton("Layout, .addStretch()")
        exp3_btn = QtWidgets.QPushButton("Butonlara fonksiyon ekleme")
        exp4_btn = QtWidgets.QPushButton("Input alma ve kontrol etme")
        exp5_btn = QtWidgets.QPushButton("Checkbox örneği")
        exp6_btn = QtWidgets.QPushButton("Radio buton örneği")
        exp7_btn = QtWidgets.QPushButton("Menü bar oluşturma")

        verticalLayout = QtWidgets.QVBoxLayout()
        verticalLayout.addWidget(exp1_btn)
        verticalLayout.addWidget(exp2_btn)
        verticalLayout.addWidget(exp3_btn)
        verticalLayout.addWidget(exp4_btn)
        verticalLayout.addWidget(exp5_btn)
        verticalLayout.addWidget(exp6_btn)
        verticalLayout.addWidget(exp7_btn)

        exp1_btn.clicked.connect(self.exp1)
        exp2_btn.clicked.connect(self.exp2)
        exp3_btn.clicked.connect(self.exp3)
        exp4_btn.clicked.connect(self.exp4)
        exp5_btn.clicked.connect(self.exp5)
        exp6_btn.clicked.connect(self.exp6)
        exp7_btn.clicked.connect(self.exp7)

        self.setLayout(verticalLayout)
        self.show()

    def exp1(self):
        self.new_window = QtWidgets.QWidget()
        self.new_window.setWindowTitle("PyQt5 Demo")
        self.new_window.setGeometry(450, 100, 500, 500)

        text = QtWidgets.QLabel("Hello world", self.new_window)
        text.move(50, 50)

        pic = QtWidgets.QLabel(self.new_window)
        pic.setPixmap(QtGui.QPixmap("python.png"))  # Resim yolu düzeltildi
        pic.move(125, 100)

        button = QtWidgets.QPushButton("Button", self.new_window)
        button.move(220, 400)

        self.new_window.show()

    def exp2(self):
        self.new_window = QtWidgets.QWidget()
        self.new_window.setWindowTitle("PyQt5 Demo")
        self.new_window.setGeometry(450, 100, 500, 500)

        button1 = QtWidgets.QPushButton("Button1 (Vertical)")
        button2 = QtWidgets.QPushButton("Button2 (Vertical)")

        verticalLayout = QtWidgets.QVBoxLayout()
        verticalLayout.addStretch()
        verticalLayout.addWidget(button1)
        verticalLayout.addWidget(button2)

        self.new_window.setLayout(verticalLayout)
        self.new_window.show()

    def exp3(self):
        import btn_func as btn
        self.new_window = btn.Window()
        self.new_window.show()

    def exp4(self):
        import user_input as ui
        self.new_window = ui.Window()
        self.new_window.show()

    def exp5(self):
        import checkbox as ch
        self.new_window = ch.Window()
        self.new_window.show()

    def exp6(self):
        import radiobutton as rd
        self.new_window = rd.Window()
        self.new_window.show()

    def exp7(self):
        import menu as menu
        self.new_window = menu.Window()
        self.new_window.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
