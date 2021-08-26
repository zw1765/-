#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 14:57:17 2021

@author: zw
"""

import pandas as pd
import requests
from lxml import etree

# 模拟浏览器: 让服务器认为我是在用浏览器访问他的数据
headers = {
    '''User-Agent''': '''Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0'''
}


def get_house(page=1):
    url = f'https://sz.lianjia.com/ershoufang/pg{page}/'
    req=requests.get(url,headers=headers)

    myhtml=etree.HTML(req.text)
    
    title=myhtml.xpath('/html/body/div[4]/div[1]/ul/li/div[1]/div[1]/a/text()')
    
    positionInfo=myhtml.xpath('//*[@data-el="region"]/text()')
    priceInfo_list=(myhtml.xpath('//*[@class="priceInfo"]'))
    Total_price=[]
    Unit_price=[]
    for proice in  priceInfo_list:
        number1=proice.xpath('./div[1]/span/text()')
        number2=proice.xpath('./div[2]/span/text()')
        Total_price.append(number1)
        Unit_price.append(number2)
    dictinfo={
        'title':title,
        'positionInfo':positionInfo,
        'Total_price/万元':Total_price,
        'Unit_price':Unit_price
        }
    return dictinfo

def Save_csv(data,name):
    df=pd.DataFrame.from_dict(data)
    df.to_csv(f'./data/{name}.txt')
    
        
# 标题  小区  总价  单价   存储到txt文件中
def main():
    data=get_house()
    
    Save_csv(data, 'fist')
    
    

if __name__ == '__main__':
    main()
