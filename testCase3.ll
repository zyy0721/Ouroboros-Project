; ModuleID = 'testCase3.cpp'
source_filename = "testCase3.cpp"
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
  %12 = alloca i32*, align 8
  %13 = alloca i32*, align 8
  store i32 0, i32* %1, align 4
  store i32 1, i32* %2, align 4
  store i32 2, i32* %3, align 4
  store i32 3, i32* %4, align 4
  %14 = load i32, i32* %2, align 4
  %15 = load i32, i32* %3, align 4
  %16 = add nsw i32 %14, %15
  %17 = load i32, i32* %4, align 4
  %18 = add nsw i32 %16, %17
  store i32 %18, i32* %5, align 4
  %19 = load i32, i32* %2, align 4
  %20 = load i32, i32* %3, align 4
  %21 = sub nsw i32 %19, %20
  store i32 %21, i32* %5, align 4
  %22 = load i32, i32* %5, align 4
  %23 = load i32, i32* %2, align 4
  %24 = mul nsw i32 %22, %23
  store i32 %24, i32* %4, align 4
  %25 = load i32, i32* %4, align 4
  %26 = add nsw i32 %25, 1
  store i32 %26, i32* %3, align 4
  %27 = load i32**, i32*** %7, align 8
  store i32** %27, i32*** %6, align 8
  %28 = load i32**, i32*** %6, align 8
  %29 = load i32*, i32** %28, align 8
  store i32* %29, i32** @global, align 8
  %30 = load i32, i32* %3, align 4
  %31 = icmp sgt i32 %30, 0
  br i1 %31, label %32, label %39

; <label>:32:                                     ; preds = %0
  %33 = load i32*, i32** %9, align 8
  %34 = load i32**, i32*** %6, align 8
  store i32* %33, i32** %34, align 8
  %35 = load i32**, i32*** %6, align 8
  %36 = load i32*, i32** %35, align 8
  store i32* %36, i32** %10, align 8
  store i32** %10, i32*** %8, align 8
  %37 = load i32*, i32** %11, align 8
  %38 = load i32**, i32*** %7, align 8
  store i32* %37, i32** %38, align 8
  br label %43

; <label>:39:                                     ; preds = %0
  %40 = load i32*, i32** %11, align 8
  %41 = load i32**, i32*** %8, align 8
  store i32* %40, i32** %41, align 8
  %42 = load i32*, i32** %10, align 8
  store i32* %42, i32** %9, align 8
  store i32* %3, i32** %11, align 8
  br label %43

; <label>:43:                                     ; preds = %39, %32
  br label %44

; <label>:44:                                     ; preds = %47, %43
  %45 = load i32, i32* %2, align 4
  %46 = icmp ne i32 %45, 0
  br i1 %46, label %47, label %51

; <label>:47:                                     ; preds = %44
  %48 = load i32**, i32*** %8, align 8
  %49 = load i32*, i32** %48, align 8
  store i32* %49, i32** %10, align 8
  %50 = load i32*, i32** %11, align 8
  store i32* %50, i32** %9, align 8
  br label %44

; <label>:51:                                     ; preds = %44
  %52 = load i32, i32* %4, align 4
  switch i32 %52, label %63 [
    i32 1, label %53
    i32 2, label %57
  ]

; <label>:53:                                     ; preds = %51
  %54 = load i32, i32* %2, align 4
  %55 = load i32, i32* %4, align 4
  %56 = add nsw i32 %54, %55
  store i32 %56, i32* %5, align 4
  store i32* %5, i32** %11, align 8
  br label %64

; <label>:57:                                     ; preds = %51
  %58 = load i32, i32* %5, align 4
  %59 = load i32, i32* %4, align 4
  %60 = sub nsw i32 %59, 1
  %61 = mul nsw i32 %60, 2
  %62 = add nsw i32 %58, %61
  store i32 %62, i32* %2, align 4
  store i32* %2, i32** %11, align 8
  br label %64

; <label>:63:                                     ; preds = %51
  br label %64

; <label>:64:                                     ; preds = %63, %57, %53
  %65 = load i32, i32* %5, align 4
  %66 = icmp sgt i32 %65, 0
  br i1 %66, label %67, label %69

; <label>:67:                                     ; preds = %64
  %68 = load i32*, i32** %10, align 8
  call void @_Z4fun1Pi(i32* %68)
  br label %71

; <label>:69:                                     ; preds = %64
  %70 = load i32**, i32*** %6, align 8
  call void @_Z4fun2PPi(i32** %70)
  br label %71

; <label>:71:                                     ; preds = %69, %67
  %72 = call noalias i8* @malloc(i64 40) #4
  %73 = bitcast i8* %72 to i32*
  store i32* %73, i32** %12, align 8
  %74 = call i8* @_Znam(i64 40) #5
  %75 = bitcast i8* %74 to i32*
  store i32* %75, i32** %13, align 8
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
