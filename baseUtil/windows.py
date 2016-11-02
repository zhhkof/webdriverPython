# -*- coding: utf-8 -*-
'''
Created on 2014年12月23日
@author: zhh
'''

class Window:
    @classmethod
    def __init__(cls,driver):
        cls.driver=driver

    @classmethod
    def switch_from(cls,nowhandle):
        '''切换到非传入的另一个窗口，只支持2个窗口中切换到1个窗口'''
        allhandles = cls.driver.window_handles
#        handles=iter(allhandles)
        for i in range(5):
            #print len(allhandles)
            if len(allhandles)<=1:#模态窗口需要获取2次window_handles才能得到，selenium的bug
                print "Only one window or less. Retry."
                allhandles = cls.driver.window_handles
            else:
                for handle in allhandles :
                    if handle != nowhandle:
                        cls.driver.switch_to_window(handle)
                        if cls.driver.title !='':
                            print "Now in <" + cls.driver.title + "> page."
                        else:
                            print "Now in function page."
                break
            
    @classmethod        
    def switch_to(cls,handle):
        cls.driver.switch_to_window(handle)
        #print "Now in <" + cls.driver.title + "> page."

    @classmethod 
    def window_get(cls):
        """在登录后可执行这句，获取窗口"""
        window = cls.driver.current_window_handle
        return window
    @classmethod
    def window_close(cls):
        cls.driver.close()
