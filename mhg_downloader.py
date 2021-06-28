# -*- coding:utf-8 -*-
###################################################################
###   @FilePath: \Simple_Viewer\mhg_downloader.py
###   @Author: Ziang Liu
###   @Date: 2021-04-29 11:08:55
###   @LastEditors: Ziang Liu
###   @LastEditTime: 2021-05-12 17:06:16
###   @Copyright (C) 2021 SJTU. All rights reserved.
###################################################################

from bs4 import BeautifulSoup
import re
import requests
import mhgParser as ps
import os
import tqdm

baseURL = "https://www.mhgui.com"
# baseURL = "https://www.manhuagui.com"
imgURL = "https://i.hamreus.com"
headers = {
        "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:70.0) Gecko/20100101 Firefox/70.0"
    }

addition_text = '''
<div class="chapter-list cf mt10" id="chapter-list-1"><ul style="display:block"><li><a href="/comic/1147/423408.html" title="第64卷" class="status0" target="_blank"><span>第64卷<i>187p</i></span></a></li><li><a href="/comic/1147/414370.html" title="第63卷" class="status0" target="_blank"><span>第63卷<i>187p</i></span></a></li><li><a href="/comic/1147/363178.html" title="第62卷" class="status0" target="_blank"><span>第62卷<i>180p</i></span></a></li><li><a href="/comic/1147/157958.html" title="第61卷" class="status0" target="_blank"><span>第61卷<i>196p</i></span></a></li><li><a href="/comic/1147/157957.html" title="第60卷" class="status0" target="_blank"><span>第60卷<i>182p</i></span></a></li><li><a href="/comic/1147/157956.html" title="第59卷" class="status0" target="_blank"><span>第59卷<i>184p</i></span></a></li><li><a href="/comic/1147/157955.html" title="第58卷" class="status0" target="_blank"><span>第58卷<i>182p</i></span></a></li><li><a href="/comic/1147/148748.html" title="第57卷" class="status0" target="_blank"><span>第57卷<i>194p</i></span></a></li><li><a href="/comic/1147/148747.html" title="第56卷" class="status0" target="_blank"><span>第56卷<i>217p</i></span></a></li><li><a href="/comic/1147/143659.html" title="第55卷" class="status0" target="_blank"><span>第55卷<i>207p</i></span></a></li><li><a href="/comic/1147/141033.html" title="第54卷" class="status0" target="_blank"><span>第54卷<i>209p</i></span></a></li><li><a href="/comic/1147/140347.html" title="第53卷" class="status0" target="_blank"><span>第53卷<i>200p</i></span></a></li><li><a href="/comic/1147/149749.html" title="第52卷" class="status0" target="_blank"><span>第52卷<i>202p</i></span></a></li><li><a href="/comic/1147/149642.html" title="第51卷" class="status0" target="_blank"><span>第51卷<i>197p</i></span></a></li><li><a href="/comic/1147/148749.html" title="第50卷" class="status0" target="_blank"><span>第50卷<i>196p</i></span></a></li><li><a href="/comic/1147/141587.html" title="第49卷" class="status0" target="_blank"><span>第49卷<i>195p</i></span></a></li><li><a href="/comic/1147/141586.html" title="第48卷" class="status0" target="_blank"><span>第48卷<i>197p</i></span></a></li><li><a href="/comic/1147/141585.html" title="第47卷" class="status0" target="_blank"><span>第47卷<i>187p</i></span></a></li><li><a href="/comic/1147/72852.html" title="第46卷" class="status0" target="_blank"><span>第46卷<i>198p</i></span></a></li><li><a href="/comic/1147/10544.html" title="第45卷" class="status0" target="_blank"><span>第45卷<i>190p</i></span></a></li><li><a href="/comic/1147/10541.html" title="第44卷" class="status0" target="_blank"><span>第44卷<i>187p</i></span></a></li><li><a href="/comic/1147/10540.html" title="第43卷" class="status0" target="_blank"><span>第43卷<i>181p</i></span></a></li><li><a href="/comic/1147/10539.html" title="第42卷" class="status0" target="_blank"><span>第42卷<i>187p</i></span></a></li><li><a href="/comic/1147/10538.html" title="第41卷" class="status0" target="_blank"><span>第41卷<i>183p</i></span></a></li><li><a href="/comic/1147/10537.html" title="第40卷" class="status0" target="_blank"><span>第40卷<i>191p</i></span></a></li><li><a href="/comic/1147/10536.html" title="第39卷" class="status0" target="_blank"><span>第39卷<i>184p</i></span></a></li><li><a href="/comic/1147/10535.html" title="第38卷" class="status0" target="_blank"><span>第38卷<i>193p</i></span></a></li><li><a href="/comic/1147/10534.html" title="第37卷" class="status0" target="_blank"><span>第37卷<i>187p</i></span></a></li><li><a href="/comic/1147/10533.html" title="第36卷" class="status0" target="_blank"><span>第36卷<i>191p</i></span></a></li><li><a href="/comic/1147/10532.html" title="第35卷" class="status0" target="_blank"><span>第35卷<i>191p</i></span></a></li><li><a href="/comic/1147/10531.html" title="第34卷" class="status0" target="_blank"><span>第34卷<i>193p</i></span></a></li><li><a href="/comic/1147/10530.html" title="第33卷" class="status0" target="_blank"><span>第33卷<i>193p</i></span></a></li><li><a href="/comic/1147/10529.html" title="第32卷" class="status0" target="_blank"><span>第32卷<i>193p</i></span></a></li><li><a href="/comic/1147/10528.html" title="第31卷" class="status0" target="_blank"><span>第31卷<i>201p</i></span></a></li><li><a href="/comic/1147/10527.html" title="第30卷" class="status0" target="_blank"><span>第30卷<i>209p</i></span></a></li><li><a href="/comic/1147/10526.html" title="第29卷" class="status0" target="_blank"><span>第29卷<i>209p</i></span></a></li><li><a href="/comic/1147/10525.html" title="第28卷" class="status0" target="_blank"><span>第28卷<i>193p</i></span></a></li><li><a href="/comic/1147/10524.html" title="第27卷" class="status0" target="_blank"><span>第27卷<i>193p</i></span></a></li><li><a href="/comic/1147/10523.html" title="第26卷" class="status0" target="_blank"><span>第26卷<i>193p</i></span></a></li><li><a href="/comic/1147/10522.html" title="第25卷" class="status0" target="_blank"><span>第25卷<i>193p</i></span></a></li><li><a href="/comic/1147/10521.html" title="第24卷" class="status0" target="_blank"><span>第24卷<i>201p</i></span></a></li><li><a href="/comic/1147/10520.html" title="第23卷" class="status0" target="_blank"><span>第23卷<i>193p</i></span></a></li><li><a href="/comic/1147/10519.html" title="第22卷" class="status0" target="_blank"><span>第22卷<i>193p</i></span></a></li><li><a href="/comic/1147/10518.html" title="第21卷" class="status0" target="_blank"><span>第21卷<i>201p</i></span></a></li><li><a href="/comic/1147/10517.html" title="第20卷" class="status0" target="_blank"><span>第20卷<i>191p</i></span></a></li><li><a href="/comic/1147/10516.html" title="第19卷" class="status0" target="_blank"><span>第19卷<i>192p</i></span></a></li><li><a href="/comic/1147/10515.html" title="第18卷" class="status0" target="_blank"><span>第18卷<i>193p</i></span></a></li><li><a href="/comic/1147/10514.html" title="第17卷" class="status0" target="_blank"><span>第17卷<i>200p</i></span></a></li><li><a href="/comic/1147/10513.html" title="第16卷" class="status0" target="_blank"><span>第16卷<i>209p</i></span></a></li><li><a href="/comic/1147/10512.html" title="第15卷" class="status0" target="_blank"><span>第15卷<i>201p</i></span></a></li><li><a href="/comic/1147/10511.html" title="第14卷" class="status0" target="_blank"><span>第14卷<i>201p</i></span></a></li><li><a href="/comic/1147/10510.html" title="第13卷" class="status0" target="_blank"><span>第13卷<i>195p</i></span></a></li><li><a href="/comic/1147/10509.html" title="第12卷" class="status0" target="_blank"><span>第12卷<i>192p</i></span></a></li><li><a href="/comic/1147/10508.html" title="第11卷" class="status0" target="_blank"><span>第11卷<i>193p</i></span></a></li><li><a href="/comic/1147/10507.html" title="第10卷" class="status0" target="_blank"><span>第10卷<i>191p</i></span></a></li><li><a href="/comic/1147/10506.html" title="第09卷" class="status0" target="_blank"><span>第09卷<i>200p</i></span></a></li><li><a href="/comic/1147/10505.html" title="第08卷" class="status0" target="_blank"><span>第08卷<i>209p</i></span></a></li><li><a href="/comic/1147/10504.html" title="第07卷" class="status0" target="_blank"><span>第07卷<i>201p</i></span></a></li><li><a href="/comic/1147/10503.html" title="第06卷" class="status0" target="_blank"><span>第06卷<i>209p</i></span></a></li><li><a href="/comic/1147/10502.html" title="第05卷" class="status0" target="_blank"><span>第05卷<i>201p</i></span></a></li><li><a href="/comic/1147/10501.html" title="第04卷" class="status0" target="_blank"><span>第04卷<i>207p</i></span></a></li><li><a href="/comic/1147/10500.html" title="第03卷" class="status0" target="_blank"><span>第03卷<i>209p</i></span></a></li><li><a href="/comic/1147/10499.html" title="第02卷" class="status0" target="_blank"><span>第02卷<i>201p</i></span></a></li><li><a href="/comic/1147/10498.html" title="第01卷" class="status0" target="_blank"><span>第01卷<i>193p</i></span></a></li></ul></div>
'''

def download(comic_name, comic_id, headers):
    req = requests.get(baseURL+f'/comic/{comic_id}', headers=headers)
    html = req.text
    # table_bf = BeautifulSoup(html)
    # chapters = table_bf.find(attrs={'class': 'chapter cf mt16'}).find_all('a')

    table_bf = BeautifulSoup(addition_text)
    chapters = table_bf.find_all('a')

    print(f"Totally {len(chapters)} chapters are found in {comic_name}.")

    for chapter in tqdm.tqdm(chapters[47:]):
        page_url = baseURL + chapter.attrs['href']
        chapter_name = chapter.text
        if chapter_name[0]!='第':
            chapter_name = '第'+chapter_name
            
        core_info = ps.getCoreInfo(page_url)
        refURL = baseURL+"/comic/"+str(core_info['bid'])+"/"+str(core_info['cid'])+".html"
        headers = {
            "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:70.0) Gecko/20100101 Firefox/70.0",
            "Referer": refURL
        }
        
        chapter_dir = os.path.join(f'./{comic_name}', chapter_name)
        os.makedirs(chapter_dir, exist_ok=True)
        for img_url in core_info['files']:
            mangaurl = imgURL+core_info['path']+re.match(r".*?\.[a-z]*", img_url).group(0)
            img_name = os.path.basename(mangaurl)
            getFile = requests.get(mangaurl, headers=headers).content
            with open(os.path.join(chapter_dir, img_name),"wb") as f:
                f.write(getFile)
    print('download complete')


### may require VPN
download('fire', 1147, headers)
# download('zombie2', 36649, headers)