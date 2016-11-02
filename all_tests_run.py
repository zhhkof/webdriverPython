# -*- coding: utf-8 -*-
'''
Created on 2014年12月28日

@author: zhh
'''
import unittest,sys,shutil,os
from datetime import datetime
from baseUtil.tools import tools
moduleNameList=tools.test_moduleName_get("test_cases")
sys.path.append("test_cases")
modulesList=[]
for moduleName in moduleNameList:
    __import__(moduleName)
    modulesList.append(sys.modules[moduleName])
# from test_cases import AT001_videoCreate
# from test_cases import AT002_videoEdit

testunit=unittest.TestSuite()

#方法一：caseModuleList导入module，遍历module并提取testMethod
# caseModuleList=[AT001_videoCreate]

#方法二：通过unittest.defaultTestLoader.discover找到所有匹配的测试modules
#discover返回类型是modules，并已经封装成了suite，不是py里的测试class.
#但坑爹的是，这个方法只会对单个class里的method排序，无法根据class排序,以后有空再研究吧，扫全目录确实很方便
#caseList=unittest.defaultTestLoader.discover('test_cases', pattern='AT*.py', top_level_dir=None)

#可能有一个module的类下有多个testMethod的情况，2层循环，先获得module对应的tests，在遍历得到test
for module in modulesList:
    test_suite=unittest.defaultTestLoader.loadTestsFromModule(module)
    for test_case in test_suite:
        testunit.addTest(test_case)


if __name__ == '__main__':
    nowtime = datetime.now().strftime('%Y%m%d%H%M%S')
    if os.path.exists("d:/img/test"):
        shutil.rmtree("d:/img/test")
    os.makedirs("d:/img/test")
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(testunit)
    shutil.move("d:/img/test", "d:/img/"+nowtime)