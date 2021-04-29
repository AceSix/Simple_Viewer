# -*- coding:utf-8 -*-
###################################################################
###   @FilePath: \Simple_Viewer\UI\Elements\Senior.py
###   @Author: Ziang Liu
###   @Date: 2021-03-07 12:31:19
###   @LastEditors: Ziang Liu
###   @LastEditTime: 2021-03-07 19:30:10
###   Copyright (C) 2021 SJTU. All rights reserved.
###################################################################

from PyQt5 import QtWidgets, Qt
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QGridLayout, QDateTimeEdit, QProgressBar
from PyQt5.QtCore import QDate, QTime, QBasicTimer, pyqtSignal

class ColorButton(QPushButton):
    def __init__(self, init_color):
        super().__init__()
        self.cd = Qt.QColorDialog(init_color,self)
        self.color = init_color
        self.clicked.connect(self.update_color)

        self.convert(init_color)

    def update_color(self):
        def update_color_(color):
            self.color = color
            self.convert(color)

        self.cd.colorSelected.connect(update_color_)
        self.cd.show()

    def paintEvent(self, event):
        super().paintEvent(event)
        r = min(self.size().width(), self.size().height())
        self.resize(r,r)

    def convert(self, color):
        r,g,b = color.red(), color.green(), color.blue()
        self.setStyleSheet("QPushButton{background-color: rgb"+f"({r}, {g}, {b})"+";}")

class DateTimeEditDemo(QWidget):
    def __init__(self):
        super(DateTimeEditDemo, self).__init__()
        self.initUI()

    def initUI(self):
        #设置窗口的标题与初始大小
        self.setWindowTitle('QDateTimeEdit例子')
        self.resize(300, 90)
    
        formLayout = QGridLayout()
    
        dateEdit = QDateTimeEdit(QDate.currentDate(), self)
        timeEdit = QDateTimeEdit(QTime.currentTime(), self)
    
        dateEdit.setDisplayFormat("yyyy.MM.dd")
        timeEdit.setDisplayFormat("HH:mm:ss")
    
        dateEdit.setReadOnly(True)
        timeEdit.setReadOnly(True)
    
        dataLabel = QLabel('日期', self)
        dataLabel.setBuddy(dateEdit)
        timeLabel = QLabel('时间', self)
        timeLabel.setBuddy(timeEdit)
    
        formLayout.addWidget(dataLabel,0,0)
        formLayout.addWidget(dateEdit,0,1)
        formLayout.addWidget(timeLabel,1,0)
        formLayout.addWidget(timeEdit,1,1)
    
        self.setLayout(formLayout)

class ProgressBar(QWidget):
    update_ = pyqtSignal(str)
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.pbar = QProgressBar(self)
        self.pbar.setStyleSheet(''' QProgressBar{ 
                                        font:bold 32px;
                                        text-align:center;
                                        border-style: solid;
                                        border-width: 5px;
                                        border-color: rgb(0, 91, 169);
                                    } 
                                    QProgressBar::chunk{
                                        background-color:rgb(77,186,242);
                                    }''')
        self.timer = QBasicTimer()

    def start(self):
        self.timer.start(200, self)
        self.step = 0

    def timerEvent(self, e):
        if self.step >= 100:
            self.timer.stop()
            self.update_.emit('final')
            return
        self.step = self.step+1
        self.pbar.setValue(self.step)

