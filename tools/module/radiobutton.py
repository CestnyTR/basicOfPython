import sys
from PyQt5 import QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_UI()

    def init_UI(self):
        self.question = QtWidgets.QLabel("Hangi Dili Daha Çok Seviyorsunuz?")
        self.python = QtWidgets.QRadioButton("Python")
        self.java = QtWidgets.QRadioButton("Java")
        self.php = QtWidgets.QRadioButton("Php")

        self.message = QtWidgets.QLabel()

        self.buton = QtWidgets.QPushButton("Kontrol Et")

        v_box = QtWidgets.QVBoxLayout()

        v_box.addWidget(self.question)
        v_box.addWidget(self.python)
        v_box.addWidget(self.java)
        v_box.addWidget(self.php)
        v_box.addWidget(self.buton)
        v_box.addStretch()
        v_box.addWidget(self.message)

        self.setLayout(v_box)
        self.setGeometry(100,100,500,500)
        self.setWindowTitle("RadioButton")

        self.buton.clicked.connect(lambda : self.click(self.python.isChecked(),
                                              self.java.isChecked(),
                                              self.php.isChecked(),
                                              self.message))

        self.show()

    def click(self,python,java,php,message):
        if python:
            self.message.setText("Python")
        if java:
            self.message.setText("Java")
        if php:
            self.message.setText("Php")





# app = QtWidgets.QApplication(sys.argv)

# window = Window()

# sys.exit(app.exec_())
