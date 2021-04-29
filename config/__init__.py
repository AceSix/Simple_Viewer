# -*- coding:utf-8 -*-
###################################################################
###   @FilePath: \PyQt5-FDD\config\__init__.py
###   @Author: Ziang Liu
###   @Date: 2020-11-23 22:17:55
###   @LastEditors: Ziang Liu
###   @LastEditTime: 2020-11-30 20:35:51
###   @Copyright (C) 2020 SJTU. All rights reserved.
###################################################################

from PyQt5 import QtCore
from .styles import main_style

def List2Qrect(size, widget):
    w, h = widget.baseSize().w, widget.baseSize().h
    position = QtCore.QRect(size[0]*w,  ### x
                            size[1]*h,  ### y
                            size[2]*w,  ### width
                            size[3]*h)  ### height
    return position

def List2Cord(size, widget):
    w, h = widget.baseSize().w, widget.baseSize().h
    position = [size[0]*w,  ### x
                size[1]*h,  ### y
                size[2]*w,  ### width
                size[3]*h]  ### height
    return position