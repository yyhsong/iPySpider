#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""requests库的基本使用

request()方法：
requests.request(method, url, **kwargs)
- method 请求方式，如GET、POST等
- url 请求地址
- **kwargs 访问控制参数，共13个
request()方法是其他几种请求方法调用的底层方法

requests.get(url, params=None, **kwargs)  # **kwargs 12个
requests.post(url, data=None, json=None, **kwargs)  # **kwargs 11个
把各自常用的控制参数进行了显示定义

**kwargs 控制访问参数，均为可选项
1、params 字典或字节序列，作为参数增加到url中
2、data 字典、字节序列或文件对象，作为请求传递的内容
3、json json格式的数据，作为请求传递的内容
4、files 字典类型，传输文件
5、headers 字典，HTTP定制头信息
6、cookies 字典或CookieJar，请求中的cookie
7、auth 元组，支持HTTP认证功能
8、proxies 字典类型，设置访问代理服务器，可以增加登录认证
9、timeout 设置超时时间，以秒为单位
10、allow_redirects 重定向开关，默认为True
11、stream 获取内容立即下载开关，默认为True
12、verify 认证SSL证书开关，默认为True
13、cert 本地SSL证书路径
"""

import requests


# get()方法
# params 字典或字节序列，作为参数增加到url中
r = requests.get('https://www.baidu.com/s?', params={"wd":"python", "lang":"中文"})
print(r.url)

# head()方法，获取头信息
r = requests.head('https://www.baidu.com')
print(r.headers)

# post()方法
# data传递一个字典，编码为form
r = requests.post('http://httpbin.org/post', data={'id':1, 'name':'Neo'})
print(r.text)
# data传递一个字符串，编码为data
r = requests.post('http://httpbin.org/post', data='Hello World')
print(r.text)
# json传递一个字典，编码为json
r = requests.post('http://httpbin.org/post', json={'id':1, 'name':'Neo'})
print(r.text)

# files传递文件
# fs = {'file1': open('01-start.py', 'rb')}
# r = requests.post('http://httpbin.org/post', files=fs)
# print(r.text)

# 使用代理
# pxs = {
#     'http': 'http://user:pass@10.10.10.1:8080',
#     'https': 'https://10.10.10.2:8080'
# }
# r = requests.request('GET', 'http://www.abc.com', proxies=pxs)
