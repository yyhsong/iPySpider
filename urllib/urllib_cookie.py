#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""urllib
使用Cookie
"""

from urllib import request
from urllib import parse
from http import cookiejar

url = 'http://www.abc.com/login'
post_data = parse.urlencode({
    'username': 'admin',
    'pwt': 'abc123'
}).encode('utf-8')

req = request.Request(url, post_data)
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36')

cjar = cookiejar.CookieJar()
opener = request.build_opener(request.HTTPCookieProcessor(cjar))
request.install_opener(opener)

with open('urllib_cookie.html', 'wb') as f:
    f.write(opener.open(req).read())
