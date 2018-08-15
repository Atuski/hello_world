#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 21:55:32 2018

@author: shengyeqing
"""
import re
import bs4
import requests
import openpyxl
def open_url(url):
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
    res = requests.get(url,headers=headers)
    return res
def find_date(res):
    date = []
    soup = bs4.BeautifulSoup(res.text,"html.parser")
    content = soup.find(id="Cnt-Main-Article-QQ")
    target = content.find_all('p',style="TEXT-INDENT: 2em")
    target = iter(target)
    for each in target:
        if each.text.isnumeric():
            date.append([
            re.search(r'\[(.+)\]',next(target).text).group(1),
            re.search(r'\d.*',next(target).text).group(),
            re.search(r'\d.*',next(target).text).group(),
            re.search(r'\d.*',next(target).text).group()])
    return date
def save_excel(date):
    wb = openpyxl.Workbook()
    wb.guess_types = True
    ws = wb.active
    ws.append(['城市','平均房价','平均工资','房价工资比'])
    for each in date:
        ws.append(each)
    wb.save('2017全国城市房价工资排行榜.xlsx')
def main():
    url = 'http://news.house.qq.com/a/20170702/003985.htm'
    res = open_url(url)
    date = find_date(res)
    save_excel(date)
if __name__=='__main__':
    main()
