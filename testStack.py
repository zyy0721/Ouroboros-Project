
import re
#输入的dot文件
filename = 'cfg.Case2_Z4fun2PPi.dot'

#输出想要的dot文件
newFilename = 'cfg.zyy.fun2test.dot'
fobj = open(newFilename, 'wb+')

#用来存操作符的栈
stackOp=[]
#用来存statement的栈
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
        '''
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
        '''
        '''
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
        '''
        # alloca statement
        if (len(res2) >= 5 and res2[4] == 'alloca'):
            tmpSta = Statement()
            tmpSta.leftVal = res2[2]
            tmpSta.Op = 'alloca'
            tmpSta.firstType = res2[5]
            tmpStr = "alloca " + tmpSta.firstType + " " + tmpSta.leftVal + "\\l "
            print("alloca " + tmpSta.firstType + " " + tmpSta.leftVal)
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
                    tmpStr = tmpSta.secondType + ' ' + tmpSta.rightVal + " = alloca " + tmpSta.firstType + ' ' + tmpSta.leftVal + "\\l "
                    print(tmpSta.secondType + ' ' + tmpSta.rightVal + " = alloca " + tmpSta.firstType + ' ' + tmpSta.leftVal)
                    return tmpStr

            # if there is only one 'load' keyword in the stack
            if (len(stackLV) == 1):
                # fetch the top value of stack
                tmpStament = stackLV.pop()
                if (tmpStament.leftVal == tmpSta.leftVal):
                    tmpStr = "assign: " + tmpSta.rightVal + "=" + tmpStament.rightVal + "\\l "
                    print("assign: " + tmpSta.rightVal + "=" + tmpStament.rightVal)
                    return tmpStr

            # if there are two 'load' keywords in the stack
            if (len(stackLV) >= 2):
                # fetch the top two values of stack
                # the name of variable is for intuitively operating
                tmpStament2 = stackLV.pop()
                tmpStament1 = stackLV.pop()
                if (tmpStament1.leftVal == tmpSta.leftVal and tmpStament2.leftVal == tmpSta.rightVal):
                    tmpStr = "store: " + "*" + tmpStament2.rightVal + " = " + tmpStament1.rightVal + "\\l "
                    print("store: " + "*" + tmpStament2.rightVal + " = " + tmpStament1.rightVal)
                    return tmpStr
                if (tmpStament2.leftVal == tmpSta.leftVal and tmpStament1.leftVal == tmpStament2.rightVal):
                    tmpStr = "load: " + tmpSta.rightVal + " = " + "*" + tmpStament1.rightVal + "\\l "
                    print("load: " + tmpSta.rightVal + " = " + "*" + tmpStament1.rightVal)
                    return tmpStr

            # if there are more than two 'load' keywords in the satck
            # if(len(stackLV) >= 3):
            #    stackLV.clear()
            #    continue

        # if is a call key word
        if(len(res2)>=3 and res2[2]=='call'):
            tmpSta = Statement()
            tmpSta.Op = 'call'
            tmpSta.firstType = res2[3]#return type of function
            tmpSta.secondType = res2[4] # functionName & formal parameter type
            #if there is one formal parameter not two more parameters
            tmpSta.rightVal = res2[5].replace(")","")#
            #找上一句load 指令，来找到真实的变量寄存器号，如果相等则继续
            tmpStament = stackLV.pop()
            if tmpStament.leftVal == tmpSta.rightVal:
                tmpStr = "call " +tmpSta.firstType + tmpSta.secondType+" "+tmpStament.rightVal+")"+"\\l "
                return tmpStr

        #if is a switch key word
        if (len(res2) >= 3 and res2[2] == 'switch'):
            tmpSta = Statement()
            tmpSta.Op = 'switch'
            tmpSta.firstType = res2[3]
            tmpSta.leftVal = res2[4]
            #找上一句load指令，来找到真实的变量寄存号
            tmpStament = stackLV.pop()
            if tmpStament.leftVal == tmpSta.leftVal:
                tmpStr = "switch" + " "+ tmpSta.firstType + " "+ tmpStament.rightVal + "\\l "
                return tmpStr

        '''
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
        '''



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
            input1 = bytes(line, encoding="utf8")
            fobj.write(input1)


