#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""urllib
使用代理
"""

from urllib import request


def do_proxy(proxy_addr, url):
    proxy = request.ProxyHandler({
        'http': proxy_addr
    })
    opener = request.build_opener(proxy, request.HTTPHandler)
    request.install_opener(opener)
    data = request.urlopen(url).read().decode('utf-8')
    return data


proxy_addr = '202.75.210.45:7777'
url = 'http://www.baidu.com/'
data = do_proxy(proxy_addr, url)
print(data)
