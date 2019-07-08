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
#strLine = "  call void @apr_table_addn(%struct.apr_table_t* %73, i8* getelementptr inbounds ([5 x i8], [5 x i8]* @.str.10.1625, i32 0, i32 0), i8* %call78)"
#strLine = "  call void (i8*, i32, i32, i32, i32, %struct.request_rec.1168*, i8*, ...) bitcast (void (i8*, i32, i32, i32, i32, %struct.request_rec*, i8*, ...)* @ap_log_rerror_ to void (i8*, i32, i32, i32, i32, %struct.request_rec.1168*, i8*, ...)*)(i8* getelementptr inbounds ([19 x i8], [19 x i8]* @.str.7.2598, i32 0, i32 0), i32 539, i32 %cond89, i32 3, i32 %115, %struct.request_rec.1168* %116, i8* getelementptr inbounds ([51 x i8], [51 x i8]* @.str.8.2599, i32 0, i32 0), i64 %117, i64 %118, i64 %119), !dbg !91696"
#strLine = "  call void bitcast (void (%struct.ap_filter_t*)* @ap_remove_output_filter to void (%struct.ap_filter_t.1169*)*)(%struct.ap_filter_t.1169* %46), !dbg !91557"
strLine = "  %call = call i32 bitcast (i32 (%struct.ap_filter_t*, %struct.apr_bucket_brigade*)* @ap_pass_brigade to i32 (%struct.ap_filter_t.1169*, %struct.apr_bucket_brigade*)*)(%struct.ap_filter_t.1169* %48, %struct.apr_bucket_brigade* %49), !dbg !91561"
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
            if len(resz) == 5:
                if '@' in resz[1]:
                    print("function name could be ",resz[1])
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

#
bitcastLine = "  %4 = bitcast %struct.ap_conf_vector_t* %3 to i8**, !dbg !514441"
res22 = re.split(",| ",bitcastLine)
print("res bitcast is ", res22)
tmpSta = Statement()
tmpSta.Op = 'bitcast'
tmpSta.leftVal = res22[2]
tmpSta.firstType = res22[5]
tmpSta.rightVal = res22[6]
tmpSta.secondType = res22[8]
print("Statement Op is: ", tmpSta.Op,", leftVal is: ",tmpSta.leftVal,", firstType is: ",tmpSta.firstType,", rightVal is: ",tmpSta.rightVal,", secondType is: ",tmpSta.secondType)


#line = "  %yy_buffer_stack_top17 = getelementptr inbounds %struct.yyguts_t, %struct.yyguts_t* %33, i32 0, i32 3, !dbg !518042"
#line = "  %arrayidx10 = getelementptr inbounds %struct.yy_buffer_state*, %struct.yy_buffer_state** %25, i64 %27, !dbg !518042"
#line = "  %v_type = getelementptr inbounds %struct.typval_T, %struct.typval_T* %0, i32 0, i32 0, !dbg !80290"
#line = "  %incdec.ptr = getelementptr inbounds %struct.hashitem_S, %struct.hashitem_S* %19, i32 1, !dbg !80248"
#, !10
#line = "  store i32 %23, i32* %yy_n_chars11, align 8, !dbg !80248"
#line = "  store %struct.hashitem_S* %incdec.ptr, %struct.hashitem_S** %hi, align 8, !dbg !80248"
#line = "  %28 = load i32, i32* %abort, align 4, !dbg !80272"
#line = "  %tobool = icmp ne %struct.yy_buffer_state** %4, null, !dbg !518042"
#  %cmp = icmp eq i32 %1, 6, !dbg !80291


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~icmp test ok
# line = "  %cmp1 = icmp ne %struct.dictvar_S* %4, null, !dbg !80301"
#
#res2 = re.split(",| ", line)
#print("res2 is ",res2)
# #icmp
# tmpSta = Statement()
# tmpSta.Op = 'icmp'
# tmpSta.firstType = res2[5] #'ne' or 'eq'
# tmpSta.secondType = res2[6] #true type
# tmpSta.leftVal = res2[7] #op1
# tmpSta.rightVal = res2[9] #op2
# if '!dbg' in res2:
#     tmpSta.linenumber = res2[12]
#
# if res2[9] == 'null':
#     print("this is null",res2[9])
# print("Statement Op is: ", tmpSta.Op,", leftVal is: ",tmpSta.leftVal,", firstType is: ",tmpSta.firstType,", rightVal is: ",tmpSta.rightVal,", secondType is: ",tmpSta.secondType,", linenumber is: ",tmpSta.linenumber)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~test ok
#load test
# tmpSta = Statement()
# tmpSta.Op = 'load'
# tmpSta.leftVal = res2[2]
# tmpSta.firstType = res2[5]
# tmpSta.secondType = res2[7]
# tmpSta.rightVal = res2[8]
# if '!dbg' in res2:
#     tmpSta.linenumber = res2[14]
#
#
# print("Statement Op is: ", tmpSta.Op,", leftVal is: ",tmpSta.leftVal,", firstType is: ",tmpSta.firstType,", rightVal is: ",tmpSta.rightVal,", secondType is: ",tmpSta.secondType,", linenumber is: ",tmpSta.linenumber)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~test ok
#getelementptr
# tmpSta = Statement()
# tmpSta.Op = 'getelementptr'
# tmpSta.leftVal = res2[2]
# # 用 ‘x’ 来区分是否为数组,有bug，还没有考虑到变量名称带有x的情况
# if 'x' not in res2:
#     print("in getelementptr shows res2 size is", len(res2), res2)
#     tmpSta.rightVal = res2[9]
#     tmpSta.firstType = res2[6]
#     if '!dbg' in res2:
#         if len(res2) == 19:
#             tmpSta.secondType = res2[15]  # it means the index of a pointer variable in the struct object
#             tmpSta.linenumber = res2[18]
#         if len(res2) == 16:
#             tmpSta.secondType = res2[12]  # it means the index of a pointer variable in the struct object
#             tmpSta.linenumber = res2[15]
#     else:
#         if len(res2) == 18:
#             tmpSta.secondType = res2[15]  # it means the index of a pointer variable in the struct object
#             #tmpSta.linenumber = res2[17]
#         if len(res2) == 15:
#             tmpSta.secondType = res2[12]  # it means the index of a pointer variable in the struct object
#             #tmpSta.linenumber = res2[14]
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

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~test ok
#store
#
#
# tmpSta = Statement()
# tmpSta.Op = 'store'
# tmpSta.leftVal = res2[4]
# tmpSta.firstType = res2[3]
# tmpSta.rightVal = res2[7]
# tmpSta.secondType = res2[6]
# if '!dbg' in res2:
#     tmpSta.linenumber = res2[13]
#
# print("Statement Op is: ", tmpSta.Op,", leftVal is: ",tmpSta.leftVal,", firstType is: ",tmpSta.firstType,", rightVal is: ",tmpSta.rightVal,", secondType is: ",tmpSta.secondType,", linenumber is: ",tmpSta.linenumber)
#,", linenumber is: ",tmpSta.linenumber


#strPPP = "  %call158 = call i8* (%struct.apr_pool_t*, i8*, ...) @apr_psprintf(%struct.apr_pool_t* %178, i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str.19.1633, i32 0, i32 0), i32 %conv157)"
#getFunctionPara(strPPP)



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~call instruction test ok
#strLine = "  store %struct.lpos_T* %arraydecay, %struct.lpos_T** getelementptr inbounds (%struct.regexec_T, %struct.regexec_T* @rex, i32 0, i32 4), align 8, !dbg !357900"
#strLine = "  %2 = load i8*, i8** getelementptr inbounds ([68 x i8*], [68 x i8*]* @term_strings, i64 0, i64 0), align 16, !dbg !451447"
#strLine = "  %2 = load %struct.regmatch_T*, %struct.regmatch_T** getelementptr inbounds (%struct.regexec_T, %struct.regexec_T* @rex, i32 0, i32 0), align 8, !dbg !357887"
#strLine = "  call void (i8*, i32, i32, i32, i32, %struct.conn_rec*, i8*, ...) @ap_log_cerror_(i8* getelementptr inbounds ([14 x i8], [14 x i8]* @.str.200, i32 0, i32 0), i32 404, i32 0, i32 3, i32 0, %struct.conn_rec* %cond, i8* getelementptr inbounds ([45 x i8], [45 x i8]* @.str.3.201, i32 0, i32 0), i8* %45), !dbg !514441"
#strLine = "  %call27 = call i8* (%struct.apr_pool_t*, ...) @apr_pstrcat(%struct.apr_pool_t* %21, i8* %23, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @.str.51.2521, i32 0, i32 0), i8* null), !dbg !514441"
#strLine ="  call void @apr_table_addn(%struct.apr_table_t* %73, i8* getelementptr inbounds ([5 x i8], [5 x i8]* @.str.10.1625, i32 0, i32 0), i8* %call78), !dbg !514441"
#strLine= "  %call101 = call i8* @apr_pstrmemdup(%struct.apr_pool_t* %114, i8* %116, i64 %sub.ptr.sub), !dbg !514441"
#strLine = "  %call = call i8* (%struct.apr_pool_t*, ...) @apr_pstrcat(%struct.apr_pool_t* %6, i8* %9, i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str.37.1044, i32 0, i32 0), i8* %10, i8* null), !dbg !514441"
#strLine = "  %call = call i32 @find_listeners(%struct.ap_listen_rec** @ap_listeners, %struct.ap_listen_rec** null, i8* %0, i16 zeroext %1), !dbg !514441"
#strLine = "  %call = call i64 @write(i32 2, i8* %0, i64 %conv), !dbg !514441"
#strLine = "  %call2 = call i32 @setsockopt(i32 %2, i32 1, i32 13, i8* %3, i32 8) #11, !dbg !514441"
#strLine = "  %call = call i32 @A_is_ok(i32 %0), !dbg !40868"
#strLine = "  %call887 = call i8* @infinity_str(i32 %conv886, i8 signext %394, i32 %395, i32 %396), !dbg !514441"
#strLine = "  call void @ap_relieve_child_processes(void (i32, i32, i32)* @event_note_child_killed), !dbg !514441"
#strLine = "  call void @apr_table_addn(%struct.apr_table_t* %73, i8* getelementptr inbounds ([5 x i8], [5 x i8]* @.str.10.1625, i32 0, i32 0), i8* %call78), !dbg !514441"
#strLine = "  call void @apr_table_addn(%struct.apr_table_t* %73, i8* getelementptr inbounds ([5 x i8], [5 x i8]* @.str.10.1625, i32 0, i32 0), i8* %call78), !dbg !514441"

#strLine = "  %1 = load volatile i32, i32* @got_int, align 4, !dbg !187006"
#strLine = "  %7 = load i32, i32* getelementptr inbounds ([2 x %struct.spat], [2 x %struct.spat]* @spats, i64 0, i64 0, i32 3, i32 0), align 16, !dbg !386095"
#strLine = "  %27 = load i8*, i8** getelementptr inbounds ([2 x %struct.spat], [2 x %struct.spat]* @spats, i64 0, i64 1, i32 0), align 8, !dbg !386174"
#strLine = "  store i32 %8, i32* getelementptr inbounds ([2 x %struct.spat], [2 x %struct.spat]* @spats, i64 0, i64 0, i32 3, i32 0), align 16, !dbg !386100"
#strLine = "  %144 = load i64, i64* getelementptr inbounds ([2 x %struct.spat], [2 x %struct.spat]* @spats, i64 0, i64 0, i32 3, i32 3), align 16, !dbg !386498"
#strLine = "  %148 = load i64, i64* getelementptr inbounds ([2 x %struct.spat], [2 x %struct.spat]* @spats, i64 0, i64 0, i32 3, i32 3), align 16, !dbg !386526"
#strLine = "  %26 = load i8*, i8** getelementptr inbounds ([2 x %struct.spat], [2 x %struct.spat]* @spats, i64 0, i64 0, i32 0), align 16, !dbg !386169"
#strLine = "  %1 = load i8*, i8** getelementptr inbounds ([463 x %struct.vimoption], [463 x %struct.vimoption]* @options, i64 0, i64 0, i32 0), align 16, !dbg !306956"
#strLine = "  %1 = load i64, i64* getelementptr inbounds ([81 x %struct.vimvar], [81 x %struct.vimvar]* @vimvars, i64 0, i64 0, i32 1, i32 0, i32 2, i32 0), align 8, !dbg !92990"
#strLine = "  store i64 %2, i64* getelementptr inbounds ([81 x %struct.vimvar], [81 x %struct.vimvar]* @vimvars, i64 0, i64 0, i32 1, i32 0, i32 2, i32 0), align 8, !dbg !92994"
strLine = "  store i64 %3, i64* getelementptr inbounds ([81 x %struct.vimvar], [81 x %struct.vimvar]* @vimvars, i64 0, i64 1, i32 1, i32 0, i32 2, i32 0), align 8, !dbg !92996"
resZ = re.split(",| ",strLine)
if '!dbg' in resZ:
    print("length is: ",len(resZ),"resZ is : " ,resZ, "\nlinenumber of call instruction is: ",resZ[-1])
count11 = 0
for item in resZ:
    print("index ", count11, " is: ", item)
    count11 += 1
#ret instruction










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
str1 = "retval.addr"
str2 = "retval1"
if '.addr' in str1:
    tmpSta_rightVal = str1.replace(".addr", "")
    print("tmpSta_rightVal is ", tmpSta_rightVal)
    tmpSta_leftVal = str2.replace(tmpSta_rightVal, "")
    print("tmpSta_leftVal is ", tmpSta_leftVal)
    if tmpSta_leftVal.isdigit():
        print("maybe this case: store i32 * % retval1, i32 ** % retval.addr, do nothing")

