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
#strLine = "  %call = call i32 bitcast (i32 (%struct.ap_filter_t*, %struct.apr_bucket_brigade*)* @ap_pass_brigade to i32 (%struct.ap_filter_t.1169*, %struct.apr_bucket_brigade*)*)(%struct.ap_filter_t.1169* %48, %struct.apr_bucket_brigade* %49), !dbg !91561"
#strLine = "  %call = call i32 @apr_file_open_stdout(%struct.apr_file_t** %out, %struct.apr_pool_t* %0), !dbg !60008"
#strLine = "  %call.i.i245.i = call i8** @_ZN13nsCOMPtr_base16begin_assignmentEv(%class.nsCOMPtr_base* nonnull %79) #21, !dbg !7044245"
#strLine = "  %call = call [1 x %struct.__jmp_buf_tag]* @MOZ_PNG_set_longjmp_fn(%struct.png_struct_def* nonnull %1, void (%struct.__jmp_buf_tag*, i32)* nonnull @__longjmp_chk, i64 200) #17, !dbg !301182"
strLine = "  call void bitcast (void (%'class.mozilla::binding_danger::TErrorResult.1'*, %struct.JSContext*)* @_ZN7mozilla14binding_danger12TErrorResultINS0_30AssertAndSuppressCleanupPolicyEE27StealExceptionFromJSContextEP9JSContext to void (%'class.mozilla::binding_danger::TErrorResult'*, %struct.JSContext*)*)(%'class.mozilla::binding_danger::TErrorResult'* %72, %struct.JSContext* nonnull %aCx) #21, !dbg !13266065"
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
                if ('%' in resz[1] or '@' in resz[1]) and '*' not in resz[1]:
                    print("1111",resz[1])
                    funformalPara.append(resz[1])
            if len(resz) ==3:
                if '@.str' not in resz[2] and  'inbounds' not in resz[2]  and ']' not in resz[2] and ('%' in resz[2] or '@' in resz[2]):
                    funformalPara.append(resz[2])
                    print("~~~~~~~~~~~~~~the formalPara is ",resz[2])
            if len(resz) ==4:
                if resz[2] == 'zeroext':
                    funformalPara.append(resz[3])
                if resz[2] == 'nonnull':
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
#strLine = "  store i64 %3, i64* getelementptr inbounds ([81 x %struct.vimvar], [81 x %struct.vimvar]* @vimvars, i64 0, i64 1, i32 1, i32 0, i32 2, i32 0), align 8, !dbg !92996"
#strLine ="  %next.gep = getelementptr [33 x i8], [33 x i8]* %buffer, i64 0, i64 %index"
#strLine = "  %ind.end = getelementptr [33 x i8], [33 x i8]* %buffer, i64 0, i64 %n.vec, !dbg !979824"
#strLine = "  %wide.load = load <16 x i8>, <16 x i8>* %32, align 16, !dbg !979824"
#strLine = "  %114 = getelementptr inbounds [10 x [10 x i32*]], [10 x [10 x i32*]]* %14, i64 0, i64 %113"
#strLine = "  %114 = getelementptr inbounds [10 x [10 x i32*]], [10 x [10 x i32*]]* %14, i64 0, i64 %113, !dbg !979824"
#strLine = "  store i8** %call, i8*** %note, align 8, !dbg !47439"
#strLine = "  %call10.i = call noalias i8* @__kmalloc(i64 %add2, i32 3264) #12, !dbg !5619"
#strLine = "  %arrayidx7.i = getelementptr [3 x [14 x %struct.kmem_cache*]], [3 x [14 x %struct.kmem_cache*]]* @kmalloc_caches, i64 0, i64 0, i64 %retval.0.i.ph.i, !dbg !5616"
#strLine = "  %add.ptr6 = getelementptr i8, i8* %incdec.ptr, i64 %mul, !dbg !5629"
#strLine = "  %0 = load %struct.blkcg_policy.14873*, %struct.blkcg_policy.14873** getelementptr inbounds ([5 x %struct.blkcg_policy.14873*], [5 x %struct.blkcg_policy.14873*]* @blkcg_policy, i64 0, i64 0), align 16, !dbg !362626"
#strLine = "  call void @llvm.dbg.value(metadata i8* %raw_pkcs7, metadata !5237, metadata !DIExpression()), !dbg !5252"
#strLine = " call void @llvm.dbg.value(metadata %struct.pkcs7_message* inttoptr (i64 -6148914691236517206 to %struct.pkcs7_message*), metadata !5243, metadata !DIExpression()), !dbg !5252"
#strLine = "  call void @llvm.dbg.value(metadata i32 -1431655766, metadata !5247, metadata !DIExpression()), !dbg !5252"
#strLine = "  call void @llvm.dbg.value(metadata %struct.task_struct* inttoptr (i64 -6148914691236517206 to %struct.task_struct*), metadata !5320, metadata !DIExpression()) #7, !dbg !5327"
#strLine = "  call void @llvm.dbg.value(metadata i64 %add2, metadata !5528, metadata !DIExpression()) #7, !dbg !5535"
#strLine  = "  %call10.i = call noalias i8* @__kmalloc(i64 %add2, i32 3264) #12, !dbg !5619"
#strLine = "  store i8* inttoptr (i64 -6148914691236517206 to i8*), i8** %command_line, align 8, !dbg !32940"
#strLine = "  %2 = call { i64, i64 } asm sideeffect '771:\0A\09999:\0A\09.pushsection .discard.retpoline_safe\0A\09 .quad  999b\0A\09.popsection\0A\09call *${3:c};\0A772:\0A.pushsection .parainstructions,\22a\22\0A .balign 8 \0A .quad  771b\0A  .byte ${2:c}\0A  .byte 772b-771b\0A  .short ${4:c}\0A.popsection\0A', '={ax},={rsp},i,i,i,1,~{memory},~{cc},~{dirflag},~{fpsr},~{flags}'(i64 39, i8** getelementptr inbounds (%struct.paravirt_patch_template, %struct.paravirt_patch_template* @pv_ops, i64 0, i32 3, i32 2, i32 0), i32 1, i64 %1) #16, !dbg !32947, !srcloc !32103"
#strLine = "  %measured_times.i = alloca [5 x i64], align 16"
#strLine = "Node0xa057420 [shape=record,label='{if.end58:                                         \l  %call59 = call i32 @early_irq_init() #19, !dbg !7525\l  call void @init_IRQ() #21, !dbg !7526\l  call void @tick_init() #21, !dbg !7527\l  call void @init_timers() #19, !dbg !7528\l  call void @hrtimers_init() #21, !dbg !7529\l  call void @softirq_init() #19, !dbg !7530\l  call void @timekeeping_init() #19, !dbg !7531\l  %call60 = call i32 @rand_initialize() #21, !dbg !7532\l  %13 = load i8*, i8** %command_line, align 8, !dbg !7533\l  call void @llvm.dbg.value(metadata i8* %13, metadata !7356, metadata\l... !DIExpression()), !dbg !7384\l  %call61 = call i64 @strlen(i8* %13) #22, !dbg !7534\l  %conv62 = trunc i64 %call61 to i32, !dbg !7534\l  call void @add_device_randomness(i8* %13, i32 %conv62) #19, !dbg !7535\l  %14 = bitcast i64* %canary.i to i8*, !dbg !7536\l  call void @llvm.lifetime.start.p0i8(i64 8, i8* nonnull %14) #17, !dbg !7536\l  call void @llvm.dbg.value(metadata i64 -6148914691236517206, metadata !7074,\l... metadata !DIExpression()) #17, !dbg !7538\l  store i64 -6148914691236517206, i64* %canary.i, align 8, !dbg !7539\l  call void @llvm.dbg.value(metadata i64 -6148914691236517206, metadata !7075,\l... metadata !DIExpression()) #17, !dbg !7538\l  call void @get_random_bytes(i8* nonnull %14, i32 8) #19, !dbg !7540\l  call void @llvm.dbg.value(metadata i64 -6148914691236517206, metadata !7541,\l... metadata !DIExpression()) #17, !dbg !7548\l  call void @llvm.dbg.value(metadata i64 -6148914691236517206, metadata !7547,\l... metadata !DIExpression()) #17, !dbg !7548\l  %15 = call \{ i64, i64 \} asm sideeffect \"rdtsc\",\l... \"=\{ax\},=\{dx\},~\{dirflag\},~\{fpsr\},~\{flags\}\"() #17, !dbg !7550, !srcloc !7551\l  %asmresult.i.i = extractvalue \{ i64, i64 \} %15, 0, !dbg !7550\l  %asmresult1.i.i = extractvalue \{ i64, i64 \} %15, 1, !dbg !7550\l  call void @llvm.dbg.value(metadata i64 %asmresult.i.i, metadata !7541,\l... metadata !DIExpression()) #17, !dbg !7548\l  call void @llvm.dbg.value(metadata i64 %asmresult1.i.i, metadata !7547,\l... metadata !DIExpression()) #17, !dbg !7548\l  %shl.i.i = shl i64 %asmresult1.i.i, 32, !dbg !7552\l  %or.i.i = or i64 %shl.i.i, %asmresult.i.i, !dbg !7552\l  call void @llvm.dbg.value(metadata i64 %or.i.i, metadata !7075, metadata\l... !DIExpression()) #17, !dbg !7538\l  %add.i173 = mul i64 %or.i.i, 4294967297, !dbg !7553\l  %16 = load i64, i64* %canary.i, align 8, !dbg !7554\l  call void @llvm.dbg.value(metadata i64 %16, metadata !7074, metadata\l... !DIExpression()) #17, !dbg !7538\l  %add1.i = add i64 %add.i173, %16, !dbg !7554\l  %and.i174 = and i64 %add1.i, -256, !dbg !7555\l  call void @llvm.dbg.value(metadata i64 %and.i174, metadata !7074, metadata\l... !DIExpression()) #17, !dbg !7538\l  store i64 %and.i174, i64* %canary.i, align 8, !dbg !7555\l  call void @llvm.dbg.value(metadata %struct.task_struct* inttoptr (i64\l... -6148914691236517206 to %struct.task_struct*), metadata !7556, metadata\l... !DIExpression()) #17, !dbg !7563\l  %17 = call %struct.task_struct* asm \"movq %gs:$\{1:P\},$0\",\l... \"=r,im,~\{dirflag\},~\{fpsr\},~\{flags\}\"(%struct.task_struct** nonnull\l... @current_task) #14, !dbg !7565, !srcloc !7566\l  call void @llvm.dbg.value(metadata %struct.task_struct* %17, metadata !7556,\l... metadata !DIExpression()) #17, !dbg !7563\l  %stack_canary.i = getelementptr inbounds %struct.task_struct,\l... %struct.task_struct* %17, i64 0, i32 55, !dbg !7567\l  store i64 %and.i174, i64* %stack_canary.i, align 16, !dbg !7568\l  call void @llvm.dbg.value(metadata i64 %and.i174, metadata !7074, metadata\l... !DIExpression()) #17, !dbg !7538\l  call void asm \"movq $1,%gs:$0\", \"=*m,re,*m,~\{dirflag\},~\{fpsr\},~\{flags\}\"(i64*\l... getelementptr inbounds (%struct.fixed_percpu_data, %struct.fixed_percpu_data*\l... @fixed_percpu_data, i64 0, i32 1), i64 %and.i174, i64* getelementptr inbounds\l... (%struct.fixed_percpu_data, %struct.fixed_percpu_data* @fixed_percpu_data,\l... i64 0, i32 1)) #17, !dbg !7569, !srcloc !7571\l  call void @llvm.lifetime.end.p0i8(i64 8, i8* nonnull %14) #17, !dbg !7572\l  call void @time_init() #19, !dbg !7573\l  call void @printk_safe_init() #19, !dbg !7574\l  call void @perf_event_init() #19, !dbg !7575\l  %call63 = call i32 @profile_init() #19, !dbg !7576\l  call void @call_function_init() #21, !dbg !7577\l  call void @llvm.dbg.value(metadata i32 -1431655766, metadata !7371, metadata\l... !DIExpression()), !dbg !7578\l  call void @llvm.dbg.value(metadata i64 -6148914691236517206, metadata !7373,\l... metadata !DIExpression()), !dbg !7579\l  call void @llvm.dbg.value(metadata i64 -6148914691236517206, metadata !7479,\l... metadata !DIExpression()) #17, !dbg !7580\l  call void @llvm.dbg.value(metadata i64 -6148914691236517206, metadata !7485,\l... metadata !DIExpression()) #17, !dbg !7580\l  call void @llvm.dbg.value(metadata i64 -6148914691236517206, metadata !7485,\l... metadata !DIExpression()) #17, !dbg !7580\l  call void @llvm.dbg.value(metadata i64 -6148914691236517206, metadata !7486,\l... metadata !DIExpression()) #17, !dbg !7580\l  call void @llvm.dbg.value(metadata i64 -6148914691236517206, metadata !7486,\l... metadata !DIExpression()) #17, !dbg !7580\l  call void @llvm.dbg.value(metadata i64 -6148914691236517206, metadata !7487,\l... metadata !DIExpression()) #17, !dbg !7580\l  call void @llvm.dbg.value(metadata i64 -6148914691236517206, metadata !7487,\l... metadata !DIExpression()) #17, !dbg !7580\l  call void @llvm.dbg.value(metadata i64 -6148914691236517206, metadata !7488,\l... metadata !DIExpression()) #17, !dbg !7580\l  call void @llvm.dbg.value(metadata i64 -6148914691236517206, metadata !7488,\l... metadata !DIExpression()) #17, !dbg !7580\l  call void @llvm.dbg.value(metadata i64 -6148914691236517206, metadata !7489,\l... metadata !DIExpression()) #17, !dbg !7580\l  call void @llvm.dbg.value(metadata i64 -6148914691236517206, metadata !7489,\l... metadata !DIExpression()) #17, !dbg !7580\l  %18 = call i64 @llvm.read_register.i64(metadata !7348) #17, !dbg !7582\l  %19 = call \{ i64, i64 \} asm sideeffect \"771:\\0A\\09999:\\0A\\09.pushsection\l... .discard.retpoline_safe\\0A\\09 .quad  999b\\0A\\09.popsection\\0A\\09call *$\{3:c\}\l  %asmresult.i175 = extractvalue \{ i64, i64 \} %19, 0, !dbg !7582\l  %asmresult1.i176 = extractvalue \{ i64, i64 \} %19, 1, !dbg !7582\l  call void @llvm.dbg.value(metadata i64 %asmresult.i175, metadata !7489,\l... metadata !DIExpression()) #17, !dbg !7580\l  call void @llvm.write_register.i64(metadata !7348, i64 %asmresult1.i176)\l... #17, !dbg !7582\l  call void @llvm.dbg.value(metadata i64 %asmresult.i175, metadata !7479,\l... metadata !DIExpression()) #17, !dbg !7580\l  call void @llvm.dbg.value(metadata i64 %asmresult.i175, metadata !7373,\l... metadata !DIExpression()), !dbg !7579\l  %20 = and i64 %asmresult.i175, 512, !dbg !7583\l  %tobool83 = icmp eq i64 %20, 0, !dbg !7583\l  call void @llvm.dbg.value(metadata i1 %tobool83, metadata !7371, metadata\l... !DIExpression()), !dbg !7578\l  br i1 %tobool83, label %if.end108, label %do.body99, !dbg !7583, !prof !7499\l|{<s0>T|<s1>F}}'];"
#strLine = "  call fastcc void @initcall_debug_enable() #26, !dbg !33050"
#strLine = "  %range.sroa.8109.0..sroa_idx110 = getelementptr [0 x %struct.kvm_io_range.1949], [0 x %struct.kvm_io_range.1949]* %25, i64 0, i64 %conv21, i32 2, !dbg !62453"
#strLine = "  %5 = call { i64, i1 } @llvm.umul.with.overflow.i64(i64 %conv, i64 24) #5, !dbg !62369"
#strLine = "  %28 = load %struct.kmem_cache*, %struct.kmem_cache** getelementptr inbounds ([3 x [14 x %struct.kmem_cache*]], [3 x [14 x %struct.kmem_cache*]]* @kmalloc_caches, i64 0, i64 0, i64 9), align 8, !dbg !58243"
#strLine = "  %arraydecay175 = getelementptr inbounds %struct.kvm_signal_mask, %struct.kvm_signal_mask* %39, i64 0, i32 1, i64 0, !dbg !58350"
#strLine = "  %rlock.i.i.i.i372 = getelementptr inbounds %struct.kern_ipc_perm, %struct.kern_ipc_perm* %call.i, i64 0, i32 0, i32 0, i32 0, !dbg !45521"
#strLine = "  %arrayidx.i44.i = getelementptr %struct.io_cq.7131, %struct.io_cq.7131* %9, i64 1, i32 1, !dbg !349396"
#strLine = "  %126 = load i64, i64* bitcast (i16** @_ZN12nsCharTraitsIDsE12sEmptyBufferE to i64*), align 8, !dbg !160029"
#strLine = "  %arrayidx.i.i.i = getelementptr %struct.snd_ac97, %struct.snd_ac97* %ac97, i64 0, i32 22, i64 42, !dbg !6489"
#strLine = "  %arrayidx.i495 = getelementptr %struct.snd_ac97, %struct.snd_ac97* %ac97, i64 0, i32 22, i64 %idxprom.i494, !dbg !6580"
#strLine = "  %tmp_pmatch = alloca [10 x %struct.conn_state_t], align 16"
#strLine = "  %arraydecay = getelementptr inbounds [10 x %struct.conn_state_t], [10 x %struct.conn_state_t]* %tmp_pmatch, i32 0, i32 0, !dbg !53680"
#strLine = "  %mData.i.i.i.i = getelementptr inbounds %class.nsAtomCString, %class.nsAtomCString* %ref.tmp, i64 0, i32 0, i32 0, i32 0, i32 0, !dbg !208109"
#strLine = "  %arraydecay = getelementptr inbounds [90 x [40 x i8]], [90 x [40 x i8]]* @_ZL15kEventTypeNames, i64 0, i64 %conv, i64 0, !dbg !208015"
#strLine = "  %mClassFlags.i.i.i.i = getelementptr inbounds %class.nsAtomCString, %class.nsAtomCString* %ref.tmp, i64 0, i32 0, i32 0, i32 0, i32 3, !dbg !208112"
#strLine = "  ret i8* %14, !dbg !324365"
#strLine  = "  %14 = load i8*, i8** getelementptr inbounds (%class.nsTString.393, %class.nsTString.393* @_ZZN7mozilla4a11y14AccessibleWrap12ReturnStringER12nsTSubstringIDsEE14returnedString, i64 0, i32 0, i32 0, i32 0), align 8, !dbg !324364"
#strLine = "  %switch.gep = getelementptr inbounds [3 x %struct.nsRoleMapEntry*], [3 x %struct.nsRoleMapEntry*]* @switch.table._ZN7mozilla4a11y20xpcAccessibleGenericC2EPNS0_10AccessibleE, i64 0, i64 %1, !dbg !149373"
#strLine = "  %add.ptr.i = getelementptr inbounds [114 x %struct.nsRoleMapEntry], [114 x %struct.nsRoleMapEntry]* @_ZL12sWAIRoleMaps, i64 0, i64 %idx.ext.i, !dbg !149374"
#strLine = "  %tobool.i30 = icmp eq %'class.mozilla::LinkedList.213'* %28, null, !dbg !108703"
#strLine = "  %28 = load %'class.mozilla::LinkedList.213'*, %'class.mozilla::LinkedList.213'** getelementptr inbounds (%'class.mozilla::Array.212', %'class.mozilla::Array.212'* @_ZN7mozilla24ClearOnShutdown_Internal18sShutdownObserversE, i64 0, i32 0, i64 5, i32 0), align 8, !dbg !108665"
#strLine = "  %allowed.sroa.11 = alloca <{ i8, [5 x i8] }>, align 2"
#strLine = "  %allowed.sroa.11.0..sroa_idx379 = getelementptr inbounds <{ i8, [5 x i8] }>, <{ i8, [5 x i8] }>* %allowed.sroa.11, i64 0, i32 0"
#strLine = "  %ref.tmp.sroa.0 = alloca <{ %'class.mozilla::media::TimeUnit', %'class.mozilla::media::TimeUnit', %'class.mozilla::media::TimeUnit' }>, align 8"
#strLine = "  %ref.tmp.sroa.0.0..sroa_cast43 = bitcast <{ %'class.mozilla::media::TimeUnit', %'class.mozilla::media::TimeUnit', %'class.mozilla::media::TimeUnit' }>* %ref.tmp.sroa.0 to i8*, !dbg !4838470"
#strLine = "  %ref.tmp.sroa.0.16..sroa_idx32 = getelementptr inbounds <{ %'class.mozilla::media::TimeUnit', %'class.mozilla::media::TimeUnit', %'class.mozilla::media::TimeUnit' }>, <{ %'class.mozilla::media::TimeUnit', %'class.mozilla::media::TimeUnit', %'class.mozilla::media::TimeUnit' }>* %ref.tmp.sroa.0, i64 0, i32 1, !dbg !4838490"
#strLine = "  %arrayidx = getelementptr inbounds [146 x %class.JSObject* (%struct.JSContext*)*], [146 x %class.JSObject* (%struct.JSContext*)*]* bitcast (<{ [138 x %class.JSObject* (%struct.JSContext*)*], [8 x %class.JSObject* (%struct.JSContext*)*] }>* @_ZN7mozilla3domL26sConstructorGetterCallbackE to [146 x %class.JSObject* (%struct.JSContext*)*]*), i64 0, i64 %idxprom, !dbg !12528166"
#strLine = "  %rq_iov138 = getelementptr inbounds %struct.smb_rqst, %struct.smb_rqst* %arrayidx137, i64 0, i32 0, !dbg !445793"
#strLine = "  %arrayidx137 = getelementptr inbounds [3 x %struct.smb_rqst], [3 x %struct.smb_rqst]* %rqst, i64 0, i64 1, !dbg !445792"
#strLine = "  %124 = getelementptr inbounds 'class.mozilla::dom::asmjscache::(anonymous namespace)::ParentRunnable', %'class.mozilla::dom::asmjscache::(anonymous namespace)::ParentRunnable'* %this, i64 0, i32 0, i32 0, i32 0, !dbg !12893"
#strLine = "  %call.i.i245.i = call i8** @_ZN13nsCOMPtr_base16begin_assignmentEv(%class.nsCOMPtr_base* nonnull %79) #21, !dbg !7044245"
#strLine = "  %mMetadataFile.i = getelementptr inbounds %'class.mozilla::dom::asmjscache::(anonymous namespace)::ParentRunnable', %'class.mozilla::dom::asmjscache::(anonymous namespace)::ParentRunnable'* %this, i64 0, i32 14, !dbg !7044240"
#strLine = "  %call = call [1 x %struct.__jmp_buf_tag]* @MOZ_PNG_set_longjmp_fn(%struct.png_struct_def* nonnull %1, void (%struct.__jmp_buf_tag*, i32)* nonnull @__longjmp_chk, i64 200) #17, !dbg !301182"
strLine = "  call void bitcast (void (%'class.mozilla::binding_danger::TErrorResult.1'*, %struct.JSContext*)* @_ZN7mozilla14binding_danger12TErrorResultINS0_30AssertAndSuppressCleanupPolicyEE27StealExceptionFromJSContextEP9JSContext to void (%'class.mozilla::binding_danger::TErrorResult'*, %struct.JSContext*)*)(%'class.mozilla::binding_danger::TErrorResult'* %72, %struct.JSContext* nonnull %aCx) #21, !dbg !13266065"
if 'function' in strLine:
    print("now ! actually function is really in line!!!!!!!!")
resZ = re.split(",| ",strLine)
if '!dbg' in resZ:
    print("length is: ",len(resZ),"resZ is : " ,resZ, "\nlinenumber of call instruction is: ",resZ[-1])
count11 = 0
for item in resZ:
    print("index ", count11, " is: ", item)
    count11 += 1

if 'asm' in resZ:
    print("no~!~~~~~~~~~~~~~~~~~~~")
if '@llvm.umul.with.overflow' in strLine:
    print("llvm !!!!!!!!!!!!!!!!")
#ret instruction



teststr = "-14316%55766"
if teststr.isdigit():
    print("负数也是digit")
else:
    print("负数不是digit")
    if '-' in teststr:
        teststr = teststr.replace('-','').replace('%','')
        print(teststr)

tmpline = "	Node0xa0572e0:s0 -> Node0xa057380[label='W:2000'];"
if 'label' in tmpline:
    print("yeah!!")
if '->' in tmpline:
    print("->>>>>>>>>>>>>>>>>>")



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

left = "%struct.walk_cache_t*"
if '*' in left:
    print("oh yes")