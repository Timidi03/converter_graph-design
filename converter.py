import sys
from PyQt5.QtCore import pyqtSlot, QDate,QTime,QDateTime,Qt
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
import requests
import os
import time
from bs4 import BeautifulSoup


class Conv(QMainWindow):
    def __init__(self):
        super(Conv, self).__init__()
        loadUi('converter.ui', self)
        self.setWindowTitle('Конвертер')
        self.setWindowIcon(QtGui.QIcon('конвертер.png'))
        now = QDateTime.currentDateTime()
        self.textEdit_2.setText(now.toString())
        x = self.fillCombobox()
        x1 = self.fillCombobox1()
        self.pushButton.clicked.connect(self.retrieveText)
    def fillCombobox(self):
        per_iz = ['Выберите', 'RUB', 'USD', 'EUR', 'CHF']
        for i in per_iz:
            self.comboBox.addItem(i)

    def fillCombobox1(self):
        per_iz = ['Выберите', 'RUB', 'USD', 'EUR', 'CHF']
        for i in per_iz:
            self.comboBox_2.addItem(i)

    def retrieveText(self):
        summ = self.plainTextEdit.toPlainText()
        summ = int(summ)
        site = 'https://finance.rambler.ru/calculators/converter/'
        site = site + str(summ) + '-' + self.comboBox.currentText() + "-" + self.comboBox_2.currentText()+'/'
        os.system("cls")

        #headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.69'}

        full_page = requests.get(site)

        soup = BeautifulSoup(full_page.content, 'html.parser')

        date = soup.findAll('div', {'class': 'converter-display__value'})

        self.textEdit.setText(str(date[1].text) + " " + self.comboBox_2.currentText())

        #now = QDateTime.currentDateTime()

        #print("Local datetime: ", now.toString(Qt.ISODate))
        #self.textEdit_2.setText(now.toString(Qt.ISODate))
        #print("Universal datetime: ", now.toUTC().toString(Qt.ISODate))

        #print("The offset from UTC is: {0} seconds".format(now.offsetFromUtc()))

#if __name__ == "__main__":
app = QApplication(sys.argv)
widget = Conv()
widget.show()
sys.exit(app.exec_())
