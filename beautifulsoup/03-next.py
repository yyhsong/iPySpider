#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""beautifulsoup库的进阶使用

信息的标记
- 标记后的信息可形成信息组织结构，增加了信息维度
- 标记的结构与信息一样具有重要价值
- 标记后的信息可用于存储、通信或展示
- 标记后的信息更有利于程序理解和运用

信息标记的三种形式
- XML: eXtensible Markup Language
- JSON: JavaScript Object Notation
- YAML: YAML Ain't Markup Language
    - 无类型键值对
    - 缩进表示从属关系
    - 连接线 - 表示并列关系
    - 竖线 | 表示整块数据
    - 井号 # 表示注释

信息提取的一般方法
1. 完整解析信息的标记形式，再提取关键信息
    - 需要标记解析器
    - 优点：信息解析准确
    - 缺点：提取过程繁琐，速度慢
2. 无视标记形式，直接搜索关键信息
    - 需要文本查找函数
    - 优点：提取过程简洁，速度较快
    - 提取结果准确性与信息内容相关
3. 结合形式解析和搜索方法，提取关键信息
    - 需要标记解析器和文本查找函数

bs4的信息提取方法，格式：find_xxx()
- find_all(name, attrs, recursive, string, **kwargs)  # 返回列表，存储匹配的结果
    - name 对标签名称的检索字符串，可以用list同时查找多个
    - attrs 对标签属性的检索字符串，可标注属性检索，字典类型
    - recursive 是否对后代元素全部检索，默认True
    - string 文本检索字符串，通常配合正则使用
"""

import requests
from bs4 import BeautifulSoup
import re

url = 'https://blog.csdn.net/'
headers= {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
}

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, 'html.parser')

# items = soup.find_all('div', {'class':'title'})
# print('---------- Blog List ----------')
# for item in items:
#     print(item.a.text.strip(), ':', item.a.get('href'))  # 获取属性值

# 使用CSS选择器
links = soup.select('#feedlist_id .list_con .title h2 a')
print('\n---------- 博客列表 ----------')
for link in links:
    print(link.text.strip(), ':', link.get('href'))

print('\n---------- 包含Python的链接 ----------')
for link in soup.find_all('a', string=re.compile('Python')):
    print(link.text.strip())
