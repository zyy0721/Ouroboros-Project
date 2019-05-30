; ModuleID = 'testCase6Without.cpp'
source_filename = "testCase6Without.cpp"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-unknown-linux-gnu"

%struct.PointerCase = type { i32*, i32*, i32**, i32**, i32 }

@globalA = dso_local global i32* null, align 8
@globalB = dso_local global i32** null, align 8

; Function Attrs: noinline nounwind optnone uwtable
define dso_local i32* @_Z4fun1iPiPS_(i32 %n, i32* %ptr, i32** %pptr) #0 {
entry:
  %n.addr = alloca i32, align 4
  %ptr.addr = alloca i32*, align 8
  %pptr.addr = alloca i32**, align 8
  store i32 %n, i32* %n.addr, align 4
  store i32* %ptr, i32** %ptr.addr, align 8
  store i32** %pptr, i32*** %pptr.addr, align 8
  %0 = load i32*, i32** %ptr.addr, align 8
  store i32* %0, i32** @globalA, align 8
  %1 = load i32**, i32*** @globalB, align 8
  store i32** %1, i32*** %pptr.addr, align 8
  %2 = load i32*, i32** %ptr.addr, align 8
  ret i32* %2
}

; Function Attrs: noinline nounwind optnone uwtable
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
  store i32* %n.addr, i32** @globalA, align 8
  %1 = load i32*, i32** %ptr.addr, align 8
  %2 = load i32**, i32*** %pptr.addr, align 8
  store i32* %1, i32** %2, align 8
  %3 = load i32**, i32*** %pptr.addr, align 8
  %4 = load i32*, i32** %3, align 8
  store i32* %4, i32** %ptr1.addr, align 8
  %5 = load i32*, i32** %ptr1.addr, align 8
  store i32* %5, i32** %ptr.addr, align 8
  %6 = load i32**, i32*** %pptr.addr, align 8
  store i32** %6, i32*** %retval, align 8
  br label %return

if.else:                                          ; preds = %entry
  store i32** %ptr1.addr, i32*** @globalB, align 8
  store i32* %n.addr, i32** %ptr.addr, align 8
  %7 = load i32*, i32** %ptr.addr, align 8
  %8 = load i32**, i32*** @globalB, align 8
  store i32* %7, i32** %8, align 8
  %9 = load i32**, i32*** %pptr.addr, align 8
  %10 = load i32*, i32** %9, align 8
  store i32* %10, i32** %ptr1.addr, align 8
  %11 = load i32**, i32*** @globalB, align 8
  store i32** %11, i32*** %retval, align 8
  br label %return

return:                                           ; preds = %if.else, %if.then
  %12 = load i32**, i32*** %retval, align 8
  ret i32** %12
}

; Function Attrs: noinline nounwind optnone uwtable
define dso_local void @_Z4fun3iPi(i32 %n, i32* %ptr) #0 {
entry:
  %n.addr = alloca i32, align 4
  %ptr.addr = alloca i32*, align 8
  store i32 %n, i32* %n.addr, align 4
  store i32* %ptr, i32** %ptr.addr, align 8
  store i32* %n.addr, i32** %ptr.addr, align 8
  ret void
}

; Function Attrs: noinline norecurse optnone uwtable
define dso_local i32 @main() #1 {
entry:
  %retval = alloca i32, align 4
  %a = alloca i32, align 4
  %b = alloca i32, align 4
  %c = alloca i32, align 4
  %d = alloca i32, align 4
  %e = alloca i32**, align 8
  %f = alloca i32**, align 8
  %q = alloca i32**, align 8
  %g = alloca i32*, align 8
  %h = alloca i32*, align 8
  %p = alloca i32*, align 8
  %ArrayTmp = alloca [10 x i32], align 16
  %PointerArray = alloca [10 x i32*], align 16
  %pointerCase = alloca %struct.PointerCase, align 8
  %i = alloca i32, align 4
  %j = alloca i32, align 4
  %newP = alloca i32*, align 8
  %newPP = alloca i32*, align 8
  store i32 0, i32* %retval, align 4
  store i32 1, i32* %a, align 4
  store i32 2, i32* %b, align 4
  store i32 3, i32* %c, align 4
  %0 = load i32, i32* %a, align 4
  %1 = load i32, i32* %b, align 4
  %add = add nsw i32 %0, %1
  %2 = load i32, i32* %c, align 4
  %add1 = add nsw i32 %add, %2
  store i32 %add1, i32* %d, align 4
  %3 = load i32, i32* %a, align 4
  %4 = load i32, i32* %b, align 4
  %sub = sub nsw i32 %3, %4
  store i32 %sub, i32* %d, align 4
  %5 = load i32, i32* %d, align 4
  %6 = load i32, i32* %a, align 4
  %mul = mul nsw i32 %5, %6
  store i32 %mul, i32* %c, align 4
  %7 = load i32, i32* %c, align 4
  %add2 = add nsw i32 %7, 1
  store i32 %add2, i32* %b, align 4
  %8 = load i32**, i32*** %f, align 8
  store i32** %8, i32*** %e, align 8
  %9 = load i32**, i32*** %e, align 8
  %10 = load i32*, i32** %9, align 8
  store i32* %10, i32** @globalA, align 8
  %11 = load i32, i32* %b, align 4
  %cmp = icmp sgt i32 %11, 0
  br i1 %cmp, label %if.then, label %if.else

if.then:                                          ; preds = %entry
  %12 = load i32*, i32** %g, align 8
  %13 = load i32**, i32*** %e, align 8
  store i32* %12, i32** %13, align 8
  %14 = load i32**, i32*** %e, align 8
  %15 = load i32*, i32** %14, align 8
  store i32* %15, i32** %h, align 8
  store i32** %h, i32*** %q, align 8
  %16 = load i32*, i32** %p, align 8
  %17 = load i32**, i32*** %f, align 8
  store i32* %16, i32** %17, align 8
  br label %if.end

if.else:                                          ; preds = %entry
  %18 = load i32*, i32** %p, align 8
  %19 = load i32**, i32*** %q, align 8
  store i32* %18, i32** %19, align 8
  %20 = load i32*, i32** %h, align 8
  store i32* %20, i32** %g, align 8
  store i32* %b, i32** %p, align 8
  br label %if.end

if.end:                                           ; preds = %if.else, %if.then
  br label %while.cond

while.cond:                                       ; preds = %while.body, %if.end
  %21 = load i32, i32* %a, align 4
  %cmp3 = icmp ne i32 %21, 0
  br i1 %cmp3, label %while.body, label %while.end

while.body:                                       ; preds = %while.cond
  %22 = load i32**, i32*** %q, align 8
  %23 = load i32*, i32** %22, align 8
  store i32* %23, i32** %h, align 8
  %24 = load i32*, i32** %p, align 8
  store i32* %24, i32** %g, align 8
  br label %while.cond

while.end:                                        ; preds = %while.cond
  %25 = load i32, i32* %c, align 4
  switch i32 %25, label %sw.default [
    i32 1, label %sw.bb
    i32 2, label %sw.bb5
  ]

sw.bb:                                            ; preds = %while.end
  %26 = load i32, i32* %a, align 4
  %27 = load i32, i32* %c, align 4
  %add4 = add nsw i32 %26, %27
  store i32 %add4, i32* %d, align 4
  store i32* %d, i32** %p, align 8
  br label %sw.epilog

sw.bb5:                                           ; preds = %while.end
  %28 = load i32, i32* %d, align 4
  %29 = load i32, i32* %c, align 4
  %sub6 = sub nsw i32 %29, 1
  %mul7 = mul nsw i32 %sub6, 2
  %add8 = add nsw i32 %28, %mul7
  store i32 %add8, i32* %a, align 4
  store i32* %a, i32** %p, align 8
  br label %sw.epilog

sw.default:                                       ; preds = %while.end
  br label %sw.epilog

sw.epilog:                                        ; preds = %sw.default, %sw.bb5, %sw.bb
  %30 = load i32, i32* %d, align 4
  %cmp9 = icmp sgt i32 %30, 0
  br i1 %cmp9, label %if.then10, label %if.else11

if.then10:                                        ; preds = %sw.epilog
  %31 = load i32, i32* %a, align 4
  %32 = load i32*, i32** %g, align 8
  %33 = load i32**, i32*** %e, align 8
  %call = call i32* @_Z4fun1iPiPS_(i32 %31, i32* %32, i32** %33)
  store i32* %call, i32** %p, align 8
  br label %if.end13

if.else11:                                        ; preds = %sw.epilog
  %34 = load i32, i32* %b, align 4
  %35 = load i32*, i32** %h, align 8
  %36 = load i32**, i32*** %q, align 8
  %37 = load i32*, i32** %p, align 8
  %call12 = call i32** @_Z4fun2iPiPS_S_(i32 %34, i32* %35, i32** %36, i32* %37)
  store i32** %call12, i32*** %e, align 8
  br label %if.end13

if.end13:                                         ; preds = %if.else11, %if.then10
  %38 = load i32, i32* %c, align 4
  %39 = load i32*, i32** %g, align 8
  call void @_Z4fun3iPi(i32 %38, i32* %39)
  %40 = load i32, i32* %c, align 4
  %cmp14 = icmp ne i32 %40, 1
  br i1 %cmp14, label %if.then15, label %if.else43

if.then15:                                        ; preds = %if.end13
  %41 = load i32*, i32** %g, align 8
  %a16 = getelementptr inbounds %struct.PointerCase, %struct.PointerCase* %pointerCase, i32 0, i32 0
  store i32* %41, i32** %a16, align 8
  %b17 = getelementptr inbounds %struct.PointerCase, %struct.PointerCase* %pointerCase, i32 0, i32 1
  %42 = load i32*, i32** %b17, align 8
  store i32* %42, i32** %h, align 8
  %43 = load i32*, i32** %p, align 8
  %d18 = getelementptr inbounds %struct.PointerCase, %struct.PointerCase* %pointerCase, i32 0, i32 2
  %44 = load i32**, i32*** %d18, align 8
  store i32* %43, i32** %44, align 8
  %e19 = getelementptr inbounds %struct.PointerCase, %struct.PointerCase* %pointerCase, i32 0, i32 3
  %45 = load i32**, i32*** %e19, align 8
  %46 = load i32*, i32** %45, align 8
  store i32* %46, i32** %h, align 8
  %47 = load i32, i32* %a, align 4
  %cmp20 = icmp sgt i32 %47, 0
  br i1 %cmp20, label %if.then21, label %if.else29

if.then21:                                        ; preds = %if.then15
  %arrayidx = getelementptr inbounds [10 x i32], [10 x i32]* %ArrayTmp, i64 0, i64 2
  store i32* %arrayidx, i32** %p, align 8
  store i32 0, i32* %i, align 4
  br label %for.cond

for.cond:                                         ; preds = %for.inc26, %if.then21
  %48 = load i32, i32* %i, align 4
  %cmp22 = icmp slt i32 %48, 10
  br i1 %cmp22, label %for.body, label %for.end28

for.body:                                         ; preds = %for.cond
  store i32 0, i32* %j, align 4
  br label %for.cond23

for.cond23:                                       ; preds = %for.inc, %for.body
  %49 = load i32, i32* %j, align 4
  %cmp24 = icmp slt i32 %49, 10
  br i1 %cmp24, label %for.body25, label %for.end

for.body25:                                       ; preds = %for.cond23
  %50 = load i32, i32* %a, align 4
  %51 = load i32*, i32** %p, align 8
  call void @_Z4fun3iPi(i32 %50, i32* %51)
  br label %for.inc

for.inc:                                          ; preds = %for.body25
  %52 = load i32, i32* %j, align 4
  %inc = add nsw i32 %52, 1
  store i32 %inc, i32* %j, align 4
  br label %for.cond23

for.end:                                          ; preds = %for.cond23
  br label %for.inc26

for.inc26:                                        ; preds = %for.end
  %53 = load i32, i32* %i, align 4
  %inc27 = add nsw i32 %53, 1
  store i32 %inc27, i32* %i, align 4
  br label %for.cond

for.end28:                                        ; preds = %for.cond
  br label %if.end42

if.else29:                                        ; preds = %if.then15
  %54 = load i32*, i32** %p, align 8
  %arrayidx30 = getelementptr inbounds [10 x i32*], [10 x i32*]* %PointerArray, i64 0, i64 2
  store i32* %54, i32** %arrayidx30, align 16
  %b31 = getelementptr inbounds %struct.PointerCase, %struct.PointerCase* %pointerCase, i32 0, i32 1
  %55 = load i32*, i32** %b31, align 8
  %arrayidx32 = getelementptr inbounds [10 x i32*], [10 x i32*]* %PointerArray, i64 0, i64 1
  store i32* %55, i32** %arrayidx32, align 8
  %arrayidx33 = getelementptr inbounds [10 x i32*], [10 x i32*]* %PointerArray, i64 0, i64 5
  %d34 = getelementptr inbounds %struct.PointerCase, %struct.PointerCase* %pointerCase, i32 0, i32 2
  store i32** %arrayidx33, i32*** %d34, align 8
  %arrayidx35 = getelementptr inbounds [10 x i32*], [10 x i32*]* %PointerArray, i64 0, i64 6
  %56 = load i32*, i32** %arrayidx35, align 16
  %e36 = getelementptr inbounds %struct.PointerCase, %struct.PointerCase* %pointerCase, i32 0, i32 3
  %57 = load i32**, i32*** %e36, align 8
  store i32* %56, i32** %57, align 8
  %e37 = getelementptr inbounds %struct.PointerCase, %struct.PointerCase* %pointerCase, i32 0, i32 3
  %58 = load i32**, i32*** %e37, align 8
  %59 = load i32*, i32** %58, align 8
  %arrayidx38 = getelementptr inbounds [10 x i32*], [10 x i32*]* %PointerArray, i64 0, i64 7
  store i32* %59, i32** %arrayidx38, align 8
  %arrayidx39 = getelementptr inbounds [10 x i32*], [10 x i32*]* %PointerArray, i64 0, i64 1
  store i32** %arrayidx39, i32*** %f, align 8
  %60 = load i32**, i32*** %f, align 8
  %61 = load i32*, i32** %60, align 8
  %arrayidx40 = getelementptr inbounds [10 x i32*], [10 x i32*]* %PointerArray, i64 0, i64 3
  store i32* %61, i32** %arrayidx40, align 8
  %arrayidx41 = getelementptr inbounds [10 x i32*], [10 x i32*]* %PointerArray, i64 0, i64 4
  %62 = load i32*, i32** %arrayidx41, align 16
  %63 = load i32**, i32*** %e, align 8
  store i32* %62, i32** %63, align 8
  br label %if.end42

if.end42:                                         ; preds = %if.else29, %for.end28
  br label %if.end48

if.else43:                                        ; preds = %if.end13
  %e44 = getelementptr inbounds %struct.PointerCase, %struct.PointerCase* %pointerCase, i32 0, i32 3
  store i32** %g, i32*** %e44, align 8
  %a45 = getelementptr inbounds %struct.PointerCase, %struct.PointerCase* %pointerCase, i32 0, i32 0
  store i32** %a45, i32*** %f, align 8
  %b46 = getelementptr inbounds %struct.PointerCase, %struct.PointerCase* %pointerCase, i32 0, i32 1
  %64 = load i32*, i32** %b46, align 8
  %65 = load i32**, i32*** %e, align 8
  store i32* %64, i32** %65, align 8
  %66 = load i32**, i32*** %f, align 8
  %67 = load i32*, i32** %66, align 8
  %a47 = getelementptr inbounds %struct.PointerCase, %struct.PointerCase* %pointerCase, i32 0, i32 0
  store i32* %67, i32** %a47, align 8
  br label %if.end48

if.end48:                                         ; preds = %if.else43, %if.end42
  br label %while.cond49

while.cond49:                                     ; preds = %if.end58, %if.end48
  %68 = load i32, i32* %a, align 4
  %cmp50 = icmp sgt i32 %68, 0
  br i1 %cmp50, label %while.body51, label %while.end59

while.body51:                                     ; preds = %while.cond49
  %arrayidx52 = getelementptr inbounds [10 x i32*], [10 x i32*]* %PointerArray, i64 0, i64 0
  %69 = load i32*, i32** %arrayidx52, align 16
  store i32* %69, i32** %g, align 8
  %arrayidx53 = getelementptr inbounds [10 x i32*], [10 x i32*]* %PointerArray, i64 0, i64 1
  %70 = load i32*, i32** %arrayidx53, align 8
  %a54 = getelementptr inbounds %struct.PointerCase, %struct.PointerCase* %pointerCase, i32 0, i32 0
  store i32* %70, i32** %a54, align 8
  %71 = load i32, i32* %a, align 4
  %dec = add nsw i32 %71, -1
  store i32 %dec, i32* %a, align 4
  %72 = load i32, i32* %b, align 4
  %cmp55 = icmp sgt i32 %72, 0
  br i1 %cmp55, label %if.then56, label %if.else57

if.then56:                                        ; preds = %while.body51
  %73 = load i32*, i32** %g, align 8
  %74 = load i32**, i32*** %e, align 8
  store i32* %73, i32** %74, align 8
  %75 = load i32**, i32*** %e, align 8
  %76 = load i32*, i32** %75, align 8
  store i32* %76, i32** %h, align 8
  store i32** %h, i32*** %q, align 8
  %77 = load i32*, i32** %p, align 8
  %78 = load i32**, i32*** %f, align 8
  store i32* %77, i32** %78, align 8
  br label %if.end58

if.else57:                                        ; preds = %while.body51
  %79 = load i32*, i32** %p, align 8
  %80 = load i32**, i32*** %q, align 8
  store i32* %79, i32** %80, align 8
  %81 = load i32*, i32** %h, align 8
  store i32* %81, i32** %g, align 8
  store i32* %b, i32** %p, align 8
  br label %if.end58

if.end58:                                         ; preds = %if.else57, %if.then56
  br label %while.cond49

while.end59:                                      ; preds = %while.cond49
  %call60 = call noalias i8* @malloc(i64 40) #4
  %82 = bitcast i8* %call60 to i32*
  store i32* %82, i32** %newP, align 8
  %call61 = call i8* @_Znam(i64 40) #5
  %83 = bitcast i8* %call61 to i32*
  store i32* %83, i32** %newPP, align 8
  ret i32 0
}

; Function Attrs: nounwind
declare dso_local noalias i8* @malloc(i64) #2

; Function Attrs: nobuiltin
declare dso_local noalias i8* @_Znam(i64) #3

attributes #0 = { noinline nounwind optnone uwtable "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "min-legal-vector-width"="0" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #1 = { noinline norecurse optnone uwtable "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "min-legal-vector-width"="0" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #2 = { nounwind "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #3 = { nobuiltin "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #4 = { nounwind }
attributes #5 = { builtin }

!llvm.module.flags = !{!0}
!llvm.ident = !{!1}

!0 = !{i32 1, !"wchar_size", i32 4}
!1 = !{!"clang version 8.0.0 (tags/RELEASE_800/final 361961) (llvm/tags/RELEASE_800/final 361957)"}
