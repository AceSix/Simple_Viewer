# -*- coding:utf-8 -*-
###################################################################
###   @FilePath: \Simple_Viewer\UI\Elements\EmbedChart.py
###   @Author: Ziang Liu
###   @Date: 2020-11-25 19:04:29
###   @LastEditors: Ziang Liu
###   @LastEditTime: 2021-04-29 13:29:41
###   @Copyright (C) 2020 SJTU. All rights reserved.
###################################################################

from PyQt5.QtGui import QMovie, QPixmap
from PyQt5.QtWidgets import QBoxLayout, QSpacerItem, QLabel
from PyQt5.QtCore import Qt
from .Basic import Label, Layout
from config.styles import digit_board_style, digit_label_style

class DigitBoard(QLabel):
    def __init__(self, name, parent=None, horizontal=False):
        super(DigitBoard, self).__init__(parent)
        name_ = Label(None, name, style=digit_label_style)
        self.board = Label(None, '', style=digit_board_style)
        name_.setAlignment(Qt.AlignCenter)
        self.board.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("background-color:rgba(0,0,0,0); ")

        layout = Layout([name_, self.board], [1,1], horizontal)
        layout.setSpacing(0)
        self.setLayout(layout)

class EmbedChart(QLabel):
    def __init__(self, img_path, base_size, board_config, parent=None, ratio=1.5, horizontal=False):
        super(EmbedChart, self).__init__(parent)
        
        self.demo_area = QLabel(self)
        self.demo_area.setScaledContents(True)
        self.setLayout(QBoxLayout(QBoxLayout.LeftToRight, self))

        self.digits = {}
        for configs in board_config:
            self.digits[configs[0]] = {}
            self.digits[configs[0]]['element'] = DigitBoard(configs[0], self.demo_area, horizontal=horizontal)
            self.digits[configs[0]]['position'] = configs[1]

        self.layout().addItem(QSpacerItem(0, 0))
        self.layout().addWidget(self.demo_area)
        self.layout().addItem(QSpacerItem(0, 0))
        self.layout().setContentsMargins(0, 0, 0, 0)

        if 'gif' not in img_path:
            pixmap = QPixmap(img_path)
            self.aspect_ratio = pixmap.size().width() / pixmap.size().height()
            # pixmap = pixmap.scaled(256, 256, Qt.KeepAspectRatio)
            self.demo_area.setPixmap(pixmap)
        else:
            movie = QMovie(img_path)
            # self.aspect_ratio = movie.size().width() / movie.size().height()
            self.aspect_ratio = ratio
            # movie = movie.scaled(512, 512, Qt.KeepAspectRatio)
            self.demo_area.setMovie(movie)
            movie.start()

        self.setMinimumHeight(base_size)
        self.setMinimumWidth(base_size*self.aspect_ratio)

    def update_digit(self, id, text):
        text = str(text)
        self.digits[id]['element'].board.setText(text)

    def __rearrage_board__(self, width, height):
        for key in self.digits.keys():
            x = self.digits[key]['position'][0]*width
            y = self.digits[key]['position'][1]*height
            w = self.digits[key]['position'][2]*width
            h = self.digits[key]['position'][3]*height
            self.digits[key]['element'].setGeometry(x,y,w,h)

    def resizeEvent(self, e):
        w = e.size().width()
        h = e.size().height()

        if w / h > self.aspect_ratio:  # too wide
            self.layout().setDirection(QBoxLayout.LeftToRight)
            widget_stretch = h * self.aspect_ratio
            outer_stretch = (w - widget_stretch) / 2
        else:                          # too tall
            self.layout().setDirection(QBoxLayout.TopToBottom)
            widget_stretch = w / self.aspect_ratio
            outer_stretch = (h - widget_stretch) / 2

        self.layout().setStretch(0, outer_stretch)
        self.layout().setStretch(1, widget_stretch)
        self.layout().setStretch(2, outer_stretch)

        self.__rearrage_board__(self.demo_area.size().width(), self.demo_area.size().height())


        
class OverlapChart(QLabel):
    def __init__(self, img_path, base_size, board_config, parent=None, ratio=1.5):
        super(OverlapChart, self).__init__(parent)
        self.setStyleSheet("background-color : rgba(0, 0, 0, 0);")
        self.demo_area = QLabel(self)
        # sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        # sizePolicy.setHeightForWidth(True)
        # self.demo_area.setSizePolicy(sizePolicy)
        self.demo_area.setScaledContents(True)
        self.setLayout(QBoxLayout(QBoxLayout.LeftToRight, self))

        self.digits = {}
        for configs in board_config:
            name, positions, text, obj = configs
            self.digits[name] = {}
            self.digits[name]['element'] = obj
            obj.setParent(self.demo_area)
            try:
                self.digits[name]['element'].setText(text)
            except:
                pass
            self.digits[name]['position'] = positions

        self.layout().addItem(QSpacerItem(0, 0))
        self.layout().addWidget(self.demo_area)
        self.layout().addItem(QSpacerItem(0, 0))
        self.layout().setContentsMargins(0, 0, 0, 0)

        if 'gif' not in img_path:
            pixmap = QPixmap(img_path)
            self.aspect_ratio = pixmap.size().width() / pixmap.size().height()
            self.demo_area.setPixmap(pixmap)
        else:
            movie = QMovie(img_path)
            self.aspect_ratio = ratio
            self.demo_area.setMovie(movie)
            movie.start()

        self.setMinimumHeight(base_size)
        self.setMinimumWidth(base_size*self.aspect_ratio)

    def update_chart(self, img_path, ratio):
        if 'gif' not in img_path:
            pixmap = QPixmap(img_path)
            self.aspect_ratio = pixmap.size().width() / pixmap.size().height()
            self.demo_area.setPixmap(pixmap)
        else:
            movie = QMovie(img_path)
            self.aspect_ratio = ratio
            self.demo_area.setMovie(movie)
            movie.start()

    def update_digit(self, id, state):
        self.digits[id]['element'].set_state(state)

    def __rearrage_board__(self, width, height):
        for key in self.digits.keys():
            x = self.digits[key]['position'][0]*width
            y = self.digits[key]['position'][1]*height
            w = self.digits[key]['position'][2]*width
            h = self.digits[key]['position'][3]*height
            self.digits[key]['element'].setGeometry(x,y,w,h)

    def resizeEvent(self, e):
        w = e.size().width()
        h = e.size().height()

        if w / h > self.aspect_ratio:  # too wide
            self.layout().setDirection(QBoxLayout.LeftToRight)
            widget_stretch = h * self.aspect_ratio
            outer_stretch = (w - widget_stretch) / 2
        else:                          # too tall
            self.layout().setDirection(QBoxLayout.TopToBottom)
            widget_stretch = w / self.aspect_ratio
            outer_stretch = (h - widget_stretch) / 2

        self.layout().setStretch(0, outer_stretch)
        self.layout().setStretch(1, widget_stretch)
        self.layout().setStretch(2, outer_stretch)

        self.__rearrage_board__(self.demo_area.size().width(), self.demo_area.size().height())