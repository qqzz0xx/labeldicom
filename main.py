import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from gui.mainwindow import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)

    win = MainWindow()

    win.show()

    app.exec()

