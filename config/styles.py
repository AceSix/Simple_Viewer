# -*- coding:utf-8 -*-
###################################################################
###   @FilePath: \Simple_Viewer\config\styles.py
###   @Author: Ziang Liu
###   @Date: 2020-11-25 19:04:29
###   @LastEditors: Ziang Liu
###   @LastEditTime: 2021-04-29 13:28:04
###   @Copyright (C) 2020 SJTU. All rights reserved.
###################################################################
from .style_maker import Style_Maker
def intstr(val):
    return str(int(val))

light_blue = [77, 166, 222]
mid_blue = [0,101,179]
dark_blue = [0, 66, 144]
empty_color = [0,0,0,0]
white = [255,255,255]
black = [0,0,0]
gray = [240,240,240]

####################### detailed styles ######################
base_tone        = Style_Maker('', bgd_color=white, color=dark_blue)
text_tone        = Style_Maker('', bgd_color=empty_color, color=black, border_style='none')
button_tone      = Style_Maker('QPushButton', text_align='center', bgd_color=gray+[0.5],
                                font=12, border_width='1px', border_radius='6px',
                                border_style='outset', border_color=black, padding='5 5 5 5px')

######################## detailed styles ########################
main_style = base_tone.style()

############################ texts ##############################
info_style          =  text_tone.head('QLabel').alter(font=18).style()

############################ buttons ############################
leaf_button_style   =  button_tone.style() + \
                       button_tone.head('QPushButton:hover').alter(bgd_color=[230, 230, 230]).style() + \
                       button_tone.head('QPushButton:pressed').alter(bgd_color=[0, 0, 0]).style()
