#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2014年12月25日
@author: zhh
'''
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')
from baseUtil.windows import Window
from baseUtil.db import DB
from base.mainProcessPage import MainPage
from baseUtil.pages import VideoFirstAuditPage
from AT001_videoCreate import nowtime #引用相关case中的变量
import unittest,time
#nowtime='20150113133050'
videoName=u'视频自动化测试'+nowtime

class videoEdit(unittest.TestCase):
    def setUp(self):
        #初始化登录主页和driver
        #print "\n[AT003_videoFirstAudit] START"
        print "\nvideoName:"+videoName
        self.driver=MainPage().login("ie","http://192.168.88.109:8050/icms/login/login.do", "admin", "cq3q")
        #mainPage.icms3_check()
        #初始化主页面和主窗口
        self.mainWindow=Window(self.driver).window_get()
        self.verificationErrors = []
        self.accept_next_alert = True

    def test(self):
        driver=self.driver
        vfa=VideoFirstAuditPage(driver)
        vfa.go_to_page("视频初审")
        assetid=DB.get_element_value("assetid", "t_video_item", "filename='"+videoName+"'")
        assert assetid
        vfa.search(videoName,assetid)
        vfa.checkbox_click(videoName)
        #vfa.video_choose(videoName)
        vfa.button_click("认领并审核通过")
        time.sleep(2)
        Window.switch_from(self.mainWindow)
        vfa.select("内容类型", "电影")
        #vfa.create_contentType_chose("单视频")
        vfa.button_click("确定")
        Window.switch_to(self.mainWindow)
        vfa.do_alert("accept")
        
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__=="__main__":
    unittest.main()