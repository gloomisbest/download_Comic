#coding:GBK
import os
import sys
reload(sys)
sys.setdefaultencoding('GBK')


def create_dir_path(name):

    path_N = "Z:\Comic\\"+ name
    print 'Folder path :',path_N
    exists = os.path.exists(path_N)
    if not exists:
        print "create directory"
        os.makedirs(path_N)
    else:
        print "Folder already exists "
    return path_N


#print name
#create_dir_path(name)
