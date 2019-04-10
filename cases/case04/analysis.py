#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""对mzitu网站图集名称简要分析

使用jieba进行分词
使用字典等进行词频统计
"""

# 导入需要的模块
import os
import json
import jieba

# 将所有文件夹名称转换为str类型
# folder_name = ' '.join(os.listdir(os.path.join(os.path.abspath(os.path.curdir), 'pics')))
folder_name_str = ' '.join(os.listdir(r'./pics'))

# 停用词
stopwords = set([word.strip() for word in open('./data/mzitu_stopwords.txt', 'r', encoding='utf-8').readlines()])

# 分词
jieba.load_userdict(r'./data/mzitu_dict.txt')  # 加载自定义词典，可省略
seg_list = jieba.lcut(folder_name_str, cut_all=False)  # 精确模式

# 利用字典统计词频
counter = dict()
for seg in seg_list:
    if seg not in stopwords:
        if seg != ' ':
            counter[seg] = counter.get(seg, 1) + 1

# 根据词频统计对字典进行排序
counter_sort = sorted(counter.items(), key=lambda val: val[1], reverse=True)
print('词频统计：')
for c in counter_sort:
    print(c)

# 解析成json并写入文件
words = json.dumps(counter_sort, ensure_ascii=False)
with open(r'./data/words.json', 'w+', encoding='utf-8') as f:
    f.write(words)
