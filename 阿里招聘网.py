#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 16:42:32 2021

@author: zw
"""

import pandas as pd
import urllib
import requests
import pymysql

def get_data(name,n):

    
    keywd=urllib.request.quote(name)
    
    url='''https://job.alibaba.com/zhaopin/socialPositionList/doList.json'''
    
    
        
    name_list=[]
    degree_list=[]
    requirement_list=[]
    departmentName_list=[]
    firstCategory_list=[]
    workExperience_list=[]
    workLocation_list=[]
    
    for j in range(1,n+1):
        payload = {
                "pageSize": 10,
                "t": 0.20076864226884727,
                'keyWord':keywd,
                "pageIndex": j
            }
        r = requests.post(url,data=payload) 
        
        data=r.json()['returnValue']['datas']
        
    
        
        
        for i in data:
            name_list.append(i['name'])
            degree_list.append(i['degree'])
            requirement_list.append(i['requirement'])
            departmentName_list.append(i['departmentName'])
            firstCategory_list.append(i['firstCategory'])
            workExperience_list.append(i['workExperience'])
            workLocation_list.append(i['workLocation'])
            
    dict1={'name':name_list,
                'degree':degree_list,
                'departmentName':departmentName_list,
                'firstCategory':firstCategory_list,
                'workExperience':workExperience_list,
                'workLocation':workLocation_list,
                }
    
    return dict1

def Save_data(data,savename):
    df=pd.DataFrame(data)
    df.to_csv(f'./data/{savename}-post.csv')

def Save_data_sql(data,name):
    db = pymysql.connect(host='192.168.19.149' , user='root',
                         password='Uplooking_123' , port=3306 , db='spiders' , charset='utf8')
    cursor = db.cursor()
    cursor.execute(f'drop table if exists {name}_db')
    df=pd.DataFrame(data)
    
    sql1 = f'''create table {name}_db(id int auto_increment primary key not null,
                            name varchar(256) ,
                            degree varchar(256),
                            departmentName varchar(256),
                            firstCategory varchar(256),
                            workExperience varchar(256),
                            workLocation  varchar(256),
                            )'''
    cursor.execute(sql1)
    for dt in range(len(df)):
        data1=df.iloc[dt].values
        sql2 = f'insert into {name}_db values(%d,%s,%s,%s,%s,%s,%s)'
        try:
            cursor.execute(sql2,(data1[0],data1[1],data1[2],data1[3],data1[4],data1[5],data1[6]))
            db.commit()
            
        
        except:
            print("插入失败")
            db.rollback()

    
def main():
    name=input("input post:")
    n=int(input('Enter the number of pages:'))
    data=get_data(name,n)
    Save_data(data,name)
    Save_data_sql(data,name)
if __name__=='__main__':
    main()
    

