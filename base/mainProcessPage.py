# -*- coding: utf-8 -*-
'''
Created on 2014年12月23日
@author: zhh
'''

from selenium.webdriver.ie.webdriver import WebDriver as WebDriverIE
#from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from base.event_firing_webdriver2 import EventFiringWebDriver
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
import time
from base.webdriverExceptionUtil import WebDriverExceptionListener

class MainPage(object):
    def __init__(self):
        #self.main_leftmenuframe = self.driver.find_element_by_xpath("//frame[@name='main_leftmenuframe']")
        #self.main_tabframe = self.driver.find_element_by_xpath("//frame[@name='main_tabframe']")
        """TODO"""
    def refresh_main_page(self):
        if self.driver is not None:
            self.driver.refresh()
        else:
            print "No webdriver"
    def login(self,browser,url,user,passwd):
        '''init and return driver'''
        if browser=="ie":
            dr = webdriver.Ie("e:/driver/IEDriverServer.exe")
        elif browser=="chrome":
            dr = webdriver.Chrome("../driver/chromedriver")
        else:
            return #先不写其他的
        #此处driver为何不兼容
        
        self.driver=EventFiringWebDriver(dr,WebDriverExceptionListener())
        self.driver.implicitly_wait(2)
        try:
            self.driver.get(url)
            self.driver.set_window_size(1440,800)
            #self.driver.maximize_window()
            #print type(self.driver.find_element_by_name("loginName"))
            self.driver.find_element_by_name("loginName").send_keys(user)
            self.driver.find_element_by_name("password").send_keys(passwd)
            self.driver.find_element_by_xpath("""//a[@href="javascript:submitForm('login')"]""").click()
            self.icms3_check()
            return self.driver
        except Exception:
            self.driver.quit()
    
    def icms3_check(self):
        for i in range(5): 
            if self.driver.title == u"思华科技统一内容管理系统":
                print "Now in <" + self.driver.title + "> main page."
                break
            else:
                if i == 4:
                    print "time out, not in correct page.."
                    self.driver.quit()
                time.sleep(1)
    def is_driver_exist(self):
        '''TODO'''
        pass

class MainProcessPage():
    '''
    面向主页上的主流程功能页继承(录入、加工、初审、编目、终审、发布)，各种弹出页建议重写。
    '''
    def __init__(self, driver):
        self.driver = driver
        self.driver.switch_to_default_content()
        self.main_leftmenuframe = self.driver.find_element_by_xpath("//frame[@name='main_leftmenuframe']")
        self.main_tabframe = self.driver.find_element_by_xpath("//frame[@name='main_tabframe']")
    def reset_frame(self):
        if self.driver.title == u"思华科技统一内容管理系统":
            self.driver.switch_to_default_content()
            self.driver.switch_to_frame(self.main_tabframe)
            self.driver.switch_to_frame("mainFrame")
        else:
            self.driver.switch_to_default_content()
    def go_to_page(self,pagename):
        '''pagename in main_leftmenuframe，即左侧栏的按钮'''
        self.driver.switch_to_default_content()
        self.driver.switch_to_frame(self.main_leftmenuframe)
        self.driver.find_element_by_link_text(pagename).click()
        self.reset_frame()    
    
    #输入方法
    def input_text(self,inputName,value):
        '''input标签输入框输入，需传入input标签的name属性或者id'''
        try:
            self.driver.find_element_by_xpath('''//input[@name="'''+inputName+'''"]''').clear()
            self.driver.find_element_by_xpath('''//input[@name="'''+inputName+'''"]''').send_keys(value)
        except NoSuchElementException:
            self.driver.find_element_by_xpath('''//input[@id="'''+inputName+'''"]''').clear()
            self.driver.find_element_by_xpath('''//input[@id="'''+inputName+'''"]''').send_keys(value)
    def input(self,key,value):
        '''传入input的上一个兄弟节点的text来定位，适用于常规页面'''
        self.reset_frame()
        self.driver.find_element_by_xpath('''//td[contains(text(),"'''+key+'''")]/following-sibling::td//input''').send_keys(value)
    
    #按钮点击
    def button_click(self,value,op='accept'):
        self.reset_frame()
        '''input,button,a链接标签按钮点击,默认确认弹出框'''
        self.driver.find_element_by_xpath('''(//input[@value="'''+value+'''"])|(//button[text()="'''+value+'''"])|(//a[text()="'''+value+'''"])''').click()
        try:
            self.do_alert(op)
        except Exception:
            pass
    #弹出框处理
    def do_alert(self,op):
        alert = self.driver.switch_to_alert()
        if op=='accept':
            alert.accept()
        elif op=='dismiss':
            alert.dismiss()
        else:
            '''TODO'''
            pass
    
    #下拉框选择
    def select_choose(self,selectName,value):
        '''select标签选择，需传入select标签的name属性'''
        self.driver.find_element_by_xpath('''//select[@name="'''+selectName+'''"]/option[text()="''' + value + '''" or @value="''' + value + '''"]''').click()
    def select(self,key,value,*args):
        self.reset_frame()
        '''传入select的上一个兄弟节点的text来定位，适用于常规页面'''
        if len(args)==0:
            self.driver.find_element_by_xpath('''//td[contains(text(),"'''+key+'''")]/following-sibling::td//select/option[text()="''' + value + '''" or @value="''' + value + '''"]''').click()
        elif args[0]=='loop':
            elements=self.driver.find_elements_by_xpath('''//td[contains(text(),"'''+key+'''")]/following-sibling::td//select/option[text()="''' + value + '''" or @value="''' + value + '''"]''')
            for ele in elements:
                ele.click()
        else:
            self.driver.find_element_by_xpath('''//td[contains(text(),"'''+key+'''")]/following-sibling::td//select[@name="'''+args[0]+'''"]/option[text()="''' + value + '''" or @value="''' + value + '''"]''').click()
    
    #勾选框选择方法
    def checkbox_click(self,value=""):
        try:
            self.driver.find_element_by_xpath('''//a[@href and text()="'''+value+'''"]/../preceding-sibling::td/input[@type="checkbox"]''').click()
        except NoSuchElementException:
            self.driver.find_element_by_xpath('''//a[@href and contains(text(),"'''+value+'''")]/../preceding-sibling::td/input[@type="checkbox"]''').click()
    
    #页面根据内容名称和id查询方法
    def search(self,videoName,assetId="",retryTimes=12,waitSeconds=5):
        """适用于大部分查询页面"""
        #self.driver.find_element_by_xpath("""//input[@name="mingcheng"]""").send_keys(videoName)
        self.input_text("mingcheng", videoName)
        if assetId!="":
            #self.driver.find_element_by_xpath("""//input[@name="assetId"]""").send_keys(assetId)
            self.input_text("assetId", assetId)
        for i in range(retryTimes):
            try:
                #driver.find_element_by_xpath("""//button[text()='"""+'查询'.decode("utf-8")+"""']""").click() #也可以根据text()定位
                self.button_click("查询")
                try:
                    self.element=self.driver.find_element_by_xpath("""//a[@href and text()='"""+videoName+"""']""")
                    print "Item found in list."
                    break
                except NoSuchElementException:
                    self.element=self.driver.find_element_by_xpath("""//a[@href and contains(text(),'"""+videoName+"""')]""")
                    print "ItemName match in list."
                    break
            except NoSuchElementException:
                if i==11:
                    print "time out, break."
                else:
                    print "No found, maybe in process, retry after 5 seconds."
                    time.sleep(waitSeconds-1)

        