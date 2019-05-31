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

strLine = "  %n.addr = alloca i32, align 4"

res = re.split(",| ",strLine)

count = 0
for item in res:
    if 'addr' in item:
        print(count, item)
        count +=1

if 'malloc' in strLine:
    print(1111111111111111111111)


#print(res)
tmpStr = "call " + "void" + " " + "zyyfunc" + "( "


'''
with open(filename,'r') as f:

    for line in f:
        res = re.split(",| ",line)
        print(line)
        print(res)
'''