#coding:UTF-8
import urllib2
from bs4 import BeautifulSoup

#获取所有页面列表
def get_pagelist(url):
    request = urllib2.Request(url)
    request.add_header('User-Agent','Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6')
    opener = urllib2.build_opener()
    f= opener.open(request)
    html = f.read()
    soup = BeautifulSoup(html,'lxml')
    page_list = soup.find('div',class_='wp-pagenavi')
    page_next = page_list.find('a',class_='nextpostslink')
    try:
        page_next_url = page_next.get('href')
        return page_next_url
    except:
        return None