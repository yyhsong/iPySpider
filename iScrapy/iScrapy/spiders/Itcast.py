# -*- coding: utf-8 -*-
import scrapy
from iScrapy.items import ItcastItem


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = (
        'http://www.itcast.cn/channel/teacher.shtml',
    )

    # 重写start_requests()方法，动态改变起始URL
    # def start_requests(self):
    #     for url in self.start_urls:
    #         for i in range(1, 3):
    #             url += '&page=' + str(i)
    #             yield self.make_requests_from_url(url)

    def parse(self, response):
        items = []
        for each in response.xpath("//div[@class='li_txt']"):
            item = ItcastItem()
            name = each.xpath('h3/text()').extract()
            title = each.xpath('h4/text()').extract()
            info = each.xpath('p/text()').extract()

            item['name'] = name[0].strip()
            item['title'] = title[0].strip()
            item['info'] = info[0].strip()
            items.append(item)
        return items
