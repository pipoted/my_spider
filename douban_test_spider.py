from urllib import request

url = 'https://movie.douban.com/top250'
headers = {
    'User-Agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}

re = request.Request(url=url, headers=headers)
resp = request.urlopen(re)
# print(resp.read().decode())

url = 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p480747492.webp'
request.urlretrieve(url, filename='test.jpg')
