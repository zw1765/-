#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 21:09:39 2021

@author: zw
"""

import scrapy.cmdline
scrapy.cmdline.execute('scrapy crawl mydangdang --nolog -o ./data/tata.csv'.split())