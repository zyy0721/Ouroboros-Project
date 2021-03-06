#！/usr/bin/env python
#!-*-coding:utf-8 -*-
#!@Create :2019/5/15 21:38
#!@Author : zyy
#!@File   : testFun.py

import re
filename = 'testCase.ll'
stackOp=[]
stackLV=[]
stackRV=[] #not use
topLevel=('')#for record topLevel variable
addressTaken=('')#for record addressTaken variable
#create a class called 'Statement' to store each line
class Statement:
    def __init__(self):
        self.leftVal = ''
        self.Op = ''
        self.firstType = ''
        self.secondType = ''
        self.rightVal = ''

def analysisLine(line):
    # split each line to get what we want
    res2 = re.split(',| ', line)
    # skip space line
    if (len(res2) == 0):
        #continue
        print("len of res is 0")
    else:
        if (res2[0] == '}\n'):  # means at the end of main function
            #break
            print("there should be a break")
            # skip annotation
        if (res2[0] == ';'):
            # shows that is a branch
            if ('preds' in res2):
                # preds 表示前驱
                print('\n')
                lable = res2[1].replace('<label>', '')
                lable = lable.replace(':', '')
                preds = []
                for item in res2:
                    if ('%' in item):
                        preds.append(item)
                print("block label is " + lable)
                print("preds:")
                for pred in preds:
                    print(pred.replace('\n', ''))
            # print(res2)
            #continue
            # skip source name
        if (res2[0] == 'source_name'):
            #continue
            print("source name is res20")
            # skip target name
        if (res2[0] == 'target'):
            #continue
            print("targe is ")
        if (res2[0] == '@.str'):
            #continue
            print("@.str")

        # alloca statement
        if (len(res2) >= 5 and res2[4] == 'alloca'):
            tmpSta = Statement()
            tmpSta.leftVal = res2[2]
            tmpSta.Op = 'alloca'
            tmpSta.firstType = res2[5]
            print("alloca " + tmpSta.firstType + " " + tmpSta.leftVal)
            #continue
            print("alloca statement1")
        # skip return 0 case
        if (len(res2) >= 3 and res2[2] == 'store' and res2[4] == 0):
            #continue
            print("alloca statement2")

        # every time when we meet 'load' instruction, we add this line to a stack called 'stackLV'
        if (len(res2) >= 5 and res2[4] == 'load'):
            stackOp.append('load')
            tmpSta = Statement()
            tmpSta.Op = 'load'
            tmpSta.leftVal = res2[2]
            tmpSta.firstType = res2[5]
            tmpSta.secondType = res2[7]
            tmpSta.rightVal = res2[8]
            stackLV.append(tmpSta)

        # when we meet the key word 'store', we should check the 'stackLV'. When the size of stackLV is 1, that is to say it's assignment .
        # When the size of stackLV is 2, we will go further to determine it's a deref statement or not.
        if (len(res2) >= 3 and res2[2] == 'store'):

            tmpSta = Statement()
            tmpSta.Op = 'store'
            tmpSta.leftVal = res2[4]
            tmpSta.firstType = res2[3]
            tmpSta.rightVal = res2[7]
            tmpSta.secondType = res2[6]

            # if there is no 'load' keyword
            if (len(stackLV) == 0):
                # judge whether it is an alloca statement or not
                if (tmpSta.firstType == 'i32*' or tmpSta.firstType == 'i32**'):
                    print(
                        tmpSta.secondType + ' ' + tmpSta.rightVal + " = alloca " + tmpSta.firstType + ' ' + tmpSta.leftVal)

            # if there is only one 'load' keyword in the stack
            if (len(stackLV) == 1):
                # fetch the top value of stack
                tmpStament = stackLV.pop()
                if (tmpStament.leftVal == tmpSta.leftVal):
                    print("assign: " + tmpSta.rightVal + "=" + tmpStament.rightVal)

            # if there are two 'load' keywords in the stack
            if (len(stackLV) >= 2):
                # fetch the top two values of stack
                # the name of variable is for intuitively operating
                tmpStament2 = stackLV.pop()
                tmpStament1 = stackLV.pop()
                if (tmpStament1.leftVal == tmpSta.leftVal and tmpStament2.leftVal == tmpSta.rightVal):
                    print("load: " + "*" + tmpStament2.rightVal + " = " + tmpStament1.rightVal)
                if (tmpStament2.leftVal == tmpSta.leftVal and tmpStament1.leftVal == tmpStament2.rightVal):
                    print("store: " + tmpSta.rightVal + " = " + "*" + tmpStament1.rightVal)

            # if there are more than two 'load' keywords in the satck
            # if(len(stackLV) >= 3):
            #    stackLV.clear()
            #    continue

        # branch for & if case
        if (len(res2) >= 3 and res2[2] == 'br'):
            # before leaving a block, should clear the whold stackLV
            stackLV.clear()
            tmpSta = Statement()
            tmpSta.Op = 'br'
            tmpSta.firstType = res2[3]
            if tmpSta.firstType != 'label':
                tmpSta.leftVal = res2[7]
                tmpSta.rightVal = res2[10].replace('\n', '')
            else:
                tmpSta.leftVal = res2[4].replace('\n', '')
            if tmpSta.rightVal == '':
                print("branch goto lable " + tmpSta.leftVal)
            else:
                print("branch goto lable " + tmpSta.leftVal + " or lable " + tmpSta.rightVal)
with open(filename,'r') as f:

    for line in f:
        analysisLine(line)


