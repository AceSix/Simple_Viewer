# -*- coding:utf-8 -*-
###################################################################
###   @FilePath: \Comic_Reader\UI\Elements\GroupItem.py
###   @Author: Ziang Liu
###   @Date: 2021-01-29 15:42:07
###   @LastEditors: Ziang Liu
###   @LastEditTime: 2021-04-02 22:51:35
###   @Copyright (C) 2021 SJTU. All rights reserved.
###################################################################


from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from .Basic import Layout


class ImageWidget(QWidget):
    def __init__(self, image_path, parent=None):
        super(ImageWidget, self).__init__(parent)

        # self.setStyleSheet('QWidget { background-color:blue; border-style:outset; border-color:black; border-width:5px;}')
        # self.setStyleSheet('QLabel { background-image:url('+image_path+')}')
        pixmap = QPixmap(image_path)
        # self.resize(pixmap.size().width(), pixmap.size().height() )
        self.img_h = pixmap.size().height()
        self.img_w = pixmap.size().width()
        self.aspect_ratio = self.img_h / self.img_w

        self.demo_area = QLabel()
        self.demo_area.setScaledContents(True)
        self.demo_area.setPixmap(pixmap)
        self.demo_area.setScaledContents(True)
        self.demo_area.setMinimumSize(1, 1)

        
        # self.setLayout(QBoxLayout(QBoxLayout.LeftToRight, self))
        # self.layout().addItem(QSpacerItem(0, 0))
        # self.layout().addWidget(self.demo_area)
        # self.layout().addItem(QSpacerItem(0, 0))
        # self.layout().setContentsMargins(0, 0, 0, 0)

        self.setLayout(Layout([self.demo_area], [], True))

    def resizeEvent(self, e):
        w = e.size().width()
        h = e.size().height()
        self.resize(w, int(w*self.aspect_ratio))

class GroupImage(QWidget):
    def __init__(self, parent=None, horizontal=False):
        super(GroupImage, self).__init__(parent)
        self.horizontal = horizontal
        layout = QVBoxLayout(self)
        
        self.setStyleSheet('QWidget { background-color:white;}')

    def set_up(self, image_list):
        tmp = QWidget()
        tmp.setLayout(self.layout())
        del tmp
        
        self.images = []
        image_ratios = []
        for image in image_list:
            image_widget = ImageWidget(image)
            image_ratio = image_widget.img_h/ image_widget.img_w
            image_ratios.append(image_ratio)
            self.images.append(image_widget)

        layout = Layout(self.images, [ratio*10 for ratio in image_ratios], self.horizontal)
        layout.setSpacing(0)
        self.setLayout(layout)

        self.total_ratio = sum(image_ratios)

    # def resizeEvent(self, e):
    #     w = e.size().width()
    #     h = e.size().height()
    #     self.resize(w, int(w*self.total_ratio))

    

