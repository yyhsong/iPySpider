#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""案例 - 爬取中国大学简介

1. 动态初始化请求URLs
2. 请求中国大学介绍页面
3. 解析返回的HTML，提取大学名称、网站及简介等信息
4. 把提取的信息保存到本地的文本文件
"""

import scrapy
import os


class UniversityinfoSpider(scrapy.Spider):
    # 爬虫名称
    name = 'universityinfo'
    # allowed_domains = ['shanghairanking.cn']

    # 初始化请求URLs
    def start_requests(self):
        # start_urls = [
        #     'https://www.shanghairanking.cn/institution/tsinghua-university',
        #     'https://www.shanghairanking.cn/institution/peking-university',
        #     'https://www.shanghairanking.cn/institution/zhejiang-university'
        # ]
        # for url in start_urls:
        #     yield scrapy.Request(url=url, callback=self.parse)

        with open('files/university-rankings.txt', 'r', encoding='utf-8') as f:
            lines = f.read().splitlines()
            for line in lines:
                if line and line.split(' | ')[-1]:
                    url = 'https://www.shanghairanking.cn' + line.split(' | ')[-1]
                    yield scrapy.Request(url=url, callback=self.parse)


    # 处理请求响应，解析响应内容，发现新的URL爬取请求
    def parse(self, resp):
        # 解析HTML
        u_name = resp.xpath('//div[@class="univ-name"]/text()').extract()[0].strip()
        u_enname = resp.xpath('//div[@class="univ-enName"]/text()').extract()[0].strip()
        u_website = resp.xpath('//div[@class="univ-website"]/a/@href').extract()[0].strip()
        try:
            u_intro = resp.xpath('//div[@class="univ-introduce"]/p[1]/text()').extract()[0].strip()
        except:
            u_intro = '无'

        doc_txt = u_name + '\n' + u_enname + '\n' + u_website + '\n' + u_intro

        fname = resp.url.split('/')[-1] + '.txt'
        fpath = 'files' + os.path.sep + fname
        with open(fpath, 'w', encoding='utf-8') as f:
            # f.write(resp.body)
            f.write(doc_txt)

        self.log('Saved %s'.format(fname))
