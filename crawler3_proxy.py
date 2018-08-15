# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 17:39:18 2018

@author: sheng
"""
import random
import urllib.request
url = 'https://www.baidu.com'
iplist = ['103.204.210.112:8080','111.203.133.96:80','142.93.68.156:3128','46.39.252.172:8080']
proxy = urllib.request.ProxyHandler({'https':random.choice(iplist)})
opener = urllib.request.build_opener(proxy)
opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36')]
urllib.request.install_opener(opener)
response = urllib.request.urlopen(url)
html = response.read().decode("utf-8")
print(html)
