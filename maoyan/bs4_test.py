#!/usr/bin/env python
# -*- coding: utf-8 -*-

# # html = """
# # <html><head><title>The Dormouse's story</title></head>
# # <body>
# # <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
# # <p class="story">Once upon a time there were three little sisters; and their names were
# # <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
# # <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# # <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# # and they lived at the bottom of a well.</p>
# # <p class="story">...</p>
# # """
# #
# # from bs4 import BeautifulSoup
# #
# # soup = BeautifulSoup(html, 'lxml')
# # # print(soup.prettify())
# # print(soup.title.string)
#
# html='''
# <div class="panel">
#     <div class="panel-heading">
#         <h4>Hello</h4>
#     </div>
#     <div class="panel-body">
#         <ul class="list" id="list-1">
#             <li class="element">Foo</li>
#             <li class="element">Bar</li>
#             <li class="element">Jay</li>
#         </ul>
#         <ul class="list list-small" id="list-2">
#             <li class="element">Foo</li>
#             <li class="element">Bar</li>
#         </ul>
#     </div>
# </div>
# '''
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html, 'lxml')
# # print(soup.find_all(name='ul'))
# # print(type(soup.find_all(name='ul')[0]))
#
# for ul in soup.find_all(name='ul'):
#     print(ul.find_all(name='li'))
#     for li in ul.find_all(name='li'):
#         print(li.string)

from bs4 import BeautifulSoup
import requests

url = 'https://maoyan.com/board/4?offset=0'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}

content = requests.get(url=url, headers=headers).content.decode()
soup = BeautifulSoup(content, 'lxml')

title = soup.find_all(name='a', attrs={"class": "image-link", "data-act": "boarditem-click"})
print(title)
print()
