import re
filename = 'testAdd.ll'
stackOp=[]
stackLV=[]
stackRV=[] #not use

#create a class called 'Statement' to store each line
class Statement:
    def __init__(self):
        self.leftVal = ''
        self.Op = ''
        self.firstType = ''
        self.secondType = ''
        self.rightVal = ''

with open(filename,'r') as f:

    for line in f:
        #split each line to get what we want
        res2 = re.split(',| ',line)
        #skip space line
        if(len(res2) == 0):
            continue
        else:
            if (res2[0] == '}\n'):  # means at the end of main function
                break
                # skip annotation
            if (res2[0] == ';'):
                continue
                #skip source name
            if (res2[0] == 'source_name'):
                continue
                #skip target name
            if(res2[0] == 'target'):
                continue
            if(res2[0] == '@.str'):
                continue

            # alloca statement
            if (len(res2) >= 5 and res2[4] == 'alloca'):
                tmpSta = Statement()
                tmpSta.leftVal = res2[2]
                tmpSta.Op = 'alloca'
                tmpSta.firstType = res2[5]
                print("alloca " + tmpSta.firstType +" " +tmpSta.leftVal)
                continue
            # skip return 0 case
            if (len(res2) >= 3 and res2[2] == 'store' and res2[4] == 0):
                continue

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

                #if there is no 'load' keyword
                if(len(stackLV) == 0):
                    #filter the statement
                    continue

                #if there is only one 'load' keyword in the stack
                if (len(stackLV) == 1):
                    # fetch the top value of stack
                    tmpStament = stackLV.pop()
                    if (tmpStament.leftVal == tmpSta.leftVal):
                        print("assign: " + tmpSta.rightVal + "=" + tmpStament.rightVal)

                #if there are two 'load' keywords in the stack
                if (len(stackLV) == 2):
                    # fetch the top two values of stack
                    # the name of variable is for intuitively operating
                    tmpStament2 = stackLV.pop()
                    tmpStament1 = stackLV.pop()
                    if (tmpStament1.leftVal == tmpSta.leftVal and tmpStament2.leftVal == tmpSta.rightVal):
                        print("load: " + "*" + tmpStament2.rightVal + "=" + tmpStament1.rightVal)
                    if (tmpStament2.leftVal == tmpSta.leftVal and tmpStament1.leftVal == tmpStament2.rightVal):
                        print("store: " + tmpSta.rightVal + "=" + "*" + tmpStament1.rightVal)

                #if there are more than two 'load' keywords in the satck
                if(len(stackLV) >= 3):
                    continue










print("Hello World!")