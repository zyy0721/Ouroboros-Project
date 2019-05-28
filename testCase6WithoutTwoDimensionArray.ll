; ModuleID = 'testCase6WithoutTwoDimensionArray.cpp'
source_filename = "testCase6WithoutTwoDimensionArray.cpp"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-unknown-linux-gnu"

%struct.PointerCase = type { i32*, i32*, i32**, i32**, i32 }

@globalA = global i32* null, align 8
@globalB = global i32** null, align 8

; Function Attrs: noinline nounwind optnone uwtable
define i32* @_Z4fun1iPiPS_(i32, i32*, i32**) #0 {
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
  ret i32* %9
}

; Function Attrs: noinline nounwind optnone uwtable
define i32** @_Z4fun2iPiPS_S_(i32, i32*, i32**, i32*) #0 {
  %5 = alloca i32**, align 8
  %6 = alloca i32, align 4
  %7 = alloca i32*, align 8
  %8 = alloca i32**, align 8
  %9 = alloca i32*, align 8
  store i32 %0, i32* %6, align 4
  store i32* %1, i32** %7, align 8
  store i32** %2, i32*** %8, align 8
  store i32* %3, i32** %9, align 8
  %10 = load i32, i32* %6, align 4
  %11 = icmp sgt i32 %10, 0
  br i1 %11, label %12, label %19

; <label>:12:                                     ; preds = %4
  store i32* %6, i32** @globalA, align 8
  %13 = load i32*, i32** %7, align 8
  %14 = load i32**, i32*** %8, align 8
  store i32* %13, i32** %14, align 8
  %15 = load i32**, i32*** %8, align 8
  %16 = load i32*, i32** %15, align 8
  store i32* %16, i32** %9, align 8
  %17 = load i32*, i32** %9, align 8
  store i32* %17, i32** %7, align 8
  %18 = load i32**, i32*** %8, align 8
  store i32** %18, i32*** %5, align 8
  br label %25

; <label>:19:                                     ; preds = %4
  store i32** %9, i32*** @globalB, align 8
  store i32* %6, i32** %7, align 8
  %20 = load i32*, i32** %7, align 8
  %21 = load i32**, i32*** @globalB, align 8
  store i32* %20, i32** %21, align 8
  %22 = load i32**, i32*** %8, align 8
  %23 = load i32*, i32** %22, align 8
  store i32* %23, i32** %9, align 8
  %24 = load i32**, i32*** @globalB, align 8
  store i32** %24, i32*** %5, align 8
  br label %25

; <label>:25:                                     ; preds = %19, %12
  %26 = load i32**, i32*** %5, align 8
  ret i32** %26
}

; Function Attrs: noinline nounwind optnone uwtable
define void @_Z4fun3iPi(i32, i32*) #0 {
  %3 = alloca i32, align 4
  %4 = alloca i32*, align 8
  store i32 %0, i32* %3, align 4
  store i32* %1, i32** %4, align 8
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
  %12 = alloca [10 x i32], align 16
  %13 = alloca [10 x i32*], align 16
  %14 = alloca %struct.PointerCase, align 8
  %15 = alloca i32, align 4
  %16 = alloca i32, align 4
  %17 = alloca i32*, align 8
  %18 = alloca i32*, align 8
  store i32 0, i32* %1, align 4
  store i32 1, i32* %2, align 4
  store i32 2, i32* %3, align 4
  store i32 3, i32* %4, align 4
  %19 = load i32, i32* %2, align 4
  %20 = load i32, i32* %3, align 4
  %21 = add nsw i32 %19, %20
  %22 = load i32, i32* %4, align 4
  %23 = add nsw i32 %21, %22
  store i32 %23, i32* %5, align 4
  %24 = load i32, i32* %2, align 4
  %25 = load i32, i32* %3, align 4
  %26 = sub nsw i32 %24, %25
  store i32 %26, i32* %5, align 4
  %27 = load i32, i32* %5, align 4
  %28 = load i32, i32* %2, align 4
  %29 = mul nsw i32 %27, %28
  store i32 %29, i32* %4, align 4
  %30 = load i32, i32* %4, align 4
  %31 = add nsw i32 %30, 1
  store i32 %31, i32* %3, align 4
  %32 = load i32**, i32*** %7, align 8
  store i32** %32, i32*** %6, align 8
  %33 = load i32**, i32*** %6, align 8
  %34 = load i32*, i32** %33, align 8
  store i32* %34, i32** @globalA, align 8
  %35 = load i32, i32* %3, align 4
  %36 = icmp sgt i32 %35, 0
  br i1 %36, label %37, label %44

; <label>:37:                                     ; preds = %0
  %38 = load i32*, i32** %9, align 8
  %39 = load i32**, i32*** %6, align 8
  store i32* %38, i32** %39, align 8
  %40 = load i32**, i32*** %6, align 8
  %41 = load i32*, i32** %40, align 8
  store i32* %41, i32** %10, align 8
  store i32** %10, i32*** %8, align 8
  %42 = load i32*, i32** %11, align 8
  %43 = load i32**, i32*** %7, align 8
  store i32* %42, i32** %43, align 8
  br label %48

; <label>:44:                                     ; preds = %0
  %45 = load i32*, i32** %11, align 8
  %46 = load i32**, i32*** %8, align 8
  store i32* %45, i32** %46, align 8
  %47 = load i32*, i32** %10, align 8
  store i32* %47, i32** %9, align 8
  store i32* %3, i32** %11, align 8
  br label %48

; <label>:48:                                     ; preds = %44, %37
  br label %49

; <label>:49:                                     ; preds = %52, %48
  %50 = load i32, i32* %2, align 4
  %51 = icmp ne i32 %50, 0
  br i1 %51, label %52, label %56

; <label>:52:                                     ; preds = %49
  %53 = load i32**, i32*** %8, align 8
  %54 = load i32*, i32** %53, align 8
  store i32* %54, i32** %10, align 8
  %55 = load i32*, i32** %11, align 8
  store i32* %55, i32** %9, align 8
  br label %49

; <label>:56:                                     ; preds = %49
  %57 = load i32, i32* %4, align 4
  switch i32 %57, label %68 [
    i32 1, label %58
    i32 2, label %62
  ]

; <label>:58:                                     ; preds = %56
  %59 = load i32, i32* %2, align 4
  %60 = load i32, i32* %4, align 4
  %61 = add nsw i32 %59, %60
  store i32 %61, i32* %5, align 4
  store i32* %5, i32** %11, align 8
  br label %69

; <label>:62:                                     ; preds = %56
  %63 = load i32, i32* %5, align 4
  %64 = load i32, i32* %4, align 4
  %65 = sub nsw i32 %64, 1
  %66 = mul nsw i32 %65, 2
  %67 = add nsw i32 %63, %66
  store i32 %67, i32* %2, align 4
  store i32* %2, i32** %11, align 8
  br label %69

; <label>:68:                                     ; preds = %56
  br label %69

; <label>:69:                                     ; preds = %68, %62, %58
  %70 = load i32, i32* %5, align 4
  %71 = icmp sgt i32 %70, 0
  br i1 %71, label %72, label %77

; <label>:72:                                     ; preds = %69
  %73 = load i32, i32* %2, align 4
  %74 = load i32*, i32** %9, align 8
  %75 = load i32**, i32*** %6, align 8
  %76 = call i32* @_Z4fun1iPiPS_(i32 %73, i32* %74, i32** %75)
  store i32* %76, i32** %11, align 8
  br label %83

; <label>:77:                                     ; preds = %69
  %78 = load i32, i32* %3, align 4
  %79 = load i32*, i32** %10, align 8
  %80 = load i32**, i32*** %8, align 8
  %81 = load i32*, i32** %11, align 8
  %82 = call i32** @_Z4fun2iPiPS_S_(i32 %78, i32* %79, i32** %80, i32* %81)
  store i32** %82, i32*** %6, align 8
  br label %83

; <label>:83:                                     ; preds = %77, %72
  %84 = load i32, i32* %4, align 4
  %85 = load i32*, i32** %9, align 8
  call void @_Z4fun3iPi(i32 %84, i32* %85)
  %86 = load i32, i32* %4, align 4
  %87 = icmp ne i32 %86, 1
  br i1 %87, label %88, label %145

; <label>:88:                                     ; preds = %83
  %89 = load i32*, i32** %9, align 8
  %90 = getelementptr inbounds %struct.PointerCase, %struct.PointerCase* %14, i32 0, i32 0
  store i32* %89, i32** %90, align 8
  %91 = getelementptr inbounds %struct.PointerCase, %struct.PointerCase* %14, i32 0, i32 1
  %92 = load i32*, i32** %91, align 8
  store i32* %92, i32** %10, align 8
  %93 = load i32*, i32** %11, align 8
  %94 = getelementptr inbounds %struct.PointerCase, %struct.PointerCase* %14, i32 0, i32 2
  %95 = load i32**, i32*** %94, align 8
  store i32* %93, i32** %95, align 8
  %96 = getelementptr inbounds %struct.PointerCase, %struct.PointerCase* %14, i32 0, i32 3
  %97 = load i32**, i32*** %96, align 8
  %98 = load i32*, i32** %97, align 8
  store i32* %98, i32** %10, align 8
  %99 = load i32, i32* %2, align 4
  %100 = icmp sgt i32 %99, 0
  br i1 %100, label %101, label %121

; <label>:101:                                    ; preds = %88
  %102 = getelementptr inbounds [10 x i32], [10 x i32]* %12, i64 0, i64 2
  store i32* %102, i32** %11, align 8
  store i32 0, i32* %15, align 4
  br label %103

; <label>:103:                                    ; preds = %117, %101
  %104 = load i32, i32* %15, align 4
  %105 = icmp slt i32 %104, 10
  br i1 %105, label %106, label %120

; <label>:106:                                    ; preds = %103
  store i32 0, i32* %16, align 4
  br label %107

; <label>:107:                                    ; preds = %113, %106
  %108 = load i32, i32* %16, align 4
  %109 = icmp slt i32 %108, 10
  br i1 %109, label %110, label %116

; <label>:110:                                    ; preds = %107
  %111 = load i32, i32* %2, align 4
  %112 = load i32*, i32** %11, align 8
  call void @_Z4fun3iPi(i32 %111, i32* %112)
  br label %113

; <label>:113:                                    ; preds = %110
  %114 = load i32, i32* %16, align 4
  %115 = add nsw i32 %114, 1
  store i32 %115, i32* %16, align 4
  br label %107

; <label>:116:                                    ; preds = %107
  br label %117

; <label>:117:                                    ; preds = %116
  %118 = load i32, i32* %15, align 4
  %119 = add nsw i32 %118, 1
  store i32 %119, i32* %15, align 4
  br label %103

; <label>:120:                                    ; preds = %103
  br label %144

; <label>:121:                                    ; preds = %88
  %122 = load i32*, i32** %11, align 8
  %123 = getelementptr inbounds [10 x i32*], [10 x i32*]* %13, i64 0, i64 2
  store i32* %122, i32** %123, align 16
  %124 = getelementptr inbounds %struct.PointerCase, %struct.PointerCase* %14, i32 0, i32 1
  %125 = load i32*, i32** %124, align 8
  %126 = getelementptr inbounds [10 x i32*], [10 x i32*]* %13, i64 0, i64 1
  store i32* %125, i32** %126, align 8
  %127 = getelementptr inbounds [10 x i32*], [10 x i32*]* %13, i64 0, i64 5
  %128 = getelementptr inbounds %struct.PointerCase, %struct.PointerCase* %14, i32 0, i32 2
  store i32** %127, i32*** %128, align 8
  %129 = getelementptr inbounds [10 x i32*], [10 x i32*]* %13, i64 0, i64 6
  %130 = load i32*, i32** %129, align 16
  %131 = getelementptr inbounds %struct.PointerCase, %struct.PointerCase* %14, i32 0, i32 3
  %132 = load i32**, i32*** %131, align 8
  store i32* %130, i32** %132, align 8
  %133 = getelementptr inbounds %struct.PointerCase, %struct.PointerCase* %14, i32 0, i32 3
  %134 = load i32**, i32*** %133, align 8
  %135 = load i32*, i32** %134, align 8
  %136 = getelementptr inbounds [10 x i32*], [10 x i32*]* %13, i64 0, i64 7
  store i32* %135, i32** %136, align 8
  %137 = getelementptr inbounds [10 x i32*], [10 x i32*]* %13, i64 0, i64 1
  store i32** %137, i32*** %7, align 8
  %138 = load i32**, i32*** %7, align 8
  %139 = load i32*, i32** %138, align 8
  %140 = getelementptr inbounds [10 x i32*], [10 x i32*]* %13, i64 0, i64 3
  store i32* %139, i32** %140, align 8
  %141 = getelementptr inbounds [10 x i32*], [10 x i32*]* %13, i64 0, i64 4
  %142 = load i32*, i32** %141, align 16
  %143 = load i32**, i32*** %6, align 8
  store i32* %142, i32** %143, align 8
  br label %144

; <label>:144:                                    ; preds = %121, %120
  br label %154

; <label>:145:                                    ; preds = %83
  %146 = getelementptr inbounds %struct.PointerCase, %struct.PointerCase* %14, i32 0, i32 3
  store i32** %9, i32*** %146, align 8
  %147 = getelementptr inbounds %struct.PointerCase, %struct.PointerCase* %14, i32 0, i32 0
  store i32** %147, i32*** %7, align 8
  %148 = getelementptr inbounds %struct.PointerCase, %struct.PointerCase* %14, i32 0, i32 1
  %149 = load i32*, i32** %148, align 8
  %150 = load i32**, i32*** %6, align 8
  store i32* %149, i32** %150, align 8
  %151 = load i32**, i32*** %7, align 8
  %152 = load i32*, i32** %151, align 8
  %153 = getelementptr inbounds %struct.PointerCase, %struct.PointerCase* %14, i32 0, i32 0
  store i32* %152, i32** %153, align 8
  br label %154

; <label>:154:                                    ; preds = %145, %144
  br label %155

; <label>:155:                                    ; preds = %179, %154
  %156 = load i32, i32* %2, align 4
  %157 = icmp sgt i32 %156, 0
  br i1 %157, label %158, label %180

; <label>:158:                                    ; preds = %155
  %159 = getelementptr inbounds [10 x i32*], [10 x i32*]* %13, i64 0, i64 0
  %160 = load i32*, i32** %159, align 16
  store i32* %160, i32** %9, align 8
  %161 = getelementptr inbounds [10 x i32*], [10 x i32*]* %13, i64 0, i64 1
  %162 = load i32*, i32** %161, align 8
  %163 = getelementptr inbounds %struct.PointerCase, %struct.PointerCase* %14, i32 0, i32 0
  store i32* %162, i32** %163, align 8
  %164 = load i32, i32* %2, align 4
  %165 = add nsw i32 %164, -1
  store i32 %165, i32* %2, align 4
  %166 = load i32, i32* %3, align 4
  %167 = icmp sgt i32 %166, 0
  br i1 %167, label %168, label %175

; <label>:168:                                    ; preds = %158
  %169 = load i32*, i32** %9, align 8
  %170 = load i32**, i32*** %6, align 8
  store i32* %169, i32** %170, align 8
  %171 = load i32**, i32*** %6, align 8
  %172 = load i32*, i32** %171, align 8
  store i32* %172, i32** %10, align 8
  store i32** %10, i32*** %8, align 8
  %173 = load i32*, i32** %11, align 8
  %174 = load i32**, i32*** %7, align 8
  store i32* %173, i32** %174, align 8
  br label %179

; <label>:175:                                    ; preds = %158
  %176 = load i32*, i32** %11, align 8
  %177 = load i32**, i32*** %8, align 8
  store i32* %176, i32** %177, align 8
  %178 = load i32*, i32** %10, align 8
  store i32* %178, i32** %9, align 8
  store i32* %3, i32** %11, align 8
  br label %179

; <label>:179:                                    ; preds = %175, %168
  br label %155

; <label>:180:                                    ; preds = %155
  %181 = call noalias i8* @malloc(i64 40) #4
  %182 = bitcast i8* %181 to i32*
  store i32* %182, i32** %17, align 8
  %183 = call i8* @_Znam(i64 40) #5
  %184 = bitcast i8* %183 to i32*
  store i32* %184, i32** %18, align 8
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
