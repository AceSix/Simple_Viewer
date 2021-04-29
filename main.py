# -*- coding:utf-8 -*-
###################################################################
###   @FilePath: \Comic_Reader\main.py
###   @Author: Ziang Liu
###   @Date: 2020-11-25 19:04:29
###   @LastEditors: Ziang Liu
###   @LastEditTime: 2021-04-02 20:52:07
###   @Copyright (C) 2020 SJTU. All rights reserved.
###################################################################

import sys 	
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt

side_config = ['menu', 'content']

DEBUG = True
if __name__=="__main__":
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)

    size = (384, 512)

    from Framework import PageManager
    from UI import UI1, UI2

    project = PageManager(DEBUG, size=size, side=side_config, top='')
    project.initialize(UI1(project), UI2())
    project.show()
    
    sys.exit(app.exec_())

