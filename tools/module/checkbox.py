import sys

from PyQt5 import QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_UI()

    def init_UI(self):
        self.checkbox = QtWidgets.QCheckBox("Python'ı Seviyor Musunuz?")
        self.message = QtWidgets.QLabel("")
        self.buton = QtWidgets.QPushButton("Tıkla")

        v_box = QtWidgets.QVBoxLayout()

        v_box.addWidget(self.checkbox)
        v_box.addWidget(self.message)
        v_box.addWidget(self.buton)

        self.setLayout(v_box)
        self.setGeometry(100,100,500,500)
        self.setWindowTitle("CheckBox")

        self.buton.clicked.connect(lambda : self.click(self.checkbox.isChecked(),self.message))

        self.show()

    def click(self,checkbox,message):
        if checkbox:
            message.setText("Çok Güzel!")
        else:
            message.setText("Neden Sevmiyorsun?")



# app = QtWidgets.QApplication(sys.argv)

# window = Window()

# sys.exit(app.exec_())