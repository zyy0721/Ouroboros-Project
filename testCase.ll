; ModuleID = 'testCase.cpp'
source_filename = "testCase.cpp"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-unknown-linux-gnu"

; Function Attrs: noinline norecurse nounwind optnone uwtable
define i32 @main() #0 {
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
  %26 = load i32, i32* %3, align 4
  %27 = icmp sgt i32 %26, 0
  br i1 %27, label %28, label %35

; <label>:28:                                     ; preds = %0
  %29 = load i32*, i32** %9, align 8
  %30 = load i32**, i32*** %6, align 8
  store i32* %29, i32** %30, align 8
  %31 = load i32**, i32*** %6, align 8
  %32 = load i32*, i32** %31, align 8
  store i32* %32, i32** %10, align 8
  store i32** %10, i32*** %8, align 8
  %33 = load i32*, i32** %11, align 8
  %34 = load i32**, i32*** %7, align 8
  store i32* %33, i32** %34, align 8
  br label %39

; <label>:35:                                     ; preds = %0
  %36 = load i32*, i32** %11, align 8
  %37 = load i32**, i32*** %8, align 8
  store i32* %36, i32** %37, align 8
  %38 = load i32*, i32** %10, align 8
  store i32* %38, i32** %9, align 8
  store i32* %3, i32** %11, align 8
  br label %39

; <label>:39:                                     ; preds = %35, %28
  ret i32 0
}

attributes #0 = { noinline norecurse nounwind optnone uwtable "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }

!llvm.module.flags = !{!0}
!llvm.ident = !{!1}

!0 = !{i32 1, !"wchar_size", i32 4}
!1 = !{!"clang version 5.0.0 (tags/RELEASE_500/final 358156)"}
