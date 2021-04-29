# -*- coding:utf-8 -*-
###################################################################
###   @FilePath: \Simple_Viewer\UI\UI2.py
###   @Author: Ziang Liu
###   @Date: 2020-11-26 19:25:34
###   @LastEditors: Ziang Liu
###   @LastEditTime: 2021-04-03 17:42:54
###   @Copyright (C) 2020 SJTU. All rights reserved.
###################################################################

import os
import re
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
        super(VerticalScrollArea, self).resizeEvent(e)
        new_w = e.size().width()
        self.widget().setMinimumHeight(new_w*self.widget().total_ratio)
        
class UI2(Template):
    def __init__(self):
        super(UI2, self).__init__()
    
    def __setup__(self):
        self.chapter_selector = QComboBox()
        self.chapter_selector.currentIndexChanged.connect(self.__specific_chapter__)
        
        self.Pic_region = GroupImage()
        # self.Pic_region.setBackgroundRole(QtGui.QPalette.Base)
        self.scrollarea = VerticalScrollArea()
        self.scrollarea.setWidget(self.Pic_region)
        # scroll1.setBackgroundRole(QtGui.QPalette.Dark)

        next_chapter = Button(None, 'next', style=leaf_button_style)
        next_chapter.clicked.connect(self.__next_chapter__)
        previous_chapter = Button(None, 'previous', style=leaf_button_style)
        previous_chapter.clicked.connect(self.__previous_chapter__)
        control_region = Layout([
            'space', previous_chapter, self.chapter_selector, next_chapter, 'space'
        ], [1,1,3,1,1], True)

        layout = Layout([
            control_region, self.scrollarea
        ], [1,20], False)
        self.setLayout(layout)

    def __next_chapter__(self):
        chapter_id = self.chapter_selector.currentIndex()
        if chapter_id+1<len(self.chapters):
            self.chapter_selector.setCurrentIndex(chapter_id+1)
            images = load_images(self.chapter_dirs[chapter_id+1])
            self.Pic_region.set_up(images)

            new_w = self.Pic_region.size().width()
            self.Pic_region.setMinimumHeight(new_w*self.Pic_region.total_ratio)
        self.scrollarea.verticalScrollBar().setValue(0)

    def __previous_chapter__(self):
        chapter_id = self.chapter_selector.currentIndex()
        if chapter_id-1>-1:
            self.chapter_selector.setCurrentIndex(chapter_id-1)
            images = load_images(self.chapter_dirs[chapter_id-1])
            self.Pic_region.set_up(images)

            new_w = self.Pic_region.size().width()
            self.Pic_region.setMinimumHeight(new_w*self.Pic_region.total_ratio)
        self.scrollarea.verticalScrollBar().setValue(0)

    def __specific_chapter__(self, new_id):
        images = load_images(self.chapter_dirs[new_id])
        self.Pic_region.set_up(images)

        new_w = self.Pic_region.size().width()
        self.Pic_region.setMinimumHeight(new_w*self.Pic_region.total_ratio)
        self.scrollarea.verticalScrollBar().setValue(0)

    def load_comic(self, path):
        list_dirs = glob.glob(os.path.join(path,'*'))
        self.chapter_dirs = list(filter(os.path.isdir, list_dirs))
        try:
            self.chapter_dirs.sort(key=lambda x:int(re.findall(f"\d+", os.path.basename(x)+'chapter')[0]))
        except:
            self.chapter_dirs.sort()

        # print(list(map(lambda x:re.findall(f"\d+", os.path.basename(x))[0], self.chapter_dirs)))
        self.chapters = [os.path.basename(d) for d in self.chapter_dirs]

        self.chapter_selector.addItems(self.chapters)
        images = load_images(self.chapter_dirs[0])
        self.Pic_region.set_up(images)

    
        
