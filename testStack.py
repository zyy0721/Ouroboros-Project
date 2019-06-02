
import re
#输入的dot文件
filename = 'llvm8/tC6main.dot'

#输出想要的dot文件
newFilename = 'llvm8/tC6maintest.dot'
fobj = open(newFilename, 'wb+')

#用来存操作符的栈
stackOp=[]
#用来存statement的栈
stackLV=[]
#用来存每个函数的形参栈
FormalParameter=[] #to store every function's formal parameters
#用来存储每个Pointer类型变量
allPointer=[] # to store pointer type variables
#用来存储每个topLevel类型的变量
topLevel=[]#for record topLevel variable
#用来存储每个address Taken类型的变量
addressTaken=[]#for record addressTaken variable
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
    res2 = re.split(",| ", line)
    # skip space line
    if (len(res2) == 0):
        #continue
        print("len of res is 0")
    else:
        if (res2[0] == '}\n'):  # means at the end of main function
            #break
            print("there should be a break")
            # skip annotation

        # alloca statement
        #在判断alloca语句的同时，通过是否有addr属性决定形参
        if (len(res2) >= 5 and res2[4] == 'alloca'):
            tmpSta = Statement()
            tmpSta.leftVal = res2[2]
            tmpSta.Op = 'alloca'
            if 'i32]'  in res2 or 'i32*]' in res2 or 'i32**]' in res2 :
                tmpSta.firstType = res2[7].replace(']','')
            else:
                tmpSta.firstType = res2[5]
            #如果有addr属性 说明是形参
            if 'addr' in tmpSta.leftVal:
                FormalParameter.append(tmpSta.leftVal)

            #skip int type variable 跳过int类型的变量
            if tmpSta.firstType!= 'i32':
                tmpStr = "alloca:" + tmpSta.firstType + " " + tmpSta.leftVal + "\\l "
                allPointer.append(tmpSta.leftVal)
                return tmpStr

        # skip return 0 case
        if (len(res2) >= 3 and res2[2] == 'store' and res2[4] == 0):
            #continue
            #print("alloca statement2")
            return "zero" + "\\l "

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

        # getelementptr
        if(len(res2) >=5 and res2[4] == 'getelementptr'):
            tmpSta = Statement()
            tmpSta.Op = 'getelementptr'
            tmpSta.leftVal = res2[2]
            #用 ‘x’ 来区分是否为数组
            if 'x' not in res2:
                tmpSta.rightVal = res2[9]
                tmpSta.secondType=res2[15] #it means the index of a pointer variable in the struct object
            else:#it means an array type
                if len(res2) == 24:#it means a two-dimensional array
                    tmpSta.firstType = res2[10].replace(']','')
                    tmpSta.rightVal = res2[17]
                    tmpSta.secondType = res2[23]
                else:
                    tmpSta.firstType = res2[8].replace(']','')# a key word to judge whether should go further calculation, only pointer type needed
                    tmpSta.rightVal = res2[13]
                    tmpSta.secondType = res2[19]
            stackLV.append(tmpSta)

        #if a call function has return value
        if (len(res2)>=5 and res2[4] == 'call'):
            tmpSta = Statement()
            tmpSta.Op = 'call'
            tmpSta.leftVal = res2[2]
            tmpSta.firstType = res2[5]#return type of function
            funcName = res2[6].split('(')
            tmpSta.secondType = funcName[0] # functionName

            tmpStr = "call: " + tmpSta.leftVal+" = "+tmpSta.firstType+" "+tmpSta.secondType + "("
            #在调用该函数处时，输出 传入该函数的实参 实现：
            for i in range(len(stackLV)):
                if i == len(stackLV)-1:
                    tmpStr += stackLV[i].rightVal + ")" + "\\l "
                else:
                    tmpStr += stackLV[i].rightVal+", "
            #remove all load statement
            for i in range(len(stackLV)):
                stackLV.pop()

            #用来区分是否是malloc或者new类型，如果是则不把call语句加入stackLV，需要进行特殊的单独处理
            #
            if 'malloc' in line or 'Znam' in line :
                tmpStr = ""
            else:
                stackLV.append(tmpSta)

            return tmpStr

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
            if (len(stackLV) == 0 ):
                # judge whether it is an alloca statement or not
                if (tmpSta.firstType == 'i32*' or tmpSta.firstType == 'i32**'):
                    tmpLeftVal = tmpSta.leftVal + ".addr"
                    if tmpLeftVal == tmpSta.rightVal:
                        print("........................")
                    else:
                        tmpStr = "alloca:"+' ' + tmpSta.rightVal + " = " + tmpSta.leftVal + "\\l "
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
                        if tmpStament.leftVal == tmpSta.rightVal:
                            tmpStr = "alloca: " +tmpStament.rightVal+"."+tmpStament.secondType+" = "+tmpSta.leftVal+"\\l "
                            if tmpSta.leftVal not in addressTaken:
                                addressTaken.append(tmpSta.leftVal)
                            tmpPointer = tmpStament.rightVal+"."+tmpStament.secondType
                            if tmpPointer not in allPointer:
                                allPointer.append(tmpPointer)
                            return tmpStr
                        if tmpStament.leftVal == tmpSta.leftVal:
                            tmpStr = "alloca: "+tmpSta.rightVal+" = "+tmpStament.rightVal+"."+tmpStament.secondType+"\\l "
                            tmpPointer = tmpStament.rightVal+"."+tmpStament.secondType
                            if tmpPointer not in addressTaken:
                                addressTaken.append(tmpPointer)
                            tmpPointer = tmpStament.rightVal+"."+tmpStament.secondType
                            if tmpPointer not in allPointer:
                                allPointer.append(tmpPointer)
                            return tmpStr
                elif tmpStament.Op =='call':
                    tmpStr = "assign: "+ tmpSta.rightVal + " = " + tmpSta.leftVal + "\\l "
                    addressTaken.append(tmpSta.leftVal)
                    if tmpSta.rightVal not in allPointer:
                        allPointer.append(tmpSta.rightVal)
                    return tmpStr
                else:
                    if (tmpStament.leftVal == tmpSta.leftVal):
                        tmpStr = "assign:" +' '+tmpSta.rightVal + " = " +tmpStament.rightVal + "\\l "
                        if tmpSta.rightVal not in allPointer:
                            allPointer.append(tmpSta.rightVal)
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
                if tmpStament2.Op == 'getelementptr' :
                    if tmpStament2.firstType != 'i32':
                        if (tmpStament1.leftVal == tmpSta.leftVal and tmpStament2.leftVal == tmpSta.rightVal):
                            tmpStr = "assign: "+ tmpStament2.rightVal+"."+tmpStament2.secondType +" = "+ tmpStament1.rightVal + "\\l "
                            tmpPointer = tmpStament2.rightVal+"."+tmpStament2.secondType
                            if tmpPointer not in allPointer:
                                allPointer.append(tmpPointer)
                            if tmpStament1.rightVal not in allPointer:
                                allPointer.append(tmpStament1.rightVal)
                            return tmpStr

                        #like pointerCase.d = &PointerArray[5];
                        if tmpStament1.Op == 'getelementptr':
                            if tmpSta.leftVal == tmpStament1.leftVal and tmpSta.rightVal == tmpStament2.leftVal:
                                tmpStr = "alloca: " + tmpStament2.rightVal + "." + tmpStament2.secondType +" = "+tmpStament1.rightVal+"."+tmpStament1.secondType + "\\l "
                                tmpPointer1 = tmpStament2.rightVal+"."+tmpStament2.secondType
                                tmpPointer2 = tmpStament1.rightVal+"."+tmpStament1.secondType
                                if tmpPointer2 not in addressTaken:
                                    addressTaken.append(tmpPointer2)
                                if tmpPointer1 not in allPointer:
                                    allPointer.append(tmpPointer1)
                                return tmpStr
                elif tmpStament1.Op == 'getelementptr' :
                    if tmpStament1.firstType != 'i32':
                        if (tmpStament1.leftVal == tmpStament2.rightVal and tmpStament2.leftVal == tmpSta.leftVal):
                            tmpStr = "assign: "+ tmpSta.rightVal + " = " + tmpStament1.rightVal+"."+tmpStament1.secondType + "\\l "
                            tmpPointer = tmpStament1.rightVal+"."+tmpStament1.secondType
                            if tmpPointer not in allPointer:
                                allPointer.append(tmpPointer)
                            if tmpSta.rightVal not in allPointer:
                                allPointer.append(tmpSta.rightVal)
                            return tmpStr
                else :
                    if (tmpStament1.leftVal == tmpSta.leftVal and tmpStament2.leftVal == tmpSta.rightVal):
                        tmpStr = "store: " + "*" + tmpStament2.rightVal + " = " + tmpStament1.rightVal + "\\l "
                        if tmpStament1.rightVal not in allPointer:
                            allPointer.append(tmpStament1.rightVal)
                        if tmpStament2.rightVal not in allPointer:
                            allPointer.append(tmpStament2.rightVal)
                        return tmpStr
                    if (tmpStament2.leftVal == tmpSta.leftVal and tmpStament1.leftVal == tmpStament2.rightVal):
                        tmpStr = "load: " + tmpSta.rightVal + " = " + "*" + tmpStament1.rightVal + "\\l "
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
            if(len(stackLV) == 3):
                tmpStament3 = stackLV.pop()
                tmpStament2 = stackLV.pop()
                tmpStament1 = stackLV.pop()
                tmpStr = ""
                if tmpStament2.Op == 'getelementptr':
                    if tmpStament2.firstType != 'i32':
                        if (tmpStament1.leftVal == tmpSta.leftVal and tmpStament2.leftVal == tmpStament3.rightVal and tmpStament3.leftVal == tmpSta.rightVal):
                            tmpStr = "store: "+"*"+tmpStament2.rightVal+"."+tmpStament2.secondType+" = "+tmpStament1.rightVal+"\\l "
                            tmpPointer = tmpStament2.rightVal+"."+tmpStament2.secondType
                            if tmpPointer not in allPointer:
                                allPointer.append(tmpPointer)
                            if tmpStament1.rightVal not in allPointer:
                                allPointer.append(tmpStament1.rightVal)

                        if (tmpStament2.leftVal == tmpStament3.rightVal and tmpStament3.leftVal == tmpSta.leftVal):
                            tmpStr = "assign: "+tmpSta.rightVal+" = "+tmpStament2.rightVal+".i"+ "\\l "
                            tmpPointer = tmpStament2.rightVal+".i"
                            if tmpSta.rightVal not in allPointer:
                                allPointer.append(tmpSta.rightVal)
                            if tmpPointer not in allPointer:
                                allPointer.append(tmpPointer)

                elif tmpStament1.Op == 'getelementptr':
                    if tmpStament1.firstType != 'i32':
                        if (tmpStament1.leftVal == tmpStament2.rightVal and tmpStament2.leftVal == tmpSta.leftVal and tmpStament3.leftVal == tmpSta.rightVal):
                            tmpStr = "store: "+"*"+tmpStament3.rightVal+" = "+tmpStament1.rightVal+"."+tmpStament1.secondType+"\\l "
                            tmpPointer = tmpStament1.rightVal+"."+tmpStament1.secondType
                            if tmpPointer not in allPointer:
                                allPointer.append(tmpPointer)
                            if tmpStament3.rightVal not in allPointer:
                                allPointer.append(tmpStament3.rightVal)
                        if (tmpStament1.leftVal == tmpStament2.rightVal and tmpStament2.leftVal == tmpStament3.rightVal and tmpStament3.leftVal == tmpSta.leftVal):
                            tmpStr = "load: "+tmpSta.rightVal+" = "+"*"+tmpStament1.rightVal+"."+tmpStament1.secondType+"\\l "
                            tmpPointer = tmpStament1.rightVal+"."+tmpStament1.secondType
                            if tmpPointer not in allPointer:
                                allPointer.append(tmpPointer)
                            if tmpSta.rightVal not in allPointer:
                                allPointer.append(tmpSta.rightVal)

                        if tmpStament3.Op == 'getelementptr':
                            if tmpStament1.leftVal == tmpStament2.rightVal and tmpStament2.leftVal == tmpSta.leftVal and tmpStament3.leftVal == tmpSta.rightVal:
                                tmpStr = "assign: " + tmpStament1.rightVal+"."+tmpStament1.secondType + " = " + tmpStament3.rightVal + "." +tmpStament3.secondType + "\\l "
                                tmpPointer1 = tmpStament1.rightVal+"."+tmpStament1.secondType
                                tmpPointer2 = tmpStament3.rightVal + "." +tmpStament3.secondType
                                if tmpPointer1 not in allPointer:
                                    allPointer.append(tmpPointer1)
                                if tmpPointer2 not in allPointer:
                                    allPointer.append(tmpPointer2)
                                return tmpStr
                elif tmpStament3.Op == 'getelementptr':
                    if tmpStament3.firstType != 'i32':
                        if(tmpStament1.leftVal == tmpStament2.rightVal and tmpStament2.leftVal == tmpSta.leftVal and tmpStament3.leftVal == tmpSta.rightVal):
                            tmpStr = "load: "+tmpStament3.rightVal+"."+tmpStament3.secondType+" = "+"*"+tmpStament1.rightVal+"\\l "
                            tmpPointer = tmpStament3.rightVal+"."+tmpStament3.secondType
                            if tmpPointer not in allPointer:
                                allPointer.append(tmpPointer)
                            if tmpStament1.rightVal not in allPointer:
                                allPointer.append(tmpStament1.rightVal)


                else :
                    if tmpStament1.leftVal == tmpStament2.rightVal :
                        tmpStr = "load: " + tmpStament2.leftVal+" = " + "*" + tmpStament1.rightVal + "\\l "
                        if tmpStament2.leftVal not in allPointer:
                            allPointer.append(tmpStament2.leftVal)
                        if tmpStament1.rightVal not in allPointer:
                            allPointer.append(tmpStament1.rightVal)
                    if tmpStament3.leftVal == tmpSta.rightVal and tmpSta.leftVal == tmpStament2.leftVal:
                        tmpStr += "store: " + "*"+ tmpStament3.rightVal+" = "+tmpStament2.leftVal + "\\l "
                        if tmpStament3.rightVal not in allPointer:
                            allPointer.append(tmpStament3.rightVal)
                        if tmpStament2.leftVal not in allPointer:
                            allPointer.append(tmpStament2.leftVal)
                return tmpStr
            #*pointerCase.e = PointerArray[6];
            if (len(stackLV) == 4):
                tmpStament4 = stackLV.pop()
                tmpStament3 = stackLV.pop()
                tmpStament2 = stackLV.pop()
                tmpStament1 = stackLV.pop()
                if tmpStament1.Op == 'getelementptr' and tmpStament3.Op == 'getelementptr':
                    if tmpStament1.leftVal == tmpStament2.rightVal and tmpStament2.leftVal == tmpSta.leftVal and tmpStament3.leftVal == tmpStament4.rightVal and tmpStament4.leftVal == tmpSta.rightVal:
                        tmpStr = "store: " +"*"+tmpStament3.rightVal+"."+tmpStament3.secondType+" = "+tmpStament1.rightVal+"."+tmpStament1.secondType+"\\l "
                        tmpPointer1 = tmpStament3.rightVal+"."+tmpStament3.secondType
                        tmpPointer2 = tmpStament1.rightVal+"."+tmpStament1.secondType
                        if tmpPointer1 not in allPointer:
                            allPointer.append(tmpPointer1)
                        if tmpPointer2 not in allPointer:
                            allPointer.append(tmpPointer2)
                        return tmpStr
                if tmpStament1.Op == 'getelementptr' and tmpStament4.Op == 'getelementptr':
                    if tmpStament1.leftVal == tmpStament2.rightVal and tmpStament2.leftVal == tmpStament3.rightVal and tmpStament3.leftVal == tmpSta.leftVal and tmpStament4.leftVal == tmpSta.rightVal:
                        tmpStr = "load: "+tmpStament4.rightVal+"."+tmpStament4.secondType+" = "+"*"+tmpStament1.rightVal+"."+tmpStament1.secondType+"\\l "
                        tmpPointer1 = tmpStament4.rightVal+"."+tmpStament4.secondType
                        tmpPointer2 = tmpStament1.rightVal+"."+tmpStament1.secondType
                        if tmpPointer1 not in allPointer:
                            allPointer.append(tmpPointer1)
                        if tmpPointer2 not in allPointer:
                            allPointer.append(tmpPointer2)
                        return tmpStr



        # if is a call key word
        if(len(res2)>=3 and res2[2]=='call'):
            tmpSta = Statement()
            tmpSta.Op = 'call'
            tmpSta.firstType = res2[3]#return type of function
            funcName = res2[4].split('(')
            tmpSta.secondType = funcName[0] # functionName
            #if there is one formal parameter not two more parameters

            tmpStr = "call: " + "NULL"+" = "+tmpSta.firstType + " "+tmpSta.secondType + "("
            print(tmpStr)
            for i in range(len(stackLV)):
                if i == len(stackLV)-1:
                    tmpStr += stackLV[i].rightVal + ")" + "\\l "
                else:
                    tmpStr += stackLV[i].rightVal+", "
            #remove all load statement
            for i in range(len(stackLV)):
                stackLV.pop()

            return tmpStr

        #if is a ret instruction
        if(len(res2)>=3 and res2[2] == 'ret'):
            tmpSta = Statement()
            tmpSta.Op = 'ret'
            tmpSta.firstType = res2[3] #return value's type
            if tmpSta.firstType != 'void':
                tmpSta.leftVal = res2[4]
            if tmpSta.firstType != 'void' and tmpSta.firstType != 'i32':
                if len(stackLV)>=1:
                    tmpStament1 = stackLV.pop()
                    if tmpSta.leftVal == tmpStament1.leftVal:
                        tmpStr = 'ret ' + tmpStament1.rightVal + "\\l "
                        return tmpStr





#读取文件
with open(filename,'r') as f:
    #按行读入
    for line in f:
        #res = re.split('\| ', line)
        input2=''
        # 以label为关键字,判断是否为一个block
        if 'label' in line:
        #如果label在，则可能是一个block
            if 'function' in line:
                #如果有function关键字在，说明仍不是一个block，则直接写入
                input1 = bytes(line, encoding="utf8")
                fobj.write(input1)
            else:
                #说明是一个block，则需要进一步处理（但不排除，有其他case没有考虑到
                line = line.replace('\l...','')
                strLine = line.split("\\l")#依据\l 进行划分
                print(strLine[0])
                input1 = bytes(strLine[0]+"\\l ", encoding="utf8")
                fobj.write(input1)
                i = 1
                while i < len(strLine):
                    #对每一行进行分析
                    tmpStr = analysisLine(strLine[i])

                    if tmpStr != None:
                        input1 = bytes(tmpStr,encoding="utf8")
                        fobj.write(input1)
                    i+=1
                #把一句写完整
                tmpLast = strLine[-1]
                #print(tmpLast)
                input2 = bytes(tmpLast,encoding="utf8")
                fobj.write(input2)
                #在离开一个block之前，把stackLV清空
                stackLV.clear()

        #没有label，直接写到新文件中
        else:
            strContent=""
            #如果碰到} 说明整个文件读结束，需要写入一个新的node1来传一些后续所需的信息
            if "}" in line:
                for item in allPointer:
                    if item not in addressTaken:
                        strContent += item +" topLevel" + "\\l "

                #print addressTaken variables
                for item in addressTaken:
                    strContent += item + " addressTaken" + "\\l "
                #print function's parameters
                for item in FormalParameter:
                    strContent += item + " formarlParameter" + "\\l "

                strBlock = "\tNode1 [shape=record,label=" + '"' + "{" + strContent + "}" + '"' + "];"
                input3 = bytes(strBlock,encoding="utf8")
                fobj.write(input3)
            input1 = bytes(line, encoding="utf8")
            fobj.write(input1)

        # to write a tributary block for displaying addressTaken and toplevel
        # Node1 [shape=record,label="{testest zyy\l }"];



fobj.close()

print("all pointer type variables")
for item in allPointer:
    print(item)


print("all addressTaken variables")
for item in addressTaken:
    print(item)

print("top level")
for item in allPointer:
    if item not in addressTaken:
        print(item)