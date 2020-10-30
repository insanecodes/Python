import sys
from decimal import Decimal

from PyQt5 import QtCore, QtGui, QtWidgets, uic


qtCreatorFile = "mainwindow.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.calc_tax_button.clicked.connect(self.calculate_tax)
    
    def calculate_tax(self):
        price = Decimal(self.price_box.text())
        tax = Decimal(self.tax_rate.value())
        total_price = price  + ((tax / 100) * price)
        total_price_string = "The total price with tax is: {:.2f}".format(total_price)
        self.results_output.setText(total_price_string)

        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
