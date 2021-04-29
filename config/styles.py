# -*- coding:utf-8 -*-
###################################################################
###   @FilePath: \Simple_Viewer\config\styles.py
###   @Author: Ziang Liu
###   @Date: 2020-11-25 19:04:29
###   @LastEditors: Ziang Liu
###   @LastEditTime: 2021-04-29 11:19:36
###   @Copyright (C) 2020 SJTU. All rights reserved.
###################################################################
from .style_maker import Style_Maker, font_ratio
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
chart_text_tone  = Style_Maker('', color=[30, 30, 80, 0])
digit_tone       = Style_Maker('QLabel', text_align='center', font=16, text_style='bold')
frame_tone       = Style_Maker('',border_style='solid')
button_tone      = Style_Maker('QPushButton', text_align='center', bgd_color=gray+[0.5],
                                font=12, border_width='1px', border_radius='6px',
                                border_style='outset', border_color=black, padding='5 5 5 5px')

######################## detailed styles ########################
main_style = base_tone.style()

title_style         =  text_tone.head('QLabel').alter(font=10).style()
panel_title_style   =  text_tone.head('QLabel').alter(font= 20).style()
login_title_style   =  text_tone.head('QLabel').alter(font=60).style()

######################### chart texts ###########################
bar_chart_style     =  chart_text_tone.alter(font=8).style()
combine_chart_style =  chart_text_tone.alter(font=5).style()
pie_chart_style     =  chart_text_tone.alter(font=8, text_style='bold').style()

############################ texts ##############################
info_style          =  text_tone.head('QLabel').alter(font=18).style()
indicator_style     =  text_tone.head('QLabel').alter(font=23).style()
error_info_style    =  text_tone.head('QLabel').alter(font=15).style()
state_info_style    =  text_tone.alter(font=26, border_style='inset', border_width='1px').style()
error_header_style  =  text_tone.alter(font=26).style()

######################### label&widget ##########################
transparent_style   =  text_tone.style()
panel_style         =  frame_tone.alter(border_width='1px', border_color=[100, 100, 100]).style()
sub_panel_style     =  frame_tone.alter(border_width='2px', border_color=dark_blue).style()
digit_board_style   =  digit_tone.alter(bgd_color=mid_blue+[0.5], border_width='1px', border_radius='10px', 
                                        border_style='inset', border_color=mid_blue+[0.8], 
                                        color=dark_blue).style()
digit_label_style   =  digit_tone.alter(bgd_color=empty_color, color=white).style()
choosebar_style     =  digit_tone.head('QLabel').alter(bgd_color=[20, 90, 162], font=14, 
                                                  border_style='outset').style()

############################ buttons ############################
leaf_button_style   =  button_tone.style() + \
                       button_tone.head('QPushButton:hover').alter(bgd_color=[230, 230, 230]).style() + \
                       button_tone.head('QPushButton:pressed').alter(bgd_color=[0, 0, 0]).style()
