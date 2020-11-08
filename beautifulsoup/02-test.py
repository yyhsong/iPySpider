#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""beautifulsoup库的基本用法

标签树的遍历方法：
1、下行遍历
2、上行遍历
3、平行遍历

下行遍历
- contents 子节点列表
- children 子节点迭代类型，用于循环遍历子节点
- descendants 所有后代节点的迭代类型

上行遍历
- parent 父节点
- parents 先辈节点的迭代类型，用于循环遍历先辈节点

平行遍历
- next_sibling 下一个平行（兄弟）节点
- previous_sibling 上一个平行节点
- next_siblings 迭代类型，后续所有平行节点
- previous_sibling 迭代类型，前面所有平行节点
"""

import requests
from bs4 import BeautifulSoup as bs

url = 'http://python123.io/ws/demo.html'
headers= {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
}

r = requests.get(url, headers=headers)
soup = bs(r.text, 'html.parser')

print('---------- 下行遍历 ----------')

print(type(soup.body.contents))  # 返回list对象
print(type(soup.body.children))  # 返回list_iterator对象
print(type(soup.body.descendants))  # 返回generator对象

print('Contents[1]：', soup.body.contents[1])
for child in soup.body.children:
    print('子节点：', child)
for child in soup.body.descendants:
    print('后代节点：', child)

print('---------- 上行遍历 ----------')

print(type(soup.a.parent))  # 返回element对象
print(type(soup.a.parents))  # 返回generator对象

print('父节点：', soup.a.parent)
for parent in soup.a.parents:  # 遍历所有先辈节点，包括了soup本身
    if parent is None:
        print(parent)
    else:
        print('先辈节点：', parent.name)

print('---------- 平行遍历 ----------')

print(type(soup.a.next_sibling))  # 返回element
print(type(soup.a.previous_sibling))  # 返回element
print(type(soup.a.next_siblings))  # 返回generator
print(type(soup.a.previous_siblings))  # 返回generator

for sibling in soup.a.next_siblings:
    print('后续平行节点：', sibling)
