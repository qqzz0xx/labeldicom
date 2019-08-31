#!/usr/bin/env python  
# -*- coding:utf-8 _*-  

""" 
@author:sqz
@time: 2019/8/31

"""
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow

from ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    @pyqtSlot()
    def on_pushButton_clicked(self):
        print(111111111)

