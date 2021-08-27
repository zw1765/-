#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 19:30:55 2021

@author: zw
"""

import scrapy.cmdline
scrapy.cmdline.execute("scrapy crawl mylianjia --nolog -o ./data/data.csv".split())