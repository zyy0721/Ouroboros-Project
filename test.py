#！/usr/bin/env python
#!-*-coding:utf-8 -*-
#!@Create :2019/5/24 22:19
#!@Author : zyy
#!@File   : test.py

import re
filename = 'testCase4.ll'
strLine = "{testest zyy\l %12 = getelementptr inbounds %struct.PointerCase, %struct.PointerCase* %9,\l... i32 0, i32 0\l}"
if '...' in strLine:
    print("hhhhhhh")
if '\l...' in strLine:
    strLine = strLine.replace('\l...','')
    print("00000000000000")

print(strLine)
with open(filename,'r') as f:

    for line in f:
        res = re.split(",| ",line)
        print(line)
        print(res)