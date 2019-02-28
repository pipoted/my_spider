# import requests

# r = requests.get('http://www.baidu.com')
# print(type(r))
# print(r.status_code)
# print(type(r.text))
# print(r.text)
# print(r.cookies)

# r = requests.get('http://httpbin.org/get')
# print(r.text)

# data = {
#     'name': 'xiao',
#     'age': 22,
# }

# r = requests.get('http://httpbin.org/get')
# print(r.json())

# import requests
# import re
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
# }
# r = requests.get("https://www.zhihu.com/explore", headers=headers)
# pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
# titles = re.findall(pattern, r.text)
# print(titles)

# import requests
#
# r = requests.get("https://github.com/favicon.ico")
# with open('favicon.ico', 'wb') as f:
#     f.write(r.content)

# import requests
#
# files = {'file': open('favicon.ico', 'rb')}
# r = requests.post("http://httpbin.org/post", files=files)
# print(r.text)

import requests

r = requests.get('http://www.baidu.com')
print(r.cookies)

for key, value in r.cookies.items():
    print(key, value)
