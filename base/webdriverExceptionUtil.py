# -*- coding: utf-8 -*-
'''
Created on 2015年1月18日
@author: zhh
'''
from selenium.webdriver.support.abstract_event_listener import AbstractEventListener
from selenium.common.exceptions import WebDriverException
import time
class WebDriverExceptionListener(AbstractEventListener):
    '''
    extend from AbstractEventListener
    '''
    def __init__(self):
        '''
        Constructor
        '''

    def on_exception(self, exception, driver):
        if isinstance(exception,WebDriverException):
            t=time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
            try:
                driver.get_screenshot_as_file("d:/img/test/screenshot_"+t+".png")
                print "webdriver err, get screenshot as 'screenshot_"+t+".png'"
            except Exception,e:
                print e
                
