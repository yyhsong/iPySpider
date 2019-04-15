# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ItcastPipeline(object):
    def process_item(self, item, spider):
        txt = item['name'] + ' | ' + item['title'] + ' | ' + item['info'] + '\n'
        with open('teachers.txt', 'a', encoding='utf-8') as f:
            f.write(txt)

        return item
