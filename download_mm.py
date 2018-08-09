# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 18:04:40 2018

@author: sheng
"""
from urllib import request
import os
#输入为网址，输出为获取的html
def url_open(url):
    req = request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36')
    response = request.urlopen(req)
    html = response.read()
    return html
#输入网址，获取该页面的所在页数
def get_page(url):
    html = url_open(url)
    html = html.decode('utf-8')
    a = html.find('current-comment-page')+23#利用find函数，通过字符查找来实现获得当前页面数
    b = html.find(']',a) 
    return html[a:b]
#输入所在页数的网址，获得img的保存地址
def find_imgs(url):
    html = url_open(url).decode('utf-8')
    img_addrs = []
    a = html.find('img src=')
    while a != -1:
        b = html.find('.jpg',a,a+255)
        if b != -1:
            img_addrs.append(html[a+9:b+4])
        else:
            b = a + 9
        a = html.find('img src=',b)
    for each in img_addrs:
        print(each)
    return img_addrs

#输入img的地址，保存img
def save_imgs(img_addrs):
    for each in img_addrs:
        img_name = each.split('/')[-1]
        html = url_open(each)
        with open(img_name,'wb') as f:
            f.write(html)
#煎蛋的网址，主函数需实现获得前十页图片
def download(folder='ooxx',pages=10):
    os.mkdir(folder)
    os.chdir(folder)
    url = "http://jandan.net/ooxx"
    page_num = int(get_page(url))#最新页面数
    #获得前十页的地址
    for i in range(pages):
        page_num -= 1
        page_url = url + '/page-' + str(page_num) + '#comment'
        img_addrs = find_imgs(page_url)
        save_imgs(img_addrs)
        print(page_url)

if __name__=="__main__":
    download()
