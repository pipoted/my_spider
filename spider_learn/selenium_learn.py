#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = 'http://www.baidu.com'
driver = webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(10)

driver.find_element_by_id('kw').send_keys('python')
driver.find_element_by_id('kw').send_keys(Keys.ENTER)

texts = driver.find_elements_by_xpath('//div/h3/a')
for text in texts:
    print(text.text)

driver.close()
