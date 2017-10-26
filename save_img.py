#coding:GBK
import os
import urllib2
import sys
reload(sys)
sys.setdefaultencoding('GBK')

def save(path,name,url):
    path_i = path + '\\' + str(name) + '.jpg'
    exists = os.path.exists(path_i)
    if not exists:
        req = urllib2.Request(url)
        req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36')
        req.add_header('GET',url)

        resp = urllib2.urlopen(req, timeout=20)
        data_img = resp.read()
        fp = open(path_i,"wb")
        fp.write(data_img)
        fp.close()
        print 'Saved img ',name,':',url
    else:
        print 'File',str(name),'already exists'
