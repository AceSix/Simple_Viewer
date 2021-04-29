# -*- coding:utf-8 -*-
###################################################################
###   @FilePath: \Comic_Reader\Framework\Manager.py
###   @Author: Ziang Liu
###   @Date: 2021-04-02 16:50:36
###   @LastEditors: Ziang Liu
###   @LastEditTime: 2021-04-02 16:50:52
###   @Copyright (C) 2021 SJTU. All rights reserved.
###################################################################
# -*- coding:utf-8 -*-
###################################################################
###   @FilePath: \PyQt5-FDD\Framework\Manager.py
###   @Author: Ziang Liu
###   @Date: 2020-11-25 19:04:29
###   @LastEditors: Ziang Liu
###   @LastEditTime: 2021-04-02 16:25:20
###   @Copyright (C) 2020 SJTU. All rights reserved.
###################################################################

import sys 	
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QStatusBar, QDateEdit, QDateTimeEdit
from PyQt5.QtCore import pyqtSignal
from config.styles import leaf_button_style
from .BaseUI import BaseUI

class PageManager(QMainWindow):
    def __init__(self, debug, **kwargs):
        super(PageManager, self).__init__()
        self.pages = {}
        self.relations = {}

        self.kwargs = kwargs
        self.debug = debug

    def initialize(self, menu, content):
        self.menu_page = menu
        self.content_page = content

        self.interface = BaseUI()
        self.interface.setup_UI(self)
        self.interface.stack([self.menu_page, self.content_page])
        
