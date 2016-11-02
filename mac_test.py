# -*- coding: utf-8 -*-
'''
Created on 2014年12月23日
@author: zhh
'''

from selenium import webdriver
import time,os
dr=webdriver.Chrome("driver/chromedriver_mac")
dr.get("http://www.baidu.com")
dr.find_element_by_id("kw").send_keys("selenium")
dr.find_element_by_id("su").click()
time.sleep(5)
dr.quit()
# print os.environ
# dr2=webdriver.Safari()
# dr2.get("http://www.baidu.com")