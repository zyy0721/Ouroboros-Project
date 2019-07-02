#！/usr/bin/env python
#!-*-coding:utf-8 -*-
#!@Create :2019/5/24 22:19
#!@Author : zyy
#!@File   : test.py

import re
import time
class Statement:
    def __init__(self):
        self.leftVal = ''
        self.Op = ''
        self.firstType = ''
        self.secondType = ''
        self.rightVal = ''

filename = 'testCase4.ll'
stack=[]
sta1 = Statement()
sta2 = Statement()
sta3 = Statement()
sta1.Op = '+'
sta2.Op = '-'
sta3.Op = '*'
stack.append(sta1)
stack.append(sta2)
stack.append(sta3)

stack[-1].Op = 'zyy'
sta2.Op = '/'
print(stack[-2])
for item in stack:
    print(item.Op)
print(stack[-1].Op)

#strLine = "  call void (i8*, i32, i32, i32, i32, %struct.conn_rec*, i8*, ...) @ap_log_cerror_(i8* getelementptr inbounds ([14 x i8], [14 x i8]* @.str.200, i32 0, i32 0), i32 404, i32 0, i32 3, i32 0, %struct.conn_rec* %cond, i8* getelementptr inbounds ([45 x i8], [45 x i8]* @.str.3.201, i32 0, i32 0), i8* %45)"
#strLine = "  %call27 = call i8* (%struct.apr_pool_t*, ...) @apr_pstrcat(%struct.apr_pool_t* %21, i8* %23, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @.str.51.2521, i32 0, i32 0), i8* null)"
#strLine ="  call void @apr_table_addn(%struct.apr_table_t* %73, i8* getelementptr inbounds ([5 x i8], [5 x i8]* @.str.10.1625, i32 0, i32 0), i8* %call78)"
#strLine= "  %call101 = call i8* @apr_pstrmemdup(%struct.apr_pool_t* %114, i8* %116, i64 %sub.ptr.sub)"
#strLine = "  %call = call i8* (%struct.apr_pool_t*, ...) @apr_pstrcat(%struct.apr_pool_t* %6, i8* %9, i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str.37.1044, i32 0, i32 0), i8* %10, i8* null)"
#strLine = "  %call = call i32 @find_listeners(%struct.ap_listen_rec** @ap_listeners, %struct.ap_listen_rec** null, i8* %0, i16 zeroext %1)"
#strLine = "  %call = call i64 @write(i32 2, i8* %0, i64 %conv)"
#strLine = "  %call2 = call i32 @setsockopt(i32 %2, i32 1, i32 13, i8* %3, i32 8) #11"
#strLine = "  %call = call i32 @A_is_ok(i32 %0), !dbg !40868"
#strLine = "  %call887 = call i8* @infinity_str(i32 %conv886, i8 signext %394, i32 %395, i32 %396), !dbg !514441"
#strLine = "  call void @ap_relieve_child_processes(void (i32, i32, i32)* @event_note_child_killed)"
#strLine = "  call void @apr_table_addn(%struct.apr_table_t* %73, i8* getelementptr inbounds ([5 x i8], [5 x i8]* @.str.10.1625, i32 0, i32 0), i8* %call78)"
strLine = "  call void @apr_table_addn(%struct.apr_table_t* %73, i8* getelementptr inbounds ([5 x i8], [5 x i8]* @.str.10.1625, i32 0, i32 0), i8* %call78)"
    #for i in range(len(res2)):
    #    print(count4,res2[i])

    #    count4 += 1
    #for i in range(len(res2)):
    #    print(i)
        #if i == 0:
        #    print(res2[1])
        #else:
        #    print(res2[2])

strLine1 = ""
funformalPara = []
ppp = []
def getFunctionPara(line):
    strline1 = line
    if '...' in strline1:
        strline1 = strline1.split("...")[-1].replace(") ","")
        print (strline1)
        #return
    res = re.split("\(|\)", strline1)
    print(res)
    for item in res:
        print("res item ", item)
        spitem = re.split(",",item)
        print("spitem is ", spitem)
        for item2 in spitem:
            resz = re.split(" ",item2)
            if len(resz) == 1:
                if '@' in resz[0]:
                    ppp.append(resz[0])
                    print("PPP function Name is ",resz[0])
            print("~~~~resz is ",resz)
            if len(resz) ==2:
                if ('%' in resz[1] or '@' in resz[1]):
                    print("1111",resz[1])
                    funformalPara.append(resz[1])
            if len(resz) ==3:
                if '@.str' not in resz[2] and  'inbounds' not in resz[2]  and ']' not in resz[2] and ('%' in resz[2] or '@' in resz[2]):

                    funformalPara.append(resz[2])
                    print("~~~~~~~~~~~~~~the formalPara is ",resz[2])
            if len(resz) ==4:
                if resz[2] == 'zeroext':
                    funformalPara.append(resz[3])
    print("~~~~~~~~~~~~funciton formalPara is :")

    for item in funformalPara:
        print(item)
    '''
    if 'getelementptr' in strline1:
        res1 = re.split(",", res[1])
        res1 += re.split(",", res[3])

        print("res1 is ",res1)
    else:
        res1 = re.split(",", res[1])
        print("res1 is ",res1)
    res1=""
    ##for i in range(len(res)):
    #    res1 += re.split(",",res[1])
    #print(res1)
    funformalPara = []

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
    print("funciton formalPara is :")
    '''

getFunctionPara(strLine)


bitcastLine = "  %4 = bitcast %struct.ap_conf_vector_t* %3 to i8**"
res22 = re.split(",| ",bitcastLine)
print("res bitcast is ", res22)
tmpSta = Statement()
tmpSta.Op = 'bitcast'
tmpSta.leftVal = res22[2]
tmpSta.firstType = res22[5]
tmpSta.rightVal = res22[6]
tmpSta.secondType = res22[8]
print("Statement Op is: ", tmpSta.Op,", leftVal is: ",tmpSta.leftVal,", firstType is: ",tmpSta.firstType,", rightVal is: ",tmpSta.rightVal,", secondType is: ",tmpSta.secondType)


#line = "  %yy_buffer_stack_top17 = getelementptr inbounds %struct.yyguts_t, %struct.yyguts_t* %33, i32 0, i32 3, !10"
#line = "  %arrayidx10 = getelementptr inbounds %struct.yy_buffer_state*, %struct.yy_buffer_state** %25, i64 %27, !10"
#line = "  %v_type = getelementptr inbounds %struct.typval_T, %struct.typval_T* %0, i32 0, i32 0, !dbg !80290, !10"
#line = "  %incdec.ptr = getelementptr inbounds %struct.hashitem_S, %struct.hashitem_S* %19, i32 1, !dbg !80248, !10"
#, !10
#line = "  store i32 %23, i32* %yy_n_chars11, align 8, !10"
#line = "  store %struct.hashitem_S* %incdec.ptr, %struct.hashitem_S** %hi, align 8, !dbg !80248, !10"
# line = "  %28 = load i32, i32* %abort, align 4, !dbg !80272, !10"
#line = "  %tobool = icmp ne %struct.yy_buffer_state** %4, null, !10"
#  %cmp = icmp eq i32 %1, 6, !dbg !80291

line = "  %cmp1 = icmp ne %struct.dictvar_S* %4, null, !dbg !80301, !10"

res2 = re.split(",| ", line)
print("res2 is ",res2)
#icmp
tmpSta = Statement()
tmpSta.Op = 'icmp'
tmpSta.firstType = res2[5] #'ne' or 'eq'
tmpSta.secondType = res2[6] #true type
tmpSta.leftVal = res2[7] #op1
tmpSta.rightVal = res2[9] #op2
if '!dbg' in res2:
    tmpSta.linenumber = res2[14]
else:
    tmpSta.linenumber = res2[11]
if res2[9] == 'null':
    print("this is null",res2[9])
print("Statement Op is: ", tmpSta.Op,", leftVal is: ",tmpSta.leftVal,", firstType is: ",tmpSta.firstType,", rightVal is: ",tmpSta.rightVal,", secondType is: ",tmpSta.secondType,", linenumber is: ",tmpSta.linenumber)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~test ok
#load test
# tmpSta = Statement()
# tmpSta.Op = 'load'
# tmpSta.leftVal = res2[2]
# tmpSta.firstType = res2[5]
# tmpSta.secondType = res2[7]
# tmpSta.rightVal = res2[8]
# if '!dbg' in res2:
#     tmpSta.linenumber = res2[16]
# else:
#     tmpSta.linenumber = res2[13]
#
# print("Statement Op is: ", tmpSta.Op,", leftVal is: ",tmpSta.leftVal,", firstType is: ",tmpSta.firstType,", rightVal is: ",tmpSta.rightVal,", secondType is: ",tmpSta.secondType,", linenumber is: ",tmpSta.linenumber)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~test ok
# getelementptr
# tmpSta = Statement()
# tmpSta.Op = 'getelementptr'
# tmpSta.leftVal = res2[2]
# # 用 ‘x’ 来区分是否为数组,有bug，还没有考虑到变量名称带有x的情况
# if 'x' not in res2:
#     print("in getelementptr shows res2 size is", len(res2), res2)
#     tmpSta.rightVal = res2[9]
#     tmpSta.firstType = res2[6]
#     if '!dbg' in res2:
#         if len(res2) == 21:
#             tmpSta.secondType = res2[15]  # it means the index of a pointer variable in the struct object
#             tmpSta.linenumber = res2[20]
#         if len(res2) == 18:
#             tmpSta.secondType = res2[12]  # it means the index of a pointer variable in the struct object
#             tmpSta.linenumber = res2[17]
#     else:
#         if len(res2) == 18:
#             tmpSta.secondType = res2[15]  # it means the index of a pointer variable in the struct object
#             tmpSta.linenumber = res2[17]
#         if len(res2) == 15:
#             tmpSta.secondType = res2[12]  # it means the index of a pointer variable in the struct object
#             tmpSta.linenumber = res2[14]
# else:  # it means an array type
#     if len(res2) == 24:  # it means a two-dimensional array
#         tmpSta.firstType = res2[10].replace(']', '')
#         tmpSta.rightVal = res2[17]
#         tmpSta.secondType = res2[23]
#     else:
#         tmpSta.firstType = res2[8].replace(']',
#                                            '')  # a key word to judge whether should go further calculation, only pointer type needed
#         tmpSta.rightVal = res2[13]
#         tmpSta.secondType = res2[19]
#
# print("Statement Op is: ", tmpSta.Op,", leftVal is: ",tmpSta.leftVal,", firstType is: ",tmpSta.firstType,", rightVal is: ",tmpSta.rightVal,", secondType is: ",tmpSta.secondType,", linenumber is: ",tmpSta.linenumber)
# #,", linenumber is: ",tmpSta.linenumber

#store
#
# tmpSta = Statement()
# tmpSta.Op = 'store'
# tmpSta.leftVal = res2[4]
# tmpSta.firstType = res2[3]
# tmpSta.rightVal = res2[7]
# tmpSta.secondType = res2[6]
# if '!dbg' in res2:
#     tmpSta.linenumber = res2[15]
# else:
#     tmpSta.linenumber = res2[12]
# print("Statement Op is: ", tmpSta.Op,", leftVal is: ",tmpSta.leftVal,", firstType is: ",tmpSta.firstType,", rightVal is: ",tmpSta.rightVal,", secondType is: ",tmpSta.secondType,", linenumber is: ",tmpSta.linenumber)
#,", linenumber is: ",tmpSta.linenumber


#strPPP = "  %call158 = call i8* (%struct.apr_pool_t*, i8*, ...) @apr_psprintf(%struct.apr_pool_t* %178, i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str.19.1633, i32 0, i32 0), i32 %conv157)"
#getFunctionPara(strPPP)

strZero = "  %call14 = call zeroext i8 @get_reg_type(i32 %10, i64* %reglen), !dbg !102696"
resZ = re.split(",| ",strZero)
print("resZ is : " ,resZ)

'''
for i in range(len(res1)):
    res2 = re.split(" ",res1[i])
    count2 = 0
    #print(count1,item)
    if 'getelementptr' in res2:
        print("eeee")
    else:
        if i == 0:
            print("0~~~~~~~~",res2[0],"1~~~~~~~~~",res2[1])
            #funformalPara.append(res2[1])
        else:
            if len(res2) >0:#res2不为空
                print("1~~~~~~~~",res2[1],"2~~~~~~~~~",res2[2])

            #funformalPara.append(res2[2])

    count1 +=1
funformalPara.clear()
'''



'''
with open(filename,'r') as f:

    for line in f:
        res = re.split(",| ",line)
        print(line)
        print(res)
'''
