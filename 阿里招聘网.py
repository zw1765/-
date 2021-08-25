#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 16:42:32 2021

@author: zw
"""

import pandas as pd
import urllib
import requests


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
                'workLocation_list':workLocation_list,
                }
    
    return dict1

def Save_data(data,savename):
    df=pd.DataFrame(data)
    df.to_csv(f'./data/{savename}-post.csv')

def main():
    name=input("input post:")
    n=int(input('Enter the number of pages:'))
    data=get_data(name,n)
    Save_data(data,name)

if __name__=='__main__':
    main()
    

