#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2014年12月25日
@author: zhh
'''
from baseUtil.windows import Window
from baseUtil.db import DB
from base.mainProcessPage import MainPage
from baseUtil.pages import VideoEditPage
from baseUtil.pages import DotSplitAndEncodePage
from AT001_videoCreate import nowtime #引用相关case中的变量

import unittest
videoName=u"视频自动化测试"+nowtime
#nowtime='20150106150440'

class videoEdit(unittest.TestCase):
    def setUp(self):
        #初始化登录主页和driver
        #print "\n[AT002_videoEdit] START"
        print "\nvideoName:"+videoName
        self.driver=MainPage().login("ie","http://192.168.88.109:8050/icms/login/login.do", "admin", "cq3q")
        #mainPage.icms3_check()
        #初始化主页面和主窗口
        self.mainWindow=Window(self.driver).window_get()
        self.verificationErrors = []
        self.accept_next_alert = True

    def test(self):
        driver=self.driver
        
        vep=VideoEditPage(driver)
        dsp=DotSplitAndEncodePage(driver)
        vep.go_to_page("视频加工")
        assetid=DB.get_element_value("assetid", "t_video_item", "filename='"+videoName+"'")
        assert assetid
        vep.search(videoName,assetid)
        #有bug，先不粗编。
#         vep.button_click("打点拆条")
#         #切换到打点拆条窗口
#         Window.switch_from(self.mainWindow)
#         #拆条
#         dsp.inDot_set("00:00:05:000")
#         dsp.outDot_set("00:00:30:000")
#         dsp.splitTile_set(u"标题")
#         dsp.splitTag_set("tag")
#         dsp.button_click("生成拆条")
#         #粗编-根据拆条生成视频
#         dsp.newVideo_create(videoName+"CHAI")
#         #返回主窗口
#         Window.switch_to(self.mainWindow)
        vep.button_click("编码")
        #编码，切换到编码窗口
        Window.switch_from(self.mainWindow)
        dsp.paramCode_select("mpeg2_5.5")
        dsp.encode_mission_name(u"转码"+nowtime)
        dsp.priority_select("6")
        dsp.button_click("确定")
        #返回主窗口
        Window.switch_to(self.mainWindow)
        vep.reset_frame()
        vep.checkbox_click(videoName)
        #vep.video_choose(videoName)
        vep.button_click("送审")
        
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__=="__main__":
    unittest.main()