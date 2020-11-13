#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""案例 - 爬取中国大学排名信息

1. 请求2020年中国大学排名页面
2. 解析返回的HTML
3. 提取大学排名、名称及详情介绍的URL
4. 把提取的信息保存到本地的文本文件
"""

import scrapy


class UniversityrankSpider(scrapy.Spider):
    # 爬虫名称
    name = 'universityrank'
    # allowed_domains = ['shanghairanking.cn']

    # 初始请求URLs
    start_urls = [
        'https://www.shanghairanking.cn/rankings/bcur/2020'
    ]

    # 处理请求响应，解析响应内容，发现新的URL爬取请求
    def parse(self, response):
        # 使用CSS选择器提取信息
        # 提取a的href属性值
        # links = response.css('.rk-table tbody a::attr(href)').extract()
        # doc_txt = ''
        # for link in links:
        #     doc_txt += link + '\n'

        # 使用XPath提取信息
        # 提取a包含的文本
        # links = response.xpath('//table[@class="rk-table"]/tbody/tr/td[2]/a/text()').extract()
        # doc_txt = ''
        # for link in links:
        #     doc_txt += link + '\n'

        # 提取嵌套的信息
        rows = response.xpath('//table[@class="rk-table"]/tbody/tr')
        doc_txt = ''
        for row in rows:
            u_rank = row.xpath('.//td[1]/text()').extract()[0].strip()
            u_name = row.xpath('.//td[2]/a/text()').extract()[0].strip()
            u_link = row.xpath('.//td[2]/a/@href').extract()[0].strip()
            doc_txt += u_rank + ' | ' + u_name + ' | ' + u_link + '\n'

        # 把提取信息保存到本地文件
        with open('files/university-rankings.txt', 'w', encoding='utf-8') as f:
            # f.write(response.body)
            f.write(doc_txt)
        self.log('Saved university-rankings.txt')
