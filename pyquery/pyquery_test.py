#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""pyquery库的基本用法

基于Python的XML/HTML解析库
使用jQuery风格的语法来遍历文档

三种初始化方法
1、传入字符串 PyQuery('<html>...</html>')
2、出入url参数 PyQuery(url='xxx', encoding='utf-8')
3、传入文件 PyQuery(filename='xxx.html')
"""

import requests
from pyquery import PyQuery as pq

url = 'https://blog.csdn.net/'
headers= {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
}

r = requests.get(url, headers=headers)
doc = pq(r.text)  # 把返回的字符串内容转换为HTML文档树
items = doc('#feedlist_id .list_con .title h2 a')  # 使用类似jQuery的选择器提取节点

print('---------- Blog List ----------')
for item in items:  # 遍历节点
    print(item.text.strip())  # 提取节点包含的文本
