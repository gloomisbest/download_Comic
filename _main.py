#coding:UTF-8

import page_url
import pic_url
import get_page_list
import creat_dir_path
import save_img
import os
import datetime

#爬去网站http://oreno-erohon.com/中的所有漫画并保存

start = datetime.datetime.now()

page_all_list = ['http://oreno-erohon.com/']
#生成每页的url列表

while page_all_list[-1]!=None:
    if page_all_list[-1] == 'http://oreno-erohon.com/':
        i = 'http://oreno-erohon.com/?paged=1'
        #i = 'http://oreno-erohon.com/?paged=***'调整开始页
    else:
        i = get_page_list.get_pagelist(page_all_list[-1])
    page_all_list.append(i)
    #print page_all_list

    if i != None:
        #循环获取每页中漫画的url的字典
        page_url_each = i
        print 'Now_url:',page_url_each,'\n'
        d_page_url = page_url.page_url(page_url_each)
        #print d_page_url

        start_C = datetime.datetime.now()
        #获取漫画中所有图片url的字典
        for comic_name in d_page_url:
            comic_url = d_page_url[comic_name]
            try:
                print comic_name,':',comic_url
            except:
                comic_num = comic_url[27:]
                comic_name = comic_num
                print comic_name,':',comic_url
            try:
                dic_pic_url = pic_url.pic_url(comic_url)
                #print dic_pic_url

                #创建文件夹
                img_path = creat_dir_path.create_dir_path(comic_name)
                #print img_path

                #检查是否已经下载完成
                list_test = os.listdir(img_path)
                if len(list_test) >= len(dic_pic_url):
                    print 'File already exists. ==>Skip'
                else:
                    #保存图片
                    for img_name in dic_pic_url:
                        img_url = dic_pic_url[img_name]
                        save_img.save(img_path,img_name,img_url)
                    print 'Finished'
            except:
                print 'Error page.'
        end_C = datetime.datetime.now()
        print 'Use time :',end_C-start_C,'\n'
    else:
        print 'All finishde .','\n'

end = datetime.datetime.now()
print 'Use time :',end-start
