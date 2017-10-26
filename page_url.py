# -*- coding:utf-8 -*-
import urllib2
from bs4 import BeautifulSoup

import json
# print json.dumps(dict, encoding="UTF-8", ensure_ascii=False)这是转换文字编码的例子

#获取漫画url
def page_url(url):
    request_all = urllib2.Request(url)
    request_all.add_header('User-Agent','Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6')
    opener_all = urllib2.build_opener()
    web_all = opener_all.open(request_all)
    html_all = web_all.read()
    soup_all = BeautifulSoup(html_all,'lxml')
    soup_all_texts = soup_all.find('div',id='main')
    soup_page_texts = soup_all_texts.find_all('div',class_='article-body-inner')
    dic_cim_url={}
    l_n = []
    l_u = []
    for link_C in soup_page_texts:
        try:
            C_name = link_C.a.get('title')
            C_url = link_C.a.get('href')
            #print C_name, ':', C_url
            l_n.append(C_name)
            l_u.append(C_url)
        except:
            print "Error!!!"
    dic_cim_url=dict(zip(l_n,l_u))
    #print dic_cim_url
    return dic_cim_url

#测试获取每页url
#i = page_url('http://oreno-erohon.com/?paged=57')
#print i