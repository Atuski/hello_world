# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 15:12:47 2018

@author: sheng
"""
from urllib import request
import chardet
res = request.urlopen("https://fishc.com.cn")
html = res.read()
encode = chardet.detect(html)['encoding']
print(encode)
html = html.decode("gbk")
with open("crawler1.html",'w') as f:
    f.write(html)
