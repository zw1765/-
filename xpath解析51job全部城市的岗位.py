#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 18:39:34 2021

@author: zw
"""
# 爬取51job全部城市岗位，并分别保存到单独的以城市名为文件名的html中，如: 深圳.html
# url = "https://jobs.51job.com/"

import requests
from lxml import etree
import pandas as pd

headers = {
    '''User-Agent''': '''Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0'''
}

# 获取所有城市
def get_citys(url):
    # 获取网页数据
    response = requests.get(url, headers=headers)
    content = response.content.decode('utf-8')
    myhtml=etree.HTML(content)
    
    print(content)
    hcity_name=myhtml.xpath('/html/body/div[3]/div[1]/div[2]/div[1]/a[7]/text()')
    hcity_url=myhtml.xpath('/html/body/div[3]/div[1]/div[2]/div[1]/a[7]/@href')
    
    
    print(hcity_name)
    print(hcity_url)
    hcity_info=dict(zip(hcity_name,hcity_url))
    print(hcity_info)
    return hcity_info
    

# 获取每个城市的岗位信息
def get_job(data):
    
    
    for hcity_name,hcity_url in data.items():

        response = requests.get(hcity_url, headers=headers)
        content = response.content.decode('utf-8')
        myhtml=etree.HTML(content)
        
        job_name=myhtml.xpath('/html/body/div[4]/div[2]/div[1]/div[2]/div/p[1]/span[1]/a/@title')
        company_name=myhtml.xpath('/html/body/div[4]/div[2]/div[1]/div[2]/div/p[1]/a/@title')
        place=myhtml.xpath('/html/body/div[4]/div[2]/div[1]/div[2]/div/p[1]/span[2]/text()')
        wages=myhtml.xpath('/html/body/div[4]/div[2]/div[1]/div[2]/div/p[1]/span[3]/text()')
        
        dict_job={'job_name':job_name,
                  'company_name':company_name,
                  'place':place,
                  'wages':wages
            }
        df=pd.DataFrame(dict_job)
        df.to_html(f'./data{hcity_name}_job.html')
        
    
def save_data(data,name):
    pass

if __name__ == '__main__':
    url = "https://jobs.51job.com/"
    hcity_info=get_citys(url)
    get_job(hcity_info)
    

