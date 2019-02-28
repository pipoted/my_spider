#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import os
import time
import threading
import asyncio
from urllib.parse import urlencode
from urllib.request import urlretrieve
from multiprocessing import Process


def get_data(offset):
    """
    输入offset的值，返回相应url的json（dict）数据
    :param offset: int
    :return: dict
    """
    base_url = 'https://www.toutiao.com/api/search/content/?'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
    }
    params = {
        'aid': '24',
        'app_name': 'web_search',
        'offset': offset,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
    }
    url = base_url + urlencode(params)
    response = requests.get(url, headers=headers)
    return response.json()


def get_image(data):
    info_list = []
    for i in data:
        image_list = []
        if 'abstract' in i:
            # print(i['image_list'])
            for j in i['image_list']:
                image_list.append(j['url'])
            info_dict = {
                'title': i['title'],
                'image': image_list,
            }
            del image_list
            info_list.append(info_dict)

    return info_list


def save_as_dir(info_list):
    for info in info_list:
        if not os.path.exists('img/%s' % info['title']):
            os.mkdir('img/%s' % info['title'])
        for img in info['image']:
            urlretrieve(img, 'img/%s/%s.jpg' % (info['title'], time.time()))


async def main(offset):
    data = get_data(offset)['data']
    info_list = get_image(data)
    save_as_dir(info_list)


def thread_run():
    for i in range(0, 100, 20):
        threading.Thread(target=main, args=(i,)).start()
        print('thread' + str(i) + 'start')


def process_run():
    for i in range(0, 100, 20):
        Process(target=main, args=(i,)).start()
        print('Process' + str(i) + 'start')


def common_run():
    for i in range(0, 100, 20):
        main(i)


def loop_run():
    loop = asyncio.get_event_loop()
    for i in range(0, 100, 20):
        task = loop.create_task(main(i))
        print(task)
    loop.run_until_complete(task)
