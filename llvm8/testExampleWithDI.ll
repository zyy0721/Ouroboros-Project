; ModuleID = 'testExample.cpp'
source_filename = "testExample.cpp"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-unknown-linux-gnu"

@globalC = dso_local global i32* null, align 8, !dbg !0
@globalD = dso_local global i32** null, align 8, !dbg !9

; Function Attrs: noinline optnone uwtable
define dso_local i32* @_Z4fun1iPiPS_(i32 %n, i32* %ptr, i32** %pptr) #0 !dbg !16 {
entry:
  %n.addr = alloca i32, align 4
  %ptr.addr = alloca i32*, align 8
  %pptr.addr = alloca i32**, align 8
  %newP = alloca i32*, align 8
  %newPP = alloca i32*, align 8
  store i32 %n, i32* %n.addr, align 4
  call void @llvm.dbg.declare(metadata i32* %n.addr, metadata !19, metadata !DIExpression()), !dbg !20
  store i32* %ptr, i32** %ptr.addr, align 8
  call void @llvm.dbg.declare(metadata i32** %ptr.addr, metadata !21, metadata !DIExpression()), !dbg !22
  store i32** %pptr, i32*** %pptr.addr, align 8
  call void @llvm.dbg.declare(metadata i32*** %pptr.addr, metadata !23, metadata !DIExpression()), !dbg !24
  %0 = load i32*, i32** %ptr.addr, align 8, !dbg !25
  store i32* %0, i32** @globalC, align 8, !dbg !26
  %1 = load i32**, i32*** @globalD, align 8, !dbg !27
  store i32** %1, i32*** %pptr.addr, align 8, !dbg !28
  call void @llvm.dbg.declare(metadata i32** %newP, metadata !29, metadata !DIExpression()), !dbg !30
  %call = call noalias i8* @malloc(i64 40) #4, !dbg !31
  %2 = bitcast i8* %call to i32*, !dbg !32
  store i32* %2, i32** %newP, align 8, !dbg !33
  call void @llvm.dbg.declare(metadata i32** %newPP, metadata !34, metadata !DIExpression()), !dbg !35
  %call1 = call i8* @_Znam(i64 40) #5, !dbg !36
  %3 = bitcast i8* %call1 to i32*, !dbg !36
  store i32* %3, i32** %newPP, align 8, !dbg !37
  %4 = load i32*, i32** %ptr.addr, align 8, !dbg !38
  ret i32* %4, !dbg !39
}

; Function Attrs: nounwind readnone speculatable
declare void @llvm.dbg.declare(metadata, metadata, metadata) #1

; Function Attrs: nounwind
declare dso_local noalias i8* @malloc(i64) #2

; Function Attrs: nobuiltin
declare dso_local noalias i8* @_Znam(i64) #3

; Function Attrs: noinline optnone uwtable
define dso_local i32** @_Z4fun2iPiPS_S_(i32 %n, i32* %ptr, i32** %pptr, i32* %ptr1) #0 !dbg !40 {
entry:
  %retval = alloca i32**, align 8
  %n.addr = alloca i32, align 4
  %ptr.addr = alloca i32*, align 8
  %pptr.addr = alloca i32**, align 8
  %ptr1.addr = alloca i32*, align 8
  store i32 %n, i32* %n.addr, align 4
  call void @llvm.dbg.declare(metadata i32* %n.addr, metadata !43, metadata !DIExpression()), !dbg !44
  store i32* %ptr, i32** %ptr.addr, align 8
  call void @llvm.dbg.declare(metadata i32** %ptr.addr, metadata !45, metadata !DIExpression()), !dbg !46
  store i32** %pptr, i32*** %pptr.addr, align 8
  call void @llvm.dbg.declare(metadata i32*** %pptr.addr, metadata !47, metadata !DIExpression()), !dbg !48
  store i32* %ptr1, i32** %ptr1.addr, align 8
  call void @llvm.dbg.declare(metadata i32** %ptr1.addr, metadata !49, metadata !DIExpression()), !dbg !50
  %0 = load i32, i32* %n.addr, align 4, !dbg !51
  %cmp = icmp sgt i32 %0, 0, !dbg !53
  br i1 %cmp, label %if.then, label %if.else, !dbg !54

if.then:                                          ; preds = %entry
  store i32* %n.addr, i32** @globalC, align 8, !dbg !55
  %1 = load i32*, i32** %ptr.addr, align 8, !dbg !57
  %2 = load i32**, i32*** %pptr.addr, align 8, !dbg !58
  store i32* %1, i32** %2, align 8, !dbg !59
  %3 = load i32**, i32*** %pptr.addr, align 8, !dbg !60
  %4 = load i32*, i32** %3, align 8, !dbg !61
  store i32* %4, i32** %ptr1.addr, align 8, !dbg !62
  %5 = load i32*, i32** %ptr1.addr, align 8, !dbg !63
  store i32* %5, i32** %ptr.addr, align 8, !dbg !64
  %6 = load i32, i32* %n.addr, align 4, !dbg !65
  %7 = load i32*, i32** %ptr.addr, align 8, !dbg !66
  %8 = load i32**, i32*** %pptr.addr, align 8, !dbg !67
  %call = call i32* @_Z4fun1iPiPS_(i32 %6, i32* %7, i32** %8), !dbg !68
  store i32* %call, i32** %ptr1.addr, align 8, !dbg !69
  %9 = load i32**, i32*** %pptr.addr, align 8, !dbg !70
  store i32** %9, i32*** %retval, align 8, !dbg !71
  br label %return, !dbg !71

if.else:                                          ; preds = %entry
  store i32** %ptr1.addr, i32*** @globalD, align 8, !dbg !72
  store i32* %n.addr, i32** %ptr.addr, align 8, !dbg !74
  %10 = load i32*, i32** %ptr.addr, align 8, !dbg !75
  %11 = load i32**, i32*** @globalD, align 8, !dbg !76
  store i32* %10, i32** %11, align 8, !dbg !77
  %12 = load i32**, i32*** %pptr.addr, align 8, !dbg !78
  %13 = load i32*, i32** %12, align 8, !dbg !79
  store i32* %13, i32** %ptr1.addr, align 8, !dbg !80
  %14 = load i32*, i32** %ptr.addr, align 8, !dbg !81
  store i32* %14, i32** %ptr1.addr, align 8, !dbg !82
  %15 = load i32**, i32*** @globalD, align 8, !dbg !83
  store i32** %15, i32*** %retval, align 8, !dbg !84
  br label %return, !dbg !84

return:                                           ; preds = %if.else, %if.then
  %16 = load i32**, i32*** %retval, align 8, !dbg !85
  ret i32** %16, !dbg !85
}

attributes #0 = { noinline optnone uwtable "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "min-legal-vector-width"="0" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #1 = { nounwind readnone speculatable }
attributes #2 = { nounwind "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #3 = { nobuiltin "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #4 = { nounwind }
attributes #5 = { builtin }

!llvm.dbg.cu = !{!2}
!llvm.module.flags = !{!12, !13, !14}
!llvm.ident = !{!15}

!0 = !DIGlobalVariableExpression(var: !1, expr: !DIExpression())
!1 = distinct !DIGlobalVariable(name: "globalC", scope: !2, file: !3, line: 3, type: !6, isLocal: false, isDefinition: true)
!2 = distinct !DICompileUnit(language: DW_LANG_C_plus_plus, file: !3, producer: "clang version 8.0.0 (tags/RELEASE_800/final 361961) (llvm/tags/RELEASE_800/final 361957)", isOptimized: false, runtimeVersion: 0, emissionKind: FullDebug, enums: !4, retainedTypes: !5, globals: !8, nameTableKind: None)
!3 = !DIFile(filename: "testExample.cpp", directory: "/usr/local/llvm8/build/examples/Ouroboros")
!4 = !{}
!5 = !{!6}
!6 = !DIDerivedType(tag: DW_TAG_pointer_type, baseType: !7, size: 64)
!7 = !DIBasicType(name: "int", size: 32, encoding: DW_ATE_signed)
!8 = !{!0, !9}
!9 = !DIGlobalVariableExpression(var: !10, expr: !DIExpression())
!10 = distinct !DIGlobalVariable(name: "globalD", scope: !2, file: !3, line: 4, type: !11, isLocal: false, isDefinition: true)
!11 = !DIDerivedType(tag: DW_TAG_pointer_type, baseType: !6, size: 64)
!12 = !{i32 2, !"Dwarf Version", i32 4}
!13 = !{i32 2, !"Debug Info Version", i32 3}
!14 = !{i32 1, !"wchar_size", i32 4}
!15 = !{!"clang version 8.0.0 (tags/RELEASE_800/final 361961) (llvm/tags/RELEASE_800/final 361957)"}
!16 = distinct !DISubprogram(name: "fun1", linkageName: "_Z4fun1iPiPS_", scope: !3, file: !3, line: 6, type: !17, scopeLine: 7, flags: DIFlagPrototyped, spFlags: DISPFlagDefinition, unit: !2, retainedNodes: !4)
!17 = !DISubroutineType(types: !18)
!18 = !{!6, !7, !6, !11}
!19 = !DILocalVariable(name: "n", arg: 1, scope: !16, file: !3, line: 6, type: !7)
!20 = !DILocation(line: 6, column: 15, scope: !16)
!21 = !DILocalVariable(name: "ptr", arg: 2, scope: !16, file: !3, line: 6, type: !6)
!22 = !DILocation(line: 6, column: 23, scope: !16)
!23 = !DILocalVariable(name: "pptr", arg: 3, scope: !16, file: !3, line: 6, type: !11)
!24 = !DILocation(line: 6, column: 34, scope: !16)
!25 = !DILocation(line: 8, column: 15, scope: !16)
!26 = !DILocation(line: 8, column: 13, scope: !16)
!27 = !DILocation(line: 9, column: 12, scope: !16)
!28 = !DILocation(line: 9, column: 10, scope: !16)
!29 = !DILocalVariable(name: "newP", scope: !16, file: !3, line: 10, type: !6)
!30 = !DILocation(line: 10, column: 11, scope: !16)
!31 = !DILocation(line: 11, column: 19, scope: !16)
!32 = !DILocation(line: 11, column: 12, scope: !16)
!33 = !DILocation(line: 11, column: 10, scope: !16)
!34 = !DILocalVariable(name: "newPP", scope: !16, file: !3, line: 12, type: !6)
!35 = !DILocation(line: 12, column: 10, scope: !16)
!36 = !DILocation(line: 13, column: 13, scope: !16)
!37 = !DILocation(line: 13, column: 11, scope: !16)
!38 = !DILocation(line: 14, column: 12, scope: !16)
!39 = !DILocation(line: 14, column: 5, scope: !16)
!40 = distinct !DISubprogram(name: "fun2", linkageName: "_Z4fun2iPiPS_S_", scope: !3, file: !3, line: 21, type: !41, scopeLine: 22, flags: DIFlagPrototyped, spFlags: DISPFlagDefinition, unit: !2, retainedNodes: !4)
!41 = !DISubroutineType(types: !42)
!42 = !{!11, !7, !6, !11, !6}
!43 = !DILocalVariable(name: "n", arg: 1, scope: !40, file: !3, line: 21, type: !7)
!44 = !DILocation(line: 21, column: 16, scope: !40)
!45 = !DILocalVariable(name: "ptr", arg: 2, scope: !40, file: !3, line: 21, type: !6)
!46 = !DILocation(line: 21, column: 24, scope: !40)
!47 = !DILocalVariable(name: "pptr", arg: 3, scope: !40, file: !3, line: 21, type: !11)
!48 = !DILocation(line: 21, column: 35, scope: !40)
!49 = !DILocalVariable(name: "ptr1", arg: 4, scope: !40, file: !3, line: 21, type: !6)
!50 = !DILocation(line: 21, column: 46, scope: !40)
!51 = !DILocation(line: 23, column: 8, scope: !52)
!52 = distinct !DILexicalBlock(scope: !40, file: !3, line: 23, column: 8)
!53 = !DILocation(line: 23, column: 9, scope: !52)
!54 = !DILocation(line: 23, column: 8, scope: !40)
!55 = !DILocation(line: 25, column: 17, scope: !56)
!56 = distinct !DILexicalBlock(scope: !52, file: !3, line: 24, column: 5)
!57 = !DILocation(line: 26, column: 17, scope: !56)
!58 = !DILocation(line: 26, column: 10, scope: !56)
!59 = !DILocation(line: 26, column: 15, scope: !56)
!60 = !DILocation(line: 27, column: 17, scope: !56)
!61 = !DILocation(line: 27, column: 16, scope: !56)
!62 = !DILocation(line: 27, column: 14, scope: !56)
!63 = !DILocation(line: 28, column: 15, scope: !56)
!64 = !DILocation(line: 28, column: 13, scope: !56)
!65 = !DILocation(line: 29, column: 19, scope: !56)
!66 = !DILocation(line: 29, column: 22, scope: !56)
!67 = !DILocation(line: 29, column: 27, scope: !56)
!68 = !DILocation(line: 29, column: 14, scope: !56)
!69 = !DILocation(line: 29, column: 12, scope: !56)
!70 = !DILocation(line: 30, column: 16, scope: !56)
!71 = !DILocation(line: 30, column: 9, scope: !56)
!72 = !DILocation(line: 34, column: 17, scope: !73)
!73 = distinct !DILexicalBlock(scope: !52, file: !3, line: 33, column: 5)
!74 = !DILocation(line: 35, column: 13, scope: !73)
!75 = !DILocation(line: 36, column: 20, scope: !73)
!76 = !DILocation(line: 36, column: 10, scope: !73)
!77 = !DILocation(line: 36, column: 18, scope: !73)
!78 = !DILocation(line: 37, column: 17, scope: !73)
!79 = !DILocation(line: 37, column: 16, scope: !73)
!80 = !DILocation(line: 37, column: 14, scope: !73)
!81 = !DILocation(line: 38, column: 14, scope: !73)
!82 = !DILocation(line: 38, column: 12, scope: !73)
!83 = !DILocation(line: 39, column: 16, scope: !73)
!84 = !DILocation(line: 39, column: 9, scope: !73)
!85 = !DILocation(line: 41, column: 1, scope: !40)
