import re
filename = 'test.ll'
stackOp=[]
stackLV=[]
stackRV=[]
class Statement:
    def __init__(self):
        self.leftVal = ''
        self.Op = ''
        self.firstType = ''
        self.secondType = ''
        self.rightVal = ''
with open(filename,'r') as f:
    #skip useless information
    next(f)
    next(f)
    next(f)
    next(f)
    next(f)
    next(f)
    next(f)
    next(f)
    next(f)
    for line in f:
        res2 = re.split(',| ',line)
        if(res2[0]=='}\n'):
            break
        #skip alloca
        if( len(res2)>=5 and res2[4] == 'alloca'):
            continue
        #skip return 0 case
        if(len(res2)>=3 and res2[2] == 'store' and res2[4] == 0):
            continue
        
        if(len(res2)>=5 and res2[4] == 'load'):
            stackOp.append('load')
            tmpSta = Statement()
            tmpSta.Op = 'load'
            tmpSta.leftVal = res2[2]
            tmpSta.firstType = res2[5]
            tmpSta.secondType = res2[7]
            tmpSta.rightVal = res2[8]
            stackLV.append(tmpSta)
        
        if(len(res2)>=3 and res2[2] == 'store'):

            tmpSta = Statement()
            tmpSta.Op = 'store'
            tmpSta.leftVal = res2[4]
            tmpSta.firstType = res2[3]
            tmpSta.rightVal = res2[7]
            tmpSta.secondType = res2[6]
            if(len(stackLV) == 1):
                tmpStament = stackLV.pop()
                if(tmpStament.leftVal == tmpSta.leftVal):
                    print("Assign Statement: " +tmpSta.rightVal+ "=" + tmpStament.rightVal)

            if(len(stackLV) == 2):
                tmpStament2 = stackLV.pop()
                tmpStament1 = stackLV.pop()
                if(tmpStament1.leftVal == tmpSta.leftVal and tmpStament2.leftVal == tmpSta.rightVal):
                    print("Deref Statement?: " + "*"+tmpStament2.rightVal + "=" + tmpStament1.rightVal)
                if(tmpStament2.leftVal == tmpSta.leftVal and tmpStament1.leftVal == tmpStament2.rightVal):
                    print("Ampersand Statement?: " + tmpSta.rightVal + "=" + "*" + tmpStament1.rightVal)







print("Hello World!")