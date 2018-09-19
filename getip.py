[code]import urllib.request
from bs4 import BeautifulSoup
import re
#获取IP地址
def find_ip(str1):
    comp = re.compile(r'(([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-4])\.){3}([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])')
    ip = re.search(comp,str1)
    return ip
#获取端口号
def find_port(str1):
    comp = re.compile(r'<td>(([0-9]{0,1}){0,5})</td>')
    port = re.search(comp,str1)
    return port
#获取国家
def find_country(str1):
    comp = re.compile(r'(((<td.{*}</td>){0,3})(<td>.*</td>))',re.DOTALL)
    country = re.search(comp,str1)
    return country
#获取类型
def find_http(str1):
    comp = re.compile(r'<td>(([A-Z]){4,5})</td>')
    http = re.search(comp,str1)
    return http

url = 'http://www.xicidaili.com/'

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

req = urllib.request.Request(url=url,headers=headers)

html = urllib.request.urlopen(req)

soup = BeautifulSoup(html,'html.parser')

for each in soup.find_all('tr'):
    ip = str(each).split('</tr>')
    for x in ip:
        if '\n' in x:
            pass
        try:
            chinese = re.sub(r'[<td/\\>a-zA-Z]','',str(find_country(x)).split(r'\n')[-1])
            print(find_ip(x).group(),':',find_port(x).group(1),'--->',find_http(x).group(1),chinese)
        except TypeError and AttributeError:
            pass
