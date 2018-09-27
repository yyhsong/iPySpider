#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""urllib

"""

from urllib import request

url = 'https://www.baidu.com/s?wd='
# 对中文进行编码
wd = request.quote('爬虫')
url += wd
req = request.Request(url)
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36')

with open('urllib_get_result.html', 'wb') as f:
    f.write(request.urlopen(req).read())
