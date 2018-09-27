#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""urllib

"""

from urllib import request
from urllib import parse

url = 'http://www.iqianyue.com/mypost/'
post_data = parse.urlencode({
    'name': 'Neo',
    'pass': 'abc123'
}).encode('utf-8')

req = request.Request(url, post_data)
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36')

with open('urllib_post_result.html', 'wb') as f:
    f.write(request.urlopen(req).read())
