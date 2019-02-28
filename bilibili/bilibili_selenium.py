#!/usr/bin/env python
# -*- coding: utf-8 -*-


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from lxml import etree
from concurrent.futures import ThreadPoolExecutor
from multiprocessing.pool import Pool
from multiprocessing import Queue, Process
import threading


def get_info_list_selenium(i: int):
    url = 'https://search.bilibili.com/all?keyword=PYTHON%E7%88%AC%E8%99%AB&page={}'.format(i)
    options = Options()
    options.add_argument('--headless')
    browser = webdriver.Chrome(options=options)

    browser.get(url)
    content = browser.page_source

    tree = etree.HTML(content)

    info_list = []
    li_list = tree.xpath('//li[@class="video matrix"]')
    for li in li_list:
        title = li.xpath('.//a[@class="title"]/@title')[0].strip()
        info = li.xpath('.//div[@class="des hide"]/text()')[0].strip()
        types = li.xpath('.//span[@class="type hide"]/text()')[0].strip()
        play_num = li.xpath('.//span[@class="so-icon watch-num"]/text()')[0].strip()
        bar_num = li.xpath('.//span[@class="so-icon hide"]/text()')[0].strip()
        time = li.xpath('.//span[@class="so-icon time"]/text()')[0].strip()
        user_name = li.xpath('.//span[@class="so-icon"]/a/text()')[0].strip()
        img = 'https:' + li.xpath('.//div[@class="lazy-img"]/img/@src')[0]
        url = 'https:' + li.xpath('.//a[@class="img-anchor"]/@href')[0]
        li_dict = {
            'title': title,
            'info': info,
            'types': types,
            'play_num': play_num,
            'bar_num': bar_num,
            'time': time,
            'user_name': user_name,
            'img': img,
            'url': url,
        }
        info_list.append(li_dict)
        del li_dict
    return info_list


async def save_to_mongo(info_list: list):
    import pymongo

    mongo = pymongo.MongoClient('mongodb://localhost:27017/')
    my_db = mongo['spider']
    my_col = my_db['bilibili']

    for i in info_list:
        my_col.insert_one(i)
        # print(i['title'], 'success')


def save_to_redis(info_list):
    import redis

    r = redis.Redis(host='localhost', port=6379, password='xzx199110', db=2)
    for i in info_list:
        r.hmset(i['title'], i)


# info_list = []
# save_to_mongo(get_info_list_selenium(1, info_list))


def thread_pool_save():
    with ThreadPoolExecutor(10) as executor:
        for i in range(1, 50):
            executor.submit(save_to_mongo, get_info_list_selenium(i))
            print(i, 'success')


def process_pool_save():
    pool = Pool(5)
    for i in range(1, 50):
        pool.apply_async(save_to_mongo, (get_info_list_selenium(i),))
        print(i, 'success')


def asyncio_to_run():
    import asyncio

    info_list = []
    for i in range(1, 50):
        corcoutine = get_info_list_selenium(i, info_list)
        loop = asyncio.get_event_loop()
        loop.run_until_complete(corcoutine)
        print(i, 'success')

    print(info_list)
