import sys
from PyQt5 import QtWidgets


class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()


    def init_ui(self):
        self.yazi_text = QtWidgets.QLabel("Sayı")
        self.buton1 = QtWidgets.QPushButton("Arttır")
        self.buton2 = QtWidgets.QPushButton("Eksilt")
        self.sayi = 0


        horizontalLayout = QtWidgets.QHBoxLayout()
        horizontalLayout.addWidget(self.yazi_text)
        horizontalLayout.addWidget(self.buton1)
        horizontalLayout.addWidget(self.buton2)

        verticalLayout = QtWidgets.QVBoxLayout()
        verticalLayout.addStretch()
        verticalLayout.addLayout(horizontalLayout)
        verticalLayout.addStretch()

        self.buton1.clicked.connect(self.arttir)
        self.buton2.clicked.connect(self.eksilt)

        self.setLayout(verticalLayout)
        self.show()


    def arttir(self):
        self.sayi += 1
        self.yazi_text.setText(str(self.sayi))
    def eksilt(self):
        self.sayi -= 1
        self.yazi_text.setText(str(self.sayi))


# app = QtWidgets.QApplication(sys.argv)

# pencere = Pencere()

# sys.exit(app.exec_())

