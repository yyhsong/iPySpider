#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""爬取猫眼电影Top100的名称、时间、评分、图片等信息

使用requests库爬取数据
使用正则表达式进行信息抽取
"""

import requests
from requests.exceptions import RequestException
import re
import time
import json


# 爬取网页
def crawl_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
    }
    try:
        resp = requests.get(url, headers=headers)
        if resp.status_code == 200:
            return resp.text
        return None
    except RequestException:
        return None


# 抽取数据
def extract_info(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                         + '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'score': item[5] + item[6]
        }


# 保存数据
def save_data(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


# 执行爬虫
def do_spider(offset=0):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = crawl_html(url)
    for item in extract_info(html):
        print(item)
        save_data(item)


if __name__ == '__main__':
    for i in range(10):
        do_spider(offset=i*10)
        time.sleep(5)
