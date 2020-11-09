#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""案例：爬取中国大学排名

定向爬虫，不爬取网页内的链接扩展
0. 通过网站Robots协议，确认爬取可行性
1. 对目标网页结构进行分析
2. 确定程序结构
    - 获取HTML内容：requests
    - 提取信息：BeautifulSoup
    - 保存数据：保存数据到本地
3、通过主函数调用执行
"""

import requests
from bs4 import BeautifulSoup


# 获取网页内容
def getHTML(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
    }
    try:
        r = requests.get(url, headers=headers, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''


# 提取信息
def extractInfo(html, info):
    soup = BeautifulSoup(html, 'lxml')  # 使用lxml解析器
    rows = soup.select('.rk-table tbody tr')
    for row in rows:
        cells = row.find_all('td')
        item = (cells[0].text.strip(), cells[1].text.strip(), cells[4].text.strip())
        info.append(item)


# 保存数据
def saveData(info, limit):
    info = info[:limit]
    print(info)

    # 打印输出
    print('---------- 2020年中国大学排行 ----------')
    # 居中对齐，宽度为10，使用空格填充
    print('{0:^10}\t{1:{3}^10}\t{2:^10}'.format('排名', '学校名称', '总分', chr(12288)))
    for i in info:
        print('{0:^10}\t{1:{3}^10}\t{2:^10}'.format(i[0], i[1], i[2], chr(12288)))

    # 保存到本地txt文件
    txt = ''
    for item in info:
        txt += ','.join(item) + '\n'
    with open('university_ranking.txt', 'w', encoding='utf-8') as f:
        f.write(txt)


# 主函数
def main():
    url = 'https://www.shanghairanking.cn/rankings/bcur/2020'  # 目标URL
    html = getHTML(url)  # 获取HTML内容
    info = []  # 保存目标信息
    extractInfo(html, info)  # 提取目标信息
    saveData(info, 100)  # 保存前100条记录


# 调用执行
main()
