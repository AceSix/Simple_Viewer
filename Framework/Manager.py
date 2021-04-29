# -*- coding:utf-8 -*-
###################################################################
###   @FilePath: \Simple_Viewer\Framework\Manager.py
###   @Author: Ziang Liu
###   @Date: 2021-04-02 16:50:36
###   @LastEditors: Ziang Liu
###   @LastEditTime: 2021-04-29 13:30:08
###   @Copyright (C) 2021 SJTU. All rights reserved.
###################################################################

from PyQt5.QtWidgets import QMainWindow
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
        

