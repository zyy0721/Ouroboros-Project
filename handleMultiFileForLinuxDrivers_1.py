#！/usr/bin/env python
#!-*-coding:utf-8 -*-
#!@Create :2019/7/23 10:29
#!@Author : zyy
#!@File   : handleMultiFileForLinuxDrivers_1.py
import os
import re
import time

# 输出singleTon的结果txt文件
#drivers
#singleTontxt = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\linux\\drivers\\acpi\\res\singleTonResult.txt"
#singleTontxt = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\linux\\drivers\\ata\\res\singleTonResult.txt"
#singleTontxt = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\linux\\drivers\\atm\\res\singleTonResult.txt"
#singleTontxt = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\linux\\drivers\\auxdisplay\\res\singleTonResult.txt"
#singleTontxt = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\linux\\drivers\\base\\res\singleTonResult.txt"
#singleTontxt = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\linux\\drivers\\bcma\\res\singleTonResult.txt"
#singleTontxt = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\linux\\drivers\\block\\res\singleTonResult.txt"
#singleTontxt = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\linux\\drivers\\bluetooth\\res\singleTonResult.txt"
#singleTontxt = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\linux\\drivers\\cdrom\\res\singleTonResult.txt"
#singleTontxt = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\linux\\drivers\\char\\res\singleTonResult.txt"
#singleTontxt = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\linux\\drivers\\clk\\res\singleTonResult.txt"
#singleTontxt = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\linux\\drivers\\clocksource\\res\singleTonResult.txt"
#singleTontxt = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\linux\\drivers\\connector\\res\singleTonResult.txt"
#singleTontxt = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\linux\\drivers\\cpufreq\\res\singleTonResult.txt"
#singleTontxt = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\linux\\drivers\\cpuidle\\res\singleTonResult.txt"
#singleTontxt = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\linux\\drivers\\crypto\\res\singleTonResult.txt"
#singleTontxt = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\linux\\drivers\\dax\\res\singleTonResult.txt"
#singleTontxt = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\linux\\drivers\\dca\\res\singleTonResult.txt"
#singleTontxt = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\linux\\drivers\\devfreq\\res\singleTonResult.txt"
#singleTontxt = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\linux\\drivers\\dma\\res\singleTonResult.txt"
singleTontxt = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\linux\\drivers\\dma-buf\\res\singleTonResult.txt"



fsT = open(singleTontxt, 'a+')

# 用来存操作符的栈
stackOp = []
# 用来存statement的栈
stackLV = []
# 用来存每个函数的形参栈
FormalParameter = []  # to store every function's formal parameters
# 用来存储每个Pointer类型变量
allPointer = []  # to store pointer type variables
# 用来存储每个topLevel类型的变量
topLevel = []  # for record topLevel variable
# 用来存储每个address Taken类型的变量
addressTaken = []  # for record addressTaken variable
# 将所有的alloca变量都放入singleTon中
singleTon = []
# 将所有的new 或者malloca出来的变量放入notSingleTon中
notSingleTon = []
# 每个函数的形参列表
funformalPara = []
# 用来存每个dot文件，即每个函数文件中的alloca变量，这些都是memory类型
memoryvar_for_each_fun = []



# create a class called 'Statement' to store each line
class Statement:
    def __init__(self):
        self.leftVal = ''
        self.Op = ''
        self.firstType = ''
        self.secondType = ''
        self.rightVal = ''
        self.linenumber = ''

# 该函数用于，获取每条call指令的函数形参列表
def getFunctionPara(line):
    print(line)
    if '...' in line:
        line = line.split("...")[-1].replace(") ", "  ")
        print(line)
        return
    res = re.split("\(|\)", line)
    for item in res:
        print("res item ", item)
        spitem = re.split(",", item)
        print("spitem is ", spitem)
        for item2 in spitem:
            resz = re.split(" ", item2)
            print("~~~~resz is ", resz)
            if len(resz) == 2:
                if ('%' in resz[1] or '@' in resz[1]) and '*' not in resz[1]:
                    print("1111", resz[1])
                    if '%cond' not in resz[1] and '%conv' not in resz[1]:
                        funformalPara.append(resz[1])
            if len(resz) == 3:
                if '@.str' not in resz[2] and 'inbounds' not in resz[2] and ']' not in resz[2] and (
                        '%' in resz[2] or '@' in resz[2]):
                    if '%cond' not in resz[2] and '%conv' not in resz[2]:
                        funformalPara.append(resz[2])
                        print("~~~~~~~~~~~~~~the formalPara is ", resz[2])
            if len(resz) == 4:
                if resz[2] == 'zeroext' or resz[2] == 'signext' or resz[2] == 'nonnull':
                    if '%cond' not in resz[3] and '%conv' not in resz[3]:
                        funformalPara.append(resz[3])
    '''
    if 'getelementptr' in line:
        res1 = re.split(",", res[1])
        res1 += re.split(",", res[3])
    else:
        res1 = re.split(",", res[1])
    count = 0
    for j in range(len(res1)):
        print(count, res1[j])
        count += 1
        res2 = re.split(" ", res1[j])
        count4 = 0
        if 'getelementptr' in res2:
            print("11111")
        else:
            if len(res2) > 1:
                if j == 0:
                    print(res2[1])
                    funformalPara.append(res2[1])
                else:
                    print(res2[2])
                    funformalPara.append(res2[2])

    '''
    print("funciton formalPara is :")
    for item in funformalPara:
        print(item)


def analysisLine(line):
    # split each line to get what we want
    res2 = re.split(",| ", line)
    # skip space line
    if (len(res2) == 0):
        # continue
        print("len of res is 0")
    else:
        if (res2[0] == '}\n'):  # means at the end of main function
            # break
            print("there should be a break")
            # skip annotation

        # alloca statement
        # 在判断alloca语句的同时，通过是否有addr属性决定形参
        if (len(res2) >= 5 and res2[4] == 'alloca'):
            tmpSta = Statement()
            tmpSta.leftVal = res2[2]
            tmpSta.Op = 'alloca'
            # 把所有的alloca变量加入singleTon中
            singleTon.append(tmpSta.leftVal)
            # 把所有的alloca变量都加入memoryvar_for_each_fun中, 需要在离开每个file的时候清空
            memoryvar_for_each_fun.append(tmpSta.leftVal)
            if 'i32]' in res2 or 'i32*]' in res2 or 'i32**]' in res2 or 'i8]' in res2 or 'i8*]' in res2 or 'i8**]' in res2 or 'i64]' in res2 or 'i64*]' in res2 or 'i64**]' in res2 or 'i16**]' in res2 or 'i16*]' in res2 or 'i16]' in res2 or (len(res2) >=8 and']' in res2[7]):
                if '}>' in res2 and 'x' in res2:
                    tmpSta.firstType = res2[10].replace(']','')
                else:
                    tmpSta.firstType = res2[7].replace(']', '')
                    if len(tmpSta.firstType) == 0:
                        tmpSta.firstType == res2[6]
            else:
                if '}>' in res2 or '<{' in res2:
                    tmpSta.firstType = res2[6]
                else:
                    tmpSta.firstType = res2[5]
                    if len(tmpSta.firstType) == '{':
                        tmpSta.firstType = res2[6]
            # 如果有addr属性 说明是形参
            if 'addr' in tmpSta.leftVal:
                if tmpSta.leftVal not in FormalParameter:
                    FormalParameter.append(tmpSta.leftVal)

            # skip int type variable 跳过int类型的变量
            if tmpSta.firstType != 'i32' and tmpSta.firstType != 'i8' and tmpSta.firstType != 'i64' and tmpSta.firstType != 'i16':
                if len(tmpSta.firstType) != 0:
                    tmpStr = "alloca:" + tmpSta.firstType + " " + tmpSta.leftVal + "\\l "
                    allPointer.append(tmpSta.leftVal)
                    return tmpStr

        # every time when we meet 'load' instruction, we add this line to a stack called 'stackLV'
        if (len(res2) >= 5 and res2[4] == 'load'):
            stackOp.append('load')
            tmpSta = Statement()
            tmpSta.Op = 'load'
            tmpSta.leftVal = res2[2]
            if len(res2) == 16 and 'volatile' in res2:
                tmpSta.firstType = res2[6]
                tmpSta.secondType = res2[8]
                tmpSta.rightVal = res2[9]
            else:
                tmpSta.firstType = res2[5]
                if 'getelementptr' in res2:
                    if len(res2) == 28:
                        tmpSta.rightVal = res2[15]
                        tmpSta.secondType = res2[21].replace(")","")
                    elif len(res2) == 30:
                        tmpSta.rightVal = res2[17]
                        tmpSta.secondType = res2[23].replace(")","")
                    elif len(res2) == 31:
                        if res2[11] == 'inbounds':
                            tmpSta.rightVal = res2[15]
                            tmpSta.secondType = res2[24].replace(")","")
                        if res2[12] == 'inbounds':
                            tmpSta.rightVal = res2[16]
                            tmpSta.secondType = res2[24].replace(")","")
                        else:
                            tmpSta.rightVal = res2[16]
                    elif len(res2) == 32:
                        tmpSta.rightVal = res2[17]
                        tmpSta.secondType = res2[26].replace(")","")
                        if len(tmpSta.rightVal) == 0 and len(tmpSta.secondType) == 0:
                            tmpSta.rightVal = res2[13]
                            tmpSta.secondType = res2[25].replace(")","")
                    elif len(res2) == 33:
                        tmpSta.rightVal = res2[17]
                        tmpSta.secondType = res2[26].replace(")","")
                    elif len(res2) == 36:
                        tmpSta.rightVal = res2[17]
                        tmpSta.secondType = res2[29].replace(")","")
                    elif len(res2) == 37:
                        tmpSta.rightVal = res2[21]
                        tmpSta.secondType = res2[30].replace(")","")
                    elif len(res2) == 39:
                        if 'bitcast' in res2:
                            tmpSta.rightVal = res2[15]
                            tmpSta.secondType = res2[30].replace(")","")
                        elif res2[19] == 'inbounds':
                            tmpSta.rightVal = res2[23]
                            tmpSta.secondType = res2[32].replace(")","")
                        elif res2[15] == 'inbounds':
                            tmpSta.rightVal = res2[23]
                            tmpSta.secondType = res2[32].replace(")","")
                    elif len(res2) == 40:
                        tmpSta.rightVal = res2[27]
                        tmpSta.secondType = res2[33].replace(")","")
                    elif len(res2) == 42:
                        tmpSta.rightVal = res2[17]
                        tmpSta.secondType = res2[35].replace(")","")
                    elif len(res2) == 43:
                        tmpSta.rightVal = res2[27]
                        tmpSta.secondType = res2[36].replace(")","")
                    elif len(res2) == 44:
                        tmpSta.rightVal = res2[31]
                        tmpSta.secondType = res2[37].replace(")","")
                    elif len(res2) == 48:
                        tmpSta.rightVal = res2[35]
                    elif len(res2) == 51:
                        tmpSta.rightVal = res2[29]
                        tmpSta.secondType = res2[44].replace(")","")
                    elif len(res2) == 819:
                        tmpSta.rightVal = res2[803]
                        tmpSta.secondType = res2[812].replace(")","")
                    else:
                        tmpSta.rightVal = res2[13]
                        tmpSta.secondType = res2[19].replace(")","") #index
                elif 'bitcast' in res2:
                    if len(res2) == 19:
                        tmpSta.rightVal = res2[10]
                        tmpSta.secondType = res2[7]
                    if len(res2) == 20:
                        tmpSta.rightVal = res2[11]
                        tmpSta.secondType = res2[7]
                    if len(res2) == 21:
                        tmpSta.rightVal = res2[12]
                        tmpSta.secondType = res2[7]
                    if len(res2) == 22:
                        if '!noalias' in res2:
                            tmpSta.rightVal = res2[10]
                            tmpSta.secondType = res2[7]
                        if 'volatile' in res2:
                            tmpSta.firstType = res2[6]
                            tmpSta.rightVal = res2[13]
                            tmpSta.secondType = res2[8]
                    if len(res2) == 26:
                        tmpSta.rightVal = res2[17]
                        tmpSta.secondType = res2[7]
                else:
                    if len(res2) == 19 and 'x' in res2:
                        tmpSta.firstType = ""
                        tmpSta.rightVal = res2[12]
                    else:
                        if len(res2) == 17:
                            tmpSta.rightVal = res2[10]
                        elif len(res2) == 25:
                            tmpSta.rightVal = res2[18]
                        elif len(res2) == 23:
                            tmpSta.rightVal = res2[16]
                        elif len(res2) == 29:
                            tmpSta.rightVal = res2[22]
                        elif len(res2) == 33:
                            tmpSta.rightVal = res2[26]
                        else:
                            tmpSta.secondType = res2[7]
                            tmpSta.rightVal = res2[8]
            if '!dbg' in res2:
                tmpSta.linenumber = res2[-1]
            stackLV.append(tmpSta)

        # getelementptr
        if (len(res2) >= 5 and res2[4] == 'getelementptr'):
            tmpSta = Statement()
            tmpSta.Op = 'getelementptr'
            tmpSta.leftVal = res2[2]
            # 用 ‘x’ 来区分是否为数组,有bug，还没有考虑到变量名称带有x的情况
            if 'x' not in res2:
                print("in getelementptr shows res2 size is", len(res2), res2)
                tmpSta.rightVal = res2[9]
                tmpSta.firstType = res2[6]
                if '!dbg' in res2:
                    if len(res2) == 15:
                        tmpSta.secondType = res2[11]
                        tmpSta.rightVal = res2[8]
                        tmpSta.firstType = res2[5]
                    if len(res2) == 18:#需要注意下，其实是有没有inbounds这个关键字的区别，如果后续遇到相同长度的情况的话，可以加以区分
                        tmpSta.rightVal = res2[8]
                        tmpSta.firstType = res2[5]
                        tmpSta.secondType = res2[14]
                        if tmpSta.firstType == 'inbounds':
                            tmpSta.firstType = res2[6]
                            tmpSta.rightVal = res2[11]
                            tmpSta.secondType = res2[14]
                    if len(res2) == 19:
                        tmpSta.secondType = res2[15]  # it means the index of a pointer variable in the struct object
                    if len(res2) == 16:
                        tmpSta.secondType = res2[12]  # it means the index of a pointer variable in the struct object
                    if len(res2) == 21:
                        tmpSta.rightVal = res2[8]
                        tmpSta.firstType = res2[5]
                        if tmpSta.firstType == 'inbounds':
                            tmpSta.firstType = res2[6]
                            tmpSta.rightVal = res2[11]
                        tmpSta.secondType = res2[17]
                    if len(res2) == 22:
                        tmpSta.secondType = res2[18]
                    if len(res2) == 24:
                        tmpSta.firstType = res2[5]
                        tmpSta.rightVal = res2[8]
                        tmpSta.secondType = res2[20]
                        if len(tmpSta.rightVal) == 0:
                            tmpSta.firstType = res2[6]
                            tmpSta.rightVal = res2[11]
                        if '%' not in tmpSta.rightVal:
                            tmpSta.rightVal = res2[17]
                            tmpSta.firstType = res2[6]
                    if len(res2) == 25:
                        tmpSta.secondType = res2[21]
                    if len(res2) ==27:
                        tmpSta.rightVal = res2[11]
                        if len(tmpSta.rightVal) == 0:
                            tmpSta.rightVal = res2[17]
                        tmpSta.secondType = res2[23]
                    if len(res2) == 28:
                        tmpSta.secondType = res2[24]
                    if len(res2) == 29:
                        tmpSta.rightVal = res2[19]
                        tmpSta.secondType = res2[25]
                    if len(res2) == 30:
                        tmpSta.firstType = res2[5]
                        tmpSta.rightVal = res2[8]
                        tmpSta.secondType = res2[26]
                        if tmpSta.firstType == 'inbounds':
                            tmpSta.rightVal =res2[23]
                            tmpSta.firstType = res2[6]
                    if len(res2) == 31:
                        if '<{' in res2:
                            tmpSta.rightVal = res2[21]
                            tmpSta.firstType = res2[7]
                            tmpSta.secondType = res2[27]
                        else:
                            tmpSta.secondType = res2[27]
                    if len(res2) == 33:
                        tmpSta.rightVal = res2[8]
                        tmpSta.secondType = res2[29]
                        if len(tmpSta.firstType) == 0:
                            tmpSta.firstType = res2[5]
                    if len(res2) == 36:
                        tmpSta.rightVal = res2[8]
                        tmpSta.secondType = res2[32]
                        if len(tmpSta.firstType) == 0:
                            tmpSta.firstType = res2[5]
                        if '%' not in res2[8] and '@' not in res2[8]:
                            tmpSta.rightVal = res2[17]
                    if len(res2) == 38:
                        tmpSta.rightVal = res2[8]
                        tmpSta.firstType = res2[5]
                    if len(res2) == 39:
                        tmpSta.rightVal = res2[22]
                        tmpSta.secondType = res2[35]
                        tmpSta.firstType = res2[7].replace(']','')
                    if len(res2) == 42:
                        tmpSta.rightVal = res2[8]
                    if len(res2) == 45:
                        tmpSta.firstType = res2[5]
                        tmpSta.rightVal = res2[8]
                        tmpSta.secondType = res2[41]
                    if len(res2) == 63:
                        tmpSta.rightVal = res2[19]
                else:
                    if len(res2) == 16:
                        tmpSta.secondType = res2[15]  # it means the index of a pointer variable in the struct object
                    if len(res2) == 13:
                        tmpSta.secondType = res2[12]  # it means the index of a pointer variable in the struct object
                    if len(res2) == 24:
                        tmpSta.rightVal = res2[8]
                        tmpSta.secondType = res2[23]
                        if len(tmpSta.rightVal) == 0:
                            tmpSta.rightVal = res2[17]

            else:  # it means an array type
                print('contains an array type: ',res2)
                if '!dbg' in res2:
                    if len(res2) == 20:
                        tmpSta.rightVal = res2[13]
                        tmpSta.secondType = res2[16]
                        tmpSta.firstType = res2[8].replace(']','')
                    if len(res2) == 21:
                        if res2[8] == 'bitcast':
                            tmpSta.rightVal = res2[12]
                            tmpSta.secondType = res2[17]
                            tmpSta.firstType = res2[5]
                    if len(res2) == 22:
                        tmpSta.rightVal = res2[12]
                        tmpSta.secondType = res2[18]
                        tmpSta.firstType = res2[7].replace(']','')
                    if len(res2) == 23:
                        tmpSta.rightVal = res2[13]
                        tmpSta.secondType = res2[19]
                        tmpSta.firstType = res2[8].replace(']','')
                    if len(res2) == 24:
                        tmpSta.rightVal = res2[14]
                        tmpSta.secondType = res2[20]
                        tmpSta.firstType = res2[8].replace(']','')
                    if len(res2) == 25:
                        tmpSta.rightVal = res2[12]
                        tmpSta.secondType = res2[18]
                        tmpSta.firstType = res2[7].replace(']','')
                    if len(res2) ==26:
                        tmpSta.rightVal = res2[13]
                        tmpSta.secondType = res2[22]
                        tmpSta.firstType = res2[8].replace(']','')
                    if len(res2) == 27:
                        tmpSta.rightVal = res2[17]
                        tmpSta.secondType = res2[23]
                        tmpSta.firstType = res2[10].replace(']','')
                    if len(res2) == 28:
                        tmpSta.rightVal = res2[12]
                        tmpSta.secondType = res2[24]
                        tmpSta.firstType = res2[7].replace(']','')
                    if len(res2) == 29:
                        tmpSta.rightVal = res2[16]
                        tmpSta.secondType = res2[22]
                        tmpSta.firstType = res2[9].replace(']','')
                        if tmpSta.rightVal.isdigit():
                            tmpSta.rightVal = res2[13]
                            tmpSta.secondType = res2[25]
                            tmpSta.firstType = res2[8].replace(']','')
                    if len(res2) == 30:
                        tmpSta.rightVal = res2[17]
                        tmpSta.secondType = res2[26]
                        tmpSta.firstType = res2[10].replace(']','')
                    if len(res2) == 31:
                        if res2[13] == "bitcast":
                            tmpSta.rightVal = res2[17]
                            tmpSta.secondType = res2[27]
                            tmpSta.firstType = res2[8].replace(']','')
                        elif ']' in res2[13]:
                            tmpSta.rightVal = res2[18]
                            tmpSta.secondType = res2[27]
                            tmpSta.firstType = res2[8]
                        else:
                            tmpSta.rightVal = res2[12]
                            tmpSta.firstType = res2[7].replace(']','')
                            tmpSta.secondType = res2[27]
                    if len(res2) == 32:
                        tmpSta.rightVal = res2[13]
                        tmpSta.secondType = res2[28]
                        tmpSta.firstType = res2[8].replace(']','')
                        if '%' not in res2[13] and '@' not in res2[13]:
                            tmpSta.rightVal = res2[22]
                    if len(res2) == 34:
                        tmpSta.rightVal = res2[18]
                        tmpSta.secondType = res2[30]
                        tmpSta.firstType = res2[8].replace(']','')
                    if len(res2) == 35:
                        tmpSta.rightVal = res2[13]
                        tmpSta.secondType = res2[31]
                        tmpSta.firstType = res2[8].replace(']','')
                    if len(res2) == 36:
                        tmpSta.rightVal = res2[22]
                        tmpSta.secondType = res2[32]
                        tmpSta.firstType = res2[7].replace(']','')
                        if '%' not in res2[22] and '@' not in res2[22]:
                            tmpSta.rightVal = res2[26]

                    if len(res2) == 37:
                        tmpSta.rightVal = res2[21]
                        tmpSta.secondType = res2[33]
                        tmpSta.firstType = res2[12].replace(']','')
                    if len(res2) == 38:
                        tmpSta.rightVal = res2[13]
                        tmpSta.secondType = res2[34]
                        tmpSta.firstType = res2[8].replace(']','')
                    if len(res2) == 39:
                        tmpSta.rightVal = res2[22]
                        tmpSta.firstType = res2[7].replace(']', '')
                        tmpSta.secondType = res2[32]
                    if len(res2) == 40:
                        tmpSta.rightVal = res2[30]
                        tmpSta.secondType = res2[36]
                    if len(res2) == 42:
                        if 'bitcast' in res2:
                            tmpSta.rightVal = res2[27]
                            tmpSta.secondType = res2[38]
                            tmpSta.firstType = res2[8]
                        elif '<{' in res2:
                            tmpSta.rightVal = res2[29]
                    if len(res2) == 46:
                        tmpSta.rightVal = res2[23]
                    if len(res2) == 49:
                        if res2[16] == 'bitcast':
                            tmpSta.rightVal = res2[30]
                    if len(res2) == 50:
                        if res2[12] == 'bitcast':
                            tmpSta.rightVal = res2[36]
                    if len(res2) == 53:
                        if res2[12] == 'bitcast':
                            tmpSta.rightVal = res2[36]
                    if len(res2) == 54:
                        tmpSta.rightVal = res2[32]

                    if len(res2) == 59:
                        if 'bitcast' in res2:
                            tmpSta.rightVal = res2[40]
                            tmpSta.secondType = res2[55]
                            tmpSta.firstType = res2[9].replace(']','')
                        else:
                            tmpSta.rightVal = res2[49]
                    if len(res2) == 73:
                        tmpSta.rightVal = res2[59]
                    if len(res2) == 95:
                        tmpSta.rightVal = res2[78]
                    if len(res2) >=96:
                        for item in res2:
                            if '@' in item:
                                tmpSta.rightVal = item
                                break
                    '''
                    if len(res2) == 114:
                        tmpSta.rightVal = res2[100]
                    if len(res2) == 116:
                        tmpSta.rightVal = res2[102]
                    if len(res2) == 166:
                        tmpSta.firstType = res2[7].replace(']','')
                        tmpSta.rightVal = res2[146]
                        tmpSta.secondType = res2[162]
                    if len(res2) == 225:
                        tmpSta.rightVal = res2[211]
                    if len(res2) == 262:
                        tmpSta.rightVal = res2[248]
                    if len(res2) == 264:
                        tmpSta.rightVal = res2[250]
                    if len(res2) == 362:
                        tmpSta.rightVal = res2[346]
                    if len(res2) == 363:
                        tmpSta.rightVal = res2[346]
                    if len(res2) == 366:
                        tmpSta.rightVal = res2[346]
                    if len(res2) == 373:
                        tmpSta.rightVal =res2[359]
                    if len(res2) == 460:
                        tmpSta.rightVal = res2[446]
                    if len(res2) == 515:
                        tmpSta.rightVal = res2[501]
                    if len(res2) == 553:
                        tmpSta.rightVal = res2[534]
                    if len(res2) >= 554:#太奇葩的情况了
                        #不处理直接过滤掉
                        return ""
                    '''
                else:
                    if len(res2) == 19:
                        tmpSta.rightVal = res2[12]
                        tmpSta.secondType = res2[18]
                        tmpSta.firstType = res2[7].replace(']','')
                    if len(res2) == 20:
                        tmpSta.rightVal = res2[13]
                        tmpSta.secondType = res2[19]
                        tmpSta.firstType = res2[8].replace(']','')
                    if len(res2) == 24:  # it means a two-dimensional array
                        tmpSta.firstType = res2[10].replace(']', '')
                        tmpSta.rightVal = res2[17]
                        tmpSta.secondType = res2[23]
                    if len(res2) == 28:
                        if '<{' in res2 or '}>' in res2:
                            tmpSta.rightVal = res2[21]
                            tmpSta.secondType = res2[27]
                            tmpSta.firstType = res2[7]

            if '!dbg' in res2:
                tmpSta.linenumber = res2[-1]
            stackLV.append(tmpSta)

        #icmp instruction
        if (len(res2) >=5 and res2[4] == 'icmp'):
            tmpSta = Statement()
            tmpSta.Op = 'icmp'
            tmpSta.firstType = res2[5]  # 'ne' or 'eq'
            tmpSta.secondType = res2[6]  # true type
            tmpSta.leftVal = res2[7]  # op1
            tmpSta.rightVal = res2[9]  # op2
            if '!dbg' in res2:
                tmpSta.linenumber = res2[-1]

            if tmpSta.firstType == 'ne' or tmpSta.firstType == 'eq' :
                if tmpSta.rightVal == 'null':
                    if len(stackLV) >= 1:
                        tmpStament1 = stackLV.pop()
                        if tmpStament1.leftVal == tmpSta.leftVal:
                            if len(stackLV) >= 1:
                                '''
                                会存在这种例子
                                    %8 = load %struct.ap_directive_t**, %struct.ap_directive_t*** %last_ptr, align 8, !dbg !59334
                                    %9 = load %struct.ap_directive_t*, %struct.ap_directive_t** %8, align 8, !dbg !59335
                                    %tobool3 = icmp ne %struct.ap_directive_t* %9, null, !dbg !59335
                                '''
                                tmpStament2 = stackLV.pop()
                                if tmpStament2.leftVal == tmpStament1.rightVal :
                                    if len(stackLV) >= 1:
                                        '''
                                        会存在这种情况
                                            %12 = load %struct.ap_directive_t*, %struct.ap_directive_t** %current, align 8, !dbg !59343
                                            %next = getelementptr inbounds %struct.ap_directive_t, %struct.ap_directive_t* %12, i32 0, i32 2, !dbg !59344
                                            %13 = load %struct.ap_directive_t*, %struct.ap_directive_t** %next, align 8, !dbg !59344
                                            %tobool6 = icmp ne %struct.ap_directive_t* %13, null, !dbg !59342
                                        '''
                                        tmpStament3 = stackLV.pop()
                                        if tmpStament3.leftVal == tmpStament2.rightVal :
                                            if tmpStament2.secondType.isdigit():
                                                tmpStr = "cmp: " + tmpStament3.rightVal + "." + tmpStament2.secondType + tmpSta.linenumber + "\\l "
                                            else:
                                                if tmpStament3.Op == "getelementptr":
                                                    tmpStr = "cmp: " + tmpStament3.rightVal + "." + tmpStament3.secondType + tmpSta.linenumber + "\\l "
                                                else:
                                                    tmpStr = "cmp: " + tmpStament3.rightVal + tmpSta.linenumber + "\\l "
                                            return tmpStr
                                    else:
                                            tmpStr = "cmp: " + "*" + tmpStament2.rightVal + tmpSta.linenumber + "\\l "
                                            return tmpStr
                            else:
                                if tmpStament1.secondType.isdigit():
                                    tmpStr = "cmp: "+ tmpStament1.rightVal+ "."+ tmpStament1.secondType + tmpSta.linenumber+"\\l "
                                else:
                                    tmpStr = "cmp: " + tmpStament1.rightVal + tmpSta.linenumber + "\\l "
                                return tmpStr
                    else:
                        tmpStr = "cmp: " + tmpSta.leftVal + tmpSta.linenumber + "\\l "
                        return tmpStr

        #bitcast instruction
        if (len(res2) >=5 and (res2[4] == 'bitcast' or res2[4] == 'trunc' or res2[4] == 'zext' or res2[4] == 'sext' or res2[4] == 'fptrunc' or res2[4] == 'inttoptr' or res2[4] == 'ptrtoint' or res2[4] == 'sitofp' or res2[4] == 'uitofp' or res2[4] == 'fptosi' or res2[4] == 'fptoui' or res2[4] == 'fpext')):
            tmpSta = Statement()
            tmpSta.Op = res2[4]
            tmpSta.leftVal = res2[2]
            tmpSta.firstType = res2[5]
            tmpSta.rightVal = res2[6]
            tmpSta.secondType = res2[8]
            if '<{' in res2 or '}>' in res2:
                tmpSta.firstType = res2[6]
                if len(res2[7])==0 and len(res2[9]) == 0:
                    tmpSta.rightVal = res2[12]
                    tmpSta.secondType = res2[14]
            elif 'x' in res2 and len(res2) == 14 and res2[9] == 'to':
                tmpSta.firstType = res2[7].replace(']','')
                tmpSta.rightVal = res2[8]
                tmpSta.secondType = res2[10]
            elif len(res2) == 19 and res2[14] == 'to':
                tmpSta.rightVal = res2[13]
                tmpSta.secondType = res2[15]
            elif len(res2) == 17:
                if res2[8] == 'to':
                    tmpSta.rightVal = res2[7]


            if "!dbg" in res2:
                tmpSta.linenumber = res2[-1]
            #直接进行相应的变量转化
            if len(stackLV) >= 1:
                tmpStament1 = stackLV[-1]
                if tmpStament1.leftVal == tmpSta.rightVal:
                    stackLV[-1].leftVal = tmpSta.leftVal
            else:
                #如果前面没有stackLV，则把它看作是一条assign
                tmpStr = "assign: " + tmpSta.leftVal + " = " + tmpSta.rightVal + tmpSta.linenumber + "\\l "
                if tmpSta.leftVal not in allPointer:
                    allPointer.append(tmpSta.leftVal)
                if tmpSta.rightVal not in allPointer:
                    allPointer.append(tmpSta.rightVal)
                return tmpStr

        # when we meet the key word 'store', we should check the 'stackLV'. When the size of stackLV is 1, that is to say it's assignment .
        # When the size of stackLV is 2, we will go further to determine it's a deref statement or not.
        if (len(res2) >= 3 and res2[2] == 'store'):

            tmpSta = Statement()
            tmpSta.Op = 'store'
            tmpSta.leftVal = res2[4]
            tmpSta.firstType = res2[3]
            if 'getelementptr' in res2:
                if len(res2) == 25:
                    tmpSta.rightVal = res2[12]
                elif len(res2) == 27:
                    tmpSta.leftVal = res2[5]
                    tmpSta.rightVal = res2[14]
                    tmpSta.secondType = res2[20].replace(")","")
                elif len(res2) == 29:
                    if res2[5] == 'inbounds':
                        tmpSta.leftVal = res2[13]
                        tmpSta.rightVal = res2[22]
                        tmpSta.secondType = res2[19].replace(")","")
                    elif res2[3] == 'volatile':
                        tmpSta.leftVal = res2[5]
                        tmpSta.firstType = res2[4]
                        tmpSta.rightVal = res2[13]
                    else:
                        tmpSta.rightVal = res2[16]
                        tmpSta.secondType = res2[22].replace(")","")
                elif len(res2) == 30:
                    tmpSta.leftVal = res2[5]
                    tmpSta.rightVal = res2[14]
                    tmpSta.secondType = res2[23].replace(")","")
                elif len(res2) == 32:
                    tmpSta.rightVal = res2[16]
                    tmpSta.secondType = res2[25].replace(")","")
                elif len(res2) == 33:
                    tmpSta.leftVal = res2[5]
                    tmpSta.rightVal = res2[14]

                elif len(res2) == 34:
                    tmpSta.rightVal = res2[12]

                elif len(res2) == 35:
                    tmpSta.rightVal = res2[16]
                    tmpSta.secondType = res2[28].replace(")","")
                elif len(res2) == 39:
                    tmpSta.rightVal = res2[11]
                    tmpSta.leftVal = res2[26]
                    tmpSta.secondType = res2[32].replace(")","")
                elif len(res2) == 41:
                    tmpSta.rightVal = res2[16]
                    tmpSta.secondType = res2[34].replace(")","")
                    if '%' not in res2[16] and '@' not in res2[16]:
                        tmpSta.leftVal = res2[5]
                        tmpSta.rightVal = res2[22]
                elif len(res2) == 42:
                    tmpSta.leftVal = res2[11]
                    tmpSta.rightVal = res2[26]
                    tmpSta.secondType = res2[35].replace(")","")
                elif len(res2) == 43:
                    tmpSta.firstType = res2[4]
                    tmpSta.leftVal = res2[16]
                    tmpSta.rightVal = res2[34]
                    if '%' not in res2[16] and '@' not in res2[16]:
                        tmpSta.firstType = res2[3]
                        tmpSta.leftVal = res2[4]
                        tmpSta.rightVal = res2[12]
                elif len(res2) == 59:
                    tmpSta.firstType = res2[4]
                    tmpSta.leftVal = res2[16]
                    tmpSta.rightVal = res2[41]
                    tmpSta.secondType = res2[50].replace(")","")
                else:
                    tmpSta.rightVal = res2[12]
                    tmpSta.secondType = res2[18].replace(")","")#index
            else:
                if '(' in res2[4]:
                    if len(res2) == 13:
                        tmpSta.leftVal = res2[5]
                        tmpSta.rightVal = res2[9]
                        tmpSta.secondType = tmpSta.firstType + "*"
                    if len(res2) == 16:
                        if '!dbg' in res2:
                            tmpSta.leftVal = res2[5]
                            tmpSta.rightVal = res2[9]
                            tmpSta.secondType = tmpSta.firstType + "*"
                    if len(res2) == 17:
                        tmpSta.leftVal = res2[7]
                        tmpSta.rightVal = res2[13]
                        tmpSta.secondType = tmpSta.firstType + "*"
                    if len(res2) == 20:
                        if '!dbg' in res2:
                            tmpSta.leftVal = res2[7]
                            tmpSta.rightVal = res2[13]
                            tmpSta.secondType = tmpSta.firstType + "*"
                    if len(res2) == 21:
                        tmpSta.leftVal = res2[9]
                        tmpSta.rightVal = res2[17]
                        tmpSta.secondType = tmpSta.firstType + "*"
                    if len(res2) == 22:
                        tmpSta.leftVal = res2[8]
                        tmpSta.rightVal = res2[15]
                        tmpSta.secondType = tmpSta.firstType + "*"
                    if len(res2) == 24:
                        if '!dbg' in res2:
                            tmpSta.leftVal = res2[9]
                            tmpSta.rightVal = res2[17]
                            tmpSta.secondType = tmpSta.firstType + "*"
                    if len(res2) == 25:
                        tmpSta.rightVal = res2[21]
                        tmpSta.leftVal = res2[11]
                    if len(res2) == 27:
                        if res2[7] == 'inttoptr':
                            tmpSta.firstType = res2[8].replace("(","")
                            tmpSta.leftVal = res2[9]
                            tmpSta.rightVal = res2[20]
                    if len(res2) == 28:
                        tmpSta.leftVal = res2[11]
                        tmpSta.rightVal = res2[21]

                    if len(res2) == 29:
                        tmpSta.leftVal = res2[13]
                        tmpSta.rightVal = res2[25]
                        tmpSta.secondType = tmpSta.firstType + "*"
                    if len(res2) == 32:
                        tmpSta.leftVal = res2[13]
                        tmpSta.rightVal = res2[25]
                        tmpSta.secondType = tmpSta.firstType + "*"
                    if len(res2) == 33:
                        tmpSta.leftVal = res2[15]
                        tmpSta.rightVal = res2[29]
                        tmpSta.secondType = tmpSta.firstType + "*"
                    if len(res2) == 37:
                        tmpSta.leftVal = res2[17]
                        tmpSta.rightVal = res2[30]
                        tmpSta.secondType = tmpSta.firstType + "*"
                    if len(res2) == 42:
                        tmpSta.leftVal = res2[11]
                        tmpSta.rightVal = res2[26]
                        tmpSta.secondType = tmpSta.firstType + "*"
                    if len(res2) == 52:
                        tmpSta.leftVal = res2[23]
                        tmpSta.rightVal = res2[45]
                elif res2[4] == 'x':
                    if len(res2) == 15:
                        tmpSta.leftVal = res2[6]
                        tmpSta.rightVal = res2[11]
                    elif len(res2) == 18:
                        tmpSta.leftVal = res2[6]
                        tmpSta.rightVal = res2[11]
                    elif len(res2) == 28:
                        tmpSta.firstType = res2[9]
                        tmpSta.leftVal = res2[7]
                        tmpSta.rightVal = res2[21]
                elif res2[4] == 'inttoptr':
                    if len(res2) == 18:
                        tmpSta.firstType = res2[5].replace("(","")
                        tmpSta.leftVal = res2[6]
                        tmpSta.rightVal = res2[11]
                else:
                    if len(res2) == 21:
                        tmpSta.leftVal = res2[9]
                        tmpSta.firstType = res2[4]
                        tmpSta.rightVal = res2[14]
                        tmpSta.secondType = tmpSta.firstType + "*"
                    elif len(res2) == 27:
                        tmpSta.leftVal = res2[9]
                        tmpSta.rightVal = res2[18]
                        tmpSta.firstType = res2[4]
                        tmpSta.secondType = tmpSta.firstType + "*"
                    else:
                        tmpSta.rightVal = res2[7]
                        tmpSta.secondType = res2[6]
            if '!dbg' in res2:
                tmpSta.linenumber = res2[-1]


            relationmap = {} #用来存中间的映射关系
            memvar = [] #用来存mem类型的变量
            tmpStrStack = [] #用来存tmpStr返回的栈，使得它能够正确的顺序输出
            #在这部分将stackLV中的内容都存在dict中,如果stackLV为空的话，直接输出处理的结果
            #进行中间过程的处理
            if len(stackLV) == 0:
                #说明只有一条store语句
                #先进行store x , y 中x 和 y 的判断， 是否为memory类型 还是 register类型
                x = tmpSta.leftVal
                y = tmpSta.rightVal
                if tmpSta.firstType == "i8" or tmpSta.firstType == "i16" or tmpSta.firstType == "i32" or tmpSta.firstType == "i64" or tmpSta.firstType == "float" or tmpSta.firstType == "double":
                    #直接略掉非pointer变量
                    print("is not pointer type")
                    return ""
                else:
                    if '.addr' in y:
                        tmpSta_rightVal = y.replace(".addr", "")
                        tmpSta_leftVal = x.replace(tmpSta_rightVal, "")
                        if tmpSta_leftVal.isdigit():
                            print("maybe this case: store i32 * % retval1, i32 ** % retval.addr, do nothing")
                            return ""
                    tmpLeftVal = x + ".addr"
                    if tmpLeftVal == y:
                        #类似 store i32* %p, i32** %p.addr, align 8的情况
                        #直接过滤掉
                        return ""

                    if x == 'null':
                        tmpStr = "assign: " + y + " = " + x + tmpSta.linenumber + "\\l "
                        if tmpSta.rightVal not in allPointer:
                            allPointer.append(tmpSta.rightVal)
                        return tmpStr


                    if x in memoryvar_for_each_fun or x in memvar or '@' in x:
                        #说明x是mem变量
                        if y in memoryvar_for_each_fun or y in memvar or '@' in y:
                            #说明y是mem变量
                            tmpStr = "alloca: " + y + " = " + "&" + x + tmpSta.linenumber+"\\l "
                            if x not in addressTaken:
                                addressTaken.append(x)
                            if y not in allPointer:
                                allPointer.append(y)
                            return tmpStr
                        #不存在 x为mem 而y为reg的情况
                    else:
                        #说明x是register变量
                        if y in memoryvar_for_each_fun or y in memvar or '@' in y:
                            #说明y是mem变量
                            tmpStr = "assign: " + y + " = " + x + tmpSta.linenumber + "\\l "
                            if x not in allPointer:
                                allPointer.append(x)
                            if y not in allPointer:
                                allPointer.append(y)
                            return tmpStr
                        else:
                            #说明y是reg变量
                            tmpStr = "store: " + "*" + y + " = " + x + tmpSta.linenumber + "\\l "
                            if x not in allPointer:
                                allPointer.append(x)
                            if y not in allPointer:
                                allPointer.append(y)
                            return tmpStr
            else:
                for i in range(len(stackLV)):
                    if stackLV[i].Op == "load":
                        x = stackLV[i].rightVal
                        y = stackLV[i].leftVal
                        if x in memoryvar_for_each_fun or x in memvar or '@' in x:
                            #说明x是mem变量
                            relationmap[y] = x  # y = x
                        else:
                            #说明x是reg变量
                            relationmap[y] = "*" + x # y = *x


                    elif stackLV[i].Op == "getelementptr":
                        x = stackLV[i].rightVal
                        y = stackLV[i].leftVal
                        memvar.append(y) #把getelementptr的左值看成mem变量
                        #relationmap[y] = "*" + x # y = *x  感觉这个关系映射是不是可以不用

            #过滤掉非pointer类型的store语句
            #进行实际的处理
            if tmpSta.firstType =="i8" or tmpSta.firstType == "i16" or tmpSta.firstType == "i32" or tmpSta.firstType == "i64" or tmpSta.firstType == "float" or tmpSta.firstType == "double" :
                #置空
                tmpStr = ""
                #同时清空stackLV
                stackLV.clear()
                #清空map关系
                relationmap.clear()
                #清空memvar
                memvar.clear()
                return tmpStr
            else:
                #最重要的逻辑处理模块
                x = tmpSta.leftVal
                y = tmpSta.rightVal
                #tmpStr = ""
                if x in memoryvar_for_each_fun or x in memvar or '@' in x:
                    #说明x是mem变量
                    if y in memoryvar_for_each_fun or y in memvar or '@' in y:
                        #说明y是mem变量
                        tmpStr = "alloca: " + y + " = " + "&" + x + tmpSta.linenumber+"\\l "
                        if x not in addressTaken:
                            addressTaken.append(x)
                        if y not in allPointer:
                            addressTaken.append(y)
                        tmpStrStack.append(tmpStr)
                        index = 0
                        while(len(stackLV) != 0):
                            tmpStament = stackLV.pop()
                            if tmpStament.Op == "getelementptr":
                                if index == 0:
                                # 说明是特殊情况
                                    if tmpStament.leftVal == x:
                                        tmpStr = "load: " + tmpStament.leftVal + " = " + "*" + tmpStament.rightVal + tmpStament.linenumber + "\\l "
                                        if tmpStament.leftVal not in allPointer:
                                            allPointer.append(tmpStament.leftVal)
                                        if tmpStament.rightVal not in allPointer:
                                            allPointer.append(tmpStament.rightVal)
                                        tmpStrStack.append(tmpStr)
                                    elif tmpStament.leftVal == y:
                                        if len(tmpStrStack) != 0:
                                            tmpStrtmp = tmpStrStack.pop()
                                            tmpStr = "store: " + "*" + tmpStament.rightVal + " = " + tmpStament.leftVal + tmpStament.linenumber + "\\l "
                                            if tmpStament.leftVal not in allPointer:
                                                allPointer.append(tmpStament.leftVal)
                                            if tmpStament.rightVal not in allPointer:
                                                allPointer.append(tmpStament.rightVal)
                                            tmpStrStack.append(tmpStr)
                                            tmpStrStack.append(tmpStrtmp)

                                else:
                                    #如果不是特殊情况，而且也是getelementptr类型的话，那么直接输出
                                    tmpStr = "load: " + tmpStament.leftVal + " = " + "*" + tmpStament.rightVal + tmpStament.linenumber + "\\l "
                                    if tmpStament.leftVal not in allPointer:
                                        allPointer.append(tmpStament.leftVal)
                                    if tmpStament.rightVal not in allPointer:
                                        allPointer.append(tmpStament.rightVal)
                                    tmpStrStack.append(tmpStr)
                            else:
                                #说明是load语句，如果有多余的load语句直接当做assign的pattern输出给后端
                                realx = relationmap.get(tmpStament.leftVal,"")
                                if len(realx) != 0:
                                    if "*" not in realx:
                                        tmpStr = "assign: " + tmpStament.leftVal + " = " + tmpStament.rightVal + tmpStament.linenumber + "\\l "
                                        if tmpStament.leftVal not in allPointer:
                                            allPointer.append(tmpStament.leftVal)
                                        if tmpStament.rightVal not in allPointer:
                                            allPointer.append(tmpStament.rightVal)
                                        tmpStrStack.append(tmpStr)
                                    else:
                                        realx = realx.replace("*","")
                                        realxx = relationmap.get(realx,"")
                                        if len(realxx) != 0:
                                            if "*" not in realxx:
                                                tmpStr = "load: " + tmpStament.leftVal + " = " + "*" + realxx + tmpStament.linenumber + "\\l "
                                                if tmpStament.leftVal not in allPointer:
                                                    allPointer.append(tmpStament.leftVal)
                                                if realxx not in allPointer:
                                                    allPointer.append(realxx)
                                                relationmap.pop(realx,"")
                                                tmpStrStack.append(tmpStr)
                                            else:
                                                tmpStr = "load: " + tmpStament.leftVal + " = " + "*" + realx + tmpStament.linenumber + "\\l "
                                                if tmpStament.leftVal not in allPointer:
                                                    allPointer.append(tmpStament.leftVal)
                                                if realx not in allPointer:
                                                    allPointer.append(realx)
                                                tmpStrStack.append(tmpStr)
                                        else:
                                            #不太应该出现
                                            print("zyy6")
                                            tmpStr = "load: " + tmpStament.leftVal + " = " + "*" + realx + tmpStament.linenumber + "\\l "
                                            if tmpStament.leftVal not in allPointer:
                                                allPointer.append(tmpStament.leftVal)
                                            if realx not in allPointer:
                                                allPointer.append(realx)
                                            tmpStrStack.append(tmpStr)


                            index = index + 1

                        toretStr = ""
                        while(len(tmpStrStack) != 0):
                            tmpStrtmp = tmpStrStack.pop()
                            toretStr += tmpStrtmp
                        # 清空map关系
                        relationmap.clear()
                        # 清空memvar
                        memvar.clear()
                        return toretStr

                    #不存在 x为mem 而y为reg的情况
                else:
                    #说明x是register变量
                    if y in memoryvar_for_each_fun or y in memvar or '@' in y:
                        #说明y是mem变量
                        index = 0
                        while(len(stackLV) != 0):
                            tmpStament = stackLV.pop()
                            if index == 0:
                                if tmpStament.Op == "getelementptr":
                                    # 说明是特殊情况
                                    if tmpStament.leftVal == y:
                                        realright = relationmap.get(tmpStament.rightVal, "")
                                        if len(realright) != 0:
                                            if "*" in realright:
                                                realleft = relationmap.get(x, "")
                                                if len(realleft) != 0:
                                                    if "*" in realleft:
                                                        tmpStr = "store: " + "*" + tmpStament.rightVal + " = " + x + tmpSta.linenumber + "\\l "
                                                        if tmpStament.rightVal not in allPointer:
                                                            allPointer.append(tmpStament.rightVal)
                                                        if x not in allPointer:
                                                            allPointer.append(x)
                                                        tmpStrStack.append(tmpStr)

                                                    else:
                                                        tmpStr = "store: " + "*" + tmpStament.rightVal + " = " + realleft + tmpSta.linenumber + "\\l "
                                                        if tmpStament.rightVal not in allPointer:
                                                            allPointer.append(tmpStament.rightVal)
                                                        if realleft not in allPointer:
                                                            allPointer.append(realleft)
                                                        tmpStrStack.append(tmpStr)
                                                        relationmap.pop(x,"")
                                                else:
                                                    tmpStr = "store: " + "*" + tmpStament.rightVal + " = " + x + tmpSta.linenumber + "\\l "
                                                    if tmpStament.rightVal not in allPointer:
                                                        allPointer.append(tmpStament.rightVal)
                                                    if x not in allPointer:
                                                        allPointer.append(x)
                                                    tmpStrStack.append(tmpStr)
                                            else:
                                                realleft = relationmap.get(x, "")
                                                if len(realleft) != 0:
                                                    if "*" in realleft:
                                                        tmpStr = "store: " + "*" + realright + " = " + x + tmpSta.linenumber + "\\l "
                                                        if realright not in allPointer:
                                                            allPointer.append(realright)
                                                        if x not in allPointer:
                                                            allPointer.append(x)
                                                        tmpStrStack.append(tmpStr)

                                                    else:
                                                        tmpStr = "store: " + "*" + realright + " = " + realleft + tmpSta.linenumber + "\\l "
                                                        if realright not in allPointer:
                                                            allPointer.append(realright)
                                                        if realleft not in allPointer:
                                                            allPointer.append(realleft)
                                                        tmpStrStack.append(tmpStr)
                                                        relationmap.pop(x,"")
                                                else:
                                                    tmpStr = "store: " + "*" + realright + " = " + x + tmpSta.linenumber + "\\l "
                                                    if realright not in allPointer:
                                                        allPointer.append(realright)
                                                    if x not in allPointer:
                                                        allPointer.append(x)
                                                    tmpStrStack.append(tmpStr)
                                                relationmap.pop(tmpStament.rightVal,"")
                                        else:
                                            realleft = relationmap.get(x, "")
                                            if len(realleft) != 0:
                                                if "*" in realleft:
                                                    tmpStr = "store: " + "*" + tmpStament.rightVal + " = " + x + tmpSta.linenumber + "\\l "
                                                    if tmpStament.rightVal not in allPointer:
                                                        allPointer.append(tmpStament.rightVal)
                                                    if x not in allPointer:
                                                        allPointer.append(x)
                                                    tmpStrStack.append(tmpStr)

                                                else:
                                                    tmpStr = "store: " + "*" + tmpStament.rightVal + " = " + realleft + tmpSta.linenumber + "\\l "
                                                    if tmpStament.rightVal not in allPointer:
                                                        allPointer.append(tmpStament.rightVal)
                                                    if realleft not in allPointer:
                                                        allPointer.append(realleft)
                                                    tmpStrStack.append(tmpStr)
                                                    relationmap.pop(x, "")
                                            else:
                                                tmpStr = "store: " + "*" + tmpStament.rightVal + " = " + x + tmpSta.linenumber + "\\l "
                                                if tmpStament.rightVal not in allPointer:
                                                    allPointer.append(tmpStament.rightVal)
                                                if x not in allPointer:
                                                    allPointer.append(x)
                                                tmpStrStack.append(tmpStr)


                                else:
                                    #第一条如果是load语句
                                    realx = relationmap.get(tmpStament.leftVal,"") # realx = *%3
                                    if "*" not in realx:
                                        tmpStr = "assign: " + y + " = " + realx + tmpSta.linenumber + "\\l "
                                        if y not in allPointer:
                                            allPointer.append(y)
                                        if realx not in allPointer:
                                            allPointer.append(realx)
                                        tmpStrStack.append(tmpStr)
                                        relationmap.pop(x,"")
                                    else:
                                        realx = realx.replace("*","") # %3
                                        realxx = relationmap.get(realx,"") # *%2
                                        if len(realxx) != 0:
                                            if "*" not in realxx:
                                                tmpStr = "load: " + y + " = " + "*" + realxx + tmpStament.linenumber + "\\l "
                                                if y not in allPointer:
                                                    allPointer.append(y)
                                                if realxx not in allPointer:
                                                    allPointer.append(realxx)
                                                tmpStrStack.append(tmpStr)
                                                relationmap.pop(realx,"")
                                            else:
                                                tmpStr = "load: " + y + " = " + "*" + realx + tmpStament.linenumber +"\\l "
                                                if y not in allPointer:
                                                    allPointer.append(y)
                                                if realx not in allPointer:
                                                    allPointer.append(realx)
                                                tmpStrStack.append(tmpStr)
                                        else:
                                            #不太应该出现
                                            print("zyy5")
                                            tmpStr = "load: " + y + " = " + "*" + realx + tmpStament.linenumber + "\\l "
                                            if y not in allPointer:
                                                allPointer.append(y)
                                            if realx not in allPointer:
                                                allPointer.append(realx)
                                            tmpStrStack.append(tmpStr)



                            else:
                                if tmpStament.Op == "getelementptr":
                                    # 非特殊情况
                                    # 照常处理
                                    tmpStr = "load: " + tmpStament.leftVal + " = " + "*" + tmpStament.rightVal + tmpStament.linenumber + "\\l "
                                    if tmpStament.leftVal not in allPointer:
                                        allPointer.append(tmpStament.leftVal)
                                    if tmpStament.rightVal not in allPointer:
                                        allPointer.append(tmpStament.rightVal)
                                    tmpStrStack.append(tmpStr)
                                else:
                                    #不是第一条load的话
                                    #先判断
                                    realx = relationmap.get(tmpStament.leftVal,"")
                                    if len(realx) == 0:
                                        #没有匹配上的关系，说明已经在其他步骤中被处理掉了，
                                        print("zyy1")
                                    else:
                                        if "*" in realx:
                                            realx = realx.replace("*","")
                                            realxx = relationmap.get(realx,"") #
                                            if len(realxx) != 0:
                                                if "*" not in realxx:
                                                    tmpStr = "load: " + tmpStament.leftVal + " = " + "*" + realxx + tmpStament.linenumber + "\\l "
                                                    if tmpStament.leftVal not in allPointer:
                                                        allPointer.append(tmpStament.leftVal)
                                                    if realxx not in allPointer:
                                                        allPointer.append(realxx)
                                                    tmpStrStack.append(tmpStr)
                                                    relationmap.pop(realx,"")
                                                else:
                                                    tmpStr = "load: " + tmpStament.leftVal + " = " + "*" + realx + tmpStament.linenumber + "\\l "
                                                    if tmpStament.leftVal not in allPointer:
                                                        allPointer.append(tmpStament.leftVal)
                                                    if realx not in allPointer:
                                                        allPointer.append(realx)
                                                    tmpStrStack.append(tmpStr)
                                            else:
                                                #不太应该出现
                                                print("zyy6")
                                                tmpStr = "load: " + tmpStament.leftVal + " = " + "*" + realx + tmpStament.linenumber + "\\l "
                                                if tmpStament.leftVal not in allPointer:
                                                    allPointer.append(tmpStament.leftVal)
                                                if realx not in allPointer:
                                                    allPointer.append(realx)
                                                tmpStrStack.append(tmpStr)

                                        else:
                                            #讲道理不应出现这种情况
                                            print("zyy2")
                                            #不过如果出现的话，应该是看成assign的语句
                                            #即，在getelementptr前出现的，且相关联的load可以看做assign
                                            tmpStr = "assign: " + tmpStament.leftVal + " = " + tmpStament.rightVal + tmpStament.linenumber + "\\l "
                                            if tmpStament.leftVal not in allPointer:
                                                allPointer.append(tmpStament.leftVal)
                                            if tmpStament.rightVal not in allPointer:
                                                allPointer.append(tmpStament.rightVal)
                                            tmpStrStack.append(tmpStr)

                            index = index + 1



                        toretStr = ""
                        while(len(tmpStrStack) != 0):
                            tmpStrtmp = tmpStrStack.pop()
                            toretStr += tmpStrtmp
                        # 清空map关系
                        relationmap.clear()
                        # 清空memvar
                        memvar.clear()
                        return toretStr
                    else:
                        #说明y是reg变量
                        index = 0
                        while(len(stackLV) != 0):
                            tmpStament = stackLV.pop()
                            if index == 0:
                                if tmpStament.Op == "getelementpr":#不太可能出现，但还是放上来了
                                    tmpStr = "load: " + tmpStament.leftVal + " = " + "*" + tmpStament.rightVal + tmpStament.linenumber + "\\l "
                                    if tmpStament.leftVal not in allPointer:
                                        allPointer.append(tmpStament.leftVal)
                                    if tmpStament.rightVal not in allPointer:
                                        allPointer.append(tmpStament.rightVal)
                                    tmpStrStack.append(tmpStr)

                                else:
                                    #load语句
                                    if tmpStament.leftVal == y:
                                        realx = relationmap.get(tmpStament.leftVal,"") # %a
                                        if "*" not in realx:
                                            #到这可以确定左边
                                            #接着确定右边
                                            realxx = relationmap.get(x,"") # %b
                                            if len(realxx) != 0:
                                                if "*" not in realxx:
                                                    tmpStr = "store: " + "*" + realx + " = " + realxx + tmpStament.linenumber + "\\l "
                                                    if realx not in allPointer:
                                                        allPointer.append(realx)
                                                    if realxx not in allPointer:
                                                        allPointer.append(realxx)
                                                    tmpStrStack.append(tmpStr)
                                                    relationmap.pop(x,"")
                                                else:
                                                    #如果realxx 是个 *%b 的类型
                                                    tmpStr = "store: " + "*" + realx + " = " + x + tmpStament.linenumber + "\\l "
                                                    if realx not in allPointer:
                                                        allPointer.append(realx)
                                                    if x not in allPointer:
                                                        allPointer.append(x)
                                                    tmpStrStack.append(tmpStr)
                                            else:
                                                #不太应该出现
                                                print("zyy7")
                                                tmpStr = "store: " + "*" + realx + " = " + x + tmpStament.linenumber + "\\l "
                                                if realx not in allPointer:
                                                    allPointer.append(realx)
                                                if x not in allPointer:
                                                    allPointer.append(x)
                                                tmpStrStack.append(tmpStr)
                                        else:
                                            #讲道理也不应该出现这种情况
                                            #store 左边也出现*的情况，即 会有**t2 = t1 的情况，所以要拆分
                                            print("zyy4")
                                            #如果出现的话 拆分 成load和 store两条
                                            #store在这部输出，load在下面的情况输出
                                            realxx = relationmap.get(x,"") # %b
                                            if len(realxx) != 0:
                                                if "*" not in realxx:
                                                    tmpStr = "store: " + "*" + y + " = " + realxx + tmpStament.linenumber + "\\l "
                                                    if y not in allPointer:
                                                        allPointer.append(y)
                                                    if realxx not in allPointer:
                                                        allPointer.append(realxx)
                                                    tmpStrStack.append(tmpStr)
                                                    relationmap.pop(x,"")
                                                else:
                                                    #如果realxx 是个 *%b 的类型
                                                    tmpStr = "store: " + "*" + y + " = " + x + tmpStament.linenumber + "\\l "
                                                    if y not in allPointer:
                                                        allPointer.append(y)
                                                    if x not in allPointer:
                                                        allPointer.append(x)
                                                    tmpStrStack.append(tmpStr)
                                            else:
                                                #不太应该出现
                                                print("zyy8")
                                                tmpStr = "store: " + "*" + y + " = " + x + tmpStament.linenumber + "\\l "
                                                if y not in allPointer:
                                                    allPointer.append(y)
                                                if x not in allPointer:
                                                    allPointer.append(x)
                                                tmpStrStack.append(tmpStr)


                            else:
                                if tmpStament.Op == "getelementpr":
                                    tmpStr = "load: " + tmpStament.leftVal + " = " + "*" + tmpStament.rightVal + tmpStament.linenumber + "\\l "
                                    if tmpStament.leftVal not in allPointer:
                                        allPointer.append(tmpStament.leftVal)
                                    if tmpStament.rightVal not in allPointer:
                                        allPointer.append(tmpStament.rightVal)
                                    tmpStrStack.append(tmpStr)
                                else:
                                    #load语句
                                    realx = relationmap.get(tmpStament.leftVal,"")
                                    if len(realx) == 0:
                                        #不进行处理
                                        continue
                                    else:
                                        if "*" in realx:
                                            realx = realx.replace("*","")
                                            realxx = relationmap.get(realx,"") #
                                            if len(realxx) != 0:
                                                if "*" not in realxx:
                                                    tmpStr = "load: " + tmpStament.leftVal + " = " + "*" + realxx + tmpStament.linenumber + "\\l "
                                                    if tmpStament.leftVal not in allPointer:
                                                        allPointer.append(tmpStament.leftVal)
                                                    if realxx not in allPointer:
                                                        allPointer.append(realxx)
                                                    tmpStrStack.append(tmpStr)
                                                    relationmap.pop(realx,"")
                                                else:
                                                    tmpStr = "load: " + tmpStament.leftVal + " = " + "*" + realx + tmpStament.linenumber + "\\l "
                                                    if tmpStament.leftVal not in allPointer:
                                                        allPointer.append(tmpStament.leftVal)
                                                    if realx not in allPointer:
                                                        allPointer.append(realx)
                                                    tmpStrStack.append(tmpStr)
                                            else:
                                                #不太应该出现
                                                print("zyy9")
                                                tmpStr = "load: " + tmpStament.leftVal + " = " + "*" + realx + tmpStament.linenumber + "\\l "
                                                if tmpStament.leftVal not in allPointer:
                                                    allPointer.append(tmpStament.leftVal)
                                                if realx not in allPointer:
                                                    allPointer.append(realx)
                                                tmpStrStack.append(tmpStr)

                                        else:
                                            #讲道理这种情况不应该出现，但是如果有 当做assign处理，跟line 777处理一样
                                            print("zyy3")
                                            tmpStr = "assign: " + tmpStament.leftVal + " = " + tmpStament.rightVal + tmpStament.linenumber + "\\l "
                                            if tmpStament.leftVal not in allPointer:
                                                allPointer.append(tmpStament.leftVal)
                                            if tmpStament.rightVal not in allPointer:
                                                allPointer.append(tmpStament.rightVal)
                                            tmpStrStack.append(tmpStr)
                            index = index + 1

                        toretStr = ""
                        while(len(tmpStrStack) != 0):
                            tmpStrtmp = tmpStrStack.pop()
                            toretStr += tmpStrtmp
                        # 清空map关系
                        relationmap.clear()
                        # 清空memvar
                        memvar.clear()
                        return toretStr


        # if a call function has return value
        if (len(res2) >= 5 and res2[4] == 'call'):
            tmpSta = Statement()
            tmpSta.Op = 'call'
            tmpSta.leftVal = res2[2]
            if res2[5] == 'zeroext':
                tmpSta.firstType = res2[6]
                funcName = res2[7].split('(')
                tmpSta.secondType = funcName[0]
            elif res2[5] == 'noalias':
                tmpSta.firstType = res2[6]
                funcName = res2[7].split('(')
                tmpSta.secondType = funcName[0]
            elif res2[5] == 'fastcc':
                tmpSta.firstType = res2[6]
                funcName = res2[7].split('(')
                tmpSta.secondType = funcName[0]
            elif '[' in res2[5]:
                tmpSta.firstType = res2[7].replace(']','')
                funcName = res2[8].split('(')
                tmpSta.secondType = funcName[0]
            else:
                tmpSta.firstType = res2[5]  # return type of function
                funcName = res2[6].split('(')
                tmpSta.secondType = funcName[0]  # functionName
            if '!dbg' in res2:
                tmpSta.linenumber = res2[-1]

            #如果asm在call函数中，不处理
            if 'asm' in res2:
                tmpStr = ""
                return tmpStr

            #如果一些奇怪的llvm的内在函数出现的话，直接无视掉
            if '@llvm.umul.with.overflow' in line:
                tmpStr = ""
                return tmpStr
            pppfunctionName=""
            tmpStrStack = []
            # 获取函数的形参列表
            funformalPara.clear()
            getFunctionPara(line)

            print("after getFunctionPara~~~~~~~~~~~~~~")
            if '...' in line:
                #print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                line1 = line.split("...")[-1].replace(") ", "")
                #print(line1)
                res = re.split("\(|\)", line1)
                for item in res:
                    #print("res item ", item)
                    spitem = re.split(",", item)
                    #print("spitem is ", spitem)
                    for item2 in spitem:
                        resz = re.split(" ", item2)
                        #print("~~~~resz is ", resz)
                        if len(resz) == 1:
                            if '@' in resz[0]:
                                #print("add ppp")
                                pppfunctionName = resz[0]
                                #print("PPP function Name is ", resz[0])
                        if len(resz) == 5:
                            if '@' in resz[1]:
                                pppfunctionName=resz[1]
                                #print("ppp function name could be ", resz[1])
                tmpSta.secondType = pppfunctionName


            tmpStr = "call: " + tmpSta.leftVal + " = " + tmpSta.firstType + " " + tmpSta.secondType + "("
            sizeOfFunctionPara = len(funformalPara)  # 函数形参个数
            #print("line is ", line)
            #print("~~~~~funciton formalPara is :")
            #for item in funformalPara:
            #    print("in call block~", item)
            if sizeOfFunctionPara == 0:
                tmpStr += ")" + tmpSta.linenumber + "\\l "
            else:
                #把形参填写完整
                for i in range(len(funformalPara)):
                    if i == len(funformalPara) -1:
                        #if '%call' in funformalPara[i]:
                        tmpStr += funformalPara[i] + ")"+tmpSta.linenumber+"\\l "
                    else:
                        if funformalPara[i] == 'dereferenceable':
                            tmpStr += "&"
                        else:
                            tmpStr += funformalPara[i] + ","
            #如果是malloc函数或者是new函数，得当做alloca处理，并自己生成一个变量
            if tmpSta.secondType == "@malloc" or tmpSta.secondType == "@_Znam" :
                tmpVal = "T" + int(time.time()).__str__()
                tmpStr1 = "alloca: " + tmpSta.leftVal + " = " + "&" + tmpVal + tmpSta.linenumber + "\\l "
                if tmpVal not in addressTaken:
                    addressTaken.append(tmpVal)
                if tmpSta.leftVal not in allPointer:
                    allPointer.append(tmpSta.leftVal)
                tmpStrStack.append(tmpStr1)
            else:
                tmpStrStack.append(tmpStr)

            #建立relationmap
            relationmap = {}
            memvar = []
            for i in range(len(stackLV)):
                if stackLV[i].Op == "load":
                    x = stackLV[i].rightVal
                    y = stackLV[i].leftVal
                    if x in memoryvar_for_each_fun or x in memvar or '@' in x:
                        # 说明x是mem变量
                        relationmap[y] = x  # y = x
                    else:
                        # 说明x是reg变量
                        relationmap[y] = "*" + x  # y = *x


                elif stackLV[i].Op == "getelementptr":
                    x = stackLV[i].rightVal
                    y = stackLV[i].leftVal
                    memvar.append(y)  # 把getelementptr的左值看成mem变量

            while(len(stackLV) != 0):
                tmpStament = stackLV.pop()
                if tmpStament.Op == "getelementptr":
                    tmpStr = "load: " + tmpStament.leftVal + " = " + "*" + tmpStament.rightVal + tmpStament.linenumber + "\\l "
                    if tmpStament.leftVal not in allPointer:
                        allPointer.append(tmpStament.leftVal)
                    if tmpStament.rightVal not in allPointer:
                        allPointer.append(tmpStament.rightVal)
                    tmpStrStack.append(tmpStr)
                else:
                    #load语句
                    realx = relationmap.get(tmpStament.leftVal,"")
                    if len(realx) != 0:
                        if "*" not in realx:
                            tmpStr = "assign: " + tmpStament.leftVal + " = " + realx + tmpStament.linenumber + "\\l "
                            if tmpStament.leftVal not in allPointer:
                                allPointer.append(tmpStament.leftVal)
                            if realx not in allPointer:
                                allPointer.append(realx)
                            tmpStrStack.append(tmpStr)
                        else:
                            realx = realx.replace("*","")
                            realxx = relationmap.get(realx,"")
                            if len(realxx) == 0:
                                #不太应该出现
                                print("zyy10")
                                tmpStr = "load: " + tmpStament.leftVal + " = " + "*" + realx + tmpStament.linenumber + "\\l "
                                if tmpStament.leftVal not in allPointer:
                                    allPointer.append(tmpStament.leftVal)
                                if realx not in allPointer:
                                    allPointer.append(realx)
                                tmpStrStack.append(tmpStr)
                            else:
                                if "*" not in realxx:
                                    tmpStr = "load: " + tmpStament.leftVal + " = " + "*" +realxx + tmpStament.linenumber + "\\l "
                                    if tmpStament.leftVal not in allPointer:
                                        allPointer.append(tmpStament.leftVal)
                                    if realxx not in allPointer:
                                        allPointer.append(realxx)
                                    relationmap.pop(realx,"")
                                    tmpStrStack.append(tmpStr)
                                else:
                                    tmpStr = "load: " + tmpStament.leftVal + " = " + "*" + realx + tmpStament.linenumber + "\\l "
                                    if tmpStament.leftVal not in allPointer:
                                        allPointer.append(tmpStament.leftVal)
                                    if realx not in allPointer:
                                        allPointer.append(realx)
                                    tmpStrStack.append(tmpStr)

            # 离开前要清空形参列表
            funformalPara.clear()
            toretStr = ""
            while(len(tmpStrStack) != 0):
                tmpStr = tmpStrStack.pop()
                toretStr += tmpStr

            relationmap.clear()
            memvar.clear()
            return toretStr


        # if is a call key word
        if (len(res2) >= 3 and res2[2] == 'call'):
            tmpSta = Statement()
            tmpSta.Op = 'call'
            if 'fastcc' in res2:
                tmpSta.firstType = res2[4]  # return type of function
                funcName = res2[5].split('(')
                tmpSta.secondType = funcName[0]  # functionName
            else:
                tmpSta.firstType = res2[3]  # return type of function
                funcName = res2[4].split('(')
                tmpSta.secondType = funcName[0]  # functionName

            if '!dbg' in res2:
                tmpSta.linenumber = res2[-1]
            if 'asm' in res2:
                tmpStr = ""
                return tmpStr
            pppfunctionName=""
            tmpStrStack = []
            # 获取函数的形参列表
            funformalPara.clear()
            getFunctionPara(line)

            if '...' in line:
                line1 = line.split("...")[-1].replace(") ", "")
                print(line1)
                res = re.split("\(|\)", line1)
                for item in res:
                    print("res item ", item)
                    spitem = re.split(",", item)
                    print("spitem is ", spitem)
                    for item2 in spitem:
                        resz = re.split(" ", item2)
                        print("~~~~resz is ", resz)
                        if len(resz) == 1:
                            if '@' in resz[0]:
                                print("add ppp")
                                pppfunctionName=resz[0]
                                print("PPP function Name is ", resz[0])
                        if len(resz) == 5:
                            if '@' in resz[1]:
                                pppfunctionName=resz[1]
                                print("ppp function name could be ", resz[1])

                tmpSta.secondType = pppfunctionName
            tmpStr = "call: " + "NULL" + " = " + tmpSta.firstType + " " + tmpSta.secondType + "("
            if '@llvm.dbg' in tmpSta.secondType:#过滤掉 含有llvm.dbg的语句
                if "@llvm.dbg.value" in tmpSta.secondType and "inttoptr" not in res2:
                    para = ""
                    if len(res2) == 16:
                        para = res2[6]
                    if len(res2) == 23:
                        para = res2[13]

                    paratmp = para.replace('-','').replace('%','')
                    paraaddr = para + ".addr"
                    if paratmp.isdigit() or 'call' in paratmp or 'conv' in paratmp or '.' in paratmp or paraaddr in FormalParameter or para in singleTon:
                        print("it should not be a formalParameter", para)
                    else:
                        if para not in FormalParameter and len(para) >=1 and '%' in para:
                            FormalParameter.append(para)
                tmpStr = ""
                funformalPara.clear()
                return tmpStr
            #print(tmpStr)
            sizeOfFunctionPara = len(funformalPara)  # 函数形参个数
            #for item in funformalPara:
            #    print("in void call function formalPara is", item)
            # 需要先判断是否有stackLV存在
            if sizeOfFunctionPara == 0:
                tmpStr += ")" + tmpSta.linenumber+"\\l "
            else:
                # 把形参填写完整
                for i in range(len(funformalPara)):
                    if i == len(funformalPara) - 1:
                        # if '%call' in funformalPara[i]:
                        tmpStr += funformalPara[i] + ")" + tmpSta.linenumber + "\\l "
                    else:
                        if funformalPara[i] == 'dereferenceable':
                            tmpStr += "&"
                        else:
                            tmpStr += funformalPara[i] + ","
            tmpStrStack.append(tmpStr)

            relationmap = {}
            memvar = []
            for i in range(len(stackLV)):
                if stackLV[i].Op == "load":
                    x = stackLV[i].rightVal
                    y = stackLV[i].leftVal
                    if x in memoryvar_for_each_fun or x in memvar or '@' in x:
                        # 说明x是mem变量
                        relationmap[y] = x  # y = x
                    else:
                        # 说明x是reg变量
                        relationmap[y] = "*" + x  # y = *x


                elif stackLV[i].Op == "getelementptr":
                    x = stackLV[i].rightVal
                    y = stackLV[i].leftVal
                    memvar.append(y)  # 把getelementptr的左值看成mem变量

            while (len(stackLV) != 0):
                tmpStament = stackLV.pop()
                if tmpStament.Op == "getelementptr":
                    tmpStr = "load: " + tmpStament.leftVal + " = " + "*" + tmpStament.rightVal + tmpStament.linenumber + "\\l "
                    if tmpStament.leftVal not in allPointer:
                        allPointer.append(tmpStament.leftVal)
                    if tmpStament.rightVal not in allPointer:
                        allPointer.append(tmpStament.rightVal)
                    tmpStrStack.append(tmpStr)
                else:
                    # load语句
                    realx = relationmap.get(tmpStament.leftVal, "")
                    if len(realx) != 0:
                        if "*" not in realx:
                            tmpStr = "assign: " + tmpStament.leftVal + " = " + realx + tmpStament.linenumber + "\\l "
                            if tmpStament.leftVal not in allPointer:
                                allPointer.append(tmpStament.leftVal)
                            if realx not in allPointer:
                                allPointer.append(realx)
                            tmpStrStack.append(tmpStr)
                        else:
                            realx = realx.replace("*", "")
                            realxx = relationmap.get(realx, "")
                            if len(realxx) == 0:
                                # 不太应该出现
                                print("zyy11")
                                tmpStr = "load: " + tmpStament.leftVal + " = " + "*" + realx + tmpStament.linenumber + "\\l "
                                if tmpStament.leftVal not in allPointer:
                                    allPointer.append(tmpStament.leftVal)
                                if realx not in allPointer:
                                    allPointer.append(realx)
                                tmpStrStack.append(tmpStr)
                            else:
                                if "*" not in realxx:
                                    tmpStr = "load: " + tmpStament.leftVal + " = " + "*" + realxx + tmpStament.linenumber + "\\l "
                                    if tmpStament.leftVal not in allPointer:
                                        allPointer.append(tmpStament.leftVal)
                                    if realxx not in allPointer:
                                        allPointer.append(realxx)
                                    relationmap.pop(realx,"")
                                    tmpStrStack.append(tmpStr)
                                else:
                                    tmpStr = "load: " + tmpStament.leftVal + " = " + "*" + realx + tmpStament.linenumber + "\\l "
                                    if tmpStament.leftVal not in allPointer:
                                        allPointer.append(tmpStament.leftVal)
                                    if realx not in allPointer:
                                        allPointer.append(realx)
                                    tmpStrStack.append(tmpStr)

            funformalPara.clear()
            toretStr = ""
            while(len(tmpStrStack) != 0):
                tmpStr = tmpStrStack.pop()
                toretStr += tmpStr

            relationmap.clear()
            memvar.clear()
            return toretStr

        # if is a ret instruction
        if (len(res2) >= 3 and res2[2] == 'ret'):
            tmpSta = Statement()
            tmpSta.Op = 'ret'
            if '!dbg' in res2:
                tmpSta.linenumber = res2[-1]

            tmpSta.firstType = res2[3]  # return value's type
            if tmpSta.firstType != 'void':
                tmpSta.leftVal = res2[4]

            tmpStrStack = []
            if tmpSta.firstType != 'void' and tmpSta.firstType != 'i32' and tmpSta.firstType != 'i8' and tmpSta.firstType != 'i64' and tmpSta.firstType != 'i16':
                tmpStr = "ret " + tmpSta.leftVal + tmpSta.linenumber + "\\l "
                tmpStrStack.append(tmpStr)
                relationmap = {}
                memvar = []
                for i in range(len(stackLV)):
                    if stackLV[i].Op == "load":
                        x = stackLV[i].rightVal
                        y = stackLV[i].leftVal
                        if x in memoryvar_for_each_fun or x in memvar or '@' in x:
                            # 说明x是mem变量
                            relationmap[y] = x  # y = x
                        else:
                            # 说明x是reg变量
                            relationmap[y] = "*" + x  # y = *x


                    elif stackLV[i].Op == "getelementptr":
                        x = stackLV[i].rightVal
                        y = stackLV[i].leftVal
                        memvar.append(y)  # 把getelementptr的左值看成mem变量

                while (len(stackLV) != 0):
                    tmpStament = stackLV.pop()
                    if tmpStament.Op == "getelementptr":
                        tmpStr = "load: " + tmpStament.leftVal + " = " + "*" + tmpStament.rightVal + tmpStament.linenumber + "\\l "
                        if tmpStament.leftVal not in allPointer:
                            allPointer.append(tmpStament.leftVal)
                        if tmpStament.rightVal not in allPointer:
                            allPointer.append(tmpStament.rightVal)
                        tmpStrStack.append(tmpStr)
                    else:
                        # load语句
                        realx = relationmap.get(tmpStament.leftVal, "")
                        if len(realx) != 0:
                            if "*" not in realx:
                                tmpStr = "assign: " + tmpStament.leftVal + " = " + realx + tmpStament.linenumber + "\\l "
                                if tmpStament.leftVal not in allPointer:
                                    allPointer.append(tmpStament.leftVal)
                                if realx not in allPointer:
                                    allPointer.append(realx)
                                tmpStrStack.append(tmpStr)
                            else:
                                realx = realx.replace("*", "")
                                realxx = relationmap.get(realx, "")
                                if len(realxx) == 0:
                                    # 不太应该出现
                                    print("zyy11")
                                    tmpStr = "load: " + tmpStament.leftVal + " = " + "*" + realx + tmpStament.linenumber + "\\l "
                                    if tmpStament.leftVal not in allPointer:
                                        allPointer.append(tmpStament.leftVal)
                                    if realx not in allPointer:
                                        allPointer.append(realx)
                                    tmpStrStack.append(tmpStr)
                                else:
                                    if "*" not in realxx:
                                        tmpStr = "load: " + tmpStament.leftVal + " = " + "*" + realxx + tmpStament.linenumber + "\\l "
                                        if tmpStament.leftVal not in allPointer:
                                            allPointer.append(tmpStament.leftVal)
                                        if realxx not in allPointer:
                                            allPointer.append(realxx)
                                        relationmap.pop(realx,"")
                                        tmpStrStack.append(tmpStr)
                                    else:
                                        tmpStr = "load: " + tmpStament.leftVal + " = " + "*" + realx + tmpStament.linenumber + "\\l "
                                        if tmpStament.leftVal not in allPointer:
                                            allPointer.append(tmpStament.leftVal)
                                        if realx not in allPointer:
                                            allPointer.append(realx)
                                        tmpStrStack.append(tmpStr)


                toretStr = ""
                while (len(tmpStrStack) != 0):
                    tmpStr = tmpStrStack.pop()
                    toretStr += tmpStr

                relationmap.clear()
                memvar.clear()
                return toretStr



#drivers
#path = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\linux\\drivers\\acpi\llvm8"
#path = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\linux\\drivers\\ata\llvm8"
#path = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\linux\\drivers\\atm\llvm8"
#path = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\linux\\drivers\\auxdisplay\llvm8"
#path = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\linux\\drivers\\base\llvm8"
#path = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\linux\\drivers\\bcma\llvm8"
#path = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\linux\\drivers\\block\llvm8"
#path = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\linux\\drivers\\bluetooth\llvm8"
#path = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\linux\\drivers\\cdrom\llvm8"
#path = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\linux\\drivers\\char\llvm8"
#path = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\linux\\drivers\\clk\llvm8"
#path = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\linux\\drivers\\clocksource\llvm8"
#path = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\linux\\drivers\\connector\llvm8"
#path = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\linux\\drivers\\cpufreq\llvm8"
#path = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\linux\\drivers\\cpuidle\llvm8"
#path = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\linux\\drivers\\crypto\llvm8"
#path = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\linux\\drivers\\dax\llvm8"
#path = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\linux\\drivers\\dca\llvm8"
#path = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\linux\\drivers\\devfreq\llvm8"
#path = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\linux\\drivers\\dma\llvm8"
path = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\linux\\drivers\\dma-buf\llvm8"











files = os.listdir(path)
count = 0
for file in files:
    filename = os.path.join(path, file)
    print("full path is" + filename)
    newFilename = filename.replace(".dot", "").replace("llvm8", "res") + "Res" + count.__str__() + ".dot"
    fobj = open(newFilename, 'wb+')
    # 读取文件
    with open(filename, 'r') as f:
        # 按行读入
        functionName = ""
        for line in f:
            if 'digraph' in line:
                findNameLine = re.split("'| ", line)
                functionName = findNameLine[4]
                print("function Name is " + functionName)
            # res = re.split('\| ', line)
            input2 = ''
            # 以label为关键字,判断是否为一个block
            if 'label' in line:
                # 如果label在，则可能是一个block
                if ' function' in line :
                    # 如果有function关键字在，说明仍不是一个block，则直接写入
                    input1 = bytes(line, encoding="utf8")
                    fobj.write(input1)
                elif '->' in line:
                    # 如果有label关键字在，且有->在，说明仍不是一个block，则直接写入
                    input11 = bytes(line, encoding="utf8")
                    fobj.write(input11)
                else:
                    # 说明是一个block，则需要进一步处理（但不排除，有其他case没有考虑到
                    line = line.replace('\l...', '')
                    strLine = line.split("\\l")  # 依据\l 进行划分
                    print(strLine[0])
                    input1 = bytes(strLine[0] + "\\l ", encoding="utf8")
                    fobj.write(input1)
                    i = 1
                    while i < len(strLine):
                        # 对每一行进行分析
                        tmpStr = analysisLine(strLine[i])

                        if tmpStr != None:
                            input1 = bytes(tmpStr, encoding="utf8")
                            fobj.write(input1)
                        i += 1
                    # 把一句写完整
                    tmpLast = strLine[-1]
                    # print(tmpLast)
                    input2 = bytes(tmpLast, encoding="utf8")
                    fobj.write(input2)
                    # 在离开一个block之前，把stackLV清空
                    stackLV.clear()


            # 没有label，直接写到新文件中
            else:
                strContent = ""
                # 如果碰到} 说明整个文件读结束，需要写入一个新的node1来传一些后续所需的信息
                if "}" in line:
                    for item in allPointer:
                        if item not in addressTaken:
                            strContent += item + " topLevel" + "\\l "

                    # print addressTaken variables
                    for item in addressTaken:
                        strContent += item + " addressTaken" + "\\l "
                    # print function's parameters
                    for item in FormalParameter:
                        strContent += item + " formarlParameter" + "\\l "

                    strBlock = "\tNode1 [shape=record,label=" + '"' + "{" + strContent + "}" + '"' + "];"
                    input3 = bytes(strBlock, encoding="utf8")
                    fobj.write(input3)
                input1 = bytes(line, encoding="utf8")
                fobj.write(input1)

            # to write a tributary block for displaying addressTaken and toplevel
            # Node1 [shape=record,label="{testest zyy\l }"];

        # 在这里写 singleTon文件？
        strSingleTon = ""
        for itemglobal1 in allPointer:
            if '@' in itemglobal1 and itemglobal1 not in singleTon:
                singleTon.append(itemglobal1)
        for itemglobal2 in addressTaken:
            if '@' in itemglobal2 and itemglobal2 not in singleTon:
                singleTon.append(itemglobal2)

        for item in singleTon:#所有的local variable都看成是singleTon
            strSingleTon += functionName + "." + item + "\n"
        fsT.write(strSingleTon)

    # 在离开一个file之前把FormalParameter清空
    FormalParameter.clear()
    # 把allPointer 清空
    allPointer.clear()
    # 把 addressTaken清空
    addressTaken.clear()
    # 把 singleTon 清空
    singleTon.clear()
    # 把 notSingleTon清空
    notSingleTon.clear()

    count += 1
    fobj.close()
fsT.close()