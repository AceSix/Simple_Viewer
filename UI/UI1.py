# -*- coding:utf-8 -*-
###################################################################
###   @FilePath: \Simple_Viewer\UI\UI1.py
###   @Author: Ziang Liu
###   @Date: 2020-11-25 19:04:29
###   @LastEditors: Ziang Liu
###   @LastEditTime: 2021-04-29 16:21:41
###   @Copyright (C) 2020 SJTU. All rights reserved.
###################################################################

import os
from PyQt5.QtWidgets import QComboBox, QFileDialog
from .UI_template import Template
from .Elements import Label, Button, Layout
from config.styles import leaf_button_style

class UI1(Template):
    def __init__(self, manager):
        super(UI1, self).__init__()
        self.manager = manager
    
    def __setup__(self):
        self.info = Label(self, 'Select The Comic Source', "page1_title", 
                                    '''QLabel{
                                        font: bold;
                                        color: black;
                                        font : 20px;
                                    }''')
        self.button1 = Button(None, 'select_source', style=leaf_button_style)
        self.button1.setMinimumHeight(30)
        self.button1.clicked.connect(self.openFile)

        self.combo = QComboBox()
        self.combo.setMinimumHeight(30)
        self.combo.addItems(['---'])

        self.button2 = Button(None, 'GO', style=leaf_button_style)
        self.button2.setMinimumHeight(30)
        self.button2.clicked.connect(self.__GO__)
        
        select_layout = Layout(
            ['space',
             Layout([self.info, self.button1, self.combo, self.button2], [], False),
             'space'], [1,1,1,1], True)
        layout = Layout(
            ['space', select_layout, 'space'],
            [1,1,1], False)
        self.setLayout(layout)

    def __GO__(self):
        path = self.combo.currentText()
        self.manager.content_page.load_comic(path)
        self.manager.interface.work_space.setCurrentIndex(1)

    def openFile(self):
        root = QFileDialog.getExistingDirectory(self,"????????????","./")
        
        try:
            comic_dirs = os.listdir(root)
            items = []
            for dir in comic_dirs:
                if os.path.isdir(os.path.join(root, dir)):
                    items.append(os.path.join(root, dir))
            self.combo.clear()
            self.combo.addItems(items)
        except:
            self.info.setText('place select a valid path')
            pass

        

        
