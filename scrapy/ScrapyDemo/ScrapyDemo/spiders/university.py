#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""案例 - 爬取中国大学排名及简介

1. 初始爬取中国大学排名页面
2. 动态获取每个大学简介链接，生成新的爬取URL
3. 爬取大学简介页面，提取大学名称、网站及简介等信息
4. 把提取的信息封装成字典，传递给Item Pipelines
5. 在Pipelines类中处理爬取项，保存到本地文件
"""

import scrapy


class UniversitySpider(scrapy.Spider):
    name = 'university'
    # allowed_domains = ['shanghairanking.cn']

    # 爬取的初始URL
    start_urls = [
        'https://www.shanghairanking.cn/rankings/bcur/2020'
    ]

    def parse(self, resp):
        links = resp.xpath('//table[@class="rk-table"]/tbody/tr/td[2]/a/@href').extract()
        for link in links:
            try:
                # 动态生成新的爬取URL
                url = 'https://www.shanghairanking.cn' + link
                yield scrapy.Request(url, callback=self.parse_university)
            except:
                continue

    def parse_university(self, resp):
        # 定义传输给Item Pipelines的字典
        # info_dict = {}

        # 解析HTML
        u_name = resp.xpath('//div[@class="univ-name"]/text()').extract()[0].strip()
        u_enname = resp.xpath('//div[@class="univ-enName"]/text()').extract()[0].strip()
        u_website = resp.xpath('//div[@class="univ-website"]/a/@href').extract()[0].strip()
        try:
            u_intro = resp.xpath('//div[@class="univ-introduce"]/p[1]/text()').extract()[0].strip()
        except:
            u_intro = '无'

        info_dict = {
            'name': u_name,
            'enname': u_enname,
            'website': u_website,
            'introduce': u_intro
        }

        yield info_dict
