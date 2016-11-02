#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2014年12月17日
@author: zhh
'''

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from datetime import datetime

nowtime = datetime.now().strftime('%Y%m%d%H%M%S')
videoName="视频自动化测试".decode("utf8")+nowtime

driver=login.get_driver("ie", "http://192.168.88.109:8080/icms/login/login.do", "admin", "cq3q")
driver.implicitly_wait(2)
while driver.title != "思华科技统一内容管理系统".decode("utf8"):
    time.sleep(1)
print "Now in <" + driver.title + "> page."+nowtime

nowhandle = driver.current_window_handle
driver.switch_to_default_content()
main_statusbarframe = driver.find_element_by_xpath("//frame[@name='main_statusbarframe']")
main_leftmenuframe = driver.find_element_by_xpath("//frame[@name='main_leftmenuframe']")
main_tabframe = driver.find_element_by_xpath("//frame[@name='main_tabframe']")

driver.switch_to_frame(main_statusbarframe)
curModule = driver.find_element_by_name("curModule")
curModule.find_element_by_xpath("""//option[@value="110"]""").click()
#进入视频录入页面
driver.switch_to_default_content()
driver.switch_to_frame(main_leftmenuframe)
driver.find_element_by_link_text("视频录入").click()
# driver.find_element_by_xpath("""//a[@onclick="refreshMainPage('/telecom/contentBaseAssetAction.do?action=editContent')"]""").click()
driver.switch_to_default_content()
driver.switch_to_frame(main_tabframe)
driver.switch_to_frame("mainFrame")
driver.find_element_by_id("videoEncoderSelect").find_element_by_xpath("""//option[@value="H264"]""").click()
driver.find_element_by_xpath("""//select[@name="videoItem.priority" and @id="videoPriority"]/option[@value="4"]""").click()
driver.find_element_by_xpath("""//input[@name="videoItem.duration"]""").send_keys("123")
driver.find_element_by_xpath("""//input[@name="videoItem.fileName"]""").send_keys(videoName)
driver.find_element_by_xpath("""//input[@name="videoItem.contentBusinessType"]""").send_keys("IPTV")
driver.find_element_by_xpath('''//div[@id="chooseFile"]//img''').click()  # 这里全屏会找不到，原因未知
 
time.sleep(2)
allhandles = driver.window_handles
print len(allhandles)
for handle in allhandles :
    if handle != nowhandle:
        driver.switch_to_window(handle)
        print "Now in fileSelect window"
        # 定位到要双击的元素
        double = driver.find_element_by_xpath("""//span[text()='30000001']""")
        # double =driver.find_element_by_xpath("""//td[text()='public']""")
        # 对定位到的元素执行鼠标双击操作
        ActionChains(driver).double_click(double).perform()
        time.sleep(2)
        driver.switch_to_default_content()
        driver.find_element_by_xpath("""//span[text()='public']""").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_elements_by_tag_name("iframe")[0])
        #driver.switch_to_frame("monitor") #貌似也支持id定位frame
        double = driver.find_element_by_xpath("""//div[@id="autoTest.ts"]""")
        ActionChains(driver).double_click(double).perform()
        driver.switch_to_window(nowhandle) #切回主窗口
        print "Now in <" + driver.title + "> page."
  
#重新定位主体和frame
driver.switch_to_default_content()
driver.switch_to_frame(main_tabframe)
driver.switch_to_frame("mainFrame")
#保存
driver.find_element_by_xpath("""//input[@class="btn2" and @onclick="javascript:submitForm('checkFile');"]""").click()
alert=driver.switch_to_alert()
alert.accept()
#完成
driver.find_element_by_xpath("""//input[@class="btn2" and @onclick="javascript:doReturn();"]""").click()

#切到加工环节
driver.switch_to_default_content()
driver.switch_to_frame(main_leftmenuframe)
driver.find_element_by_link_text("视频加工").click()
driver.switch_to_default_content()
driver.switch_to_frame(main_tabframe)
driver.switch_to_frame("mainFrame")
driver.find_element_by_xpath("""//input[@name="mingcheng"]""").send_keys(videoName)
for i in range(12):
    try:
        #driver.find_element_by_xpath("""//button[text()='"""+'查询'.decode("utf-8")+"""']""").click() #也可以根据text()定位
        driver.find_element_by_xpath("""//button[@class="btn2" and @onclick="javascript:search('search')"]""").click()
        driver.find_element_by_xpath("""//a[@href and text()='"""+videoName+"""']""").click()
        break
    except Exception,e:
        print i
        if i==11:
            print "time out, break."
            break
        print "No found, maybe in process, wait for 5 seconds to retry."
        time.sleep(5)

time.sleep(5)
driver.quit()
