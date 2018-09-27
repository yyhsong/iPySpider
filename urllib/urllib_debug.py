#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""urllib
开启DebugLog
"""

from urllib import request

httphd = request.HTTPHandler(debuglevel=1)
httpshd = request.HTTPSHandler(debuglevel=1)

opener = request.build_opener(httphd, httpshd)
request.install_opener(opener)
data = request.urlopen('https://www.baidu.com/')
