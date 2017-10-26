#coding:UTF-8
import urllib2
from bs4 import BeautifulSoup

#获取图片url
def pic_url(url):
    request = urllib2.Request(url)
    request.add_header('User-Agent','Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6')
    opener = urllib2.build_opener()
    f= opener.open(request)
    html = f.read()
    soup = BeautifulSoup(html,'lxml')
    soup_texts = soup.find('section',class_="entry-content")
    #获取图片rul
    #pic_num = []
    pic_num_url = []
    for link in soup_texts.descendants:
        if link != '\n':
            try:
                img_url = link.get('src')
                #print img_url 图片地址测试
                if img_url != None:
                    pic_num_url.append(img_url)
            except:
                None
    pic_num = range(1,len(pic_num_url)+1)
    dic_pic_num = dict(zip(pic_num,pic_num_url))
    print "Total pages :",pic_num[-1]
    return dic_pic_num

#测试
#url = 'http://oreno-erohon.com/?p=55525'
#i = pic_url(url)
#print i