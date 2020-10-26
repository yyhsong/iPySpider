#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""requests模块基本用法"""

import requests
import re


# Get请求
def do_get_req():
    args = {
        'msg': 'Hello Get'
    }
    r = requests.get('http://httpbin.org/get', params=args)
    print('Status:', r.status_code)
    print('Text:', r.text)


# Post请求
def do_post_req():
    args = {
        'msg': 'Hello Post'
    }
    r = requests.post('http://httpbin.org/post', data=args)
    print('Status:', r.status_code)
    print('Json:', r.json())


# 添加头信息，抓取网页内容
def get_web_con():
    url = 'https://www.zhihu.com/explore'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
    }
    r = requests.get(url, headers=headers)
    pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
    questions = re.findall(pattern, r.text)
    for q in questions:
        print(q.strip())


# 抓取二进制内容
def get_binary_con():
    url = 'https://github.com/favicon.ico'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
    }
    r = requests.get(url, headers=headers)
    with open('favicon.ico', 'wb') as f:
        f.write(r.content)


# 测试
do_get_req()
