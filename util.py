# -*- coding:utf-8 -*-
###################################################################
###   @FilePath: \Comic_Reader\util.py
###   @Author: Ziang Liu
###   @Date: 2020-11-25 19:04:29
###   @LastEditors: Ziang Liu
###   @LastEditTime: 2021-04-25 20:41:29
###   @Copyright (C) 2020 SJTU. All rights reserved.
###################################################################

import base64
import os
import glob
from PyQt5.QtCore import QTimer, QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication
import time
import re

def load_images(path):
    images = glob.glob(os.path.join(path, '*.jpg'))
    images += glob.glob(os.path.join(path, '*.png'))
    try:
        images.sort(key=lambda x:int(re.findall(f"\d+", os.path.basename(x)+'chapter')[0]))
    except:
        images.sort()
    return images

def get_resolution():
    desktop = QApplication.desktop()
    screenRect = desktop.screenGeometry()
    height = screenRect.height()
    width = screenRect.width()
    return (width, height)

def group_stretch(layout, config):
    for id, length in enumerate(config):
        layout.setStretch(id, length)

def get_pic(pic_code, pic_name):
    image = open(pic_name, 'wb')
    image.write(base64.b64decode(pic_code))
    image.close()

class Data_Group(object):
    def __init__(self, group_num) -> None:
        super().__init__()
        self.series_group = []
        for i in range(group_num):
            self.series_group.append([])
        self.y_max, self.y_min = 0, 0
        self.max_len = 30
        self.n = group_num
        
    def group_append(self, group):
        if len(self.series_group[0]) > self.max_len:
            for i in range(self.n):
                self.series_group[i] = self.series_group[i][1:]
        for i,data in enumerate(group):
            self.series_group[i].append(data)

        self.y_max = max(self.y_max, max(group))
        self.y_min = min(self.y_min, min(group))

class Loop(QThread):
    update_info = pyqtSignal(str)
    def __init__(self, period):
        super().__init__()
        self.period = period

    def run(self):
        while True:
            time.sleep(self.period)
            self.update_info.emit('1')