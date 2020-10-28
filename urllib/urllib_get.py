#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""GET请求

使用urllib发送GET方式的请求
把请求返回的内容写入本地文件
"""

from urllib import request

# 爬取的目标网址
url = 'https://www.baidu.com/s?wd='

# 设置请求头信息，标识User-Agent
wd = request.quote('爬虫')  # 对中文进行编码
url += wd
req = request.Request(url)
req.add_header('User-Agent',
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36')

# 把爬取内容写入本地文本文件
with open('urllib_get_result.txt', 'wb') as f:
    f.write(request.urlopen(req).read())
    print('----- 写入结束 -----')
