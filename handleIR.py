import re
filename = 'test.ll'
stackOp=[]
stackLV=[]
stackRV=[]
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
        print(res2)
        #skip alloca 
        if(res2[5] == 'alloca'):
            continue
        #skip return 0 case
        if(res2[3] == 'store' and res2[5] == 0):
            continue
        
        if(res2[5] == 'load'):
            stackOp.append('load')
            leftValue = res2[9]
            leftValueType = res2[6]
            stackLV.append(leftValue)
        
        if(res2[3] == 'store'):

        #if res2[3] == 'store'

        #if res2[5] == 'alloca' 

        #if res2[5] == 'load'
        print(line)
        if(res2[0]=='}\n'):
            break


print("Hello World!")