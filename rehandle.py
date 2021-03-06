#！/usr/bin/env python
#!-*-coding:utf-8 -*-
#!@Create :2019/8/13 13:59
#!@Author : zyy
#!@File   : rehandle.py
import os
import re

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
#用来存assign关系的map
assignmap = {}


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
    res = re.split("\(|\)", line)
    for item in res:
        print("res item ", item)
        spitem = re.split(",", item)
        for item2 in spitem:
            resz = re.split(" ", item2)
            if len(resz) == 1:
                if '%' in resz[0]:
                    funformalPara.append(resz[0])
            print("~~~~resz is ", resz)

def analysisLine(line):
    # split each line to get what we want
    res2 = re.split(",| |!", line)
    print(res2)
    if (len(res2) >= 2 and 'alloca' in res2[1]):
        tmpSta = Statement()
        tmpSta.leftVal = res2[2]
        tmpSta.Op = 'alloca'
        if len(res2) == 3:
            memoryvar_for_each_fun.append(tmpSta.leftVal)
            tmpStr = res2[1] + " " + res2[2] + "\\l "
            return tmpStr
        if len(res2) == 6:
            tmpSta.rightVal = res2[4]
            if '!' in line:
                tmpSta.linenumber = res2[-1]
            memoryvar_for_each_fun.append(tmpSta.leftVal)
            memoryvar_for_each_fun.append(tmpSta.rightVal.replace("&",""))
            tmpStr = "alloca: " + tmpSta.leftVal + " = " + tmpSta.rightVal + "!" + tmpSta.linenumber + "\\l "
            return tmpStr

    if (len(res2) >= 2 and 'load' in res2[1]):
        tmpSta = Statement()
        tmpSta.Op = 'load'
        tmpSta.leftVal = res2[2]
        tmpSta.rightVal = res2[4]
        if '!' in line:
            tmpSta.linenumber = res2[-1]
        nostar = tmpSta.rightVal.replace("*","")
        realright = assignmap.get(nostar,"")
        if len(realright) == 0:
            #说明没有能够匹配上的，直接写回
            tmpStr = "load: " + tmpSta.leftVal + " = " + tmpSta.rightVal + "!" + tmpSta.linenumber + "\\l "
            return tmpStr
        else:
            #说明能够匹配的上，则取代并写回
            tmpStr = "load: " + tmpSta.leftVal + " = " + "*" + realright + "!" + tmpSta.linenumber + "\\l "
            return tmpStr

    if (len(res2) >=2 and 'cmp' in res2[1]):
        tmpSta = Statement()
        tmpSta.Op = 'cmp'
        tmpSta.leftVal = res2[2]
        if '!' in line:
            tmpSta.linenumber = res2[-1]
        tmpStr = "cmp: " + tmpSta.leftVal + "!" + tmpSta.linenumber + "\\l "
        return tmpStr

    if (len(res2) >= 2 and 'store' in res2[1]):
        tmpSta = Statement()
        tmpSta.Op = 'store'
        tmpSta.leftVal = res2[2]
        tmpSta.rightVal = res2[4]
        if '!' in line:
            tmpSta.linenumber = res2[-1]
        realright = assignmap.get(tmpSta.rightVal,"")
        if len(realright) == 0:
            #说明右边没有匹配
            #再看左边
            nostar = tmpSta.leftVal.replace("*","")
            realleft = assignmap.get(nostar,"")
            if len(realleft) == 0:
                #说明左边也没有匹配
                tmpStr = "store: " + tmpSta.leftVal + " = " + tmpSta.rightVal + "!" + tmpSta.linenumber + "\\l "
                return tmpStr
            else:
                #左边匹配上了
                tmpStr = "store: " + "*" + realleft + " = " + tmpSta.rightVal + "!" + tmpSta.linenumber + "\\l "
                return tmpStr
        else:
            #说明右边匹配上了
            #再看左边
            nostar = tmpSta.leftVal.replace("*","")
            realleft = assignmap.get(nostar,"")
            if len(realleft) == 0:
                #说明左边也没有匹配
                tmpStr = "store: " + tmpSta.leftVal + " = " + realright + "!" + tmpSta.linenumber + "\\l "
                return tmpStr
            else:
                #左边匹配上了
                tmpStr = "store: " + "*" + realleft + " = " + realright + "!" + tmpSta.linenumber + "\\l "
                return tmpStr

    if (len(res2) >= 2 and 'assign' in res2[1]):
        tmpSta = Statement()
        tmpSta.Op = 'assign'
        tmpSta.leftVal = res2[2]
        tmpSta.rightVal = res2[4]
        if '!' in line:
            tmpSta.linenumber = res2[-1]
        if tmpSta.leftVal in memoryvar_for_each_fun or '@' in tmpSta.leftVal:
            #说明左值是mem变量，不用加入直接return
            tmpStr = "assign: " + tmpSta.leftVal + " = " + tmpSta.rightVal + "!" + tmpSta.linenumber + "\\l "
            return tmpStr
        else:
            #说明左值是reg变量，加入assignmap中
            assignmap[tmpSta.leftVal] = tmpSta.rightVal
            print("in analysis assignmap: " ,assignmap.values())

    # if a call function has return value
    if (len(res2) >= 2 and 'call' in res2[1]):
        tmpSta = Statement()
        tmpSta.Op = 'call'
        tmpSta.leftVal = res2[2]
        tmpSta.firstType = res2[4]
        funcName = res2[5].split('(')
        tmpSta.secondType = funcName[0]  # functionName
        if '!' in line:
            tmpSta.linenumber = res2[-1]

        tmpStr = "call: " + tmpSta.leftVal + " = " + tmpSta.firstType + tmpSta.secondType + "("
        # 获取函数的形参列表
        funformalPara.clear()
        getFunctionPara(line)
        if len(funformalPara) == 0:
            tmpStr += ")" + "!" + tmpSta.linenumber + "\\l "
        else:
            for i in range(len(funformalPara)):
                if i == len(funformalPara) - 1:
                    if '&' in funformalPara[i]:
                        nosharp = funformalPara[i].replace("&","")
                        realpara = assignmap.get(nosharp,"")
                        if len(realpara) == 0:
                            tmpStr += funformalPara[i] + ")" + "!" + tmpSta.linenumber + "\\l "
                        else:
                            tmpStr += "&" + realpara + ")" + "!" + tmpSta.linenumber + "\\l "
                    else:
                        realpara = assignmap.get(funformalPara[i], "")
                        if len(realpara) == 0:
                            tmpStr += funformalPara[i] + ")" + "!" + tmpSta.linenumber + "\\l "
                        else:
                            tmpStr += realpara + ")" + "!" + tmpSta.linenumber + "\\l "
                else:
                    if '&' in funformalPara[i]:
                        nosharp = funformalPara[i].replace("&","")
                        realpara = assignmap.get(nosharp,"")
                        if len(realpara) == 0:
                            tmpStr += funformalPara[i] + ","
                        else:
                            tmpStr += "&" + realpara + ","
                    else:
                        realpara = assignmap.get(funformalPara[i], "")
                        if len(realpara) == 0:
                            tmpStr += funformalPara[i] + ","
                        else:
                            tmpStr += realpara + ","


        funformalPara.clear()
        return tmpStr


    if (len(res2) >= 2 and res2[1] == 'ret'):
        tmpSta = Statement()
        tmpSta.Op = 'ret'
        tmpSta.leftVal = res2[2]
        if '!' in line:
            tmpSta.linenumber = res2[-1]
        realret = assignmap.get(tmpSta.leftVal,"")
        if len(realret) == 0:
            #说明没有匹配上
            tmpStr = "ret " + tmpSta.leftVal + "!" + tmpSta.linenumber + "\\l "
            return tmpStr
        else:
            #说明匹配上了
            tmpStr = "ret " + realret + "!" + tmpSta.linenumber + "\\l "
            return tmpStr





#path = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\\httpd\debug\\res"
#path = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\\vim\\res"


#linux
#path = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\linux\\arch\\res"
#path = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\linux\\block\\res"
#path = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\linux\certs\\res"
#path = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\linux\\crypto\\res"
#path = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\linux\\fs\\res"
#path = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\linux\init\\res"
#path = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\linux\\ipc\\res"
#path = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\linux\\kernel\\res"
#path = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\linux\\lib\\res"
#path = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\linux\\mm\\res"
#path = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\linux\\net\\res"
#path = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\linux\\security\\res"
#path = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\linux\\sound\\res"
#path = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\linux\\virt\\res"



#####firefox

#path = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\\firefox\\accessiable\\res"
#path = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\\firefox\\browser\\res"
#path = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\\firefox\\buildunix\\res"
#path = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\\firefox\\config\\res"
#path = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\\firefox\\db_xpfe_hal\\res"
#path = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\\firefox\\devtools\\res"
#path = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\\firefox\\docshell\\res"
#path = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\\firefox\\dom\\res"
#path = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\\firefox\\editor\\res"
#path = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\\firefox\\firefox\\res"
#path = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\\firefox\\gfx\\res"
#path = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\\firefox\\image\\res"
#path = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\\firefox\\intl\\res"
#path = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\\firefox\\ipc\\res"
#path = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\\firefox\\js\\res"
#path = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\\firefox\\layout\\res"
#path = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\\firefox\\media\\res"
#path = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\\firefox\\memory\\res"
#path = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\\firefox\\mfbt\\res"
#path = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\\firefox\\modules\\res"
#path = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\\firefox\\mozglue\\res"
#path = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\\firefox\\network\\res"
#path = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\\firefox\\oth_license\\res"
#path = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\\firefox\\parser\\res"
#path = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\\firefox\\security\\res"
#path = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\\firefox\\startupcache_chrome\\res"
#path = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\\firefox\\storage\\res"
#path = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\\firefox\\third_party\\res"
#path = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\\firefox\\toolkit\\res"
#path = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\\firefox\\uri_caps\\res"
#path = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\\firefox\\widget\\res"
#path = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\\firefox\\x86_64_unknown\\res"
path = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\\firefox\\xpcom\\res"


files = os.listdir(path)

for file in files:
    filename = os.path.join(path, file)
    #print("full path is" + filename)
    newFilename = filename.replace(".dot", "").replace("res", "newres") + ".dot"
    fobj = open(newFilename, 'wb+')
    # 读取文件
    with open(filename, 'r') as f:
        # 按行读入
        functionName = ""
        for line in f:
            if 'digraph' in line:
                findNameLine = re.split("'| ", line)
                functionName = findNameLine[4]
                #print("function Name is " + functionName)
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
                    if 'Node1' in line:
                        #说明是最后一个block了，直接写入
                        input11 = bytes(line, encoding="utf8")
                        fobj.write(input11)
                    else:
                        line = line.replace('\l...', '')
                        strLine = line.split("\\l")  # 依据\l 进行划分
                        print(strLine[0])
                        input1 = bytes(strLine[0] + "\\l ", encoding="utf8")
                        fobj.write(input1)
                        i = 1
                        while i < len(strLine):
                            # 对每一行进行分析
                            print("strLine[i] is :" ,strLine[i])
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
                        # 在离开一个block之前，把map关系清空
                        print("assignmap: ",assignmap.values())
                        assignmap.clear()


            # 没有label，直接写到新文件中
            else:
                input1 = bytes(line, encoding="utf8")
                fobj.write(input1)

            # to write a tributary block for displaying addressTaken and toplevel
            # Node1 [shape=record,label="{testest zyy\l }"];



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
    # 清空
    memoryvar_for_each_fun.clear()

    fobj.close()
