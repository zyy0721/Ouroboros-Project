; ModuleID = 'testCase5.cpp'
source_filename = "testCase5.cpp"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-unknown-linux-gnu"

%struct.PointerCase = type { i32*, i32*, i32**, i32**, i32 }

@globalA = global i32* null, align 8
@globalB = global i32** null, align 8

; Function Attrs: noinline nounwind optnone uwtable
define void @_Z4fun1iPiPS_(i32, i32*, i32**) #0 {
  %4 = alloca i32, align 4
  %5 = alloca i32*, align 8
  %6 = alloca i32**, align 8
  store i32 %0, i32* %4, align 4
  store i32* %1, i32** %5, align 8
  store i32** %2, i32*** %6, align 8
  %7 = load i32*, i32** %5, align 8
  store i32* %7, i32** @globalA, align 8
  %8 = load i32**, i32*** @globalB, align 8
  store i32** %8, i32*** %6, align 8
  %9 = load i32*, i32** %5, align 8
  %10 = load i32**, i32*** @globalB, align 8
  store i32* %9, i32** %10, align 8
  store i32** @globalA, i32*** %6, align 8
  %11 = load i32**, i32*** @globalB, align 8
  %12 = load i32*, i32** %11, align 8
  store i32* %12, i32** @globalA, align 8
  ret void
}

; Function Attrs: noinline nounwind optnone uwtable
define void @_Z4fun2iPiPS_S_(i32, i32*, i32**, i32*) #0 {
  %5 = alloca i32, align 4
  %6 = alloca i32*, align 8
  %7 = alloca i32**, align 8
  %8 = alloca i32*, align 8
  store i32 %0, i32* %5, align 4
  store i32* %1, i32** %6, align 8
  store i32** %2, i32*** %7, align 8
  store i32* %3, i32** %8, align 8
  %9 = load i32, i32* %5, align 4
  %10 = icmp sgt i32 %9, 0
  br i1 %10, label %11, label %17

; <label>:11:                                     ; preds = %4
  store i32* %5, i32** @globalA, align 8
  %12 = load i32*, i32** %6, align 8
  %13 = load i32**, i32*** %7, align 8
  store i32* %12, i32** %13, align 8
  %14 = load i32**, i32*** %7, align 8
  %15 = load i32*, i32** %14, align 8
  store i32* %15, i32** %8, align 8
  %16 = load i32*, i32** %8, align 8
  store i32* %16, i32** %6, align 8
  br label %22

; <label>:17:                                     ; preds = %4
  store i32** %8, i32*** @globalB, align 8
  store i32* %5, i32** %6, align 8
  %18 = load i32*, i32** %6, align 8
  %19 = load i32**, i32*** @globalB, align 8
  store i32* %18, i32** %19, align 8
  %20 = load i32**, i32*** %7, align 8
  %21 = load i32*, i32** %20, align 8
  store i32* %21, i32** %8, align 8
  br label %22

; <label>:22:                                     ; preds = %17, %11
  ret void
}

; Function Attrs: noinline norecurse optnone uwtable
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
  %12 = alloca [10 x i32], align 16
  %13 = alloca [10 x i32*], align 16
  %14 = alloca %struct.PointerCase, align 8
  %15 = alloca i32*, align 8
  %16 = alloca i32*, align 8
  store i32 0, i32* %1, align 4
  store i32 1, i32* %2, align 4
  store i32 2, i32* %3, align 4
  store i32 3, i32* %4, align 4
  %17 = load i32, i32* %2, align 4
  %18 = load i32, i32* %3, align 4
  %19 = add nsw i32 %17, %18
  %20 = load i32, i32* %4, align 4
  %21 = add nsw i32 %19, %20
  store i32 %21, i32* %5, align 4
  %22 = load i32, i32* %2, align 4
  %23 = load i32, i32* %3, align 4
  %24 = sub nsw i32 %22, %23
  store i32 %24, i32* %5, align 4
  %25 = load i32, i32* %5, align 4
  %26 = load i32, i32* %2, align 4
  %27 = mul nsw i32 %25, %26
  store i32 %27, i32* %4, align 4
  %28 = load i32, i32* %4, align 4
  %29 = add nsw i32 %28, 1
  store i32 %29, i32* %3, align 4
  %30 = load i32**, i32*** %7, align 8
  store i32** %30, i32*** %6, align 8
  %31 = load i32**, i32*** %6, align 8
  %32 = load i32*, i32** %31, align 8
  store i32* %32, i32** @globalA, align 8
  %33 = load i32, i32* %3, align 4
  %34 = icmp sgt i32 %33, 0
  br i1 %34, label %35, label %42

; <label>:35:                                     ; preds = %0
  %36 = load i32*, i32** %9, align 8
  %37 = load i32**, i32*** %6, align 8
  store i32* %36, i32** %37, align 8
  %38 = load i32**, i32*** %6, align 8
  %39 = load i32*, i32** %38, align 8
  store i32* %39, i32** %10, align 8
  store i32** %10, i32*** %8, align 8
  %40 = load i32*, i32** %11, align 8
  %41 = load i32**, i32*** %7, align 8
  store i32* %40, i32** %41, align 8
  br label %46

; <label>:42:                                     ; preds = %0
  %43 = load i32*, i32** %11, align 8
  %44 = load i32**, i32*** %8, align 8
  store i32* %43, i32** %44, align 8
  %45 = load i32*, i32** %10, align 8
  store i32* %45, i32** %9, align 8
  store i32* %3, i32** %11, align 8
  br label %46

; <label>:46:                                     ; preds = %42, %35
  br label %47

; <label>:47:                                     ; preds = %50, %46
  %48 = load i32, i32* %2, align 4
  %49 = icmp ne i32 %48, 0
  br i1 %49, label %50, label %54

; <label>:50:                                     ; preds = %47
  %51 = load i32**, i32*** %8, align 8
  %52 = load i32*, i32** %51, align 8
  store i32* %52, i32** %10, align 8
  %53 = load i32*, i32** %11, align 8
  store i32* %53, i32** %9, align 8
  br label %47

; <label>:54:                                     ; preds = %47
  %55 = load i32, i32* %4, align 4
  switch i32 %55, label %66 [
    i32 1, label %56
    i32 2, label %60
  ]

; <label>:56:                                     ; preds = %54
  %57 = load i32, i32* %2, align 4
  %58 = load i32, i32* %4, align 4
  %59 = add nsw i32 %57, %58
  store i32 %59, i32* %5, align 4
  store i32* %5, i32** %11, align 8
  br label %67

; <label>:60:                                     ; preds = %54
  %61 = load i32, i32* %5, align 4
  %62 = load i32, i32* %4, align 4
  %63 = sub nsw i32 %62, 1
  %64 = mul nsw i32 %63, 2
  %65 = add nsw i32 %61, %64
  store i32 %65, i32* %2, align 4
  store i32* %2, i32** %11, align 8
  br label %67

; <label>:66:                                     ; preds = %54
  br label %67

; <label>:67:                                     ; preds = %66, %60, %56
  %68 = load i32, i32* %5, align 4
  %69 = icmp sgt i32 %68, 0
  br i1 %69, label %70, label %74

; <label>:70:                                     ; preds = %67
  %71 = load i32, i32* %2, align 4
  %72 = load i32*, i32** %9, align 8
  %73 = load i32**, i32*** %6, align 8
  call void @_Z4fun1iPiPS_(i32 %71, i32* %72, i32** %73)
  br label %79

; <label>:74:                                     ; preds = %67
  %75 = load i32, i32* %3, align 4
  %76 = load i32*, i32** %10, align 8
  %77 = load i32**, i32*** %8, align 8
  %78 = load i32*, i32** %11, align 8
  call void @_Z4fun2iPiPS_S_(i32 %75, i32* %76, i32** %77, i32* %78)
  br label %79

; <label>:79:                                     ; preds = %74, %70
  %80 = load i32, i32* %4, align 4
  %81 = icmp ne i32 %80, 1
  br i1 %81, label %82, label %93

; <label>:82:                                     ; preds = %79
  %83 = load i32*, i32** %9, align 8
  %84 = getelementptr inbounds %struct.PointerCase, %struct.PointerCase* %14, i32 0, i32 0
  store i32* %83, i32** %84, align 8
  %85 = getelementptr inbounds %struct.PointerCase, %struct.PointerCase* %14, i32 0, i32 1
  %86 = load i32*, i32** %85, align 8
  store i32* %86, i32** %10, align 8
  %87 = load i32*, i32** %11, align 8
  %88 = getelementptr inbounds %struct.PointerCase, %struct.PointerCase* %14, i32 0, i32 2
  %89 = load i32**, i32*** %88, align 8
  store i32* %87, i32** %89, align 8
  %90 = getelementptr inbounds %struct.PointerCase, %struct.PointerCase* %14, i32 0, i32 3
  %91 = load i32**, i32*** %90, align 8
  %92 = load i32*, i32** %91, align 8
  store i32* %92, i32** %10, align 8
  br label %102

; <label>:93:                                     ; preds = %79
  %94 = getelementptr inbounds %struct.PointerCase, %struct.PointerCase* %14, i32 0, i32 3
  store i32** %9, i32*** %94, align 8
  %95 = getelementptr inbounds %struct.PointerCase, %struct.PointerCase* %14, i32 0, i32 0
  store i32** %95, i32*** %7, align 8
  %96 = getelementptr inbounds %struct.PointerCase, %struct.PointerCase* %14, i32 0, i32 1
  %97 = load i32*, i32** %96, align 8
  %98 = load i32**, i32*** %6, align 8
  store i32* %97, i32** %98, align 8
  %99 = load i32**, i32*** %7, align 8
  %100 = load i32*, i32** %99, align 8
  %101 = getelementptr inbounds %struct.PointerCase, %struct.PointerCase* %14, i32 0, i32 0
  store i32* %100, i32** %101, align 8
  br label %102

; <label>:102:                                    ; preds = %93, %82
  br label %103

; <label>:103:                                    ; preds = %106, %102
  %104 = load i32, i32* %2, align 4
  %105 = icmp sgt i32 %104, 0
  br i1 %105, label %106, label %114

; <label>:106:                                    ; preds = %103
  %107 = getelementptr inbounds [10 x i32*], [10 x i32*]* %13, i64 0, i64 0
  %108 = load i32*, i32** %107, align 16
  store i32* %108, i32** %9, align 8
  %109 = getelementptr inbounds [10 x i32*], [10 x i32*]* %13, i64 0, i64 1
  %110 = load i32*, i32** %109, align 8
  %111 = getelementptr inbounds %struct.PointerCase, %struct.PointerCase* %14, i32 0, i32 0
  store i32* %110, i32** %111, align 8
  %112 = load i32, i32* %2, align 4
  %113 = add nsw i32 %112, -1
  store i32 %113, i32* %2, align 4
  br label %103

; <label>:114:                                    ; preds = %103
  %115 = call noalias i8* @malloc(i64 40) #4
  %116 = bitcast i8* %115 to i32*
  store i32* %116, i32** %15, align 8
  %117 = call i8* @_Znam(i64 40) #5
  %118 = bitcast i8* %117 to i32*
  store i32* %118, i32** %16, align 8
  ret i32 0
}

; Function Attrs: nounwind
declare noalias i8* @malloc(i64) #2

; Function Attrs: nobuiltin
declare noalias i8* @_Znam(i64) #3

attributes #0 = { noinline nounwind optnone uwtable "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #1 = { noinline norecurse optnone uwtable "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #2 = { nounwind "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #3 = { nobuiltin "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #4 = { nounwind }
attributes #5 = { builtin }

!llvm.module.flags = !{!0}
!llvm.ident = !{!1}

!0 = !{i32 1, !"wchar_size", i32 4}
!1 = !{!"clang version 5.0.0 (tags/RELEASE_500/final 358156)"}
