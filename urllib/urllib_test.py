#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""urllib
urllib库提供的功能就是利用程序去执行各种HTTP请求
通过标识User-Agent等手段来伪装成浏览器请求
可以执行GET POST请求，POST请求可传递数据，或使用代理

urllib.request.urlopen(url, data, timeout, ...)
返回一个file对象：
status: 请求状态码，同getcode()
reason: 请求状态描述
getheaders(): 头信息
read(): 读取内容
readlines(): 按行读取内容
readline(): 读取一行内容
"""

from urllib import request
import time

url = 'https://blog.csdn.net'
req = request.Request(url)
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36')
for i in range(100):
    with request.urlopen(req, timeout=100) as f:
        print('-------------- Request --------------')
        print('Status:', f.status)
        print('Reason:', f.reason)
        for k, v in f.getheaders():
            print('%s: %s' % (k, v))
        # print('Data:', f.read().decode('utf-8'))
    time.sleep(65)
