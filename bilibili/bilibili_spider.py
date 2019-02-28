#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import requests
import pymysql
import pymongo

from multiprocessing import Pool
from concurrent.futures import ThreadPoolExecutor
from lxml import etree


# requests version
def get_info_list(i):
    url = 'https://search.bilibili.com/all?keyword=PYTHON%E7%88%AC%E8%99%AB&page={}'.format(i)

    content = requests.get(url).content.decode()
    tree = etree.HTML(content)

    li_list = tree.xpath('//li[@class="video matrix"]')
    info_list = []
    for li in li_list:
        title = li.xpath('.//a[@class="title"]/@title')[0].strip()
        info = li.xpath('.//div[@class="des hide"]/text()')[0].strip()
        type = li.xpath('.//span[@class="type hide"]/text()')[0].strip()
        play_num = li.xpath('.//span[@class="so-icon watch-num"]/text()')[0].strip()
        bar_num = li.xpath('.//span[@class="so-icon hide"]/text()')[0].strip()
        time = li.xpath('.//span[@class="so-icon time"]/text()')[0].strip()
        user_name = li.xpath('.//span[@class="so-icon"]/a/text()')[0].strip()
        li_dict = {
            'title': title,
            'info': info,
            'type': type,
            'play_num': play_num,
            'bar_num': bar_num,
            'time': time,
            'user_name': user_name,
        }
        info_list.append(li_dict)

    return info_list





def save_to_sql(info_list):
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='xzx199110',
        database='spider',
        port=3306,
    )
    curcor = conn.cursor()

    for i in info_list:
        sql = """
        insert into bilibili values (%s,%s,%s,%s,%s,%s,%s)
        """
        curcor.execute(sql, (i['title'], i['info'], i['type'], i['play_num'], i['bar_num'], i['time'], i['user_name']))
        conn.commit()
        print('success!')

    conn.close()


def save_to_mongo(info_list):
    myclient = pymongo.MongoClient(host='mongodb://localhost:27017/')
    my_db = myclient['spider']
    my_col = my_db['bilibili']

    for i in info_list:
        my_col.insert_one(i)
        print('save success')


def save_to_redis(info_list):
    import redis

    r = redis.Redis(host='localhost', port=6379, password='xzx199110', db=0)

    for i in info_list:
        r.hmset(i['title'], i)
        # r.delete(i['title'])
        print('success')


def save_to_json(info_list: list):
    import json

    for content in info_list:
        with open('result.json', 'a') as fp:
            fp.write(json.dumps(obj=content, ensure_ascii=False, ) + '\n')
            print('success')


def save_to_csv(info_list):
    import csv

    top_list = [i for i in info_list[0]]
    with open('bilibili.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(top_list)
        for content in info_list:
            writer.writerow([content[i] for i in content])
            print('success')


def thread_pool_save():
    with ThreadPoolExecutor(10) as executor:
        for i in range(50):
            executor.submit(save_to_mongo, get_info_list(i))
            print(i, 'success')


pool = Pool(10)

for i in range(50):
    pool.apply_async(save_to_mongo, (get_info_list(i),))
    print(i, 'success')
