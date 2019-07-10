# ！/usr/bin/env python
# !-*-coding:utf-8 -*-
# !@Create :2019/6/17 21:00
# !@Author : zyy
# !@File   : handleMultiFile.py
import os
import re
import time

# 输入的dot文件
# filename = 'llvm8/testEx1fun3.dot'

# 输出想要的dot文件
# newFilename = 'llvm8/testEx1fun3test.dot'
# fobj = open(newFilename, 'wb+')

# 输出singleTon的结果txt文件
#singleTontxt = 'D:\Ouroboros\codes\Ouroboros-Project\\testfile\\vim\\res\singleTonResult.txt'
#singleTontxt = 'D:\Ouroboros\codes\Ouroboros-Project\\testfile\\httpd\debug\\res\singleTonResult.txt'
singleTontxt = 'D:\Ouroboros\codes\Ouroboros-Project\\testfile\\firefox\\toolkit\\res\singleTonResult.txt'
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
                if ('%' in resz[1] or '@' in resz[1]):
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
                if resz[2] == 'zeroext' or resz[2] == 'signext':
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
            if 'i32]' in res2 or 'i32*]' in res2 or 'i32**]' in res2 or 'i8]' in res2:
                tmpSta.firstType = res2[7].replace(']', '')
            else:
                tmpSta.firstType = res2[5]
            # 如果有addr属性 说明是形参
            if 'addr' in tmpSta.leftVal:
                if tmpSta.leftVal not in FormalParameter:
                    FormalParameter.append(tmpSta.leftVal)

            # skip int type variable 跳过int类型的变量
            if tmpSta.firstType != 'i32' and tmpSta.firstType != 'i8':
                tmpStr = "alloca:" + tmpSta.firstType + " " + tmpSta.leftVal + "\\l "
                allPointer.append(tmpSta.leftVal)
                return tmpStr

        # skip return 0 case
        if (len(res2) >= 3 and res2[2] == 'store' and res2[4] == 0):
            # continue
            # print("alloca statement2")
            return "zero" + "\\l "

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
                    if len(res2) == 30:
                        tmpSta.rightVal = res2[17]
                        tmpSta.secondType = res2[23].replace(")","")
                    elif len(res2) == 32:
                        tmpSta.rightVal = res2[17]
                        tmpSta.secondType = res2[26].replace(")","")
                    elif len(res2) == 33:
                        tmpSta.rightVal = res2[17]
                        tmpSta.secondType = res2[26].replace(")","")
                    elif len(res2) == 36:
                        tmpSta.rightVal = res2[17]
                        tmpSta.secondType = res2[29].replace(")","")
                    elif len(res2) == 42:
                        tmpSta.rightVal = res2[17]
                        tmpSta.secondType = res2[35].replace(")","")
                    else:
                        tmpSta.rightVal = res2[13]
                        tmpSta.secondType = res2[19].replace(")","") #index
                else:
                    if len(res2) == 19 and 'x' in res2:
                        tmpSta.firstType = ""
                        tmpSta.rightVal = res2[12]
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
                    if len(res2) == 19:
                        tmpSta.secondType = res2[15]  # it means the index of a pointer variable in the struct object
                        tmpSta.linenumber = res2[-1]
                    if len(res2) == 16:
                        tmpSta.secondType = res2[12]  # it means the index of a pointer variable in the struct object
                        tmpSta.linenumber = res2[-1]
                else:
                    if len(res2) == 16:
                        tmpSta.secondType = res2[15]  # it means the index of a pointer variable in the struct object
                    if len(res2) == 13:
                        tmpSta.secondType = res2[12]  # it means the index of a pointer variable in the struct object
            else:  # it means an array type
                print('contains an array type: ',res2)
                if '!dbg' in res2:
                    if len(res2) == 22:
                        tmpSta.rightVal = res2[12]
                        tmpSta.secondType = res2[18]
                        tmpSta.firstType = res2[7].replace(']','')
                    if len(res2) == 27:
                        tmpSta.rightVal = res2[17]
                        tmpSta.secondType = res2[23]
                        tmpSta.firstType = res2[10].replace(']','')
                else:
                    if len(res2) == 19:
                        tmpSta.rightVal = res2[12]
                        tmpSta.secondType = res2[18]
                        tmpSta.firstType = res2[7].replace(']','')
                    if len(res2) == 24:  # it means a two-dimensional array
                        tmpSta.firstType = res2[10].replace(']', '')
                        tmpSta.rightVal = res2[17]
                        tmpSta.secondType = res2[23]

            stackLV.append(tmpSta)

        # if a call function has return value
        if (len(res2) >= 5 and res2[4] == 'call'):
            tmpSta = Statement()
            tmpSta.Op = 'call'
            tmpSta.leftVal = res2[2]
            if res2[5] == 'zeroext':
                tmpSta.firstType = res2[6]
                funcName = res2[7].split('(')
                tmpSta.secondType = funcName[0]
            else:
                tmpSta.firstType = res2[5]  # return type of function
                funcName = res2[6].split('(')
                tmpSta.secondType = funcName[0]  # functionName
            if '!dbg' in res2:
                tmpSta.linenumber = res2[-1]
            pppfunctionName=""
            # 获取函数的形参列表
            funformalPara.clear()
            getFunctionPara(line)
            print("after getFunctionPara~~~~~~~~~~~~~~")
            if '...' in line:
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
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
                                pppfunctionName = resz[0]
                                tmpSta.secondType = pppfunctionName
                                print("PPP function Name is ", resz[0])
                        if len(resz) == 5:
                            if '@' in resz[1]:
                                pppfunctionName=resz[1]
                                print("ppp function name could be ", resz[1])


            tmpStr = "call: " + tmpSta.leftVal + " = " + tmpSta.firstType + " " + tmpSta.secondType + "("
            actualParaToWrite = ""  # 待写的实参
            sizeOfFunctionPara = len(funformalPara)  # 函数形参个数
            print("line is ", line)
            print("~~~~~funciton formalPara is :")
            for item in funformalPara:
                print("in call block~", item)

            if sizeOfFunctionPara == 0:
                tmpStr += ")" +tmpSta.linenumber+ "\\l "
            else:

                # 在调用该函数处时，输出 传入该函数的实参 实现：
                print("size of stackLV is ", len(stackLV))
                while (len(stackLV) != 0):
                    # print("1212121212")
                    tmpStament1 = stackLV[-1]
                    # print("leftval is ",tmpStament1.leftVal,"  actualParaToWrite is ", actualParaToWrite)
                    # 如果每次进来 代写实参不是空的且不是当前指令的左操作数

                    if len(actualParaToWrite) != 0 and actualParaToWrite != tmpStament1.leftVal:
                        if len(stackLV) >= 2:
                            tmpStament3 = stackLV[-2]
                            #额外考虑类似于下面的例子
                            #  %20 = load i8**, i8*** %argv.addr, align 8
                            #%21 = load i32, i32* %i, align 4
                            #%idxprom = sext i32 %21 to i64
                            #%arrayidx = getelementptr inbounds i8*, i8** %20, i64 %idxprom
                            #%22 = load i8*, i8** %arrayidx, align 8

                            if tmpStament3.leftVal == actualParaToWrite:
                                stackLV.pop()
                                continue

                        if sizeOfFunctionPara == 1:
                            tmpStr += actualParaToWrite + ")" +tmpSta.linenumber+ "\\l "
                            print("the whole tmpStr1111 is ", tmpStr)
                            print("here size is 111111111111111111111111111")
                            break  # 写完最后一个实参 要break掉
                        else:
                            tmpStr += actualParaToWrite + ","
                            print("in call inst tmp tmpStr is ", tmpStr)
                            sizeOfFunctionPara = sizeOfFunctionPara - 1
                            actualParaToWrite = ""
                            continue

                    elif len(actualParaToWrite) != 0 and actualParaToWrite == tmpStament1.leftVal:
                        # 如果代写的实参不空但是为当前指令的左操作数，需要把代写实参重新赋值
                        actualParaToWrite = tmpStament1.rightVal
                        print("actToDW not null ,and is ", actualParaToWrite)
                        if len(stackLV) == 1:
                            # 如果只剩当前的这个条语句了，也是要写
                            tmpStr += actualParaToWrite + ")" +tmpSta.linenumber+ "\\l "
                            print("here size is 11222222NULL", tmpStr)
                        stackLV.pop()
                        continue

                    if tmpStament1.leftVal in funformalPara:
                        # 如果当前指令的左操作数在形参列表中出现
                        # 就把当前指令的右操作数 用作实参
                        actualParaToWrite = tmpStament1.rightVal
                        print("leftval in funformalPara and the actParaToW is ", actualParaToWrite)
                        #删去已经匹配上的形参
                        funformalPara.remove(tmpStament1.leftVal)
                        # 并且pop掉当前的指令
                        stackLV.pop()
                        # 需要判断一下是否还能继续往上回溯
                        if len(stackLV) != 0:
                            tmpStament2 = stackLV[-1]
                            if tmpStament2.leftVal == actualParaToWrite:
                                # 相等，说明还可以回溯
                                print("should be continue")
                                continue
                            else:
                                if sizeOfFunctionPara == 1:
                                    tmpStr += actualParaToWrite + ")" +tmpSta.linenumber+ "\\l "
                                    print("the whole tmpStr22222 is ", tmpStr)
                                    print(tmpStr)
                                    print("here size is 111111111111111111111111111")
                                    break  # 写完最后一个实参 要break掉
                        else:
                            tmpStr += actualParaToWrite + ")" +tmpSta.linenumber+ "\\l "
                            print("the whole tmpStr3333 is ", tmpStr)
                            print(tmpStr)
                            print("here size is 111111111111111111111111111")
                            break  # 写完最后一个实参 要break掉
                    else:
                        if len(stackLV) != 0:
                            stackLV.pop()

                '''
                for i in range(len(stackLV)):
                    #为了防止出现连续多个call函数存在而导致出现多余逗号的错误，加入了statement Op的 判断
                    if stackLV[i].Op != 'call':
                        #如果是最后一行，需要特殊处理 加上括号 \\l 等
                        if i == len(stackLV)-1:
                            tmpleftVal = stackLV[i].leftVal#当前语句的左值
                            flag = 0#标志，判断是否出现了特例
                            for j in range(len(stackLV)):
                                if tmpleftVal == stackLV[j].rightVal:
                                    # 如果当前语句的左值等于某个语句的右值，说明是个特例
                                    tmpStr += "*"+stackLV[i].rightVal + ")" + "\\l "
                                    flag =1 #设置为1，说明出现了特例
                                    break
                            if flag == 0:#只对非特例进行处理
                                tmpStr += stackLV[i].rightVal + ")" + "\\l "
                        else:
                            tmpleftVal = stackLV[i].leftVal
                            flag = 0
                            for j in range(len(stackLV)):
                                if tmpleftVal == stackLV[j].rightVal:
                                    #如果当前语句的左值等于某个语句的右值，说明是个特例
                                    tmpStr += "*"+stackLV[i].rightVal+", "
                                    flag = 1
                                    break

                            if flag == 0:#只对非特例处理
                                if i == 0:#刚开始要写
                                    tmpStr += stackLV[i].rightVal + ", "
                                if i >= 1:#0之后，把中间过程的语句省略掉
                                    if stackLV[i].rightVal != stackLV[i-1].leftVal:
                                        tmpStr += stackLV[i].rightVal + ", "

                #remove all load statement
                for i in range(len(stackLV)):
                    stackLV.pop()
                '''

            # 用来区分是否是malloc或者new类型，如果是则不把call语句加入stackLV，需要进行特殊的单独处理
            #
            if 'malloc' in line or 'Znam' in line:
                tmpStr = ""
            else:
                print("ddddddddddddddddddd", tmpSta.leftVal)
                # 2019.6.26 尝试不要将call 语句加入stackLV
                # stackLV.append(tmpSta)

            #在离开前需要检查一下tmpStr是否为完整的句子
            #需要把形参中为%call等形式的参数放进去，6.29修改正，把剩余形参都加入进去
            if ')!' not in tmpStr:
                #说明是不完整的句子，然后把剩余的形参都输出
                for i in range(len(funformalPara)):
                    if i == len(funformalPara) -1:
                        #if '%call' in funformalPara[i]:
                        tmpStr += funformalPara[i] + ")"+tmpSta.linenumber+"\\l "
                    else:
                        tmpStr += funformalPara[i] + ","



            # 离开前要清空形参列表
            funformalPara.clear()
            print("in call case before return tmpStr is", tmpStr)
            return tmpStr

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
                            if tmpStament1.secondType.isdigit():
                                tmpStr = "cmp: "+ tmpStament1.rightVal+ "."+ tmpStament1.secondType + tmpSta.linenumber+"\\l "
                            else:
                                tmpStr = "cmp: " + tmpStament1.rightVal + tmpSta.linenumber + "\\l "
                            return tmpStr

        #bitcast instruction
        if (len(res2) >=5 and res2[4] == 'bitcast'):
            tmpSta = Statement()
            tmpSta.Op = 'bitcast'
            tmpSta.leftVal = res2[2]
            tmpSta.firstType = res2[5]
            tmpSta.rightVal = res2[6]
            tmpSta.secondType = res2[8]
            if len(stackLV) >= 1:
                tmpStament1 = stackLV[-1]
                if tmpStament1.leftVal == tmpSta.rightVal:
                    stackLV[-1].leftVal = tmpSta.leftVal
        # when we meet the key word 'store', we should check the 'stackLV'. When the size of stackLV is 1, that is to say it's assignment .
        # When the size of stackLV is 2, we will go further to determine it's a deref statement or not.
        if (len(res2) >= 3 and res2[2] == 'store'):

            tmpSta = Statement()
            tmpSta.Op = 'store'
            tmpSta.leftVal = res2[4]
            tmpSta.firstType = res2[3]
            if 'getelementptr' in res2:
                if len(res2) == 35:
                    tmpSta.rightVal = res2[16]
                    tmpSta.secondType = res2[28].replace(")","")
                elif len(res2) == 41:
                    tmpSta.rightVal = res2[16]
                    tmpSta.secondType = res2[34].replace(")","")
                else:
                    tmpSta.rightVal = res2[12]
                    tmpSta.secondType = res2[18].replace(")","")#index
            else:
                tmpSta.rightVal = res2[7]
                tmpSta.secondType = res2[6]
            if '!dbg' in res2:
                tmpSta.linenumber = res2[-1]

            # if there is no 'load' keyword
            if (len(stackLV) == 0):
                # judge whether it is an alloca statement or not
                if (tmpSta.firstType == 'i32*' or tmpSta.firstType == 'i32**'):
                    tmpLeftVal = tmpSta.leftVal + ".addr"

                    if '.addr' in tmpSta.rightVal:
                        tmpSta_rightVal = tmpSta.rightVal.replace(".addr","")
                        tmpSta_leftVal = tmpSta.leftVal.replace(tmpSta_rightVal,"")
                        if tmpSta_leftVal.isdigit():
                            print("maybe this case: store i32 * % retval1, i32 ** % retval.addr, do nothing")
                            return ""
                    #也有可能会存在这种例子，store i32 * % retval1, i32 ** % retval.addr, align 8

                    if tmpLeftVal == tmpSta.rightVal:
                        print("........................")
                    else:
                        # 如果左操作数是个一个call函数的返回值的话，就是要记作assign
                        if 'call' in tmpSta.leftVal:
                            tmpStr = "assign: " + tmpSta.rightVal + " = " + tmpSta.leftVal + tmpSta.linenumber+"\\l "
                            if tmpSta.rightVal not in allPointer:
                                allPointer.append(tmpSta.rightVal)
                            if tmpSta.leftVal not in allPointer:
                                allPointer.append(tmpSta.leftVal)
                            return tmpStr
                        else:

                            tmpStr = "alloca:" + ' ' + tmpSta.rightVal + " = " + tmpSta.leftVal + tmpSta.linenumber+"\\l "
                            print("stackLv =0 " + tmpStr)
                            # 在这里判断是否为 非singleton
                            # 需要区分 &n 和真正new、malloc的类型
                            # &n 的类型 语句的左值 是% + 变量名（非数字）
                            # new、malloc的类型 语句的左值是% + 数字
                            # 先去除%号，得到原始内容
                            tmpleftValStr = tmpSta.leftVal.replace('%', '')
                            if tmpleftValStr.isdigit():
                                # 如果全是数字，则是new、malloc类型
                                notSingleTon.append(tmpSta.rightVal)

                            if tmpSta.leftVal not in addressTaken:
                                addressTaken.append(tmpSta.leftVal)
                            if tmpSta.rightVal not in allPointer:
                                allPointer.append(tmpSta.rightVal)
                            return tmpStr

            # if there is only one 'load' keyword in the stack
            # or if there is a 'call' instruction in the stack
            if (len(stackLV) == 1):
                # fetch the top value of stack
                tmpStament = stackLV.pop()
                if tmpStament.Op == 'getelementptr':
                    if tmpStament.firstType != 'i32':
                        if tmpSta.firstType != 'i32':  # 同时要求store语句的前半句，不能为int类型
                            if tmpStament.leftVal == tmpSta.rightVal:
                                if tmpSta.leftVal == 'null':
                                    tmpStr = "assign: " + tmpStament.rightVal + "." + tmpStament.secondType + " = " + "NULL" + tmpSta.linenumber + "\\l "
                                else:
                                    tmpStr = "alloca: " + tmpStament.rightVal + "." + tmpStament.secondType + " = " + tmpSta.leftVal + tmpSta.linenumber+"\\l "
                                    if tmpSta.leftVal not in addressTaken:
                                        addressTaken.append(tmpSta.leftVal)
                                tmpPointer = tmpStament.rightVal + "." + tmpStament.secondType
                                if tmpPointer not in allPointer:
                                    allPointer.append(tmpPointer)
                                return tmpStr
                            if tmpStament.leftVal == tmpSta.leftVal:
                                tmpStr = "alloca: " + tmpSta.rightVal + " = " + tmpStament.rightVal + "." + tmpStament.secondType + tmpSta.linenumber+"\\l "
                                tmpPointer = tmpStament.rightVal + "." + tmpStament.secondType
                                if tmpPointer not in addressTaken:
                                    addressTaken.append(tmpPointer)
                                tmpPointer = tmpStament.rightVal + "." + tmpStament.secondType
                                if tmpPointer not in allPointer:
                                    allPointer.append(tmpPointer)
                                return tmpStr
                elif tmpStament.Op == 'call':#这种情况不会再出现，而且很奇怪，为什么我之前写的时候，明明是assign语句把tmpSta.leftVal给加入到了addressTaken里面去，感觉是不是弄错了，晕
                    if tmpSta.firstType != 'i32':  # 过滤掉int类型
                        tmpStr = "assign: " + tmpSta.rightVal + " = " + tmpSta.leftVal + tmpSta.linenumber+"\\l "
                        print(",,,,,,," + tmpStr)
                        addressTaken.append(tmpSta.leftVal)
                        if tmpSta.rightVal not in allPointer:
                            allPointer.append(tmpSta.rightVal)
                        return tmpStr
                else:
                    if (tmpStament.leftVal == tmpSta.leftVal):
                        if tmpStament.secondType.isdigit():
                            if 'getelementptr' in res2:
                                if tmpStament.rightVal != tmpSta.rightVal or tmpStament.secondType != tmpSta.secondType:
                                    tmpStr = "assign: " + tmpSta.rightVal+"."+tmpSta.secondType + " = " + tmpStament.rightVal + "." + tmpStament.secondType + tmpSta.linenumber + "\\l "
                                    tmp1 = tmpSta.rightVal + "." + tmpSta.secondType
                                    tmp2 = tmpStament.rightVal + "." + tmpStament.secondType
                                    if tmp1 not in allPointer:
                                        allPointer.append(tmp1)
                                    if tmp2 not in allPointer:
                                        allPointer.append(tmp2)
                                    return tmpStr
                            else:
                                tmpStr = "assign: " + tmpSta.rightVal + " = " + tmpStament.rightVal + "." + tmpStament.secondType + tmpSta.linenumber + "\\l "
                                tmp1 = tmpStament.rightVal + "." + tmpStament.secondType
                                if tmp1 not in allPointer:
                                    allPointer.append(tmp1)
                                if tmpSta.rightVal not in allPointer:
                                    allPointer.append(tmpSta.rightVal)
                                return tmpStr
                        else:
                            tmpStr = "assign: " + tmpSta.rightVal + " = " + tmpStament.rightVal + tmpSta.linenumber+"\\l "
                            if tmpStament.rightVal not in allPointer:
                                allPointer.append(tmpStament.rightVal)
                            if tmpSta.rightVal not in allPointer:
                                allPointer.append(tmpSta.rightVal)
                            return tmpStr
                    # *pptr = &n 的例子
                    if tmpStament.leftVal == tmpSta.rightVal:
                        if tmpSta.firstType != 'i8' and tmpSta.firstType != 'i32' and tmpSta.firstType != 'i64':
                            tmpVal = "T" + int(time.time()).__str__()
                            tmpStr = "alloca: " + tmpVal + " = " + tmpSta.leftVal + tmpSta.linenumber+"\\l " + "store: " + "*" + tmpStament.rightVal + " = " + tmpVal + tmpSta.linenumber+"\\l "
                            if tmpSta.leftVal not in addressTaken:
                                addressTaken.append(tmpSta.leftVal)
                            if tmpStament.rightVal not in allPointer:
                                allPointer.append(tmpStament.rightVal)
                            return tmpStr

            # if there are two 'load' keywords in the stack
            # or one load & one getelementptr
            if (len(stackLV) == 2):
                # fetch the top two values of stack
                # the name of variable is for intuitively operating
                tmpStament2 = stackLV.pop()
                tmpStament1 = stackLV.pop()
                if tmpStament2.Op == 'getelementptr':
                    if tmpStament2.firstType != 'i32':
                        if (tmpStament1.leftVal == tmpSta.leftVal and tmpStament2.leftVal == tmpSta.rightVal):
                            tmpStr = "assign: " + tmpStament2.rightVal + "." + tmpStament2.secondType + " = " + tmpStament1.rightVal + tmpSta.linenumber+"\\l "
                            tmpPointer = tmpStament2.rightVal + "." + tmpStament2.secondType
                            if tmpPointer not in allPointer:
                                allPointer.append(tmpPointer)
                            if tmpStament1.rightVal not in allPointer:
                                allPointer.append(tmpStament1.rightVal)
                            return tmpStr

                        # like pointerCase.d = &PointerArray[5];
                        if tmpStament1.Op == 'getelementptr':
                            if tmpSta.leftVal == tmpStament1.leftVal and tmpSta.rightVal == tmpStament2.leftVal:
                                tmpStr = "alloca: " + tmpStament2.rightVal + "." + tmpStament2.secondType + " = " + tmpStament1.rightVal + "." + tmpStament1.secondType + tmpSta.linenumber+"\\l "
                                tmpPointer1 = tmpStament2.rightVal + "." + tmpStament2.secondType
                                tmpPointer2 = tmpStament1.rightVal + "." + tmpStament1.secondType
                                if tmpPointer2 not in addressTaken:
                                    addressTaken.append(tmpPointer2)
                                if tmpPointer1 not in allPointer:
                                    allPointer.append(tmpPointer1)
                                return tmpStr
                elif tmpStament1.Op == 'getelementptr':
                    if tmpStament1.firstType != 'i32':
                        if (tmpStament1.leftVal == tmpStament2.rightVal and tmpStament2.leftVal == tmpSta.leftVal):
                            tmpStr = "assign: " + tmpSta.rightVal + " = " + tmpStament1.rightVal + "." + tmpStament1.secondType + tmpSta.linenumber+"\\l "
                            tmpPointer = tmpStament1.rightVal + "." + tmpStament1.secondType
                            if tmpPointer not in allPointer:
                                allPointer.append(tmpPointer)
                            if tmpSta.rightVal not in allPointer:
                                allPointer.append(tmpSta.rightVal)
                            return tmpStr
                else:
                    if (tmpStament1.leftVal == tmpSta.leftVal and tmpStament2.leftVal == tmpSta.rightVal):
                        tmpStr = "store: " + "*" + tmpStament2.rightVal + " = " + tmpStament1.rightVal + tmpSta.linenumber+"\\l "
                        if tmpStament1.rightVal not in allPointer:
                            allPointer.append(tmpStament1.rightVal)
                        if tmpStament2.rightVal not in allPointer:
                            allPointer.append(tmpStament2.rightVal)
                        return tmpStr
                    if (tmpStament2.leftVal == tmpSta.leftVal and tmpStament1.leftVal == tmpStament2.rightVal):
                        tmpStr = "load: " + tmpSta.rightVal + " = " + "*" + tmpStament1.rightVal + tmpSta.linenumber+"\\l "
                        if tmpSta.rightVal not in allPointer:
                            allPointer.append(tmpSta.rightVal)
                        if tmpStament1.rightVal not in allPointer:
                            allPointer.append(tmpStament1.rightVal)
                        return tmpStr

            # if there are more than two 'load' keywords in the satck
            # could be *x = *y case
            # need to be handled like
            # t = *y
            # *x = t
            if (len(stackLV) == 3):
                tmpStament3 = stackLV.pop()
                tmpStament2 = stackLV.pop()
                tmpStament1 = stackLV.pop()
                tmpStr = ""
                if tmpStament2.Op == 'getelementptr':
                    if tmpStament2.firstType != 'i32':
                        if (
                                tmpStament1.leftVal == tmpSta.leftVal and tmpStament2.leftVal == tmpStament3.rightVal and tmpStament3.leftVal == tmpSta.rightVal):
                            tmpStr = "store: " + "*" + tmpStament2.rightVal + "." + tmpStament2.secondType + " = " + tmpStament1.rightVal + tmpSta.linenumber+"\\l "
                            tmpPointer = tmpStament2.rightVal + "." + tmpStament2.secondType
                            if tmpPointer not in allPointer:
                                allPointer.append(tmpPointer)
                            if tmpStament1.rightVal not in allPointer:
                                allPointer.append(tmpStament1.rightVal)

                        if (tmpStament2.leftVal == tmpStament3.rightVal and tmpStament3.leftVal == tmpSta.leftVal):
                            if tmpStament3.Op == 'getelementptr' and tmpStament1.secondType.isdigit():
                                if tmpStament1.leftVal == tmpStament2.rightVal:
                                    tmpStr = "assign: " + tmpSta.rightVal + "." + tmpSta.secondType + " = " + tmpStament1.rightVal+ "." + tmpStament1.secondType+ "."+ tmpStament2.secondType+tmpSta.linenumber+"\\l "
                                    tmp1 = tmpSta.rightVal + "." + tmpSta.secondType
                                    tmp2 = tmpStament1.rightVal+ "." + tmpStament1.secondType+ "."+ tmpStament2.secondType
                                    if tmp1 not in allPointer:
                                        allPointer.append(tmp1)
                                    if tmp2 not in allPointer:
                                        allPointer.append(tmp2)
                            else:
                                tmpStr = "assign: " + tmpSta.rightVal + " = " + tmpStament2.rightVal + ".i" + tmpSta.linenumber+"\\l "
                                tmpPointer = tmpStament2.rightVal + ".i"
                                if tmpSta.rightVal not in allPointer:
                                    allPointer.append(tmpSta.rightVal)
                                if tmpPointer not in allPointer:
                                    allPointer.append(tmpPointer)

                elif tmpStament1.Op == 'getelementptr':
                    if tmpStament1.firstType != 'i32':
                        if (
                                tmpStament1.leftVal == tmpStament2.rightVal and tmpStament2.leftVal == tmpSta.leftVal and tmpStament3.leftVal == tmpSta.rightVal):
                            tmpStr = "store: " + "*" + tmpStament3.rightVal + " = " + tmpStament1.rightVal + "." + tmpStament1.secondType + tmpSta.linenumber+"\\l "
                            tmpPointer = tmpStament1.rightVal + "." + tmpStament1.secondType
                            if tmpPointer not in allPointer:
                                allPointer.append(tmpPointer)
                            if tmpStament3.rightVal not in allPointer:
                                allPointer.append(tmpStament3.rightVal)
                        if (
                                tmpStament1.leftVal == tmpStament2.rightVal and tmpStament2.leftVal == tmpStament3.rightVal and tmpStament3.leftVal == tmpSta.leftVal):
                            tmpStr = "load: " + tmpSta.rightVal + " = " + "*" + tmpStament1.rightVal + "." + tmpStament1.secondType + tmpSta.linenumber+"\\l "
                            tmpPointer = tmpStament1.rightVal + "." + tmpStament1.secondType
                            if tmpPointer not in allPointer:
                                allPointer.append(tmpPointer)
                            if tmpSta.rightVal not in allPointer:
                                allPointer.append(tmpSta.rightVal)

                        if tmpStament3.Op == 'getelementptr':
                            if tmpStament1.leftVal == tmpStament2.rightVal and tmpStament2.leftVal == tmpSta.leftVal and tmpStament3.leftVal == tmpSta.rightVal:
                                tmpStr = "assign: " + tmpStament1.rightVal + "." + tmpStament1.secondType + " = " + tmpStament3.rightVal + "." + tmpStament3.secondType + tmpSta.linenumber+"\\l "
                                tmpPointer1 = tmpStament1.rightVal + "." + tmpStament1.secondType
                                tmpPointer2 = tmpStament3.rightVal + "." + tmpStament3.secondType
                                if tmpPointer1 not in allPointer:
                                    allPointer.append(tmpPointer1)
                                if tmpPointer2 not in allPointer:
                                    allPointer.append(tmpPointer2)
                                return tmpStr
                elif tmpStament3.Op == 'getelementptr':
                    if tmpStament3.firstType != 'i32':
                        if (
                                tmpStament1.leftVal == tmpStament2.rightVal and tmpStament2.leftVal == tmpSta.leftVal and tmpStament3.leftVal == tmpSta.rightVal):
                            tmpStr = "load: " + tmpStament3.rightVal + "." + tmpStament3.secondType + " = " + "*" + tmpStament1.rightVal + tmpSta.linenumber+"\\l "
                            tmpPointer = tmpStament3.rightVal + "." + tmpStament3.secondType
                            if tmpPointer not in allPointer:
                                allPointer.append(tmpPointer)
                            if tmpStament1.rightVal not in allPointer:
                                allPointer.append(tmpStament1.rightVal)


                else:
                    if tmpStament1.leftVal == tmpStament2.rightVal:
                        tmpStr = "load: " + tmpStament2.leftVal + " = " + "*" + tmpStament1.rightVal + tmpSta.linenumber+"\\l "
                        if tmpStament2.leftVal not in allPointer:
                            allPointer.append(tmpStament2.leftVal)
                        if tmpStament1.rightVal not in allPointer:
                            allPointer.append(tmpStament1.rightVal)
                    if tmpStament3.leftVal == tmpSta.rightVal and tmpSta.leftVal == tmpStament2.leftVal:
                        tmpStr += "store: " + "*" + tmpStament3.rightVal + " = " + tmpStament2.leftVal + tmpSta.linenumber+"\\l "
                        if tmpStament3.rightVal not in allPointer:
                            allPointer.append(tmpStament3.rightVal)
                        if tmpStament2.leftVal not in allPointer:
                            allPointer.append(tmpStament2.leftVal)
                return tmpStr
            # *pointerCase.e = PointerArray[6];
            if (len(stackLV) == 4):
                tmpStament4 = stackLV.pop()
                tmpStament3 = stackLV.pop()
                tmpStament2 = stackLV.pop()
                tmpStament1 = stackLV.pop()
                if tmpStament1.Op == 'getelementptr' and tmpStament3.Op == 'getelementptr':
                    if tmpStament1.leftVal == tmpStament2.rightVal and tmpStament2.leftVal == tmpSta.leftVal and tmpStament3.leftVal == tmpStament4.rightVal and tmpStament4.leftVal == tmpSta.rightVal:
                        tmpStr = "store: " + "*" + tmpStament3.rightVal + "." + tmpStament3.secondType + " = " + tmpStament1.rightVal + "." + tmpStament1.secondType + tmpSta.linenumber+"\\l "
                        tmpPointer1 = tmpStament3.rightVal + "." + tmpStament3.secondType
                        tmpPointer2 = tmpStament1.rightVal + "." + tmpStament1.secondType
                        if tmpPointer1 not in allPointer:
                            allPointer.append(tmpPointer1)
                        if tmpPointer2 not in allPointer:
                            allPointer.append(tmpPointer2)
                        return tmpStr
                if tmpStament1.Op == 'getelementptr' and tmpStament4.Op == 'getelementptr':
                    if tmpStament1.leftVal == tmpStament2.rightVal and tmpStament2.leftVal == tmpStament3.rightVal and tmpStament3.leftVal == tmpSta.leftVal and tmpStament4.leftVal == tmpSta.rightVal:
                        tmpStr = "load: " + tmpStament4.rightVal + "." + tmpStament4.secondType + " = " + "*" + tmpStament1.rightVal + "." + tmpStament1.secondType + tmpSta.linenumber+"\\l "
                        tmpPointer1 = tmpStament4.rightVal + "." + tmpStament4.secondType
                        tmpPointer2 = tmpStament1.rightVal + "." + tmpStament1.secondType
                        if tmpPointer1 not in allPointer:
                            allPointer.append(tmpPointer1)
                        if tmpPointer2 not in allPointer:
                            allPointer.append(tmpPointer2)
                        return tmpStr

        # if is a call key word
        if (len(res2) >= 3 and res2[2] == 'call'):
            tmpSta = Statement()
            tmpSta.Op = 'call'
            tmpSta.firstType = res2[3]  # return type of function
            funcName = res2[4].split('(')
            tmpSta.secondType = funcName[0]  # functionName
            # if there is one formal parameter not two more parameters
            if '!dbg' in res2:
                tmpSta.linenumber = res2[-1]

            pppfunctionName=""
            # 获取函数的形参列表
            getFunctionPara(line)
            actualParaToWrite = ""  # 待写的实参
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
                tmpStr = ""
                funformalPara.clear()
                return tmpStr
            print(tmpStr)
            sizeOfFunctionPara = len(funformalPara)  # 函数形参个数
            for item in funformalPara:
                print("in void call function formalPara is", item)
            # 需要先判断是否有stackLV存在
            if sizeOfFunctionPara == 0:
                tmpStr += ")" + tmpSta.linenumber+"\\l "
            else:
                if len(stackLV) != 0:
                    # 在调用该函数处时，输出 传入该函数的实参 实现：
                    while (len(stackLV) != 0):
                        tmpStament1 = stackLV[-1]
                        print("in void call leftval is ", tmpStament1.leftVal, " actTodoWrite is ", actualParaToWrite)
                        # 如果每次进来 代写实参不是空的且不是当前指令的左操作数
                        if len(actualParaToWrite) != 0 and actualParaToWrite != tmpStament1.leftVal:
                            if len(stackLV) >= 2:
                                tmpStament3 = stackLV[-2]
                                # 额外考虑类似于下面的例子
                                #  %20 = load i8**, i8*** %argv.addr, align 8
                                # %21 = load i32, i32* %i, align 4
                                # %idxprom = sext i32 %21 to i64
                                # %arrayidx = getelementptr inbounds i8*, i8** %20, i64 %idxprom
                                # %22 = load i8*, i8** %arrayidx, align 8

                                if tmpStament3.leftVal == actualParaToWrite:
                                    stackLV.pop()
                                    continue


                            if sizeOfFunctionPara == 1:
                                tmpStr += actualParaToWrite + ")" + tmpSta.linenumber+"\\l "
                                print(tmpStr)
                                print("here size is 111111111111111111111111111NULL")
                                break  # 写完最后一个实参 要break掉
                            else:
                                tmpStr += actualParaToWrite + ","
                                sizeOfFunctionPara = sizeOfFunctionPara - 1
                                actualParaToWrite = ""
                                continue
                        elif len(actualParaToWrite) != 0 and actualParaToWrite == tmpStament1.leftVal:
                            # 如果代写的实参不空但是为当前指令的左操作数，需要把代写实参重新赋值
                            actualParaToWrite = tmpStament1.rightVal
                            if len(stackLV) == 1:
                                #如果只剩当前的这个条语句了，也是要写
                                tmpStr += actualParaToWrite + ")" + tmpSta.linenumber+"\\l "
                                print("here size is 11222222NULL",tmpStr)
                            stackLV.pop()
                            continue

                        if tmpStament1.leftVal in funformalPara:
                            # 如果当前指令的左操作数在形参列表中出现
                            # 就把当前指令的右操作数 用作实参
                            actualParaToWrite = tmpStament1.rightVal
                            #删除掉已经匹配上的形参
                            funformalPara.remove(tmpStament1.leftVal)
                            # 并且pop掉当前的指令
                            stackLV.pop()
                            if len(stackLV) != 0:
                                tmpStament2 = stackLV[-1]
                                if tmpStament2.leftVal == actualParaToWrite:
                                    continue
                                else:
                                    if sizeOfFunctionPara == 1:
                                        tmpStr += actualParaToWrite + ")" + tmpSta.linenumber+"\\l "
                                        print("here size is 111111333NULL",tmpStr)
                                        break
                            else:
                                if sizeOfFunctionPara != 1:#如果已经把最后的一条load 指令pop掉，且只剩一个实际要写的实参，但是由于存在形参里有%call的变量存在，
                                    #所以需要额外判断一下是不是只剩一个形参要写，如果不是
                                    tmpStr += actualParaToWrite + ","
                                else:#如果是
                                    tmpStr += actualParaToWrite + ")" + tmpSta.linenumber+"\\l "
                                print(tmpStr)
                                print("here size is 111111111111111111111111111NULL2")
                                break  # 写完最后一个实参 要break掉
                        else:
                            if len(stackLV) != 0:
                                stackLV.pop()

            '''
            #需要判断是函数名是否为空
            if len(tmpSta.secondType) == 0:
                tmpStr = ""
                return tmpStr

            #判断调用的函数 是否有传参数
            if len(stackLV) == 0:
                tmpStr += ")" + "\\l "
            else:
                for i in range(len(stackLV)):
                    if i == len(stackLV)-1:
                        tmpStr += stackLV[i].rightVal + ")" + "\\l "
                    else:
                        tmpStr += stackLV[i].rightVal+", "
                #remove all load statement
                for i in range(len(stackLV)):
                    stackLV.pop()
            '''
            #在离开前需要检查一下tmpStr是否为完整的句子
            #需要把形参中为%call等形式的参数放进去
            if ')!' not in tmpStr:
                #说明是不完整的句子
                for i in range(len(funformalPara)):
                    if i == len(funformalPara) -1:
                        tmpStr += funformalPara[i] + ")"+tmpSta.linenumber+"\\l "
                    else:
                        tmpStr += funformalPara[i] + ","


            funformalPara.clear()
            print("in void call case before return tmpStr is", tmpStr)
            return tmpStr

        # if is a ret instruction
        if (len(res2) >= 3 and res2[2] == 'ret'):
            tmpSta = Statement()
            tmpSta.Op = 'ret'
            if '!dbg' in res2:
                tmpSta.linenumber = res2[-1]

            tmpSta.firstType = res2[3]  # return value's type
            if tmpSta.firstType != 'void':
                tmpSta.leftVal = res2[4]
            if tmpSta.firstType != 'void' and tmpSta.firstType != 'i32':
                if len(stackLV) == 1:
                    tmpStament1 = stackLV.pop()
                    if tmpSta.leftVal == tmpStament1.leftVal:
                        tmpStr = 'ret ' + tmpStament1.rightVal + tmpSta.linenumber+"\\l "
                        return tmpStr
                if len(stackLV) == 2:
                    tmpStament2 = stackLV.pop()
                    tmpStament1 = stackLV.pop()
                    print("cccccccccccccccccccccc")
                    if tmpStament1.leftVal == tmpStament2.rightVal and tmpStament2.leftVal == tmpSta.leftVal:
                        tmpStr = 'ret ' + tmpStament1.rightVal + tmpSta.linenumber+"\\l "
                        return tmpStr
                    # 排除call 函数后，直接ret，没有ret语句的bug
                    if tmpStament1.Op == 'call':
                        print("aaaaaaaaaaaaaaaaaaaaa")
                        if tmpStament2.leftVal == tmpSta.leftVal:
                            print("bbbbbbbbbbbbbbbbb")
                            tmpStr = 'ret ' + tmpStament2.rightVal + tmpSta.linenumber+"\\l "
                            return tmpStr


#path = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\\httpd\debug\llvm8"
#path = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\\vim\llvm8"
path = "D:\Ouroboros\codes\Ouroboros-Project\\testfile\\firefox\\toolkit\llvm8"
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
                if 'function' in line:
                    # 如果有function关键字在，说明仍不是一个block，则直接写入
                    input1 = bytes(line, encoding="utf8")
                    fobj.write(input1)
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