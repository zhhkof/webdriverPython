#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2014年12月17日
@author: zhh
'''
from baseUtil.windows import Window
from baseUtil.db import DB
from base.mainProcessPage import MainPage
from baseUtil.pages import VideoCreatePage,FileSelectPage
from datetime import datetime
import unittest
#时间戳生成
nowtime = datetime.now().strftime('%Y%m%d%H%M%S')
videoName=u"视频自动化测试"+nowtime

class videoCreate(unittest.TestCase):
    def setUp(self):
        #初始化登录主页和driver
        #print "\n[AT001_videoCreate] START"
        print "\nvideoName:"+videoName
        mainPage=MainPage()
        self.driver=mainPage.login("ie","http://192.168.88.109:8050/icms/login/login.do", "admin", "cq3q")
        #mainPage.icms3_check()
        #初始化主页面和主窗口
        self.mainWindow=Window(self.driver).window_get()
        self.verificationErrors = []
        self.accept_next_alert = True
    def test(self):
        driver=self.driver
        #创建测试页面对象,进入页面
        vcp=VideoCreatePage(driver)
        vcp.go_to_page("视频录入")
        #操作步骤
        vcp.select("内容编码参数", "mpeg2_5.5")
        #vcp.encoder_select("mpeg2_5.5")
        vcp.input("视频时长", "123")
        #vcp.duration_set("1234")
        vcp.input("文件名称", videoName)
        #vcp.videoname_set(videoName)
        vcp.input("内容的业务分类", u"IPTV视频")
        #vcp.contentBusinessType_set(u"IPTV视频")
        vcp.select("优先级", "7", "loop")
        #vcp.priority_select("7")
        vcp.chooseFileImg_click()
        #切换窗口
        Window.switch_from(self.mainWindow)
        #创建文件选择弹出页对象
        fsp=FileSelectPage(driver)
        fsp.choose_file()
        #切换回主窗口
        Window.switch_to(self.mainWindow)
        vcp.button_click("保存")
        vcp.button_click("完成")
        assert DB.rows_exist("T_VIDEO_ITEM", "FILENAME='%s'" %videoName)
        
    def tearDown(self):
        #self.driver.get_screenshot_as_file("d:/img/test/"+__file__.split("\\")[-1].split(".")[0]+".jpg")
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()