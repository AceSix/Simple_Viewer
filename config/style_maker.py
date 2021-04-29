# -*- coding:utf-8 -*-
###################################################################
###   @FilePath: \Simple_Viewer\config\style_maker.py
###   @Author: Ziang Liu
###   @Date: 2021-03-09 14:05:34
###   @LastEditors: Ziang Liu
###   @LastEditTime: 2021-04-29 11:20:18
###   Copyright (C) 2021 SJTU. All rights reserved.
###################################################################

font_ratio = 1.5

abbreviation = {
    'bgd_color':'background-color',
}
specials = ['text_style']
def translate(key):
    if key in abbreviation.keys():
        return abbreviation[key]
    else:
        return key.replace("_","-")
        
class Style_Maker(object):
    def __init__(self, header, **kwargs):
        self.parameters = kwargs
        self.header = header

    def head(self, header):
        new_maker = Style_Maker(self.header, **self.parameters)
        new_maker.header = header
        return new_maker

    def alter(self, **kwargs):
        new_maker = Style_Maker(self.header, **self.parameters)
        for key in kwargs.keys():
            new_maker.parameters[key] = kwargs[key]
        return new_maker

    def style(self):
        stylesheet = ''
        for key in self.parameters.keys():
            if key in specials:
                continue

            value = self.parameters[key]
            
            if 'color' in key:
                r,g,b,a = (self.parameters[key]+[1])[:4]
                value = f"rgba({r},{g},{b},{a})"
            if 'font' in key:
                value = f' {int(value*font_ratio)}px'
                if 'text_style' in self.parameters.keys():
                    value = self.parameters['text_style']+value
            stylesheet += f"{translate(key)}:{value};"
        if len(self.header)>1:
            return self.header+'{'+stylesheet+'}'
        else:
            return stylesheet

    
