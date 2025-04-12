import sys
from PyQt5 import QtWidgets


class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.user_name = QtWidgets.QLineEdit()
        self.pasword = QtWidgets.QLineEdit()
        self.pasword.setEchoMode(QtWidgets.QLineEdit.Password)

        self.enter = QtWidgets.QPushButton("Giriş yap")
        self.label = QtWidgets.QLabel("")

        self.horizantal = QtWidgets.QHBoxLayout()
        self.horizantal.addStretch()
        self.horizantal.addWidget(self.user_name)
        self.horizantal.addWidget(self.pasword)
        self.horizantal.addWidget(self.enter)
        self.horizantal.addWidget(self.label)
        self.horizantal.addStretch()

        # onclick
        self.enter.clicked.connect(self.check_user_input)

        self.vektorel = QtWidgets.QVBoxLayout()
        self.vektorel.addStretch()
        self.vektorel.addLayout(self.horizantal)
        self.vektorel.addStretch()

        self.setLayout(self.vektorel)
        self.show()

    def check_user_input(self):
        if self.user_name.text() == "fahri" and self.pasword.text() == "12345":
            self.label.setText("Hoşgeldiniz "+ self.user_name.text())
        else:
            self.label.setText("Kullanıcı adı ve ya şifre yanlış")

# app = QtWidgets.QApplication(sys.argv)

# window = Window()

# sys.exit(app.exec_())
