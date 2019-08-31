#!/usr/bin/env python  
# -*- coding:utf-8 _*-  

""" 
@author:sqz
@time: 2019/8/31

"""

from PyQt5.QtWidgets import QWidget

from ui_slicecomponent import Ui_SliceComponent


class SliceComponent(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_SliceComponent()
        self.ui.setupUi(self)



