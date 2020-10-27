#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""分析Robots协议

Robots协议也称为爬虫协议、机器人协议，全称网络爬虫排除标准（Robots Exclusion Protocol），
用来告诉搜索引擎和爬虫哪些页面可以爬取，哪些不可以爬取。
Robots协议通常是一个名为robots.txt的文本文件，放在网站的根目录下。
"""

from urllib import robotparser

# 获取robots.txt文件
rp = robotparser.RobotFileParser('https://www.csdn.net/robots.txt')

# 读取robots.txt内容并分析
rp.read()

# 判断爬虫是否可以爬取某些目录或页面
# 第一个参数为爬虫名称，第二个参数为要爬取的Url
print(rp.can_fetch('*', 'https://www.csdn.net/nav/newarticles'))
print(rp.can_fetch('*', 'http://www.csdn.net/tag/cms'))


"""CSDN网站Robots协议内容

User-agent: *
Disallow: /scripts
Disallow: /public
Disallow: /css/
Disallow: /images/
Disallow: /content/
Disallow: /ui/
Disallow: /js/
Disallow: /scripts/
Disallow: /article_preview.html*
Disallow: /tag/
Disallow: /*?*
Disallow: /link/

Sitemap: http://www.csdn.net/article/sitemap.txt
"""
