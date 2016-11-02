# -*- coding: utf-8 -*-
'''
Created on 2014年12月23日
@author: zhh
'''
from selenium.webdriver.ie.webdriver import WebDriver as WebDriverIE
from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
import time
from base.mainProcessPage import MainProcessPage
from baseUtil.windows import Window

'''视频录入页，主窗口'''


class VideoCreatePage(MainProcessPage):
    def encoder_select(self, value="H264"):
        '''视频编码参数'''
        # self.driver.find_element_by_id("videoEncoderSelect").find_element_by_xpath('''//option[@value="''' + value + '''"]''').click()
        self.select_choose("encodeCode", value)

    def priority_select(self, value="7"):
        '''视频优先级'''
        # self.driver.find_element_by_xpath('''//select[@name="videoItem.priority"]/option[@value="''' + value + '''"]''').click()
        self.select_choose("videoItem.priority", value)

    def duration_set(self, value="123"):
        '''时长'''
        # self.driver.find_element_by_xpath("""//input[@name="videoItem.duration"]""").send_keys(value)
        self.input_text("videoItem.duration", value)

    def videoname_set(self, value="autoTest"):
        '''视频名称'''
        # self.driver.find_element_by_xpath("""//input[@name="videoItem.fileName"]""").send_keys(value)
        self.input_text("videoItem.fileName", value)

    def contentBusinessType_set(self, value="IPTV"):
        '''视频标签'''
        # self.driver.find_element_by_xpath("""//input[@name="videoItem.contentBusinessType"]""").send_keys(value)
        self.input_text("videoItem.contentBusinessType", value)

    '''其他属性TODO'''

    def chooseFileImg_click(self):
        '''上传图标点击'''
        self.reset_frame()
        self.driver.find_element_by_xpath('''//div[@id="chooseFile"]//img''').click()

    #     def saveBtn_click(self):
    #         '''保存按钮点击'''
    #         self.reset_frame()
    #         #self.driver.find_element_by_xpath("""//input[@class="btn2" and @onclick="javascript:submitForm('checkFile');"]""").click()
    #         self.button_click("保存")
    # #         alert = self.driver.switch_to_alert()
    # #         alert.accept()
    #     def completeBtn_click(self):
    #         #self.driver.find_element_by_xpath("""//input[@class="btn2" and @onclick="javascript:doReturn();"]""").click()
    #         self.button_click("完成")
    #     def cancelBtn_click(self):
    #         self.button_click("取消")
    '''TODO'''


'''视频录入页弹出文件选择页，弹出窗口'''


class FileSelectPage:
    def __init__(self, WebDriverIE):
        self.driver = WebDriverIE

    def choose_file(self, cp="30000001", filename="autoTest.ts"):
        ''''录入页面选择文件弹出页操作，执行前后要调用切换窗口'''
        double = self.driver.find_element_by_xpath("""//span[text()='""" + cp + """']""")
        # 对定位到的元素执行鼠标双击操作
        ActionChains(self.driver).double_click(double).perform()
        time.sleep(2)
        self.driver.switch_to_default_content()
        self.driver.find_element_by_xpath("""//span[text()='public']""").click()  # 默认public，这里不高兴再加参数化了
        self.driver.switch_to_default_content()
        self.driver.switch_to_frame(self.driver.find_elements_by_tag_name("iframe")[0])
        # driver.switch_to_frame("monitor") #貌似也支持id定位frame
        double = self.driver.find_element_by_xpath('''//div[@id="''' + filename + '''"]''')
        ActionChains(self.driver).double_click(double).perform()


'''视频加工页，主窗口'''


class VideoEditPage(MainProcessPage):
    def video_choose(self, videoName):
        self.checkbox_click(videoName)


'''打点拆条和编码页，弹出窗口'''


class DotSplitAndEncodePage(MainProcessPage):
    def __init__(self, WebDriverIE):
        self.driver = WebDriverIE

    def reset_frame(self):
        self.driver.switch_to_default_content()

    def close(self):
        """弹出窗口，增加close方法"""
        self.driver.close()

    '''打点拆条页功能方法'''

    def inDot_set(self, value):
        '''入点'''
        #         self.driver.find_element_by_xpath('''//*[@id="beginTimeInputBox"]''').click()
        #         self.driver.find_element_by_xpath('''//input[@id="beginTimeInputBox"]''').send_keys(value)
        self.input_text("beginTimeInputBox", value)  # 以前研发把标签name属性写反了，这里用id查找，name会定位错误

    def outDot_set(self, value):
        '''出点'''
        self.input_text("endTimeInputBox", value)

    def splitTile_set(self, value):
        self.input_text("title", value)

    def splitTag_set(self, value):
        self.input_text("tag", value)

    def newVideo_create(self, newItemName, splitNum="1"):
        '''根据传入编号的拆条生成视频'''
        # 拆条的checkbox特殊，不用checkbox_click方法
        self.driver.find_element_by_xpath(
            '''//div[text()="''' + splitNum + '''"]/../preceding-sibling::td/div/input[@type="checkbox"]''').click()
        # self.checkbox_click("yui-dt-checkbox")#默认选第一个拆条
        self.button_click("生成视频")
        self.input_text("newItemName", newItemName)
        self.driver.find_element_by_id("dialog1submitbutton-button").click()

    '''编码页功能方法'''

    def encode_mission_name(self, value):
        self.input_text("encoderTaskDeitil.name", value)

    def priority_select(self, value):
        self.select_choose("encoderTaskDeitil.priority", value)

    def paramCode_select(self, value):  # 页面切换一下编码参数时会刷新，需要重新定位窗口
        nowhandle = Window.window_get()  # 获取编码窗口
        self.select_choose("encodeParamCode", value)
        Window.switch_to(nowhandle)  # 再定位至编码窗口


class VideoFirstAuditPage(MainProcessPage):
    def video_choose(self, videoName):
        self.checkbox_click(videoName)

    #     def auditPass_and_createContent(self,contentType="无"):
    #         mainwindow=Window.window_get()
    #         self.button_click("认领并审核通过")
    #         Window.switch_from(mainwindow)
    #         self.select_choose("contentType", contentType)
    #         self.button_click("确定")
    def create_contentType_chose(self, contentType="无"):
        self.select_choose("contentType", contentType)
