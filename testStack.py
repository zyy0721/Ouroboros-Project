
import re
#输入的dot文件
filename = 'cfg.Case5fun2.dot'

#输出想要的dot文件
newFilename = 'cfg.zyy.Case5fun2test.dot'
fobj = open(newFilename, 'wb+')

#用来存操作符的栈
stackOp=[]
#用来存statement的栈
stackLV=[]
stackRV=[] #not use
allPointer=[] # to store pointer type variables
topLevel=[]#for record topLevel variable
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
    print(line)
    res2 = re.split(",| ", line)
    print(res2)
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
        if (len(res2) >= 5 and res2[4] == 'alloca'):
            tmpSta = Statement()
            tmpSta.leftVal = res2[2]
            tmpSta.Op = 'alloca'
            if 'i32]'  in res2 or 'i32*]' in res2 or 'i32**]' in res2 :
                tmpSta.firstType = res2[7].replace(']','')
            else:
                tmpSta.firstType = res2[5]
            #skip int type variable
            if tmpSta.firstType!= 'i32':
                tmpStr = "alloca:" + tmpSta.firstType + " " + tmpSta.leftVal + "\\l "
                allPointer.append(tmpSta.leftVal)
                return tmpStr
            #continue
            #print("alloca statement1")
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
            print(res2)
            tmpSta = Statement()
            tmpSta.Op = 'getelementptr'
            tmpSta.leftVal = res2[2]
            if 'x' not in res2:
                tmpSta.rightVal = res2[9]
                tmpSta.secondType=res2[15] #it means the index of a pointer variable in the struct object
            else:#it means is an array type
                tmpSta.firstType = res2[8].replace(']','')# a key word to judge whether should go further calculation, only pointer type needed
                tmpSta.rightVal = res2[13]
                tmpSta.secondType = res2[19]
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
            if (len(stackLV) == 0 ):
                # judge whether it is an alloca statement or not
                if (tmpSta.firstType == 'i32*' or tmpSta.firstType == 'i32**'):
                    tmpStr = "alloca:"+' ' + tmpSta.rightVal + " = " + tmpSta.leftVal + "\\l "
                    if tmpSta.leftVal not in addressTaken:
                        addressTaken.append(tmpSta.leftVal)
                    if tmpSta.rightVal not in allPointer:
                        allPointer.append(tmpSta.rightVal)
                    return tmpStr

            # if there is only one 'load' keyword in the stack
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
                            if tmpSta.rightVal not in allPointer:
                                allPointer.append(tmpSta.rightVal)

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



        # if is a call key word
        if(len(res2)>=3 and res2[2]=='call'):
            tmpSta = Statement()
            tmpSta.Op = 'call'
            tmpSta.firstType = res2[3]#return type of function
            funcName = res2[4].split('(')
            tmpSta.secondType = funcName[0] # functionName
            #if there is one formal parameter not two more parameters

            #找上一句load 指令，来找到真实的变量寄存器号，如果相等则继续
            tmpStr = "call " + tmpSta.firstType + " "+tmpSta.secondType + "( "
            print(tmpStr)
            for i in range(len(stackLV)):
                if i == len(stackLV)-1:
                    tmpStr += stackLV[i].rightVal + ")" + "\\l "
                else:
                    tmpStr += stackLV[i].rightVal+", "
            #remove all load statement
            for i in range(len(stackLV)):
                stackLV.pop()

            print(tmpStr)
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
                    print(strLine[i])
                    tmpStr = analysisLine(strLine[i])
                    #print(analysisLine(strLine[i]))
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
            if "}" in line:
                for item in allPointer:
                    if item not in addressTaken:
                        strContent += item +" topLevel" + "\\l "
                        print(strContent)
                for item in addressTaken:
                    strContent += item + " addressTaken" + "\\l "
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