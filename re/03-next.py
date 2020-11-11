#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""re库的进阶使用

Match对象的属性
- string 待匹配的文本
- re 匹配时使用的正则表达式
- pos 搜索文本的开始位置
- endpos 搜索文本的结束位置

Match对象的方法
- group(0) 获取匹配的字符串
- start() 匹配字符串在原字符串的开始位置
- end() 匹配字符串在原字符串的结束位置
- span() 返回(start(), end())

贪婪匹配与最小匹配
- re库默认采用贪婪匹配，即匹配最长的子串
- 最小匹配操作符：*? +? ?? {m,n}?
- 只要长度输出可能不同，都可以通过在操作符后加?变成最小匹配
"""

import re

# 贪婪匹配
match = re.match(r'py.*n', 'pythonanbncn')
if match:
    print('贪婪匹配：', match.group(0))

# 最小匹配
match = re.match(r'py.*?n', 'pythonanbncn')
if match:
    print('最小匹配：', match.group(0))
