#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""requests库入门

HTTP：Hypertext Transfer Protocol  超文本传输协议
基于"请求/响应"模式的、无状态的应用层协议
采用URL作为定位网络资源的标识，其基本格式如下：
http://host[:port][path]
- host: 主机域名或IP地址
- port: 端口号，缺省为80
- path: 请求资源的路径
URL是通过HTTP协议存取资源的Internet路径，一个URL对应一个数据资源

HTTP协议对资源的操作：
- HEAD 请求获取URL位置资源的响应消息报告，即获取该资源的头部信息
- GET  请求获取URL位置的资源
- POST 请求向URL位置的资源后附加新的数据
- PUT  请求向URL位置存储一个资源，覆盖该处原来的资源
- PATCH  请求局部更新URL位置的资源，即改变该处资源的部分内容
- DELETE 请求删除URL位置存储的资源

requests库的7个主要方法：
1、request() 构造一个HTTP请求，是支撑以下各方法的底层方法
2、head() 获取HTML网页头信息的方法，对应HTTP的HEAD
3、get() GET方式请求，对应HTTP的GET
4、post() POST方式请求，对应HTTP的POST
5、put() PUT方式请求，对应HTTP的PUT
6、patch() 局部修改请求，对应HTTP的PATCH
7、delete() 删除请求，对应HTTP的DELETE
构造一个向服务器请求资源的Request对象
返回一个包含服务器资源的Response对象

Response对象的属性和方法：
1、url 请求的URL地址
2、status_code 请求的返回状态，200表示成功
3、encoding 从HTTP HEADER中推测的响应内容的编码方式
4、apparent_encoding 从内容中分析出的响应内容的编码方式（备选编码方式）
5、headers 响应的头信息
6、text 响应内容的字符串形式，即url对应的页面内容
7、content 响应内容的二进制形式
8、json() 响应内容的json格式
9、cookies
包含服务器返回的所有信息，也包含请求的Request信息

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
        r = requests.get(url, timeout=10)
        r.raise_for_status()  # 如果状态不是200，抛出HTTPError异常
        r.encoding = r.apparent_encoding  # 设置编码
        return r.text
    except:
        return '产生异常'


if __name__ == '__main__':
    url = 'https://www.baidu.com/'
    print(getHTMLText(url))
