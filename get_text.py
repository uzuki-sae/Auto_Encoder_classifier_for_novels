from logging import getLogger, StreamHandler, DEBUG
logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False

import os
import time
import datetime
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import timedelta


def main():
    """
    メイン処理
    """
    # --------------------------------------
    # 作品ページのURLを指定（コメントアウト・コメントインで指定できるようにしています）
    t0=time.time()
    if not os.path.exists("corpus"):
        os.makedirs("corpus")

    with open("craw_list", "r") as n:
        ncode=n.read().splitlines()
    with open("log.txt", 'r') as log:
        x=log.read()
    ncode=ncode[int(x):]

    for i, nc in enumerate(ncode):
        url = 'https://ncode.syosetu.com/{}/'.format(nc.lower())
        stories = ""
        bs_obj = make_bs_obj(url)
        if bs_obj is None:
            continue
        else:
            pass
        time.sleep(0.3)
        url_list = ["https://ncode.syosetu.com" + a_bs_obj.find("a").attrs["href"] for a_bs_obj in bs_obj.findAll("dl", {"class": "novel_sublist2"})]
        date_list = bs_obj.findAll("dt",{"class":"long_update"})
        novel_title = bs_obj.find("p",{"class":"novel_title"}).get_text()
        for s in r'\/*?"<>:|':
            novel_title = novel_title.replace(s, '')

        # 各話の本文情報を取得
        for j in range(len(url_list)):
            url = url_list[j]
            bs_obj = make_bs_obj(url)
            if bs_obj is None:
                continue
            else:
                pass
            time.sleep(0.3)
            stories = stories + get_main_text(bs_obj)
        
        f = open('corpus/{}.txt'.format(nc), 'w')
        f.write(stories)
        f.close()
        logger.debug('{}.txt is writen.'.format(nc))
        t1=time.time()
        deltat=t1-t0
        timeleft=timedelta(seconds=deltat*(len(ncode)/(i+1)-1))
        logger.debug(f'duration:{timedelta(deltat)}, time left:{timeleft}')
        print("進捗:{}/{}, {}%".format(i, len(ncode), i*100//len(ncode)))
        with open("log.txt", 'w') as log:
            log.write(str(i+int(x)+1))



def make_bs_obj(url):
    """
    BeautifulSoupObjectを作成
    """
    try:
        html = urlopen(url)
    except Exception as e:
        print(e)
        return None
    logger.debug('access {} ...'.format(url))
    return BeautifulSoup(html,"html.parser")

def get_main_text(bs_obj):
    """
    各話のコンテンツをスクレイピング
    """
    text = ""
    text_htmls = bs_obj.findAll("div",{"id":"novel_honbun"})[0].findAll("p")

    for text_html in text_htmls:
        text = text + text_html.get_text() + "\n"

    return text




main()
