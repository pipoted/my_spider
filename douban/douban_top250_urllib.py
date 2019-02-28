from urllib import request
from lxml import etree
import re
import pymysql
import pymongo
import redis
import requests


def douban_spider_info_xpath_urllib():
    """
    xpath + re + urllib
    :return:
    """
    info_list = []
    for i in range(0, 250, 25):
        url = 'https://movie.douban.com/top250?start={}&filter='.format(i)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
        }

        resp = request.Request(url=url, headers=headers)
        resp = request.urlopen(resp)
        content = resp.read().decode()

        tree = etree.HTML(text=content)

        li = tree.xpath('//ol[@class="grid_view"]/li')
        for i in li:
            name = i.xpath('.//div[@class="hd"]//text()')[2]
            info = i.xpath('.//div[@class="bd"]//text()')
            director = re.findall('导演: (.*?)\s', info[1])[0].strip()
            actor = re.findall('主演: (.*?)\s', info[1])
            if actor:
                actor = actor[0].strip()
            else:
                actor = 'none'
            age = re.findall('\s(\d+)\s', info[2])
            if age:
                age = age[0].strip()
            else:
                age = 'none'
            area = re.findall('\s\/\s(.*?)\s\/', info[2])[0].strip()
            temp = re.findall('\s\/\s(.*?)\s+$', info[2])[0]
            types = re.findall('.*?\s\/\s(.*?)$', temp)[0].strip()
            star = i.xpath('.//span[@class="rating_num"]/text()')[0].strip()
            image = i.xpath('.//div[@class="pic"]/a/img/@src')[0].strip()
            temp_dict = {
                'name': name,
                'director': director,
                'actor': actor,
                'age': age,
                'area': area,
                'types': types,
                'star': star,
                'image': image,
            }
            info_list.append(temp_dict)
    return info_list

def douban_spider_info_xpath_requests():
    """
    xpath + re + requests
    :return:
    """
    info_list = []
    for i in range(0, 250, 25):
        url = 'https://movie.douban.com/top250?start={}&filter='.format(i)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
        }

        resp = requests.get(url=url, headers=headers)
        content = resp.content

        tree = etree.HTML(text=content)

        li = tree.xpath('//ol[@class="grid_view"]/li')
        for i in li:
            name = i.xpath('.//div[@class="hd"]//text()')[2]
            info = i.xpath('.//div[@class="bd"]//text()')
            director = re.findall('导演: (.*?)\s', info[1])[0].strip()
            actor = re.findall('主演: (.*?)\s', info[1])
            if actor:
                actor = actor[0].strip()
            else:
                actor = 'none'
            age = re.findall('\s(\d+)\s', info[2])
            if age:
                age = age[0].strip()
            else:
                age = 'none'
            area = re.findall('\s\/\s(.*?)\s\/', info[2])[0].strip()
            temp = re.findall('\s\/\s(.*?)\s+$', info[2])[0]
            types = re.findall('.*?\s\/\s(.*?)$', temp)[0].strip()
            star = i.xpath('.//span[@class="rating_num"]/text()')[0].strip()
            image = i.xpath('.//div[@class="pic"]/a/img/@src')[0].strip()
            temp_dict = {
                'name': name,
                'director': director,
                'actor': actor,
                'age': age,
                'area': area,
                'types': types,
                'star': star,
                'image': image,
            }
            info_list.append(temp_dict)
    return info_list



# sql
def save_for_mysql(aim_list):
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='xzx199110',
        database='spider',
        port=3306,
    )
    for i in aim_list:
        cursor = conn.cursor()
        sql = '''insert into douban_top(name, director, actor, age, area, types, star, image) values (
            "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}"
        )
        '''.format(i['name'], i['director'], i['actor'], i['age'], i['area'], i['types'], i['star'], i['image'])

        try:
            cursor.execute(sql)
            conn.commit()
        except:
            conn.rollback()

    conn.close()


# mongodb
def save_mongodb(slist):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["spider"]
    mycol = mydb["douban_top"]

    for tem_dict in slist:
        x = mycol.insert_one(tem_dict)


# db_list = myclient.list_database_names()
# if 'xiaojiantest' in db_list:
#     print('yes')

def save_redis(douban_list):
    r = redis.Redis(host='localhost', port=6379, password='xzx199110', db=0)

    for tem_dict in douban_list:
        r.hmset(name=tem_dict['name'], mapping=tem_dict)

save_for_mysql(douban_spider_info_xpath_urllib())
