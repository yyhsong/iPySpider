#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""爬取京东手机类前10页商品图片

使用urllib库爬取数据
使用正则表达式进行信息抽取
"""

from urllib import request
from urllib import error
import re
import os


def do_spider(url, page):
    print('Page:', page)
    html_str = request.urlopen(url).read()
    html_str = str(html_str)
    wrapper_pattern = '<div id="plist".+? <div class="page clearfix">'
    wrapper_str = re.compile(wrapper_pattern).findall(html_str)
    wrapper_str = wrapper_str[0]
    pic_pattern = '<img width="220".+? *="//(.+?\.jpg)"'
    pic_list = re.compile(pic_pattern).findall(wrapper_str)

    x = 1
    for pic_url in pic_list:
        cur_dir = os.path.abspath('.')
        pic_path = 'pic' + os.path.sep + str(page) + '-' + str(x) + '.jpg'
        pic_name = os.path.join(cur_dir, pic_path)
        pic_url = 'http://' + pic_url
        try:
            request.urlretrieve(pic_url, filename=pic_name)
        except error.URLError as e:
            if hasattr(e, 'code'):
                print('Code:', e.code)
            if hasattr(e, 'reason'):
                print('Reason:', e.reason)
        x = x + 1


url = 'https://list.jd.com/list.html?cat=9987,653,655&page='
for i in range(1, 11):
    url = url + str(i)
    do_spider(url, i)
