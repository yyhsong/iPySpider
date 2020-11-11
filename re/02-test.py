#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""re库的基本用法

re库的主要功能函数
- search() 在一个字符串中搜索匹配正则表达式的第一个位置，返回match对象
- match() 从一个字符串的开始位置起匹配正则表达式，返回匹配的第一个match对象
- findall() 搜索字符串，以list类型返回全部能匹配的字串
- split() 将一个字符串按照匹配结果进行分割，返回list类型
- finditer() 搜索字符串，返回一个匹配结果的迭代类型，每个迭代元素是match对象
- sub() 在一个字符串中替换所有匹配正则表达式的字串，返回替换后的字符串

常用控制标记flags
- re.I  re.IGNORECASE  忽略大小写，[A-Z]能够匹配小写字符
- re.M  re.MULTILINE   多行匹配，^操作符能够将给定字符串的每行当作匹配开始
- re.S  re.DOTALL      .操作符能够匹配所有字符，默认匹配除换行外的所有字符

re.compile(pattern, flags=0)
将正则表达式的字符串形式编译成正则表达式对象
面向对象的用法：编译后的多次操作
"""

import re

# re.search(pattern, string, flags=0)
search = re.search(r'\d{3,4}', 'Nanjing025, Beijing010, Shanghai021')
if search:
    print('search:', search.group(0))

# re.match(pattern, string, flags=0)
match = re.match(r'[A-Za-z]+', 'Nanjing025, Beijing010, Shanghai021')
if match:
    print('match:', match.group(0))

# re.findall(pattern, string, flags=0)
match_list = re.findall(r'[A-Za-z]+', 'Nanjing025, Beijing010, Shanghai021')
print('findall:', match_list)

# re.split(pattern, string, maxsplit=0, flags=0)
# maxsplit 最大分割数，剩余部分作为最后一个元素输出
split_list = re.split(r', ', 'Nanjing025, Beijing010, Shanghai021')
print('split:', split_list)

# re.finditer(pattern, string, flags=0)
iter_items = re.finditer(r'[A-Za-z]+', 'Nanjing025, Beijing010, Shanghai021')
for item in iter_items:
    if item:
        print('iter:', item.group(0))

# re.sub(pattern, repl, string, count=0, flags=0)
# count 最大替换次数
sub_str = re.sub(r', ', '|', 'Nanjing025, Beijing010, Shanghai021')
print('sub:', sub_str)

# re.compile(pattern, flags=0)
pat = re.compile(r'[A-Za-z]+')
pat_match = pat.match('Nanjing025, Beijing010, Shanghai021')
if pat_match:
    print('match:', pat_match.group(0))
