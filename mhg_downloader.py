# -*- coding:utf-8 -*-
###################################################################
###   @FilePath: \Simple_Viewer\mhg_downloader.py
###   @Author: Ziang Liu
###   @Date: 2021-04-29 11:08:55
###   @LastEditors: Ziang Liu
###   @LastEditTime: 2021-04-29 13:30:42
###   @Copyright (C) 2021 SJTU. All rights reserved.
###################################################################

from bs4 import BeautifulSoup
import re
import requests
import mhgParser as ps
import os
import tqdm

baseURL = "https://www.mhgui.com"
imgURL = "https://i.hamreus.com"
headers = {
        "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:70.0) Gecko/20100101 Firefox/70.0"
    }


def download(comic_name, comic_id):
    req = requests.get(baseURL+f'/comic/{comic_id}', headers=headers)
    html = req.text
    table_bf = BeautifulSoup(html)
    chapters = table_bf.find(attrs={'class': 'chapter cf mt16'}).find_all('a')

    print(f"Totally {len(chapters)} chapters are found in {comic_name}.")

    for chapter in tqdm.tqdm(chapters):
        page_url = 'https://www.mhgui.com' + chapter.attrs['href']
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
download('is the order a rabbit', 11064)