#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
#
# browser = webdriver.Chrome()
# try:
#     browser.get('http://baidu.com')
#     input = browser.find_element_by_id('kw')
#     input.send_keys('python')
#     input.send_keys(Keys.ENTER)
#     wait = WebDriverWait(browser, 10)
#     wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
#     print(browser.current_url)
#     print(browser.get_cookies())
#     print(browser.page_source)
# finally:
#     browser.close()

# browser = webdriver.Chrome()
# browser.get('https://www.taobao.com')
# # input_first = browser.find_elements(By.ID, 'q')
# # input_second = browser.find_element_by_id('q')
# # input_second.send_keys('python')
# # input_second.send_keys(Keys.ENTER)
# # browser.close()
# option = browser.find_elements_by_xpath('//li[@class="J_Cat a-all"]')
# print(option)
# browser.close()

# import time
# browser = webdriver.Chrome()
# browser.get('https://www.taobao.com')
# input = browser.find_element_by_id('q')
# input.send_keys('python')
# time.sleep(1)
# input.clear()
# input.send_keys('java')
# button = browser.find_element_by_class_name('btn-search')
# button.click()
# time.sleep(3)
# browser.close()

# import time
# from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException
#
# browser = webdriver.Chrome()
# url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
# browser.get(url)
# browser.switch_to.frame('iframeResult')
# try:
#     logo = browser.find_element_by_class_name('logo')
# except NoSuchElementException:
#     print('NO LOGO')
# browser.switch_to.parent_frame()
# logo = browser.find_element_by_class_name('logo')
# print(logo)
# print(logo.text)

# from selenium import webdriver
#
# browser = webdriver.Chrome()
# browser.implicitly_wait(10)
# browser.get('https://www.zhihu.com/explore')
# input = browser.find_element_by_class_name('zu-top-add-question')
# print(input)
# browser.close()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# browser = webdriver.Chrome()
# browser.get('https://www.taobao.com/')
# wait = WebDriverWait(browser, 10)
# input = wait.until(EC.presence_of_element_located((By.ID, 'q')))
# button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
# print(input, button)

# import time
# from selenium import webdriver
#
# browser = webdriver.Chrome()
# browser.get('https://www.baidu.com/')
# browser.get('https://www.taobao.com/')
# browser.back()
# time.sleep(1)
# browser.forward()
# browser.close()

import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
browser.execute_script('window.open()')
print(browser.window_handles)
browser.switch_to(browser.window_handles[1])
browser.get('https://www.taobao.com')
time.sleep(1)
browser.switch_to(browser.window_handles[0])
browser.get('https://python.org')
