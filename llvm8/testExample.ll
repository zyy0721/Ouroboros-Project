; ModuleID = 'testExample.cpp'
source_filename = "testExample.cpp"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-unknown-linux-gnu"

@globalC = dso_local global i32* null, align 8
@globalD = dso_local global i32** null, align 8

; Function Attrs: noinline optnone uwtable
define dso_local i32* @_Z4fun1iPiPS_(i32 %n, i32* %ptr, i32** %pptr) #0 {
entry:
  %n.addr = alloca i32, align 4
  %ptr.addr = alloca i32*, align 8
  %pptr.addr = alloca i32**, align 8
  %newP = alloca i32*, align 8
  %newPP = alloca i32*, align 8
  store i32 %n, i32* %n.addr, align 4
  store i32* %ptr, i32** %ptr.addr, align 8
  store i32** %pptr, i32*** %pptr.addr, align 8
  %0 = load i32*, i32** %ptr.addr, align 8
  store i32* %0, i32** @globalC, align 8
  %1 = load i32**, i32*** @globalD, align 8
  store i32** %1, i32*** %pptr.addr, align 8
  %call = call noalias i8* @malloc(i64 40) #3
  %2 = bitcast i8* %call to i32*
  store i32* %2, i32** %newP, align 8
  %call1 = call i8* @_Znam(i64 40) #4
  %3 = bitcast i8* %call1 to i32*
  store i32* %3, i32** %newPP, align 8
  %4 = load i32*, i32** %ptr.addr, align 8
  ret i32* %4
}

; Function Attrs: nounwind
declare dso_local noalias i8* @malloc(i64) #1

; Function Attrs: nobuiltin
declare dso_local noalias i8* @_Znam(i64) #2

; Function Attrs: noinline optnone uwtable
define dso_local i32** @_Z4fun2iPiPS_S_(i32 %n, i32* %ptr, i32** %pptr, i32* %ptr1) #0 {
entry:
  %retval = alloca i32**, align 8
  %n.addr = alloca i32, align 4
  %ptr.addr = alloca i32*, align 8
  %pptr.addr = alloca i32**, align 8
  %ptr1.addr = alloca i32*, align 8
  store i32 %n, i32* %n.addr, align 4
  store i32* %ptr, i32** %ptr.addr, align 8
  store i32** %pptr, i32*** %pptr.addr, align 8
  store i32* %ptr1, i32** %ptr1.addr, align 8
  %0 = load i32, i32* %n.addr, align 4
  %cmp = icmp sgt i32 %0, 0
  br i1 %cmp, label %if.then, label %if.else

if.then:                                          ; preds = %entry
  store i32* %n.addr, i32** @globalC, align 8
  %1 = load i32*, i32** %ptr.addr, align 8
  %2 = load i32**, i32*** %pptr.addr, align 8
  store i32* %1, i32** %2, align 8
  %3 = load i32**, i32*** %pptr.addr, align 8
  %4 = load i32*, i32** %3, align 8
  store i32* %4, i32** %ptr1.addr, align 8
  %5 = load i32*, i32** %ptr1.addr, align 8
  store i32* %5, i32** %ptr.addr, align 8
  %6 = load i32, i32* %n.addr, align 4
  %7 = load i32*, i32** %ptr.addr, align 8
  %8 = load i32**, i32*** %pptr.addr, align 8
  %call = call i32* @_Z4fun1iPiPS_(i32 %6, i32* %7, i32** %8)
  store i32* %call, i32** %ptr1.addr, align 8
  %9 = load i32**, i32*** %pptr.addr, align 8
  store i32** %9, i32*** %retval, align 8
  br label %return

if.else:                                          ; preds = %entry
  store i32** %ptr1.addr, i32*** @globalD, align 8
  store i32* %n.addr, i32** %ptr.addr, align 8
  %10 = load i32*, i32** %ptr.addr, align 8
  %11 = load i32**, i32*** @globalD, align 8
  store i32* %10, i32** %11, align 8
  %12 = load i32**, i32*** %pptr.addr, align 8
  %13 = load i32*, i32** %12, align 8
  store i32* %13, i32** %ptr1.addr, align 8
  %14 = load i32*, i32** %ptr.addr, align 8
  store i32* %14, i32** %ptr1.addr, align 8
  %15 = load i32**, i32*** @globalD, align 8
  store i32** %15, i32*** %retval, align 8
  br label %return

return:                                           ; preds = %if.else, %if.then
  %16 = load i32**, i32*** %retval, align 8
  ret i32** %16
}

attributes #0 = { noinline optnone uwtable "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "min-legal-vector-width"="0" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #1 = { nounwind "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #2 = { nobuiltin "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #3 = { nounwind }
attributes #4 = { builtin }

!llvm.module.flags = !{!0}
!llvm.ident = !{!1}

!0 = !{i32 1, !"wchar_size", i32 4}
!1 = !{!"clang version 8.0.0 (tags/RELEASE_800/final 361961) (llvm/tags/RELEASE_800/final 361957)"}
