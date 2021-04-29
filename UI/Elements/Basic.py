# -*- coding:utf-8 -*-
###################################################################
###   @FilePath: \PyQt5-FDD\UI\Elements\Basic.py
###   @Author: Ziang Liu
###   @Date: 2020-11-25 19:04:29
###   @LastEditors: Ziang Liu
###   @LastEditTime: 2021-04-02 16:24:25
###   @Copyright (C) 2020 SJTU. All rights reserved.
###################################################################

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QTableWidget
from PyQt5.QtGui import QPixmap, QMovie
from util import group_stretch

def Button(widget, text, name=None, style=None):
    element = QPushButton(widget)
    
    if name is None:
        name = text+"_button"
    element.setObjectName(name)
    element.setText(text)
    if style is not None:
        element.setStyleSheet(style)
    return element

def Custom(widget, class_item, text=None, name=None, style=None):
    element = class_item(widget)
    
    if name is None:
        name = text+"_custom"
    element.setObjectName(name)
    if text is not None:
        element.setText(text)
    if style is not None:
        element.setStyleSheet(style)
    return element


def Label(widget, text, name=None, style=None):
    element = QLabel(widget)
    
    if name is None:
        name = text+"_label"
    element.setObjectName(name)
    element.setText(text)
    if style is not None:
        element.setStyleSheet(style)
    return element

def Table(widget, name):
    element = QTableWidget(widget)

    element.setObjectName(name)
    element.setShowGrid(True)
    return element

def Layout(contents, stretch, horizontal):
    layout = QHBoxLayout() if horizontal else QVBoxLayout()
    for content in contents:
        if content == "space":
            layout.addStretch(1)
            continue
        try:
            layout.addWidget(content)
        except:
            layout.addLayout(content)

    group_stretch(layout, stretch)
    return layout
