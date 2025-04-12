import sys
from PyQt5 import QtWidgets

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        menubar = self.menuBar()
        dosya_menu = menubar.addMenu("Dosya")
        ekle_menu = menubar.addMenu("Ekle")


        dosya_yeni_proje = QtWidgets.QAction("Yeni Proje", self)
        dosya_yeni_proje.setShortcut("Ctrl+P")
        dosya_ac = QtWidgets.QAction("Ac", self)
        dosya_ac.setShortcut("Ctrl+O")
        dosya_kaydet = QtWidgets.QAction("Kaydet", self)
        dosya_kaydet.setShortcut("Ctrl+S")
        dosya_cikis = QtWidgets.QAction("Çıkış", self)
        dosya_cikis.setShortcut("Ctrl+Q")


        ekle_ara = ekle_menu.addMenu("Ara")

        ekle_ara_ara = QtWidgets.QAction("Ara", self)
        ekle_ara_ara.setShortcut("Ctrl+S")
        ekle_ara_degistir = QtWidgets.QAction("Değiştir", self)

        ekle_ara.addAction(ekle_ara_ara)
        ekle_ara.addAction(ekle_ara_degistir)




        dosya_menu.addAction(dosya_yeni_proje)
        dosya_menu.addAction(dosya_ac)
        dosya_menu.addAction(dosya_kaydet)
        dosya_menu.addAction(dosya_cikis)



        dosya_menu.triggered.connect(self.dosya_menu_def)

        self.setWindowTitle("Menubar")
        self.setGeometry(100,100,500,500)
        self.show()

    def dosya_menu_def(self, action):
        if action.text() == "Yeni Proje":
            print("Yeni Proje")
        elif action.text() == "Ac":
            print("Ac")
        elif action.text() == "Kaydet":
            print("Kaydet")
        elif action.text() == "Çıkış":
            print("Çıkış")










# app = QtWidgets.QApplication(sys.argv)

# window = Window()

# sys.exit(app.exec_())