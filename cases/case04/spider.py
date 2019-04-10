#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""爬取mzitu网站图片

使用requests进行网页爬取
使用BeautifulSoup4进行数据抽取
"""

# 导入需要的模块
import os
import re
import time
import threading
from multiprocessing import Pool, cpu_count
import requests
from bs4 import BeautifulSoup

# 请求头信息
HEADERS = {
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
    'Referer': 'http://www.mzitu.com'
}

# 图片保存路径
PIC_PATH = os.path.join(os.path.abspath(os.path.curdir), r'pics')


# 获取mzitu网站下的图集url
def get_urls():
    page_urls = ['https://www.mzitu.com/page/{cnt}'.format(cnt=cnt)
                 for cnt in range(1, 11)]  # 215
    print("正在获取图集URL...")
    pic_urls = []
    for page_url in page_urls:
        try:
            bs = BeautifulSoup(requests.get(page_url, headers=HEADERS, timeout=10).text, 'lxml').find('ul', id="pins")
            result = re.findall(r"(?<=href=)\S+", str(bs))
            pic_url = [url.replace('"', "") for url in result]
            pic_urls.extend(pic_url)
        except Exception as e:
            print(e)
    # 利用set去重
    pic_urls_set = set(pic_urls)
    print('图集URL总数：', len(pic_urls_set))
    return pic_urls_set


# 全局资源锁
lock = threading.Lock()


# 爬虫入口
def crawl_urls(url):
    try:
        r = requests.get(url, headers=HEADERS, timeout=10).text
        folder_name = BeautifulSoup(r, 'lxml').find(
            'div', class_="main-image").find('img')['alt'].replace("?", " ")
        with lock:
            if make_dir(folder_name):
                # 套图里图片张数
                max_count = BeautifulSoup(r, 'lxml').find(
                    'div', class_='pagenavi').find_all('span')[-2].get_text()
                page_urls = [url + "/" + str(i) for i in range(1, int(max_count) + 1)]
                img_urls = []

                for _, page_url in enumerate(page_urls):
                    time.sleep(0.25)
                    result = requests.get(page_url, headers=HEADERS, timeout=10).text
                    img_url = BeautifulSoup(result, 'lxml').find(
                        'div', class_="main-image").find(
                        'p').find('a').find('img')['src']
                    img_urls.append(img_url)
                for cnt, url in enumerate(img_urls):
                    save_pic(url, cnt)
    except Exception as e:
        print(e)


# 新建文件夹并切换到该目录下
def make_dir(folder_name):
    path = os.path.join(PIC_PATH, folder_name)
    # 如果目录已存在就不要重复爬取
    if not os.path.exists(path):
        os.makedirs(path)
        print('创建目录：', path)
        os.chdir(path)
        return True
    return False


# 保存图片到本地
def save_pic(pic_src, pic_cnt):
    try:
        time.sleep(0.10)
        img = requests.get(pic_src, headers=HEADERS, timeout=10)
        img_name = "pic_cnt_{}.jpg".format(pic_cnt + 1)
        with open(img_name, 'ab') as f:
            f.write(img.content)
            print('保存图片：', img_name)
    except Exception as e:
        print('Exception: ', e)


# 删除空文件夹
def delete_empty_dir(save_dir):
    if os.path.exists(save_dir):
        if os.path.isdir(save_dir):
            for d in os.listdir(save_dir):
                path = os.path.join(save_dir, d)
                if os.path.isdir(path):
                    delete_empty_dir(path)
        if not os.listdir(save_dir):
            os.rmdir(save_dir)
            print("删除空文件夹：", save_dir)
    else:
        print("启动爬虫！")


if __name__ == '__main__':
    pic_urls = get_urls()
    pool = Pool(processes=cpu_count())
    try:
        delete_empty_dir(PIC_PATH)
        pool.map(crawl_urls, pic_urls)
    except Exception as e:
        print('Exception: ', e)
        time.sleep(30)
        delete_empty_dir(PIC_PATH)
        pool.map(crawl_urls, pic_urls)
    finally:
        print('爬取结束！')
