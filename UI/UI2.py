# -*- coding:utf-8 -*-
###################################################################
###   @FilePath: \Simple_Viewer\UI\UI2.py
###   @Author: Ziang Liu
###   @Date: 2020-11-26 19:25:34
###   @LastEditors: Ziang Liu
###   @LastEditTime: 2021-04-29 11:27:29
###   @Copyright (C) 2020 SJTU. All rights reserved.
###################################################################

import os
import glob
from PyQt5.QtWidgets import QScrollArea, QComboBox
from PyQt5.QtCore import Qt
from .UI_template import Template
from .Elements import Button, GroupImage, Layout
from config.styles import leaf_button_style
from util import load_images

    
class VerticalScrollArea(QScrollArea):
    def __init__(self):
        super(VerticalScrollArea, self).__init__()
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.horizontalScrollBar().setEnabled(False)
        self.setWidgetResizable(True)
        
    def resizeEvent(self, e):
        new_w = e.size().width()
        w,h = self.widget().size().width(), self.widget().size().height()
        self.widget().resize(new_w, new_w/w*h)

class UI2(Template):
    def __init__(self):
        super(UI2, self).__init__()
    
    def __setup__(self):
        self.chapter_selector = QComboBox()
        
        self.Pic_region = GroupImage()
        scroll1 = VerticalScrollArea()
        scroll1.setWidget(self.Pic_region)

        next_chapter = Button(None, 'next', style=leaf_button_style)
        next_chapter.clicked.connect(self.__next_chapter__)
        previous_chapter = Button(None, 'previous', style=leaf_button_style)
        previous_chapter.clicked.connect(self.__previous_chapter__)
        control_region = Layout([
            'space', next_chapter, self.chapter_selector, previous_chapter, 'space'
        ], [2,1,2,1,2], True)

        layout = Layout([
            control_region, scroll1
        ], [1,20], False)
        self.setLayout(layout)

    def __next_chapter__(self):
        chapter_id = self.chapter_selector.currentIndex()
        if chapter_id+1<len(self.chapters):
            self.chapter_selector.setCurrentIndex(chapter_id+1)
            images = load_images(self.chapters[chapter_id+1])
            self.Pic_region.set_up(images)

    def __previous_chapter__(self):
        chapter_id = self.chapter_selector.currentIndex()
        if chapter_id-1>-1:
            self.chapter_selector.setCurrentIndex(chapter_id-1)
            images = load_images(self.chapters[chapter_id+1])
            self.Pic_region.set_up(images)
    
    def load_comic(self, path):
        self.chapters = list(filter(os.path.isdir, glob.glob(os.path.join(path,'*'))))
        self.chapters.sort()

        self.chapter_selector.addItems(self.chapters)
        images = load_images(self.chapters[0])
        self.Pic_region.set_up(images)

    
        
