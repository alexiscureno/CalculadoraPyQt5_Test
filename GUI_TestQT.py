import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QMainWindow



class Calculadora(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculadora Chingona')
        self.setFixedSize(235, 235)

        self._centralWidget = QWidget(self)
        self. setCentralWidget(self._centralWidget)

def main():
    calcu= QApplication(sys.argv)
    view = Calculadora()
    view.show()

    sys.exit(calcu.exec_())

if __name__=="__main__":
    main()