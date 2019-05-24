; ModuleID = 'testCase4.cpp'
source_filename = "testCase4.cpp"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-unknown-linux-gnu"

%struct.PointerCase = type { i32*, i32*, i32**, i32**, i32 }

; Function Attrs: noinline norecurse nounwind optnone uwtable
define i32 @main() #0 {
  %1 = alloca i32, align 4
  %2 = alloca i32*, align 8
  %3 = alloca i32*, align 8
  %4 = alloca i32**, align 8
  %5 = alloca i32**, align 8
  %6 = alloca i32, align 4
  %7 = alloca [10 x i32], align 16
  %8 = alloca [10 x i32*], align 16
  %9 = alloca %struct.PointerCase, align 8
  %10 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  store i32 1, i32* %6, align 4
  %11 = load i32*, i32** %2, align 8
  %12 = getelementptr inbounds %struct.PointerCase, %struct.PointerCase* %9, i32 0, i32 0
  store i32* %11, i32** %12, align 8
  %13 = load i32**, i32*** %5, align 8
  %14 = getelementptr inbounds %struct.PointerCase, %struct.PointerCase* %9, i32 0, i32 2
  store i32** %13, i32*** %14, align 8
  %15 = getelementptr inbounds %struct.PointerCase, %struct.PointerCase* %9, i32 0, i32 0
  %16 = load i32*, i32** %15, align 8
  store i32* %16, i32** %3, align 8
  %17 = load i32*, i32** %3, align 8
  %18 = getelementptr inbounds %struct.PointerCase, %struct.PointerCase* %9, i32 0, i32 2
  %19 = load i32**, i32*** %18, align 8
  store i32* %17, i32** %19, align 8
  %20 = getelementptr inbounds %struct.PointerCase, %struct.PointerCase* %9, i32 0, i32 3
  store i32** %2, i32*** %20, align 8
  %21 = getelementptr inbounds %struct.PointerCase, %struct.PointerCase* %9, i32 0, i32 0
  store i32** %21, i32*** %4, align 8
  %22 = getelementptr inbounds %struct.PointerCase, %struct.PointerCase* %9, i32 0, i32 1
  %23 = load i32*, i32** %22, align 8
  %24 = load i32**, i32*** %5, align 8
  store i32* %23, i32** %24, align 8
  %25 = load i32, i32* %6, align 4
  %26 = icmp ne i32 %25, 0
  br i1 %26, label %27, label %34

; <label>:27:                                     ; preds = %0
  %28 = getelementptr inbounds [10 x i32], [10 x i32]* %7, i64 0, i64 0
  %29 = load i32, i32* %28, align 16
  store i32 %29, i32* %6, align 4
  %30 = getelementptr inbounds [10 x i32*], [10 x i32*]* %8, i64 0, i64 0
  %31 = load i32*, i32** %30, align 16
  store i32* %31, i32** %2, align 8
  %32 = getelementptr inbounds [10 x i32*], [10 x i32*]* %8, i64 0, i64 1
  %33 = load i32*, i32** %32, align 8
  store i32* %33, i32** %3, align 8
  br label %43

; <label>:34:                                     ; preds = %0
  store i32 2, i32* %10, align 4
  %35 = load i32, i32* %10, align 4
  %36 = sext i32 %35 to i64
  %37 = getelementptr inbounds [10 x i32], [10 x i32]* %7, i64 0, i64 %36
  %38 = load i32, i32* %37, align 4
  store i32 %38, i32* %6, align 4
  %39 = load i32, i32* %10, align 4
  %40 = sext i32 %39 to i64
  %41 = getelementptr inbounds [10 x i32*], [10 x i32*]* %8, i64 0, i64 %40
  %42 = load i32*, i32** %41, align 8
  store i32* %42, i32** %2, align 8
  br label %43

; <label>:43:                                     ; preds = %34, %27
  ret i32 0
}

attributes #0 = { noinline norecurse nounwind optnone uwtable "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }

!llvm.module.flags = !{!0}
!llvm.ident = !{!1}

!0 = !{i32 1, !"wchar_size", i32 4}
!1 = !{!"clang version 5.0.0 (tags/RELEASE_500/final 358156)"}
