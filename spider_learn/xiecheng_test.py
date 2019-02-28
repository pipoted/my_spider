#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import gevent
# import time
#
#
# def show_wait(name, n):
#     for i in range(n):
#         print(name, i, 's')
#         # gevent.sleep(1)
#
#
# # show_wait('xiao', 11)
# # show_wait('xiaojian', 10)
# # show_wait('xiaojianjian', 10)
# # show_wait('xiaowang', 10)
#
# g1 = gevent.spawn(show_wait, 'xiao', 11)
# g2 = gevent.spawn(show_wait, 'xiaojian', 10)
# g3 = gevent.spawn(show_wait, 'xiaowang', 15)
#
# g1.join()
# g2.join()
# g3.join()

import gevent
from gevent import monkey

gevent.monkey.patch_all()

import requests


def download(url):
    print('start', url)
    content = requests.get(url).content
    gevent.sleep(3)
    print(len(content))


gevent.joinall([
    gevent.spawn(download, 'http://www.baidu.com'),
    gevent.spawn(download, 'http://www.163.com'),
    gevent.spawn(download, 'http://www.qq.com'),
    gevent.spawn(download, 'http://www.sina.com'),
])
