#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""IP查询"""

import requests

ip = '49.65.247.47'
url = 'https://m.ip138.com/iplookup.asp?ip=' + ip
headers= {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
}

try:
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:3000])
except:
    print('查询失败')