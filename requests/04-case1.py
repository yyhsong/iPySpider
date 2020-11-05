#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""爬取网络图片"""

import requests
import os

url = 'https://cdn.pixabay.com/photo/2016/03/26/13/09/notebook-1280538_960_720.jpg'
root = './pics/'
path = root + url.split('/')[-1]
headers= {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
}

try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url, headers=headers)
        with open(path, 'wb') as f:
            f.write(r.content)
            print('文件已保存')
    else:
        print('文件已存在')
except:
    print('爬取失败')