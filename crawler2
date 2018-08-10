# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 15:24:05 2018

@author: sheng
"""
import urllib.request
import urllib.parse
import json
def translate(content):
    url = "http://fanyi.youdao.com/translate"
    head={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
            }
    date = {'i':content,
    'from':'AUTO',
    'to':'AUTO',
    'smartresult':'dict',
    'client':'fanyideskweb',
    'salt':'1533803421680',
    'sign':'6158e39cd62f848942480d7fc8a8941a',
    'doctype':'json',
    'version':'2.1',
    'keyfrom':'fanyi.web',
    'action':'FY_BY_CLICKBUTTION',
    'typoResult':'false'}
    date = urllib.parse.urlencode(date).encode('utf-8')
    response = urllib.request.urlopen(url,date)
    html = response.read().decode('utf-8')
    target = json.loads(html)['translateResult'][0][0]['tgt']
    return target
print(translate('我是帅哥'))
