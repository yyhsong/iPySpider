#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""BeautifulSoup解析库的基本用法"""

from urllib import request
from bs4 import BeautifulSoup

url = 'http://quotes.money.163.com/f10/gszl_600398.html#01f01'
req = request.Request(url)
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36')

with request.urlopen(req) as f:
    html = f.read()
    soup = BeautifulSoup(html, 'lxml')
    for td_label in soup.select('.col_l_01 .table_bg001 .td_label'):
        td_txt = td_label.find_next(name='td').string.strip()
        print(td_label.string.strip(), ':', td_txt)
