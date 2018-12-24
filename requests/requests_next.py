#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""requests进阶使用"""

import requests


# 文件上传
def do_file_upload():
    url = 'http://httpbin.org/post'
    args = {
        'msg': 'Upload File'
    }
    files = {
        'file': open('favicon.ico', 'rb')
    }
    r = requests.post(url, data=args, files=files)
    print('Status:', r.status_code)
    print('Text:', r.text)


# 获取响应Cookie
def get_resp_cookies():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
    }
    r = requests.get('https://www.baidu.com', headers=headers)
    for k, v in r.cookies.items():
        print(k, '=', v)


# 请求头中添加Cookie信息，模拟登录状态
def do_cookie_req():
    url = 'https://www.zhihu.com/'
    headers = {
        'Host': 'www.zhihu.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
        'Cookie': '_zap=1f9fbef3-f85f-489b-83f0-5a5b079f1f9a; _xsrf=d1686643-159d-43ee-981a-4e8a750240b5; d_c0="AJAjfe30sw6PTnykmdlvmYAHJW4hWwiwvjU=|1545374861"; capsion_ticket="2|1:0|10:1545374994|14:capsion_ticket|44:YmUxMDUyZDI3ZjQyNGRmNmJhODYxYzU0NTFiOWYzYWE=|505a22cf6ad9a7ac3aec734f1ee0b21b3eef2997d593017718936bb85feff8c3"; z_c0="2|1:0|10:1545374996|4:z_c0|92:Mi4xTU5aSkFBQUFBQUFBa0NOOTdmU3pEaVlBQUFCZ0FsVk5GTnNKWFFCVlpTbDgyRVVzQklNa0twRXFkUWx4WFNJWjJR|6cdcec424e7ff1cf1feaba936391ba78ac0dd67e6daa276a4661db9772a3d96c"; tst=r; q_c1=5bd035f8a6bd48c1914c927a601741c2|1545374999000|1545374999000; tgw_l7_route=23ddf1acd85bb5988efef95d7382daa0'
    }
    r = requests.get(url, headers=headers)
    # 返回的是登录后得到的内容
    print(r.text)


# 使用Session来维持会话状态
def do_session_req():
    url = 'http://httpbin.org/cookies/set/msg/helloworld'
    s = requests.Session()
    s.get(url)
    r = s.get('http://httpbin.org/cookies')
    print(r.text)


# SSL验证, 忽略证书验证及警告
def do_ssl_req():
    url = 'https://www.12306.cn'
    requests.packages.urllib3.disable_warnings()
    r = requests.get(url, verify=False)
    print(r.status_code)


# 测试
do_ssl_req()
