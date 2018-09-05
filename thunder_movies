import urllib.request
import ssl
import re

ssl._create_default_https_context = ssl._create_unverified_context 

def open_url(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4843.400 QQBrowser/9.7.13021.400')
    page = urllib.request.urlopen(req)
    html = page.read().decode('utf-8')

    return html

def get_img(html):
    p = r'<a href="/movie/\d{5}" title="([^"]*分)"'
    movies = re.findall(p, html)
    q = r'<a href="/movie/(\d{5})" title="'
    nums = re.findall(q, html)  
    f = 0
    for each in range(len(nums)):
        http = 'https://www.80s.tw/movie/'+nums[each]
        content = open_url(http)
        g = r'<a rel="nofollow" href="([^"]*)" thunderrestitle='
        links = re.findall(g, content)
        if float(re.findall(r'\d\.\d', movies[each])[0]) > 6:
            f += 1
        print(movies[each],links[0])

    print('\n其中大于6分的有%d部'%f)

if __name__=="__main__":
    for i in range(1,11):
        print("\n第%d页"%i)
        url = ('https://www.80s.tw/movie/list/-----p%d'% i)
        get_img(open_url(url))
