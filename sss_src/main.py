# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import score_statistics
import os

if __name__ == "__main__":
    if os.path.isfile("./data.json"):
        os.remove("./data.json")

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = score_statistics.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
