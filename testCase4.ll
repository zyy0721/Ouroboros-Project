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
  %25 = getelementptr inbounds %struct.PointerCase, %struct.PointerCase* %9, i32 0, i32 3
  %26 = load i32**, i32*** %25, align 8
  %27 = load i32*, i32** %26, align 8
  store i32* %27, i32** %3, align 8
  %28 = load i32**, i32*** %4, align 8
  %29 = load i32*, i32** %28, align 8
  %30 = getelementptr inbounds %struct.PointerCase, %struct.PointerCase* %9, i32 0, i32 0
  store i32* %29, i32** %30, align 8
  %31 = load i32, i32* %6, align 4
  %32 = icmp ne i32 %31, 0
  br i1 %32, label %33, label %40

; <label>:33:                                     ; preds = %0
  %34 = getelementptr inbounds [10 x i32], [10 x i32]* %7, i64 0, i64 0
  %35 = load i32, i32* %34, align 16
  store i32 %35, i32* %6, align 4
  %36 = getelementptr inbounds [10 x i32*], [10 x i32*]* %8, i64 0, i64 0
  %37 = load i32*, i32** %36, align 16
  store i32* %37, i32** %2, align 8
  %38 = getelementptr inbounds [10 x i32*], [10 x i32*]* %8, i64 0, i64 1
  %39 = load i32*, i32** %38, align 8
  store i32* %39, i32** %3, align 8
  br label %49

; <label>:40:                                     ; preds = %0
  store i32 2, i32* %10, align 4
  %41 = load i32, i32* %10, align 4
  %42 = sext i32 %41 to i64
  %43 = getelementptr inbounds [10 x i32], [10 x i32]* %7, i64 0, i64 %42
  %44 = load i32, i32* %43, align 4
  store i32 %44, i32* %6, align 4
  %45 = load i32, i32* %10, align 4
  %46 = sext i32 %45 to i64
  %47 = getelementptr inbounds [10 x i32*], [10 x i32*]* %8, i64 0, i64 %46
  %48 = load i32*, i32** %47, align 8
  store i32* %48, i32** %2, align 8
  br label %49

; <label>:49:                                     ; preds = %40, %33
  ret i32 0
}

attributes #0 = { noinline norecurse nounwind optnone uwtable "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }

!llvm.module.flags = !{!0}
!llvm.ident = !{!1}

!0 = !{i32 1, !"wchar_size", i32 4}
!1 = !{!"clang version 5.0.0 (tags/RELEASE_500/final 358156)"}
