# -*- coding: utf-8 -*-
'''
Created on 2014年12月28日
@author: zhh
'''
import os
from selenium.selenium import selenium
class tools(object):
    @staticmethod
    def test_moduleName_get(path):
        names=[]
        testModules=os.listdir(path)
        for module in testModules:
            s=module.split('.',-1)[-1]
            if s=='py' and module[:2]=='AT':
                names.append(module.split('.',-1)[0])
        names.sort()
        print "---tests list:---"
        for name in names:
            print name
        print "================="
        return names
    
if __name__=='__main__':
    pass