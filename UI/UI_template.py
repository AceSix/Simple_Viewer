# -*- coding:utf-8 -*-
###################################################################
###   @FilePath: \FDD-Industrial\UI\UI_template.py
###   @Author: Ziang Liu
###   @Date: 2020-11-25 19:04:29
###   @LastEditors: Ziang Liu
###   @LastEditTime: 2021-03-13 17:43:21
###   @Copyright (C) 2020 SJTU. All rights reserved.
###################################################################


from PyQt5 import QtCore, QtGui, QtWidgets

class Template(QtWidgets.QWidget):
    def __init__(self):
        super(Template, self).__init__()
        self.__setup__()
    
    def __setup__(self):
        self.tim = 0

    def __make_colors__(self): ### default color cycles
        light_cycle1 = []
        light_cycle2 = []
        light_cycle3 = []
        light_cycle4 = []
        for i in range(20):
            light_cycle1.append(QtGui.QColor(255-i, 12, 12, 255-i**2*0.5 ))
            light_cycle2 = [QtGui.QColor(255-i, 12, 12, 255-i**2*0.5)]+light_cycle2

            light_cycle3.append(QtGui.QColor(255-i, 255-i, 12, 255-i**2*0.5 ))
            light_cycle4 = [QtGui.QColor(255-i, 255-i, 12, 255-i**2*0.5)]+light_cycle4
        self.red_cycle = light_cycle1 + light_cycle2
        self.yellow_cycle = light_cycle3 + light_cycle4
        self.green_cycle = [QtGui.QColor(12, 255, 12)]
        self.white_cycle = [QtGui.QColor(255, 255, 255)]