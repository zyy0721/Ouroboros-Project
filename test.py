#！/usr/bin/env python
#!-*-coding:utf-8 -*-
#!@Create :2019/5/24 22:19
#!@Author : zyy
#!@File   : test.py

import re
class Statement:
    def __init__(self):
        self.leftVal = ''
        self.Op = ''
        self.firstType = ''
        self.secondType = ''
        self.rightVal = ''

filename = 'testCase4.ll'
stack=[]
sta1 = Statement()
sta2 = Statement()
sta3 = Statement()
sta1.Op = '+'
sta2.Op = '-'
sta3.Op = '*'
stack.append(sta1)
stack.append(sta2)
stack.append(sta3)
for item in stack:
    print(item.Op)

strLine = "  %181 = call noalias i8* @malloc(i64 40) #4"
strLine2 = "  %183 = call i8* @_Znam(i64 40) #5"
res = re.split(",| ",strLine)
res2 = re.split(",| ",strLine2)
count = 0
for item in res:
    print(count, item)
    count +=1

if 'malloc' in strLine:
    print(1111111111111111111111)

count2 = 0;
for item in res2:
    print(count2,item)
    count2 +=1
if '_Znam' in strLine2:
    print(22222222222222222)
#print(res)
tmpStr = "call " + "void" + " " + "zyyfunc" + "( "


'''
with open(filename,'r') as f:

    for line in f:
        res = re.split(",| ",line)
        print(line)
        print(res)
'''