# -*- coding:utf-8 -*-
###################################################################
###   @FilePath: \Simple_Viewer\UI\Elements\GroupItem.py
###   @Author: Ziang Liu
###   @Date: 2021-01-29 15:42:07
###   @LastEditors: Ziang Liu
###   @LastEditTime: 2021-04-29 11:29:46
###   @Copyright (C) 2021 SJTU. All rights reserved.
###################################################################

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QLabel
from .Basic import Layout


class ImageWidget(QLabel):
    def __init__(self, image_path, parent=None):
        super(ImageWidget, self).__init__(parent)

        pixmap = QPixmap(image_path)

        self.aspect_ratio = pixmap.size().height() / pixmap.size().width()
        self.setPixmap(pixmap)
        self.setScaledContents(True)
    
    def resizeEvent(self, e):
        w = e.size().width()
        self.resize(w, self.aspect_ratio*w)

class GroupImage(QWidget):
    def __init__(self, parent=None, horizontal=False):
        super(GroupImage, self).__init__(parent)
        self.horizontal = horizontal

    def set_up(self, image_list):
        self.images = []
        for image in image_list:
            image_widget = ImageWidget(image)
            self.images.append(image_widget)
            
        layout = Layout(self.images, [], self.horizontal)
        self.setLayout(layout)



    

