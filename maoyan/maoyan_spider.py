#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import re
from lxml import etree
from bs4 import BeautifulSoup


def get_info_maoyan(i):
    info_list = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
    }
    url = 'https://maoyan.com/board/4?offset={}'.format(i)
    #
    resp = requests.get(url=url, headers=headers)
    content = resp.content.decode()

    tree = etree.HTML(content)
    dds = tree.xpath('//dl[@class="board-wrapper"]//dd')
    for dd in dds:
        range = dd.xpath('./i/text()')[0].strip()
        title = dd.xpath('.//p[@class="name"]/a/@title')[0].strip()
        actor = dd.xpath('.//p[@class="star"]/text()')[0].strip()
        actor = re.sub('[主演：\s]', '', actor)
        releasetime = dd.xpath('.//p[@class="releasetime"]/text()')[0].strip()
        releasetime = re.sub('[上映时间：\s]', '', releasetime)
        score = ''.join(dd.xpath('.//p[@class="score"]//text()'))
        image = dd.xpath('.//img[@class="board-img"]/@data-src')[0]
        tem_dict = {
            'range': int(range),
            'title': title,
            'actor': actor,
            'releasetime': releasetime,
            'score': score,
            'image': image,
        }
        info_list.append(tem_dict)
        print(tem_dict)
        del tem_dict
    return info_list


def save_for_mysql(aim_list):
    import pymysql
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='xzx199110',
        database='spider',
        port=3306,
    )
    cursor = conn.cursor()
    for i in aim_list:
        print(i['range'], i['title'], i['actor'], i['releasetime'], i['score'])
        sql = '''insert into maoyan_top values ("%s", "%s", "%s", "%s", "%s", "%s")
        '''

        try:
            cursor.execute(sql, (i['range'], i['title'], i['actor'], i['releasetime'], i['score'], i['image']))
            conn.commit()
            print('success')
        except:
            conn.rollback()
            print('error')

    conn.close()


def save_for_mongdb(info_list):
    import pymongo

    myclient = pymongo.MongoClient('mongodb://localhost:27017/')
    my_db = myclient['spider']
    my_col = my_db['maoyan_top']

    for i in info_list:
        my_col.insert_one(i)
        print('success')


def save_for_redis(info_list):
    import redis
    r = redis.Redis(host='localhost', port=6379, password='xzx199110')

    for tem_dict in info_list:
        r.hmset(name=tem_dict['title'], mapping=tem_dict)


def save_as_json(info_list):
    import json
    for content in info_list:
        with open('result.json', 'a') as fp:
            fp.write(json.dumps(obj=content, ensure_ascii=False, ) + '\n')
    print('success')


def save_as_csv(info_list):
    import csv
    top_list = [i for i in info_list[0]]

    with open('maoyan.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(top_list)
        for content in info_list:
            writer.writerow([content[i] for i in content])


info_list = []
for i in range(0, 100, 10):
    info_list += get_info_maoyan(i)

print(info_list)
# save_for_mongdb(get_info_maoyan(i))
# save_as_json(get_info_maoyan(i))
save_for_mysql(info_list)
# save_for_redis(get_info_maoyan(i))
# save_as_csv(info_list)
