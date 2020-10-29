#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""requests库的基本用法

requests库的7个主要方法：
1、request() 构造一个HTTP请求，是支撑以下各方法的底层方法
2、head() 获取HTML网页头信息的方法，对应HTTP的HEAD
3、get() GET方式请求，对应HTTP的GET
4、post() POST方式请求，对应HTTP的POST
5、put() PUT方式请求，对应HTTP的PUT
6、patch() 局部修改请求，对应HTTP的PATCH
7、delete() 删除请求，对应HTTP的DELETE

get()方法：
requests.get(url, params=None, **kwargs)
- url: 请求页面的url地址
- params: url中的额外参数，字典或字节流格式，可选
- **kwargs: 12个控制访问的参数
构造一个向服务器请求资源的Request对象
返回一个包含服务器资源的Response对象

Response对象：
包含服务器返回的所有信息，也包含请求的Request信息

Response对象的属性：
1、status_code 请求的返回状态，200表示成功
2、encoding 从HTTP HEADER中推测的响应内容的编码方式
3、apparent_encoding 从内容中分析出的响应内容的编码方式（备选编码方式）
4、text 响应内容的字符串形式，即url对应的页面内容
5、content 响应内容的二进制形式
6、json
7、cookies

requests库的异常：
1、ConnectionError  网络连接异常，如DNS查询失败，拒绝连接等
2、HTTPError  HTTP错误异常
3、URLRequired  URL缺少异常
4、TooManyRedirects  超过最大重定向次数，产生重定向异常
5、ConnectTimeout 连接远程服务器超时异常
6、Timeout 请求URL超时异常
"""

import requests

# 爬取网页的通用代码框架
def getHTMLText(url):
    try:
        r = requests.get(url, timeout=100)
        r.raise_for_status()  # 如果状态不是200，抛出HTTPError异常
        r.encoding = r.apparent_encoding  # 设置编码
        return r.text
    except:
        return '产生异常'


if __name__ == '__main__':
    url = 'https://www.baidu.com/'
    print(getHTMLText(url))


