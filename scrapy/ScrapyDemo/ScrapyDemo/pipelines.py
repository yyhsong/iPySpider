# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ScrapydemoPipeline(object):
    def process_item(self, item, spider):
        return item


class UniversityPipeline(object):
    # 爬虫启动时执行的方法
    def open_spider(self, spider):
        self.f = open('files/university-intro.txt', 'w', encoding='utf-8')

    # 爬虫关闭时执行的方法
    def close_spider(self, spider):
        self.f.close()

    # 处理爬取项
    def process_item(self, item, spider):
        try:
            line = str(dict(item)) + '\n'
            self.f.write(line)
        except:
            pass
        return item