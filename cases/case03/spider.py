#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""爬取京东超市商品列表

使用requests进行页面爬取
使用pyQuery进行数据抽取
"""

import requests
from pyquery import PyQuery as pq
import random
import time
import mysql.connector
from DBUtils.PooledDB import PooledDB

# 建立数据库连接池
pool = PooledDB(mysql.connector, 5, host='localhost', user='root', password='123456', database='testdb')

# 目标URL
target_urls = {
    # 零食
    '1': 'https://list.jd.com/list.html?cat=1320,1583,1590',
    # 饮料
    '2': 'https://list.jd.com/list.html?cat=1320,1585',
    # 粮油
    '3': 'https://list.jd.com/list.html?cat=1320,1584',
    # 厨具
    '4': 'https://list.jd.com/list.html?cat=6196,6197,6199',
    # 手机
    '5': 'https://list.jd.com/list.html?cat=9987,653,655',
    # 办公文具
    '6': 'https://list.jd.com/list.html?cat=670,729,4837',
    # 电饭煲
    '7': 'https://list.jd.com/list.html?cat=737,752,753',
    # 收纳用品
    '8': 'https://list.jd.com/list.html?cat=1620,13780',
    # 儿童套装
    '9': 'https://list.jd.com/list.html?cat=1319,11842,11222',
    # 箱包
    '10': 'https://list.jd.com/list.html?cat=1672,2615,9186'
}

# User-Agents
user_agents = (
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'
)


# 爬取网页
def do_spider():
    for cat_id, url in target_urls.items():
        for i in range(1, 6):
            headers = {
                'User-Agent': random.choice(user_agents)
            }
            params = {
                'page': i
            }
            r = requests.get(url, headers=headers, params=params)
            get_data(cat_id, r.text)
            time.sleep(random.choice(range(30, 60)))


# 数据抽取
# 使用children()方法，则每一级选择器都要显示声明
# 使用find()方法，则可以越级书写选择器
def get_data(cat_id, raw_html):
    doc = pq(raw_html)
    items = doc('#plist .gl-warp .gl-item').items()
    resp_data = []
    for item in items:
        pic = item.find('.p-img img').attr('data-lazy-img') or item.find('.p-img img').attr('src')
        name = item.find('.p-name>a>em').text()
        resp_data.append((int(cat_id), name, pic))
    save_data(resp_data)


# 保存数据
def save_data(data):
    # 获取连接
    conn = pool.connection()
    # 获取游标
    cur = conn.cursor()

    # 插入数据
    cur.executemany('''INSERT INTO products
            (product_category_id, name, pic) 
            VALUES (%s, %s, %s)''', data)
    conn.commit()
    print('插入 %d 条数据' % cur.rowcount)

    # 关闭游标
    cur.close()
    # 关闭连接
    conn.close()


# 测试
do_spider()
