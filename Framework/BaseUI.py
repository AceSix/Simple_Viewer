# -*- coding:utf-8 -*-
###################################################################
###   @FilePath: \Comic_Reader\Framework\BaseUI.py
###   @Author: Ziang Liu
###   @Date: 2020-11-26 19:25:34
###   @LastEditors: Ziang Liu
###   @LastEditTime: 2021-04-03 13:11:49
###   @Copyright (C) 2020 SJTU. All rights reserved.
###################################################################

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QDate,  QDateTime , QTime
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QPushButton, QListWidget, QGridLayout, QDateEdit, QDateTimeEdit, QProgressBar
from config.styles import main_style, sidebar_style
from UI.Elements import Layout, Label, DateTimeEditDemo, ProgressBar
from config.styles import title_style, transparent_style
# from canvas import base_button_icons

class BaseUI(QtWidgets.QWidget):
    def setup_UI(self, MainWindow, canvas=None):
        self.size = MainWindow.kwargs['size']
        MainWindow.resize(*self.size)
        MainWindow.setObjectName("MainWindow")
        # MainWindow
        MainWindow.setStyleSheet(main_style)

        self.setMinimumWidth(384)
        self.setMinimumHeight(512)
        
        self.__base_layout__(MainWindow)
        
        MainWindow.setWindowTitle("FDD-master")
        if not MainWindow.debug:
            MainWindow.setWindowFlags(Qt.FramelessWindowHint)  # 去掉标题栏
        MainWindow.setCentralWidget(self)


    def stack(self, widgets):
        self.stacked_widgets = []
        for widget in widgets:
            self.work_space.addWidget(widget)
            self.stacked_widgets.append(widget)


    def __base_layout__(self, MainWindow):
        self.setGeometry(0, 0, self.size[0], self.size[1])
        self.work_space = QtWidgets.QStackedWidget()
        self.work_space.setObjectName("work_space")
        
        # self.title = Label(self, 'Comic Reader', "title", title_style)
        # self.title.setAlignment(Qt.AlignCenter)
        # self.logo_region = Layout(['space', self.title, 'space'], [1,5,1], True)
        # self.logo_region.setSpacing(0)
        # self.logo_region.setContentsMargins(10, 0, 10, 0)

        vbox = Layout([
                    # self.logo_region,
                    # mid_buttons,
                    self.work_space, 
                ],[15],False)
        vbox.setSpacing(-10)
        vbox.setContentsMargins(0, 0, 0, 0)
        
        self.setLayout(vbox)

    def closeEvent(self, event):
        print('closeEvnet')

