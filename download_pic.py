#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 13:29:17 2018

@author: shengyeqing
"""
import urllib
import os,random
import re
from multiprocessing import Pool,Manager
import functools
#输入值为网页的链接，获得网页
def get_html(url):
    user_agentList = ["Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
                  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
                  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
                  "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
                  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)"
                  ]

    h = {
            'User-Agen':random.choice(user_agentList)
            }
    req = urllib.request.Request(url,headers = h)
    html = urllib.request.urlopen(req).read()
    return html
#输入为获得的页面，获得图片所在页面链接所构成的子串，并作为迭代器返回
def get_url(html):
    pat1= r'href="(http://www.meizitu.com/a(/|//)\d+?.html)"'
    page_list = re.finditer(pat1,html)
    return page_list
#输入为图片所在的网页链接，获得图片网址，并保存图片到文件夹
def get_img(url):
    page_html = get_html(url).decode('gbk')#从迭代器中取得的网址打开并获取页面
    pat2= r'src="(http://mm.chinasareview.com/wp-content/.+?\d{2}\.jpg)"'#获得图片地址 正则
    url_list = re.findall(pat2,page_html)
    #将图片保存
    for url in url_list:
        print(url)
        filename = url.split('/')[-4]+url.split('/')[-3]+url.split('/')[-2]+url.split('/')[-1]
        img = get_html(url)
        with open(filename,'wb') as f:
            f.write(img)
        
#主函数，下载meizutu.com 上面的图片
def downloadmeizi(lock,url):
    #保存图片到当前文件夹miezitu
   
    html = get_html(url).decode('gbk')#获得网页
    page_list = get_url(html)#获得图片所在页面链接
    for page in page_list:
        page_url = page.group(1)
        get_img(page_url)#获得图片网址
        
    pass
if __name__ == '__main__':
    '''
    for i in range(1,11):
        url = 'http://www.meizitu.com/a/more_%s.html' %i
        downloadmeizi(url)
    '''
    manager = Manager()
    lock = manager.Lock()
    pdownloadmeizi = functools.partial(downloadmeizi, lock)

    pool = Pool()
    pool.map(pdownloadmeizi, ['http://www.meizitu.com/a/more_%s.html' %i for i in range(1,11)])# 分配给进程池任务序列
    pool.close()
    pool.join()
    
    
    







