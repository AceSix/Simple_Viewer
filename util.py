# -*- coding:utf-8 -*-
###################################################################
###   @FilePath: \Simple_Viewer\util.py
###   @Author: Ziang Liu
###   @Date: 2020-11-25 19:04:29
###   @LastEditors: Ziang Liu
###   @LastEditTime: 2021-04-29 11:30:22
###   @Copyright (C) 2020 SJTU. All rights reserved.
###################################################################

import os
import glob

def load_images(path):
    images = glob.glob(os.path.join(path, '*.jpg'))
    images += glob.glob(os.path.join(path, '*.png'))
    images.sort()
    return images

def group_stretch(layout, config):
    for id, length in enumerate(config):
        layout.setStretch(id, length)

