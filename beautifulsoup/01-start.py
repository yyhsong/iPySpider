#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""beautifulsoup库入门

基于Python的XML/HTML解析库
bs4将任何HTML输入都变成utf-8编码

两种初始化方法：
1、BeautifulSoup('<html>...</html>', 'html.parser')
2、BeautifulSoup(open('xxx.html'), 'html.parser')

支持的解析器：
1、html.parser
2、lxml
3、xml
4、html5lib

基本元素：
1、Tag
2、Name
3、Attributes
4、NavigableString
5、Comment

格式化输出方法：prettify()
- 为HTML文本及其内容增加 \n
- 可用于具体标签 <tag>.prettify()
"""

import requests
from bs4 import BeautifulSoup

url = 'http://python123.io/ws/demo.html'
headers= {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
}

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, 'html.parser')

# 任何存在于HTML语法中的标签都可以通过soup.tagName的形式访问获得
# 当存在多个相同名称的tag时，返回第一个
print('获取标签：', soup.title)
print('获取标签名称：', soup.title.name)

# 获取标签包含的字符串，NavigableString可以跨越多个层次
print('获取标签包含字符串：', soup.p.string)

print('获取标签属性：', soup.a.attrs)  # 返回字典类型
print('获取标签属性值：', soup.a.attrs['href'])

print('---------- 格式化输出网页内容 ----------')
print(soup.prettify())
