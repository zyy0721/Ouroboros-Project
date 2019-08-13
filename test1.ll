; ModuleID = 'test1.cpp'
source_filename = "test1.cpp"
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
  %3 = load i32**, i32*** @globalB, align 8
  store i32* %2, i32** %3, align 8
  store i32** @globalA, i32*** %pptr.addr, align 8
  %4 = load i32**, i32*** @globalB, align 8
  %5 = load i32*, i32** %4, align 8
  store i32* %5, i32** @globalA, align 8
  %6 = load i32*, i32** @globalA, align 8
  ret i32* %6
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
  %s = alloca i32***, align 8
  %t = alloca i32****, align 8
  %ArrayTmp = alloca [10 x i32], align 16
  %PointerArray = alloca [10 x i32*], align 16
  %PointerDouleArray = alloca [10 x [10 x i32*]], align 16
  %pointerCase = alloca %struct.PointerCase, align 8
  %i = alloca i32, align 4
  %j = alloca i32, align 4
  %newP = alloca i32*, align 8
  %newP1 = alloca i32*, align 8
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
  %18 = load i32****, i32***** %t, align 8
  %19 = load i32***, i32**** %18, align 8
  %20 = load i32**, i32*** %19, align 8
  %21 = load i32*, i32** %20, align 8
  store i32* %21, i32** %p, align 8
  %22 = load i32***, i32**** %s, align 8
  %23 = load i32**, i32*** %22, align 8
  store i32** %23, i32*** %f, align 8
  %24 = load i32****, i32***** %t, align 8
  %25 = load i32***, i32**** %24, align 8
  %26 = load i32**, i32*** %25, align 8
  store i32** %26, i32*** %e, align 8
  br label %if.end

if.else:                                          ; preds = %entry
  %27 = load i32*, i32** %p, align 8
  %28 = load i32**, i32*** %q, align 8
  store i32* %27, i32** %28, align 8
  %29 = load i32*, i32** %h, align 8
  store i32* %29, i32** %g, align 8
  store i32* %b, i32** %p, align 8
  br label %if.end

if.end:                                           ; preds = %if.else, %if.then
  br label %while.cond

while.cond:                                       ; preds = %while.body, %if.end
  %30 = load i32, i32* %a, align 4
  %cmp3 = icmp ne i32 %30, 0
  br i1 %cmp3, label %while.body, label %while.end

while.body:                                       ; preds = %while.cond
  %31 = load i32**, i32*** %q, align 8
  %32 = load i32*, i32** %31, align 8
  store i32* %32, i32** %h, align 8
  %33 = load i32*, i32** %p, align 8
  store i32* %33, i32** %g, align 8
  br label %while.cond

while.end:                                        ; preds = %while.cond
  %34 = load i32, i32* %d, align 4
  %cmp4 = icmp sgt i32 %34, 0
  br i1 %cmp4, label %if.then5, label %if.else6

if.then5:                                         ; preds = %while.end
  %35 = load i32, i32* %a, align 4
  %36 = load i32*, i32** %g, align 8
  %37 = load i32**, i32*** %e, align 8
  %call = call i32* @_Z4fun1iPiPS_(i32 %35, i32* %36, i32** %37)
  store i32* %call, i32** %p, align 8
  br label %if.end8

if.else6:                                         ; preds = %while.end
  %38 = load i32, i32* %b, align 4
  %39 = load i32*, i32** %h, align 8
  %40 = load i32**, i32*** %q, align 8
  %41 = load i32*, i32** %p, align 8
  %call7 = call i32** @_Z4fun2iPiPS_S_(i32 %38, i32* %39, i32** %40, i32* %41)
  store i32** %call7, i32*** %e, align 8
  br label %if.end8

if.end8:                                          ; preds = %if.else6, %if.then5
  %42 = load i32, i32* %c, align 4
  %43 = load i32*, i32** %g, align 8
  call void @_Z4fun3iPi(i32 %42, i32* %43)
  %44 = load i32, i32* %c, align 4
  %cmp9 = icmp ne i32 %44, 1
  br i1 %cmp9, label %if.then10, label %if.else49

if.then10:                                        ; preds = %if.end8
  %45 = load i32*, i32** %g, align 8
  %a11 = getelementptr inbounds %struct.PointerCase, %struct.PointerCase* %pointerCase, i32 0, i32 0
  store i32* %45, i32** %a11, align 8
  %b12 = getelementptr inbounds %struct.PointerCase, %struct.PointerCase* %pointerCase, i32 0, i32 1
  %46 = load i32*, i32** %b12, align 8
  store i32* %46, i32** %h, align 8
  %47 = load i32*, i32** %p, align 8
  %d13 = getelementptr inbounds %struct.PointerCase, %struct.PointerCase* %pointerCase, i32 0, i32 2
  %48 = load i32**, i32*** %d13, align 8
  store i32* %47, i32** %48, align 8
  %e14 = getelementptr inbounds %struct.PointerCase, %struct.PointerCase* %pointerCase, i32 0, i32 3
  %49 = load i32**, i32*** %e14, align 8
  %50 = load i32*, i32** %49, align 8
  store i32* %50, i32** %h, align 8
  %51 = load i32, i32* %a, align 4
  %cmp15 = icmp sgt i32 %51, 0
  br i1 %cmp15, label %if.then16, label %if.else41

if.then16:                                        ; preds = %if.then10
  %arrayidx = getelementptr inbounds [10 x i32], [10 x i32]* %ArrayTmp, i64 0, i64 2
  store i32* %arrayidx, i32** %p, align 8
  store i32 0, i32* %i, align 4
  br label %for.cond

for.cond:                                         ; preds = %for.inc38, %if.then16
  %52 = load i32, i32* %i, align 4
  %cmp17 = icmp slt i32 %52, 10
  br i1 %cmp17, label %for.body, label %for.end40

for.body:                                         ; preds = %for.cond
  %53 = load i32, i32* %i, align 4
  %idxprom = sext i32 %53 to i64
  %arrayidx18 = getelementptr inbounds [10 x i32*], [10 x i32*]* %PointerArray, i64 0, i64 %idxprom
  %54 = load i32*, i32** %arrayidx18, align 8
  store i32* %54, i32** %g, align 8
  store i32 0, i32* %j, align 4
  br label %for.cond19

for.cond19:                                       ; preds = %for.inc, %for.body
  %55 = load i32, i32* %j, align 4
  %cmp20 = icmp slt i32 %55, 10
  br i1 %cmp20, label %for.body21, label %for.end

for.body21:                                       ; preds = %for.cond19
  %56 = load i32, i32* %i, align 4
  %idxprom22 = sext i32 %56 to i64
  %arrayidx23 = getelementptr inbounds [10 x [10 x i32*]], [10 x [10 x i32*]]* %PointerDouleArray, i64 0, i64 %idxprom22
  %57 = load i32, i32* %j, align 4
  %idxprom24 = sext i32 %57 to i64
  %arrayidx25 = getelementptr inbounds [10 x i32*], [10 x i32*]* %arrayidx23, i64 0, i64 %idxprom24
  %58 = load i32*, i32** %arrayidx25, align 8
  store i32* %58, i32** %p, align 8
  br label %for.inc

for.inc:                                          ; preds = %for.body21
  %59 = load i32, i32* %j, align 4
  %inc = add nsw i32 %59, 1
  store i32 %inc, i32* %j, align 4
  br label %for.cond19

for.end:                                          ; preds = %for.cond19
  %60 = load i32, i32* %i, align 4
  %idxprom26 = sext i32 %60 to i64
  %arrayidx27 = getelementptr inbounds [10 x [10 x i32*]], [10 x [10 x i32*]]* %PointerDouleArray, i64 0, i64 %idxprom26
  %arrayidx28 = getelementptr inbounds [10 x i32*], [10 x i32*]* %arrayidx27, i64 0, i64 1
  store i32* %a, i32** %arrayidx28, align 8
  %61 = load i32*, i32** %p, align 8
  %62 = load i32, i32* %i, align 4
  %idxprom29 = sext i32 %62 to i64
  %arrayidx30 = getelementptr inbounds [10 x [10 x i32*]], [10 x [10 x i32*]]* %PointerDouleArray, i64 0, i64 %idxprom29
  %arrayidx31 = getelementptr inbounds [10 x i32*], [10 x i32*]* %arrayidx30, i64 0, i64 2
  store i32* %61, i32** %arrayidx31, align 16
  %63 = load i32, i32* %i, align 4
  %idxprom32 = sext i32 %63 to i64
  %arrayidx33 = getelementptr inbounds [10 x [10 x i32*]], [10 x [10 x i32*]]* %PointerDouleArray, i64 0, i64 %idxprom32
  %arrayidx34 = getelementptr inbounds [10 x i32*], [10 x i32*]* %arrayidx33, i64 0, i64 3
  %64 = load i32*, i32** %arrayidx34, align 8
  %65 = load i32**, i32*** %e, align 8
  store i32* %64, i32** %65, align 8
  %66 = load i32**, i32*** %f, align 8
  %67 = load i32*, i32** %66, align 8
  %68 = load i32, i32* %i, align 4
  %idxprom35 = sext i32 %68 to i64
  %arrayidx36 = getelementptr inbounds [10 x [10 x i32*]], [10 x [10 x i32*]]* %PointerDouleArray, i64 0, i64 %idxprom35
  %arrayidx37 = getelementptr inbounds [10 x i32*], [10 x i32*]* %arrayidx36, i64 0, i64 3
  store i32* %67, i32** %arrayidx37, align 8
  br label %for.inc38

for.inc38:                                        ; preds = %for.end
  %69 = load i32, i32* %i, align 4
  %inc39 = add nsw i32 %69, 1
  store i32 %inc39, i32* %i, align 4
  br label %for.cond

for.end40:                                        ; preds = %for.cond
  br label %if.end48

if.else41:                                        ; preds = %if.then10
  %70 = load i32*, i32** %p, align 8
  %arrayidx42 = getelementptr inbounds [10 x i32*], [10 x i32*]* %PointerArray, i64 0, i64 2
  store i32* %70, i32** %arrayidx42, align 16
  %b43 = getelementptr inbounds %struct.PointerCase, %struct.PointerCase* %pointerCase, i32 0, i32 1
  %71 = load i32*, i32** %b43, align 8
  %arrayidx44 = getelementptr inbounds [10 x i32*], [10 x i32*]* %PointerArray, i64 0, i64 1
  store i32* %71, i32** %arrayidx44, align 8
  %arrayidx45 = getelementptr inbounds [10 x i32*], [10 x i32*]* %PointerArray, i64 0, i64 1
  store i32** %arrayidx45, i32*** %f, align 8
  %72 = load i32**, i32*** %f, align 8
  %73 = load i32*, i32** %72, align 8
  %arrayidx46 = getelementptr inbounds [10 x i32*], [10 x i32*]* %PointerArray, i64 0, i64 3
  store i32* %73, i32** %arrayidx46, align 8
  %arrayidx47 = getelementptr inbounds [10 x i32*], [10 x i32*]* %PointerArray, i64 0, i64 4
  %74 = load i32*, i32** %arrayidx47, align 16
  %75 = load i32**, i32*** %e, align 8
  store i32* %74, i32** %75, align 8
  br label %if.end48

if.end48:                                         ; preds = %if.else41, %for.end40
  br label %if.end54

if.else49:                                        ; preds = %if.end8
  %e50 = getelementptr inbounds %struct.PointerCase, %struct.PointerCase* %pointerCase, i32 0, i32 3
  store i32** %g, i32*** %e50, align 8
  %a51 = getelementptr inbounds %struct.PointerCase, %struct.PointerCase* %pointerCase, i32 0, i32 0
  store i32** %a51, i32*** %f, align 8
  %b52 = getelementptr inbounds %struct.PointerCase, %struct.PointerCase* %pointerCase, i32 0, i32 1
  %76 = load i32*, i32** %b52, align 8
  %77 = load i32**, i32*** %e, align 8
  store i32* %76, i32** %77, align 8
  %78 = load i32**, i32*** %f, align 8
  %79 = load i32*, i32** %78, align 8
  %a53 = getelementptr inbounds %struct.PointerCase, %struct.PointerCase* %pointerCase, i32 0, i32 0
  store i32* %79, i32** %a53, align 8
  br label %if.end54

if.end54:                                         ; preds = %if.else49, %if.end48
  br label %while.cond55

while.cond55:                                     ; preds = %if.end64, %if.end54
  %80 = load i32, i32* %a, align 4
  %cmp56 = icmp sgt i32 %80, 0
  br i1 %cmp56, label %while.body57, label %while.end65

while.body57:                                     ; preds = %while.cond55
  %arrayidx58 = getelementptr inbounds [10 x i32*], [10 x i32*]* %PointerArray, i64 0, i64 0
  %81 = load i32*, i32** %arrayidx58, align 16
  store i32* %81, i32** %g, align 8
  %arrayidx59 = getelementptr inbounds [10 x i32*], [10 x i32*]* %PointerArray, i64 0, i64 1
  %82 = load i32*, i32** %arrayidx59, align 8
  %a60 = getelementptr inbounds %struct.PointerCase, %struct.PointerCase* %pointerCase, i32 0, i32 0
  store i32* %82, i32** %a60, align 8
  %83 = load i32, i32* %a, align 4
  %dec = add nsw i32 %83, -1
  store i32 %dec, i32* %a, align 4
  %84 = load i32, i32* %b, align 4
  %cmp61 = icmp sgt i32 %84, 0
  br i1 %cmp61, label %if.then62, label %if.else63

if.then62:                                        ; preds = %while.body57
  %85 = load i32*, i32** %g, align 8
  %86 = load i32**, i32*** %e, align 8
  store i32* %85, i32** %86, align 8
  %87 = load i32**, i32*** %e, align 8
  %88 = load i32*, i32** %87, align 8
  store i32* %88, i32** %h, align 8
  store i32** %h, i32*** %q, align 8
  %89 = load i32*, i32** %p, align 8
  %90 = load i32**, i32*** %f, align 8
  store i32* %89, i32** %90, align 8
  br label %if.end64

if.else63:                                        ; preds = %while.body57
  %91 = load i32*, i32** %p, align 8
  %92 = load i32**, i32*** %q, align 8
  store i32* %91, i32** %92, align 8
  %93 = load i32*, i32** %h, align 8
  store i32* %93, i32** %g, align 8
  store i32* %b, i32** %p, align 8
  br label %if.end64

if.end64:                                         ; preds = %if.else63, %if.then62
  br label %while.cond55

while.end65:                                      ; preds = %while.cond55
  %call66 = call noalias i8* @malloc(i64 40) #4
  %94 = bitcast i8* %call66 to i32*
  store i32* %94, i32** %newP, align 8
  %call67 = call i8* @_Znam(i64 40) #5
  %95 = bitcast i8* %call67 to i32*
  store i32* %95, i32** %newP1, align 8
  ret i32 0
}

; Function Attrs: nounwind
declare dso_local noalias i8* @malloc(i64) #2

; Function Attrs: nobuiltin
declare dso_local noalias i8* @_Znam(i64) #3

attributes #0 = { noinline nounwind optnone uwtable "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "min-legal-vector-width"="0" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #1 = { noinline norecurse optnone uwtable "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "min-legal-vector-width"="0" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #2 = { nounwind "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #3 = { nobuiltin "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #4 = { nounwind }
attributes #5 = { builtin }

!llvm.module.flags = !{!0}
!llvm.ident = !{!1}

!0 = !{i32 1, !"wchar_size", i32 4}
!1 = !{!"clang version 9.0.0 "}
