# -*- coding:utf-8 -*-
###################################################################
###   @FilePath: \FDD-Industrial\config\styles_old.py
###   @Author: Ziang Liu
###   @Date: 2020-11-25 19:04:29
###   @LastEditors: Ziang Liu
###   @LastEditTime: 2021-03-09 16:38:34
###   @Copyright (C) 2020 SJTU. All rights reserved.
###################################################################


font_ratio = 1.5
def intstr(val):
    return str(int(val))
main_style = '''background-color: rgb(77, 166, 222);
                color :rgb(0, 66, 144);
                '''

panel_title_style = '''
                    QLabel{ 
                        background-color:rgba(0,0,0,0);
                        color:white;
                        font:'''+intstr(font_ratio*20)+'''px;
                    }'''

title_style = '''
                QLabel{ 
                    background-color:rgba(0,0,0,0); 
                    font:bold '''+intstr(font_ratio*36)+'''px; 
                    color:white; 
                    text-align:center;
                }
            '''



bar_chart_style = 'font : '+intstr(font_ratio*8)+'px; color : rgba(30, 30, 80, 0);'
combine_chart_style = 'font : '+intstr(font_ratio*5)+'px; color : rgba(30, 30, 80, 0);'
pie_chart_style = 'font :bold '+intstr(font_ratio*8)+'px; color : rgba(30, 30, 80, 0);'


transparent_style = '''QLabel{ 
                    background-color:rgba(0,0,0,0);
                }
            '''

menu_style = '''background-color: 
                    qlineargradient(
                        x1:0, y1:0, x2:0, y2:0.5,
                        stop:0 rgb(30, 112, 202),
                        stop:1 rgb(20, 134, 202)
                    );
                QLabel { background-color : white; color:black;}
                QLabel:hover { background-color:rgb(77, 166, 222);}
                QMenu item { background-color : white; color:black;}
                QMenu item:hover { background-color:rgb(77, 166, 222);}
                '''
sidebar_style = ''' 
                    background-color: 
                    qlineargradient(
                        x1:0, y1:0, x2:0, y2:0.5,
                        stop:0 rgba(0, 0, 0, 200),
                        stop:1 rgba(0, 0, 0, 100)
                    );
                '''

digit_board_style =  ''' QLabel
                    {
                    text-align : center;
                    background-color : rgba(0,101,179,0.5);
                    color: rgb(0, 66, 144);
                    font : bold '''+intstr(font_ratio*16)+'''px;
                    border-width: 1px;
                    border-radius: 10px;
                    border-style: inset;
                    border-color: rgba(0,101,179,0.8);
                    }'''

digit_label_style = ''' QLabel
                    {
                    text-align : center;
                    background-color : rgba(0,0,0,0);
                    color: rgb(255, 255, 255);
                    font : bold '''+intstr(font_ratio*16)+'''px;
                    }'''

panel_style =  '''  border-width: 1px;
                    border-style: solid;
                    border-color: rgb(100, 100, 100);
                    '''

sub_panel_style =  ''' 
                        border-width: 2px;
                        border-style: solid;
                        border-color: rgb(0, 66, 144);
                    '''

leaf_button_style =  ''' QPushButton
                    {
                    text-align : center;
                    background-color : rgba(0, 101, 179, 0.5);
                    font: bold '''+intstr(font_ratio*21)+'''px;
                    border-width: 3px;
                    border-radius: 10px;
                    border-style: solid;
                    border-color: rgb(0, 66, 144);
                    padding: 5 5 5 5px;
                    }
                    QPushButton:hover
                    {
                    background-color : rgb(0, 101, 179);
                    }
                    QPushButton:pressed
                    {
                    background-color : rgb(77, 166, 222);
                    }
                    QPushButton:checked
                    {
                    background-color : rgb(77, 166, 222);
                    }
                '''

panel_button_style =  ''' QPushButton
                    {
                    text-align : center;
                    background-color : rgba(50, 50, 162, 0.5);
                    color: white;
                    font : bold '''+intstr(font_ratio*16)+'''px;
                    border-style: outset;
                    border-radius: 6px;
                    border-width: 1px;
                    border-color: rgb(100, 100, 100);
                    
                    }
                    QPushButton:hover
                    {
                    background-color : rgb(50, 80, 162);
                    }
                    QPushButton:pressed
                    {
                    background-color : rgb(100, 80, 162);
                    }
                    QPushButton:checked
                    {
                    background-color : rgb(120, 120, 162);
                    }
                '''

indicator_info_style = '''QLabel{background-color : rgba(0, 0, 0, 0);
                                                       color : rgb(255, 255, 255);
                                                       font : '''+ intstr(font_ratio*23) + '''px;
                                                       border-style : none;}'''

error_info_style = '''QLabel{background-color : rgba(0, 0, 0, 0);
                                                       color : rgb(255, 255, 255);
                                                       font : '''+ intstr(font_ratio*15) + '''px;
                                                       border-style : none;}'''
                                                       
state_info_style = "color:white; font:26px; border-style: inset; border-width: 1px;"
error_header_style = "color:white; font:26px; "

report_button_style =  ''' QPushButton
                    {
                    background-color : rgb(120, 150, 30);
                    color: white;
                    font : bold '''+intstr(font_ratio*15)+'''px;
                    border-style: outset;
                    border-radius: 6px;
                    border-width: 1px;
                    border-color: rgb(100, 100, 100);
                    padding: 5 2 5 2px;
                    }
                    QPushButton:hover
                    {
                    background-color : rgb(150, 180, 30);
                    }
                    QPushButton:pressed
                    {
                    background-color : rgb(100, 80, 30);
                    }
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

light_button_style =  ''' QPushButton
                    {
                    text-align : center;
                    background-color : rgba(50, 50, 162, 0.5);
                    color: white;
                    font : bold '''+intstr(font_ratio*18)+'''px;
                    border-style: outset;
                    border-width: 1px;
                    border-radius: 5px;
                    border-color: rgb(100, 100, 100);
                    }
                    QPushButton:hover
                    {
                    background-color : rgb(50, 80, 162);
                    }
                    QPushButton:pressed
                    {
                    background-color : rgb(100, 80, 162);
                    }
                    QPushButton:checked
                    {
                    background-color : rgb(120, 120, 162);
                    }
                '''

choosebar_style = ''' QLabel
                    {
                    text-align : center;
                    background-color : rgb(20, 90, 162);
                    border-style: outset;
                    font : bold '''+intstr(font_ratio*14)+'''px;
                    }
                '''
login_title_style = '''
                QLabel{ 
                    background-color:rgba(0,0,0,0); 
                    font:bold '''+intstr(font_ratio*60)+'''px; 
                    color:rgb(255,255,255); 
                    text-align:center;
                }
            '''
login_style = '''QLabel
                {
                font : bold '''+intstr(font_ratio*32)+'''px;
                color : rgb(255,255,255);
                background-color: rgba(0,0,0,0);
                }
                QLineEdit
                {
                font : bold '''+intstr(font_ratio*32)+'''px;
                background-color: rgba(0,101,179,0.5);
                }
                QComboBox
                {
                background-color: rgba(0,101,179,0.5);
                font : bold '''+intstr(font_ratio*32)+'''px;
                }
                QPushButton
                    {
                    text-align : center;
                    background-color : rgba(0, 101, 179, 0.5);
                    font: bold '''+intstr(font_ratio*32)+'''px;
                    border-width: 3px;
                    border-radius: 10px;
                    border-style: solid;
                    border-color: rgb(0, 66, 144);
                    padding: 5 5 5 5px;
                    }
                    QPushButton:hover
                    {
                    background-color : rgb(0, 101, 179);
                    }
                    QPushButton:pressed
                    {
                    background-color : rgb(77, 166, 222);
                    }
                    QPushButton:checked
                    {
                    background-color : rgb(77, 166, 222);
                    }'''
login_connect_style =  ''' QPushButton
                    {
                    text-align : center;
                    background-color : rgba(0, 101, 179, 0.5);
                    font: bold '''+intstr(font_ratio*32)+'''px;
                    border-width: 3px;
                    border-radius: 10px;
                    border-style: solid;
                    border-color: rgb(0, 66, 144);
                    padding: 15 15 15 15px;
                    }
                    QPushButton:hover
                    {
                    background-color : rgb(0, 101, 179);
                    }
                    QPushButton:pressed
                    {
                    background-color : rgb(77, 166, 222);
                    }
                    QPushButton:checked
                    {
                    background-color : rgb(77, 166, 222);
                    }
                '''
                
text_style = '''QLabel
                {
                text-align : center;
                font : '''+intstr(font_ratio*30)+'''px;
                }'''

info_style = '''QLabel
                {
                font : '''+intstr(font_ratio*18)+'''px;
                color : white;
                background-color: rgba(0,0,0,0);
                }'''
