; ModuleID = 'testCase2.cpp'
source_filename = "testCase2.cpp"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-unknown-linux-gnu"

@global = global i32* null, align 8

; Function Attrs: noinline nounwind optnone uwtable
define void @_Z4fun1Pi(i32*) #0 {
  %2 = alloca i32*, align 8
  store i32* %0, i32** %2, align 8
  %3 = load i32*, i32** %2, align 8
  store i32* %3, i32** @global, align 8
  ret void
}

; Function Attrs: noinline nounwind optnone uwtable
define void @_Z4fun2PPi(i32**) #0 {
  %2 = alloca i32**, align 8
  store i32** %0, i32*** %2, align 8
  %3 = load i32*, i32** @global, align 8
  %4 = load i32**, i32*** %2, align 8
  store i32* %3, i32** %4, align 8
  ret void
}

; Function Attrs: noinline norecurse nounwind optnone uwtable
define i32 @main() #1 {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  %3 = alloca i32, align 4
  %4 = alloca i32, align 4
  %5 = alloca i32, align 4
  %6 = alloca i32**, align 8
  %7 = alloca i32**, align 8
  %8 = alloca i32**, align 8
  %9 = alloca i32*, align 8
  %10 = alloca i32*, align 8
  %11 = alloca i32*, align 8
  store i32 0, i32* %1, align 4
  store i32 1, i32* %2, align 4
  store i32 2, i32* %3, align 4
  store i32 3, i32* %4, align 4
  %12 = load i32, i32* %2, align 4
  %13 = load i32, i32* %3, align 4
  %14 = add nsw i32 %12, %13
  %15 = load i32, i32* %4, align 4
  %16 = add nsw i32 %14, %15
  store i32 %16, i32* %5, align 4
  %17 = load i32, i32* %2, align 4
  %18 = load i32, i32* %3, align 4
  %19 = sub nsw i32 %17, %18
  store i32 %19, i32* %5, align 4
  %20 = load i32, i32* %5, align 4
  %21 = load i32, i32* %2, align 4
  %22 = mul nsw i32 %20, %21
  store i32 %22, i32* %4, align 4
  %23 = load i32, i32* %4, align 4
  %24 = add nsw i32 %23, 1
  store i32 %24, i32* %3, align 4
  %25 = load i32**, i32*** %7, align 8
  store i32** %25, i32*** %6, align 8
  %26 = load i32**, i32*** %6, align 8
  %27 = load i32*, i32** %26, align 8
  store i32* %27, i32** @global, align 8
  %28 = load i32, i32* %3, align 4
  %29 = icmp sgt i32 %28, 0
  br i1 %29, label %30, label %37

; <label>:30:                                     ; preds = %0
  %31 = load i32*, i32** %9, align 8
  %32 = load i32**, i32*** %6, align 8
  store i32* %31, i32** %32, align 8
  %33 = load i32**, i32*** %6, align 8
  %34 = load i32*, i32** %33, align 8
  store i32* %34, i32** %10, align 8
  store i32** %10, i32*** %8, align 8
  %35 = load i32*, i32** %11, align 8
  %36 = load i32**, i32*** %7, align 8
  store i32* %35, i32** %36, align 8
  br label %41

; <label>:37:                                     ; preds = %0
  %38 = load i32*, i32** %11, align 8
  %39 = load i32**, i32*** %8, align 8
  store i32* %38, i32** %39, align 8
  %40 = load i32*, i32** %10, align 8
  store i32* %40, i32** %9, align 8
  store i32* %3, i32** %11, align 8
  br label %41

; <label>:41:                                     ; preds = %37, %30
  br label %42

; <label>:42:                                     ; preds = %45, %41
  %43 = load i32, i32* %2, align 4
  %44 = icmp ne i32 %43, 0
  br i1 %44, label %45, label %49

; <label>:45:                                     ; preds = %42
  %46 = load i32**, i32*** %8, align 8
  %47 = load i32*, i32** %46, align 8
  store i32* %47, i32** %10, align 8
  %48 = load i32*, i32** %11, align 8
  store i32* %48, i32** %9, align 8
  br label %42

; <label>:49:                                     ; preds = %42
  %50 = load i32, i32* %4, align 4
  switch i32 %50, label %61 [
    i32 1, label %51
    i32 2, label %55
  ]

; <label>:51:                                     ; preds = %49
  %52 = load i32, i32* %2, align 4
  %53 = load i32, i32* %4, align 4
  %54 = add nsw i32 %52, %53
  store i32 %54, i32* %5, align 4
  store i32* %5, i32** %11, align 8
  br label %62

; <label>:55:                                     ; preds = %49
  %56 = load i32, i32* %5, align 4
  %57 = load i32, i32* %4, align 4
  %58 = sub nsw i32 %57, 1
  %59 = mul nsw i32 %58, 2
  %60 = add nsw i32 %56, %59
  store i32 %60, i32* %2, align 4
  store i32* %2, i32** %11, align 8
  br label %62

; <label>:61:                                     ; preds = %49
  br label %62

; <label>:62:                                     ; preds = %61, %55, %51
  %63 = load i32, i32* %5, align 4
  %64 = icmp sgt i32 %63, 0
  br i1 %64, label %65, label %67

; <label>:65:                                     ; preds = %62
  %66 = load i32*, i32** %10, align 8
  call void @_Z4fun1Pi(i32* %66)
  br label %69

; <label>:67:                                     ; preds = %62
  %68 = load i32**, i32*** %6, align 8
  call void @_Z4fun2PPi(i32** %68)
  br label %69

; <label>:69:                                     ; preds = %67, %65
  ret i32 0
}

attributes #0 = { noinline nounwind optnone uwtable "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #1 = { noinline norecurse nounwind optnone uwtable "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }

!llvm.module.flags = !{!0}
!llvm.ident = !{!1}

!0 = !{i32 1, !"wchar_size", i32 4}
!1 = !{!"clang version 5.0.0 (tags/RELEASE_500/final 358156)"}
