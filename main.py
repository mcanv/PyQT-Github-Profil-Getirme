from cgitb import text
import sys
from PyQt6.QtWidgets import *
import pyperclip as pc
import webbrowser as wb
from PyQt6.QtGui import *
from githubprofile import GithubProile

app = QApplication(sys.argv)

def getUser():
    if(textbox.text() == ""):
        msgbox.setText("Lütfen geçerli bir kullanıcı adı giriniz!")
        msgbox.show()
        textbox.setText("")
    else:
        profile = GithubProile(textbox.text())
        if profile.name is not None:
            table.setRowCount(0)
            table.insertRow(0)
            table.setItem(0, 0, QTableWidgetItem(profile.name))
            table.setItem(0, 1, QTableWidgetItem(profile.location))
            table.setItem(0, 2, QTableWidgetItem(str(profile.reposCount)))
            table.setItem(0, 3, QTableWidgetItem(str(profile.reposCount)))
            table.setItem(0, 4, QTableWidgetItem(profile.url))
            textbox.setText("")
        else:
            table.setRowCount(0)
            msgbox.setText("Kullanıcı bulunamadı!")
            msgbox.show()
            textbox.setText("")


def goToLink(item):
    if item.column() == 4:
        pc.copy(item.text())
        wb.open(item.text())

pencere = QWidget()
pencere.setWindowTitle("Github Kullanıcı Bilgileri Uygulaması")
pencere.resize(700, 250)
pencere.setFixedSize(pencere.size())

yazi = QLabel(pencere)
yazi.move(10, 25)
yazi.setText("Github kullanıcı adı:")

table = QTableWidget(pencere)
table.resize(680, 50)
table.setRowCount(1)
table.setColumnCount(5)
table.horizontalHeader().setStretchLastSection(True)
table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
table.setHorizontalHeaderLabels(['Ad', 'Konum', 'Repo Sayısı', 'Takipçi Sayısı', 'Link'])
table.itemDoubleClicked.connect(goToLink)
table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
table.move(10, 100)
table.verticalHeader().setVisible(False)
table.show();

msgbox = QMessageBox()
msgbox.setWindowTitle("Hata!")
msgbox.setIcon(QMessageBox.Icon.Critical)
msgbox.setStandardButtons(QMessageBox.StandardButton.Ok)

textbox = QLineEdit(pencere)
textbox.resize(300, 30)
textbox.move(150, 20)
textbox.show()

button = QPushButton(pencere)
button.setText("Getir")
button.move(610, 200)
button.clicked.connect(getUser)

pencere.show()

sys.exit(app.exec())