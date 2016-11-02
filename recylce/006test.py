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
# from baseUtil.db import DB
from base.mainProcessPage import MainPage
from baseUtil.pages import VideoFirstAuditPage
#from AT001_videoCreate import nowtime #引用相关case中的变量
import unittest,time
#nowtime='20150112174029'
#videoName=u'饮食养生汇HD150101拆条'
videoName=u'视频自动化测试20150113130511'
class videoEdit(unittest.TestCase):
    def setUp(self):
        #初始化登录主页和driver
        self.verificationErrors = ["1"]
        self.accept_next_alert = True
    def test(self):
        print __file__
        print __file__.split("/")[-1].split(".")[0]
        assert False
        print "here"
        self.verificationErrors = [1]
    def tearDown(self):
        if self.verificationErrors !=[1]:
            print 2
        print "a"
        print "run"
        self.assertEqual(["1"], self.verificationErrors)

if __name__=="__main__":
    unittest.main()