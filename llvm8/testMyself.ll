; ModuleID = 'testMyself.cpp'
source_filename = "testMyself.cpp"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-unknown-linux-gnu"

%struct.PointerCase = type { i32*, i32*, i32**, i32**, i32 }

@globalC = dso_local global i32* null, align 8
@globalD = dso_local global i32** null, align 8

; Function Attrs: noinline optnone uwtable
define dso_local i32* @_Z4fun1iPiPS_(i32 %n, i32* %ptr, i32** %pptr) #0 {
entry:
  %n.addr = alloca i32, align 4
  %ptr.addr = alloca i32*, align 8
  %pptr.addr = alloca i32**, align 8
  store i32 %n, i32* %n.addr, align 4
  store i32* %ptr, i32** %ptr.addr, align 8
  store i32** %pptr, i32*** %pptr.addr, align 8
  %0 = load i32, i32* %n.addr, align 4
  %1 = load i32*, i32** %ptr.addr, align 8
  %2 = load i32**, i32*** %pptr.addr, align 8
  %call = call i32* @_Z4fun7iPiPS_(i32 %0, i32* %1, i32** %2)
  store i32* %call, i32** %ptr.addr, align 8
  %3 = load i32*, i32** %ptr.addr, align 8
  store i32* %3, i32** @globalC, align 8
  %4 = load i32**, i32*** @globalD, align 8
  store i32** %4, i32*** %pptr.addr, align 8
  %5 = load i32*, i32** %ptr.addr, align 8
  ret i32* %5
}

; Function Attrs: noinline optnone uwtable
define dso_local i32* @_Z4fun7iPiPS_(i32 %n, i32* %ptr, i32** %pptr) #0 {
entry:
  %n.addr = alloca i32, align 4
  %ptr.addr = alloca i32*, align 8
  %pptr.addr = alloca i32**, align 8
  store i32 %n, i32* %n.addr, align 4
  store i32* %ptr, i32** %ptr.addr, align 8
  store i32** %pptr, i32*** %pptr.addr, align 8
  %0 = load i32, i32* %n.addr, align 4
  %1 = load i32*, i32** %ptr.addr, align 8
  %2 = load i32**, i32*** %pptr.addr, align 8
  %call = call i32* @_Z4fun5iPiPS_(i32 %0, i32* %1, i32** %2)
  store i32* %call, i32** %ptr.addr, align 8
  %3 = load i32*, i32** %ptr.addr, align 8
  ret i32* %3
}

; Function Attrs: noinline nounwind optnone uwtable
define dso_local i32** @_Z4fun2iPiPS_S_(i32 %n, i32* %ptr, i32** %pptr, i32* %ptr1) #1 {
entry:
  %retval = alloca i32**, align 8
  %n.addr = alloca i32, align 4
  %ptr.addr = alloca i32*, align 8
  %pptr.addr = alloca i32**, align 8
  %ptr1.addr = alloca i32*, align 8
  %p2 = alloca i32*, align 8
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
  %6 = load i32**, i32*** %pptr.addr, align 8
  store i32** %6, i32*** %retval, align 8
  br label %return

if.else:                                          ; preds = %entry
  store i32** %ptr1.addr, i32*** @globalD, align 8
  store i32* %n.addr, i32** %ptr.addr, align 8
  %7 = load i32*, i32** %ptr.addr, align 8
  %8 = load i32**, i32*** @globalD, align 8
  store i32* %7, i32** %8, align 8
  %9 = load i32**, i32*** %pptr.addr, align 8
  %10 = load i32*, i32** %9, align 8
  store i32* %10, i32** %ptr1.addr, align 8
  %11 = load i32**, i32*** @globalD, align 8
  store i32** %11, i32*** %retval, align 8
  br label %return

return:                                           ; preds = %if.else, %if.then
  %12 = load i32**, i32*** %retval, align 8
  ret i32** %12
}

; Function Attrs: noinline optnone uwtable
define dso_local i32* @_Z4fun3iPi(i32 %n, i32* %ptr) #0 {
entry:
  %n.addr = alloca i32, align 4
  %ptr.addr = alloca i32*, align 8
  store i32 %n, i32* %n.addr, align 4
  store i32* %ptr, i32** %ptr.addr, align 8
  store i32* %n.addr, i32** %ptr.addr, align 8
  %0 = load i32, i32* %n.addr, align 4
  %1 = load i32*, i32** %ptr.addr, align 8
  %call = call i32* @_Z4fun4iPi(i32 %0, i32* %1)
  %2 = load i32*, i32** %ptr.addr, align 8
  ret i32* %2
}

; Function Attrs: noinline optnone uwtable
define dso_local i32* @_Z4fun4iPi(i32 %n, i32* %ptr) #0 {
entry:
  %n.addr = alloca i32, align 4
  %ptr.addr = alloca i32*, align 8
  store i32 %n, i32* %n.addr, align 4
  store i32* %ptr, i32** %ptr.addr, align 8
  %0 = load i32, i32* %n.addr, align 4
  %1 = load i32*, i32** %ptr.addr, align 8
  %call = call i32* @_Z4fun3iPi(i32 %0, i32* %1)
  %2 = load i32*, i32** %ptr.addr, align 8
  ret i32* %2
}

; Function Attrs: noinline optnone uwtable
define dso_local i32* @_Z4fun5iPiPS_(i32 %n, i32* %ptr, i32** %pptr) #0 {
entry:
  %n.addr = alloca i32, align 4
  %ptr.addr = alloca i32*, align 8
  %pptr.addr = alloca i32**, align 8
  store i32 %n, i32* %n.addr, align 4
  store i32* %ptr, i32** %ptr.addr, align 8
  store i32** %pptr, i32*** %pptr.addr, align 8
  %0 = load i32, i32* %n.addr, align 4
  %1 = load i32*, i32** %ptr.addr, align 8
  %2 = load i32**, i32*** %pptr.addr, align 8
  %call = call i32* @_Z4fun6iPiPS_(i32 %0, i32* %1, i32** %2)
  store i32* %call, i32** %ptr.addr, align 8
  %3 = load i32*, i32** %ptr.addr, align 8
  ret i32* %3
}

; Function Attrs: noinline optnone uwtable
define dso_local i32* @_Z4fun6iPiPS_(i32 %n, i32* %ptr, i32** %pptr) #0 {
entry:
  %n.addr = alloca i32, align 4
  %ptr.addr = alloca i32*, align 8
  %pptr.addr = alloca i32**, align 8
  store i32 %n, i32* %n.addr, align 4
  store i32* %ptr, i32** %ptr.addr, align 8
  store i32** %pptr, i32*** %pptr.addr, align 8
  %0 = load i32, i32* %n.addr, align 4
  %1 = load i32*, i32** %ptr.addr, align 8
  %2 = load i32**, i32*** %pptr.addr, align 8
  %call = call i32* @_Z4fun1iPiPS_(i32 %0, i32* %1, i32** %2)
  store i32* %call, i32** %ptr.addr, align 8
  %3 = load i32*, i32** %ptr.addr, align 8
  ret i32* %3
}

; Function Attrs: noinline norecurse optnone uwtable
define dso_local i32 @main() #2 {
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
  store i32* %10, i32** @globalC, align 8
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
  %call14 = call i32* @_Z4fun3iPi(i32 %38, i32* %39)
  %40 = load i32, i32* %c, align 4
  %41 = load i32*, i32** %g, align 8
  %call15 = call i32* @_Z4fun4iPi(i32 %40, i32* %41)
  %42 = load i32, i32* %c, align 4
  %cmp16 = icmp ne i32 %42, 1
  br i1 %cmp16, label %if.then17, label %if.else46

if.then17:                                        ; preds = %if.end13
  %43 = load i32*, i32** %g, align 8
  %a18 = getelementptr inbounds %struct.PointerCase, %struct.PointerCase* %pointerCase, i32 0, i32 0
  store i32* %43, i32** %a18, align 8
  %b19 = getelementptr inbounds %struct.PointerCase, %struct.PointerCase* %pointerCase, i32 0, i32 1
  %44 = load i32*, i32** %b19, align 8
  store i32* %44, i32** %h, align 8
  %45 = load i32*, i32** %p, align 8
  %d20 = getelementptr inbounds %struct.PointerCase, %struct.PointerCase* %pointerCase, i32 0, i32 2
  %46 = load i32**, i32*** %d20, align 8
  store i32* %45, i32** %46, align 8
  %e21 = getelementptr inbounds %struct.PointerCase, %struct.PointerCase* %pointerCase, i32 0, i32 3
  %47 = load i32**, i32*** %e21, align 8
  %48 = load i32*, i32** %47, align 8
  store i32* %48, i32** %h, align 8
  %49 = load i32, i32* %a, align 4
  %cmp22 = icmp sgt i32 %49, 0
  br i1 %cmp22, label %if.then23, label %if.else32

if.then23:                                        ; preds = %if.then17
  %arrayidx = getelementptr inbounds [10 x i32], [10 x i32]* %ArrayTmp, i64 0, i64 2
  store i32* %arrayidx, i32** %p, align 8
  store i32 0, i32* %i, align 4
  br label %for.cond

for.cond:                                         ; preds = %for.inc29, %if.then23
  %50 = load i32, i32* %i, align 4
  %cmp24 = icmp slt i32 %50, 10
  br i1 %cmp24, label %for.body, label %for.end31

for.body:                                         ; preds = %for.cond
  store i32 0, i32* %j, align 4
  br label %for.cond25

for.cond25:                                       ; preds = %for.inc, %for.body
  %51 = load i32, i32* %j, align 4
  %cmp26 = icmp slt i32 %51, 10
  br i1 %cmp26, label %for.body27, label %for.end

for.body27:                                       ; preds = %for.cond25
  %52 = load i32, i32* %a, align 4
  %53 = load i32*, i32** %p, align 8
  %call28 = call i32* @_Z4fun3iPi(i32 %52, i32* %53)
  br label %for.inc

for.inc:                                          ; preds = %for.body27
  %54 = load i32, i32* %j, align 4
  %inc = add nsw i32 %54, 1
  store i32 %inc, i32* %j, align 4
  br label %for.cond25

for.end:                                          ; preds = %for.cond25
  br label %for.inc29

for.inc29:                                        ; preds = %for.end
  %55 = load i32, i32* %i, align 4
  %inc30 = add nsw i32 %55, 1
  store i32 %inc30, i32* %i, align 4
  br label %for.cond

for.end31:                                        ; preds = %for.cond
  br label %if.end45

if.else32:                                        ; preds = %if.then17
  %56 = load i32*, i32** %p, align 8
  %arrayidx33 = getelementptr inbounds [10 x i32*], [10 x i32*]* %PointerArray, i64 0, i64 2
  store i32* %56, i32** %arrayidx33, align 16
  %b34 = getelementptr inbounds %struct.PointerCase, %struct.PointerCase* %pointerCase, i32 0, i32 1
  %57 = load i32*, i32** %b34, align 8
  %arrayidx35 = getelementptr inbounds [10 x i32*], [10 x i32*]* %PointerArray, i64 0, i64 1
  store i32* %57, i32** %arrayidx35, align 8
  %arrayidx36 = getelementptr inbounds [10 x i32*], [10 x i32*]* %PointerArray, i64 0, i64 5
  %d37 = getelementptr inbounds %struct.PointerCase, %struct.PointerCase* %pointerCase, i32 0, i32 2
  store i32** %arrayidx36, i32*** %d37, align 8
  %arrayidx38 = getelementptr inbounds [10 x i32*], [10 x i32*]* %PointerArray, i64 0, i64 6
  %58 = load i32*, i32** %arrayidx38, align 16
  %e39 = getelementptr inbounds %struct.PointerCase, %struct.PointerCase* %pointerCase, i32 0, i32 3
  %59 = load i32**, i32*** %e39, align 8
  store i32* %58, i32** %59, align 8
  %e40 = getelementptr inbounds %struct.PointerCase, %struct.PointerCase* %pointerCase, i32 0, i32 3
  %60 = load i32**, i32*** %e40, align 8
  %61 = load i32*, i32** %60, align 8
  %arrayidx41 = getelementptr inbounds [10 x i32*], [10 x i32*]* %PointerArray, i64 0, i64 7
  store i32* %61, i32** %arrayidx41, align 8
  %arrayidx42 = getelementptr inbounds [10 x i32*], [10 x i32*]* %PointerArray, i64 0, i64 1
  store i32** %arrayidx42, i32*** %f, align 8
  %62 = load i32**, i32*** %f, align 8
  %63 = load i32*, i32** %62, align 8
  %arrayidx43 = getelementptr inbounds [10 x i32*], [10 x i32*]* %PointerArray, i64 0, i64 3
  store i32* %63, i32** %arrayidx43, align 8
  %arrayidx44 = getelementptr inbounds [10 x i32*], [10 x i32*]* %PointerArray, i64 0, i64 4
  %64 = load i32*, i32** %arrayidx44, align 16
  %65 = load i32**, i32*** %e, align 8
  store i32* %64, i32** %65, align 8
  br label %if.end45

if.end45:                                         ; preds = %if.else32, %for.end31
  br label %if.end51

if.else46:                                        ; preds = %if.end13
  %e47 = getelementptr inbounds %struct.PointerCase, %struct.PointerCase* %pointerCase, i32 0, i32 3
  store i32** %g, i32*** %e47, align 8
  %a48 = getelementptr inbounds %struct.PointerCase, %struct.PointerCase* %pointerCase, i32 0, i32 0
  store i32** %a48, i32*** %f, align 8
  %b49 = getelementptr inbounds %struct.PointerCase, %struct.PointerCase* %pointerCase, i32 0, i32 1
  %66 = load i32*, i32** %b49, align 8
  %67 = load i32**, i32*** %e, align 8
  store i32* %66, i32** %67, align 8
  %68 = load i32**, i32*** %f, align 8
  %69 = load i32*, i32** %68, align 8
  %a50 = getelementptr inbounds %struct.PointerCase, %struct.PointerCase* %pointerCase, i32 0, i32 0
  store i32* %69, i32** %a50, align 8
  br label %if.end51

if.end51:                                         ; preds = %if.else46, %if.end45
  br label %while.cond52

while.cond52:                                     ; preds = %if.end61, %if.end51
  %70 = load i32, i32* %a, align 4
  %cmp53 = icmp sgt i32 %70, 0
  br i1 %cmp53, label %while.body54, label %while.end62

while.body54:                                     ; preds = %while.cond52
  %arrayidx55 = getelementptr inbounds [10 x i32*], [10 x i32*]* %PointerArray, i64 0, i64 0
  %71 = load i32*, i32** %arrayidx55, align 16
  store i32* %71, i32** %g, align 8
  %arrayidx56 = getelementptr inbounds [10 x i32*], [10 x i32*]* %PointerArray, i64 0, i64 1
  %72 = load i32*, i32** %arrayidx56, align 8
  %a57 = getelementptr inbounds %struct.PointerCase, %struct.PointerCase* %pointerCase, i32 0, i32 0
  store i32* %72, i32** %a57, align 8
  %73 = load i32, i32* %a, align 4
  %dec = add nsw i32 %73, -1
  store i32 %dec, i32* %a, align 4
  %74 = load i32, i32* %b, align 4
  %cmp58 = icmp sgt i32 %74, 0
  br i1 %cmp58, label %if.then59, label %if.else60

if.then59:                                        ; preds = %while.body54
  %75 = load i32*, i32** %g, align 8
  %76 = load i32**, i32*** %e, align 8
  store i32* %75, i32** %76, align 8
  %77 = load i32**, i32*** %e, align 8
  %78 = load i32*, i32** %77, align 8
  store i32* %78, i32** %h, align 8
  store i32** %h, i32*** %q, align 8
  %79 = load i32*, i32** %p, align 8
  %80 = load i32**, i32*** %f, align 8
  store i32* %79, i32** %80, align 8
  br label %if.end61

if.else60:                                        ; preds = %while.body54
  %81 = load i32*, i32** %p, align 8
  %82 = load i32**, i32*** %q, align 8
  store i32* %81, i32** %82, align 8
  %83 = load i32*, i32** %h, align 8
  store i32* %83, i32** %g, align 8
  store i32* %b, i32** %p, align 8
  br label %if.end61

if.end61:                                         ; preds = %if.else60, %if.then59
  br label %while.cond52

while.end62:                                      ; preds = %while.cond52
  %call63 = call noalias i8* @malloc(i64 40) #5
  %84 = bitcast i8* %call63 to i32*
  store i32* %84, i32** %newP, align 8
  %call64 = call i8* @_Znam(i64 40) #6
  %85 = bitcast i8* %call64 to i32*
  store i32* %85, i32** %newPP, align 8
  ret i32 0
}

; Function Attrs: nounwind
declare dso_local noalias i8* @malloc(i64) #3

; Function Attrs: nobuiltin
declare dso_local noalias i8* @_Znam(i64) #4

attributes #0 = { noinline optnone uwtable "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "min-legal-vector-width"="0" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #1 = { noinline nounwind optnone uwtable "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "min-legal-vector-width"="0" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #2 = { noinline norecurse optnone uwtable "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "min-legal-vector-width"="0" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #3 = { nounwind "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #4 = { nobuiltin "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #5 = { nounwind }
attributes #6 = { builtin }

!llvm.module.flags = !{!0}
!llvm.ident = !{!1}

!0 = !{i32 1, !"wchar_size", i32 4}
!1 = !{!"clang version 8.0.0 (tags/RELEASE_800/final 361961) (llvm/tags/RELEASE_800/final 361957)"}
