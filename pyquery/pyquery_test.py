#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""PyQuery的基本使用"""

from pyquery import PyQuery as pq

target_url = 'http://quotes.money.163.com/f10/zycwzb_600398,season.html'
doc = pq(url=target_url)

# 获取列数
target_table = doc('#scrollTable .col_r .table_bg001')
col_ths = target_table.children('tr:first-child th')
col_num = len(col_ths) + 1

# 按列抓取数据
res_data = []
for i in range(1, col_num):
    col_key = col_ths.filter(':nth-child(' + str(i) + ')').text()
    cols = target_table.children('tr td:nth-child(' + str(i) + ')').items()
    col_data = []
    for col in cols:
        col_data.append(col.text())
    res_data.append({
        col_key: col_data
    })

# 测试
for r in res_data:
    print(r)
