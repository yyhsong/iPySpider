#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""requests库的进阶使用"""


import requests


# GET请求
def do_get_req():
    args = {
        'msg': 'Hello GET'
    }
    r = requests.get('http://httpbin.org/get', params=args)
    print('---------- GET ----------')
    print('URL:', r.url)
    print('Status:', r.status_code)
    print('Text:', r.text)


# POST请求
def do_post_req():
    args = {
        'msg': 'Hello POST'
    }
    r = requests.post('http://httpbin.org/post', data=args)
    print('---------- POST ----------')
    print('URL:', r.url)
    print('Status:', r.status_code)
    print('Json:', r.json())


# 抓取二进制内容
def get_binary_con():
    url = 'https://github.com/favicon.ico'
    headers= {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
    }
    r = requests.get(url, headers=headers)
    with open('github_favicon.ico', 'wb') as f:
        f.write(r.content)


# 文件上传
def do_upload_file():
    url = 'http://httpbin.org/post'
    args = {
        'msg': 'Upload File'
    }
    files = {
        'file1': open('github_favicon.ico', 'rb')
    }
    r = requests.post(url, data=args, files=files)
    print('---------- Upload File ----------')
    print('Status:', r.status_code)
    print('Text:', r.text)


# 获取响应的Cookie
def get_resp_cookies():
    url = 'https://blog.csdn.net/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
    }
    r = requests.get(url, headers=headers)
    print('---------- Cookies ----------')
    for k, v in r.cookies.items():
        print(k, ':', v)


# 在请求头中添加Cookie信息，模拟登录状态
def do_cookie_req():
    url = 'https://blog.csdn.net/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
        # Cookie内容可以通过浏览器的开发者工具获取，此处为模拟
        'Cookie': 'uuid_tt_dd=10_30272075740-1604370181089-475133; dc_session_id=10_1604370181089.649993; TY_SESSION_ID=2fef6998-493f-450e-9c71-52418c1a2b88; c_first_ref=default; c_first_page=https%3A//blog.csdn.net/abc404/; c_segment=13; dc_sid=b686b90ec4745f280d0de728886e87b5; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1604364929; Hm_ct_6bcd52f51e9b3dce32bec4a3997715ac=6525*1*10_30272075740-1604370181089-475133!5744*1*abc; announcement=%257B%2522isLogin%2522%253Afalse%252C%2522announcementUrl%2522%253A%2522https%253A%252F%252Fedu.csdn.net%252FhuiyiCourse%252Fdetail%252F1461%253Futm_source%253Deduxy_gonggao_xtk%2522%252C%2522announcementCount%2522%253A0%252C%2522announcementExpire%2522%253A3600000%257D; firstDie=1; SESSION=98fc8fc8-0894-4b0f-b678-5eb85fc733d7; UN=abc; p_uid=U010000; log_Id_click=5; c_ref=https%3A//huangsong.blog.csdn.net/; UserName=abc404; UserInfo=81b54af1970a4c3f8563a74acf445a45; UserToken=81b54af1970a4c3f8563a74acf445a45; UserNick=%E8%88%AC%E8%8B%A5Abc; AU=A8B; BT=1604372260782; c_page_id=default; dc_tos=qj79kr; log_Id_pv=10; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1604372286; Hm_up_6bcd52f51e9b3dce32bec4a3997715ac=%7B%22islogin%22%3A%7B%22value%22%3A%221%22%2C%22scope%22%3A1%7D%2C%22isonline%22%3A%7B%22value%22%3A%221%22%2C%22scope%22%3A1%7D%2C%22isvip%22%3A%7B%22value%22%3A%220%22%2C%22scope%22%3A1%7D%2C%22uid_%22%3A%7B%22value%22%3A%22abc%22%2C%22scope%22%3A1%7D%7D; log_Id_view=9'
    }
    r = requests.get(url, headers=headers)
    print('---------- 返回登录后得到的网页内容 ----------')
    print(r.text)


# 使用Session来维持会话状态
def do_session_req():
    url = 'http://httpbin.org/cookies/set/msg/HelloSession'
    s = requests.Session()
    s.get(url)
    r = s.get('http://httpbin.org/cookies')
    print('---------- 设置的Cookie信息 ----------')
    print(r.text)


# SSL验证，忽略证书验证和警告
def do_ssl_req():
    url = 'https://www.12306.cn'
    requests.packages.urllib3.disable_warnings()
    r = requests.get(url, verify=False)
    print('---------- Status ----------')
    print(r.status_code)


if __name__ == '__main__':
    do_get_req()
