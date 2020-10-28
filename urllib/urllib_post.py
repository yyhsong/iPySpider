#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""POST请求

使用urllib发送POST方式的请求
把请求返回的内容写入本地文件
POST请求的主要区别在于可以发送数据
"""

from urllib import request, parse

# 爬取的目标网址
url = 'https://www.iqianyue.com/mypost/'

# 对POST传递的数据进行编码
# Params output from urlencode is encoded to bytes before it is sent to urlopen as data
# 转换后的格式：b'name=Neo&pass=abc123'
post_data = parse.urlencode({
    'name': 'Neo',
    'pass': 'abc123'
}).encode('utf-8')

# 打印输出
# with request.urlopen(url, post_data) as f:
#     print(f.read().decode('utf-8'))

# 设置请求信息，包括请求发送的数据和头信息
req = request.Request(url, post_data)
req.add_header('User-Agent',
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36')

# 把请求返回的数据写入本地文件
with open('urllib_post_result.txt', 'wb') as f:
    f.write(request.urlopen(req).read())
    print('----- 写入结束 -----')
