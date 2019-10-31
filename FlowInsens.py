#！/usr/bin/env python
#!-*-coding:utf-8 -*-
#!@Create :2019/10/31 19:34
#!@Author : zyy
#!@File   : FlowInsens.py
import os

root = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\linux\\arch\\newres"
def file_total(file_dir):
    for root, dirs, files in os.walk(file_dir):
        print("----------------")
        print(" ")
        print("----------------")
        for file in files:
            print(file)
            path = root +"\\"+ file #用于获取目录下的每个文件名的具体路径，用于后续处理
            print(path)


file_total(root)



#path = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\\firefox\\xpcom\\res"


#files = os.listdir(path)


