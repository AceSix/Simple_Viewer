# -*- coding:utf-8 -*-
###################################################################
###   @FilePath: \PyQt5-FDD\config\styles.py
###   @Author: Ziang Liu
###   @Date: 2020-11-25 19:04:29
###   @LastEditors: Ziang Liu
###   @LastEditTime: 2021-04-02 14:48:06
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

panel_button_tone   =  button_tone.alter(font=16, border_radius='6px', border_width='1px', border_color=[100, 100, 100], border_style='outset')
panel_button_style  =  button_tone.alter(bgd_color=[50, 50, 162, 0.5]).style() + \
                       button_tone.head('QPushButton:hover').alter(bgd_color=[50, 80, 162]).style() + \
                       button_tone.head('QPushButton:pressed').alter(bgd_color=[100, 80, 162]).style() + \
                       button_tone.head('QPushButton:checked').alter(bgd_color=[120, 120, 162]).style()

report_button_tone  =  panel_button_tone.alter(padding='5 2 5 2px', font=15, color=white)
report_button_style =  report_button_tone.alter(bgd_color=[120, 150, 30]).style() + \
                       report_button_tone.head('QPushButton:hover').alter(bgd_color=[150, 180, 30]).style() + \
                       report_button_tone.head('QPushButton:checked').alter(bgd_color=[100, 80, 30]).style()

light_button_tone   =  button_tone.alter(font=18, border_radius='5px', border_width='1px', border_color=[100, 100, 100])
light_button_style  =  light_button_tone.alter(bgd_color=[50, 50, 162, 0.5]).style() + \
                       light_button_tone.head('QPushButton:hover').alter(bgd_color=[50, 80, 162]).style() + \
                       light_button_tone.head('QPushButton:pressed').alter(bgd_color=[100, 80, 162]).style() + \
                       light_button_tone.head('QPushButton:checked').alter(bgd_color=[120, 120, 162]).style()

login_connect_tone  =  button_tone.alter(font=32, padding='15 15 15 15px')
login_connect_style =  login_connect_tone.style() + \
                       login_connect_tone.head('QPushButton:hover').alter(bgd_color=dark_blue).style() + \
                       login_connect_tone.head('QPushButton:pressed').alter(bgd_color=mid_blue).style() + \
                       login_connect_tone.head('QPushButton:checked').alter(bgd_color=mid_blue).style()  

login_button_tone   =  button_tone.alter(font=32)
login_button_style  =  login_button_tone.style() + \
                       login_button_tone.head('QPushButton:hover').alter(bgd_color=dark_blue).style() + \
                       login_button_tone.head('QPushButton:pressed').alter(bgd_color=mid_blue).style() + \
                       login_button_tone.head('QPushButton:checked').alter(bgd_color=mid_blue).style() 

#################### complex or combined style #################### 
login_widget_tone   =  Style_Maker('', bgd_color=mid_blue+[0.5], font=32)      
login_style         =  text_tone.head('QLabel').style() + \
                       text_tone.head('QLineEdit').style() + \
                       text_tone.head('QComboBox').style() + \
                       text_tone.head('QLineEdit').style() + \
                       login_button_style

menu_style = '''background-color: qlineargradient(
                        x1:0, y1:0, x2:0, y2:0.5,
                        stop:0 rgb(30, 112, 202),
                        stop:1 rgb(20, 134, 202)
                    );
                QLabel { background-color : white; color:black;}
                QLabel:hover { background-color:rgb(77, 166, 222);}
                QMenu item { background-color : white; color:black;}
                QMenu item:hover { background-color:rgb(77, 166, 222);}
                '''
                
sidebar_style = ''' background-color: 
                    qlineargradient(
                        x1:0, y1:0, x2:0, y2:0.5,
                        stop:0 rgba(0, 0, 0, 200),
                        stop:1 rgba(0, 0, 0, 100)
                    );
                '''

calender_style = '''
                    QDateTimeEdit{
                        color:white;
                    }
                    QCalendarWidget QWidget 
                    { 
                        alternate-background-color: rgb(78, 78, 78); 
                    }
                    QCalendarWidget QMenu {
                        color: white;
                        font-size: '''+intstr(font_ratio*18)+'''px;
                        background-color: rgb(100, 100, 100);
                    }
                    QCalendarWidget QAbstractItemView:enabled{
                        font-size:'''+intstr(font_ratio*18)+'''px;
                        color: white;
                        background-color: rgb(55, 55, 55);
                        selection-background-color: rgb(64, 64, 64);
                        selection-color: rgb(0, 255, 0);
                    }
                '''