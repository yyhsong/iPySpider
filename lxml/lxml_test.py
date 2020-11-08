#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""lxml库的基本用法

lxml is the most feature-rich and easy-to-use library for processing XML and HTML in the Python language.
支持XPath(XML Path Language) 和 XSLT(Extensible Stylesheet Language Transformation)语法
实现了ElementTree API

Element和ElementTree
XML文档是树形结构，lxml库使用Element和ElementTree分别代表节点和树

XPath
在XML文档中查找/提取信息的语言
使用路径表达式在XML文档中进行导航
包含一个标准函数库，有超过100个内建的函数
是XSLT标准中的主要元素
XQuery和XPointer均构建在XPath表达式之上

XPath有7种类型的节点：
1、文档（根）节点
2、元素
3、属性
4、文本
5、命名空间
6、处理指令
7、注释

XPath使用路径表达式选取文档中的节点或节点集，节点是沿着路径(path)或者步(step)来选取的
常用的路径表达式：
1、nodename 选取此节点的所有子节点
2、/ 从根节点选取
3、// 从匹配选择的当前节点选取文档中的节点，而不考虑它们的位置
4、. 选取当前节点
5、.. 选取当前节点的父节点
6、@ 选取属性
7、| 选取若干路径
"""

import requests
from lxml import etree

url = 'https://blog.csdn.net/'
headers= {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
}

r = requests.get(url, headers=headers)
html = etree.HTML(r.text)  # 把请求返回内容转换为ElementTree
items = html.xpath('//li[@data-type="blog"]/div[@class="list_con"]/div[@class="title"]/h2/a')  # 使用路径表达式提取节点

print('---------- Blog List ----------')
for item in items:  # 遍历节点
    print(item.text.strip())  # 提取节点包含的文本
