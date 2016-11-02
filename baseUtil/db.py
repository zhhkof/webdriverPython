# -*- coding: utf-8 -*-
'''
Created on 2014年12月23日
@author: zhh
'''
import cx_Oracle

user='cq3q01'
passwd='cq3q01'
dsn_tns = cx_Oracle.makedsn('192.168.88.186', 1521, 'ora10g')#创建dsn_tns来链接，便于后面参数化
class DB:
#    def __init__(self):
        #db = cx_Oracle.connect('hr', 'hrpwd', 'localhost:1521/XE')#分开写
        #db = cx_Oracle.connect('hr/hrpwd@localhost:1521/XE')#连起来写
        
    @staticmethod
    def rows_exist(tableName,condition="1=1"):
        '''建议配合断言assert使用
        查询有结果只返回一条记录，返回值类型元组，无记录则返回False，配置assert抛出异常。
        tableName:表名称
        condition:sql中where后面的条件。注意，有中文的话需要unicode转码:‘加u前标或decode’
        '''
        sql="select * from "+tableName+" where "+condition
        try:
            db = cx_Oracle.connect(user, user, dsn_tns)
            cr=db.cursor() #创建游标
            cr.execute(sql)
            result=cr.fetchone()
        except Exception,e:
            print e
        finally:
            cr.close()
            db.close()
        if result!=None:
            return result
        else:
            return False
    
    @staticmethod
    def get_element_value(element,tableName,condition="1=1"):
        '''建议配合断言assert使用
        查询单个记录值，返回类型string，无记录则返回False，配置assert抛出异常。
        tableName:表名称
        condition:sql中where后面的条件。注意，有中文的话需要unicode转码:‘加u前标或decode’
        '''
        sql="select "+element+" from "+tableName+" where "+condition
        #print sql
        try:
            db = cx_Oracle.connect(user, user, dsn_tns)
            cr=db.cursor() #创建游标
            cr.execute(sql)
            result=cr.fetchone()
            #print result
        except Exception,e:
            print e
        finally:
            cr.close()
            db.close()
        if result!=None:
            return str(result[0])
        else:
            return False
    
#     def close(self):
#         '''良好的释放连接的习惯'''
#         self.db.close()
#     def commit(self):
#         '''提交，后续可配合使用'''
#         self.db.commit()