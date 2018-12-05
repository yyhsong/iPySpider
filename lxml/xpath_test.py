#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib import request
from lxml import etree

url = 'http://www.cninfo.com.cn/information/brief/shmb600398.html'
req = request.Request(url)
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36')

with request.urlopen(url) as f:
    html = etree.HTML(f.read())
    res = html.xpath('//td[@class="zx_data2"]')
    for r in res:
        print(r.text.strip())
