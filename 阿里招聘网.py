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
    
    
        
    id_list=[]
    name_list=[]
    workExperience_list=[]
    degree_list=[]
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
        
    
        
        
        for job in data:
            id_list.append(job['id'])
            name_list.append(job['name'])
            workExperience_list.append(job['workExperience'])
            degree_list.append(job['degree'])
            workLocation_list.append(job['workLocation'])
           
    dict1={'id':id_list,
                'name':name_list,
                'workExperience':workExperience_list,
                'degree':degree_list,
                'workLocation':workLocation_list,
                }
    
    return dict1

def Save_data(data,savename):
    df=pd.DataFrame(data)
    df.to_csv(f'./data/{savename}-post.csv')

def Save_data_sql(data,name):
    
    df=pd.DataFrame(data)
    db=pymysql.connect(host='localhost',
                       user='root',
                       password='Uplooking_123',
                       port=3306,
                       db='spiders',
                       charset='utf8')
    
    cursor=db.cursor()
    cursor.execute(f'drop table if exists {name}_post')
    
    sql=f'''create table {name}_post(
    id int auto_increment primary key not null,
    name varchar(256) not null,
    workExperience varchar(256) not null,
    degree varchar(256) not null,
    workLocation varchar(256) not null
   )'''
    
    cursor.execute(sql)
    db.commit()
    
    
    with db.cursor() as cur:
        for i in range(len(df)):
            ds=df.iloc[i].values
            cur.execute(f'''
                        insert into {name}_post(id, name, workExperience, degree, workLocation )  
                        values({ds[0]},'{ds[1]}',
                                '{ds[2]}','{ds[3]}','{ds[4]}')
                        ''')
            db.commit()
            
    

# =============================================================================
#     list2=df.iloc[3].values
#     
#     print(f'{list2[0]},{list2[1]}') 
#     
#     db.close()
#     
# =============================================================================
def main():
    name=input("input post:")
    n=int(input('Enter the number of pages:'))
    data=get_data(name,n)
    Save_data(data,name)
    Save_data_sql(data,name)
if __name__=='__main__':
    main()
    

