; ModuleID = 'testCase6.cpp'
source_filename = "testCase6.cpp"
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
  %14 = alloca [10 x [10 x i32*]], align 16
  %15 = alloca %struct.PointerCase, align 8
  %16 = alloca i32, align 4
  %17 = alloca i32, align 4
  %18 = alloca i32*, align 8
  %19 = alloca i32*, align 8
  store i32 0, i32* %1, align 4
  store i32 1, i32* %2, align 4
  store i32 2, i32* %3, align 4
  store i32 3, i32* %4, align 4
  %20 = load i32, i32* %2, align 4
  %21 = load i32, i32* %3, align 4
  %22 = add nsw i32 %20, %21
  %23 = load i32, i32* %4, align 4
  %24 = add nsw i32 %22, %23
  store i32 %24, i32* %5, align 4
  %25 = load i32, i32* %2, align 4
  %26 = load i32, i32* %3, align 4
  %27 = sub nsw i32 %25, %26
  store i32 %27, i32* %5, align 4
  %28 = load i32, i32* %5, align 4
  %29 = load i32, i32* %2, align 4
  %30 = mul nsw i32 %28, %29
  store i32 %30, i32* %4, align 4
  %31 = load i32, i32* %4, align 4
  %32 = add nsw i32 %31, 1
  store i32 %32, i32* %3, align 4
  %33 = load i32**, i32*** %7, align 8
  store i32** %33, i32*** %6, align 8
  %34 = load i32**, i32*** %6, align 8
  %35 = load i32*, i32** %34, align 8
  store i32* %35, i32** @globalA, align 8
  %36 = load i32, i32* %3, align 4
  %37 = icmp sgt i32 %36, 0
  br i1 %37, label %38, label %45

; <label>:38:                                     ; preds = %0
  %39 = load i32*, i32** %9, align 8
  %40 = load i32**, i32*** %6, align 8
  store i32* %39, i32** %40, align 8
  %41 = load i32**, i32*** %6, align 8
  %42 = load i32*, i32** %41, align 8
  store i32* %42, i32** %10, align 8
  store i32** %10, i32*** %8, align 8
  %43 = load i32*, i32** %11, align 8
  %44 = load i32**, i32*** %7, align 8
  store i32* %43, i32** %44, align 8
  br label %49

; <label>:45:                                     ; preds = %0
  %46 = load i32*, i32** %11, align 8
  %47 = load i32**, i32*** %8, align 8
  store i32* %46, i32** %47, align 8
  %48 = load i32*, i32** %10, align 8
  store i32* %48, i32** %9, align 8
  store i32* %3, i32** %11, align 8
  br label %49

; <label>:49:                                     ; preds = %45, %38
  br label %50

; <label>:50:                                     ; preds = %53, %49
  %51 = load i32, i32* %2, align 4
  %52 = icmp ne i32 %51, 0
  br i1 %52, label %53, label %57

; <label>:53:                                     ; preds = %50
  %54 = load i32**, i32*** %8, align 8
  %55 = load i32*, i32** %54, align 8
  store i32* %55, i32** %10, align 8
  %56 = load i32*, i32** %11, align 8
  store i32* %56, i32** %9, align 8
  br label %50

; <label>:57:                                     ; preds = %50
  %58 = load i32, i32* %4, align 4
  switch i32 %58, label %69 [
    i32 1, label %59
    i32 2, label %63
  ]

; <label>:59:                                     ; preds = %57
  %60 = load i32, i32* %2, align 4
  %61 = load i32, i32* %4, align 4
  %62 = add nsw i32 %60, %61
  store i32 %62, i32* %5, align 4
  store i32* %5, i32** %11, align 8
  br label %70

; <label>:63:                                     ; preds = %57
  %64 = load i32, i32* %5, align 4
  %65 = load i32, i32* %4, align 4
  %66 = sub nsw i32 %65, 1
  %67 = mul nsw i32 %66, 2
  %68 = add nsw i32 %64, %67
  store i32 %68, i32* %2, align 4
  store i32* %2, i32** %11, align 8
  br label %70

; <label>:69:                                     ; preds = %57
  br label %70

; <label>:70:                                     ; preds = %69, %63, %59
  %71 = load i32, i32* %5, align 4
  %72 = icmp sgt i32 %71, 0
  br i1 %72, label %73, label %78

; <label>:73:                                     ; preds = %70
  %74 = load i32, i32* %2, align 4
  %75 = load i32*, i32** %9, align 8
  %76 = load i32**, i32*** %6, align 8
  %77 = call i32* @_Z4fun1iPiPS_(i32 %74, i32* %75, i32** %76)
  store i32* %77, i32** %11, align 8
  br label %84

; <label>:78:                                     ; preds = %70
  %79 = load i32, i32* %3, align 4
  %80 = load i32*, i32** %10, align 8
  %81 = load i32**, i32*** %8, align 8
  %82 = load i32*, i32** %11, align 8
  %83 = call i32** @_Z4fun2iPiPS_S_(i32 %79, i32* %80, i32** %81, i32* %82)
  store i32** %83, i32*** %6, align 8
  br label %84

; <label>:84:                                     ; preds = %78, %73
  %85 = load i32, i32* %4, align 4
  %86 = load i32*, i32** %9, align 8
  call void @_Z4fun3iPi(i32 %85, i32* %86)
  %87 = load i32, i32* %4, align 4
  %88 = icmp ne i32 %87, 1
  br i1 %88, label %89, label %162

; <label>:89:                                     ; preds = %84
  %90 = load i32*, i32** %9, align 8
  %91 = getelementptr inbounds %struct.PointerCase, %struct.PointerCase* %15, i32 0, i32 0
  store i32* %90, i32** %91, align 8
  %92 = getelementptr inbounds %struct.PointerCase, %struct.PointerCase* %15, i32 0, i32 1
  %93 = load i32*, i32** %92, align 8
  store i32* %93, i32** %10, align 8
  %94 = load i32*, i32** %11, align 8
  %95 = getelementptr inbounds %struct.PointerCase, %struct.PointerCase* %15, i32 0, i32 2
  %96 = load i32**, i32*** %95, align 8
  store i32* %94, i32** %96, align 8
  %97 = getelementptr inbounds %struct.PointerCase, %struct.PointerCase* %15, i32 0, i32 3
  %98 = load i32**, i32*** %97, align 8
  %99 = load i32*, i32** %98, align 8
  store i32* %99, i32** %10, align 8
  %100 = load i32, i32* %2, align 4
  %101 = icmp sgt i32 %100, 0
  br i1 %101, label %102, label %148

; <label>:102:                                    ; preds = %89
  %103 = getelementptr inbounds [10 x i32], [10 x i32]* %12, i64 0, i64 2
  store i32* %103, i32** %11, align 8
  store i32 0, i32* %16, align 4
  br label %104

; <label>:104:                                    ; preds = %144, %102
  %105 = load i32, i32* %16, align 4
  %106 = icmp slt i32 %105, 10
  br i1 %106, label %107, label %147

; <label>:107:                                    ; preds = %104
  store i32 0, i32* %17, align 4
  br label %108

; <label>:108:                                    ; preds = %119, %107
  %109 = load i32, i32* %17, align 4
  %110 = icmp slt i32 %109, 10
  br i1 %110, label %111, label %122

; <label>:111:                                    ; preds = %108
  %112 = load i32, i32* %16, align 4
  %113 = sext i32 %112 to i64
  %114 = getelementptr inbounds [10 x [10 x i32*]], [10 x [10 x i32*]]* %14, i64 0, i64 %113
  %115 = load i32, i32* %17, align 4
  %116 = sext i32 %115 to i64
  %117 = getelementptr inbounds [10 x i32*], [10 x i32*]* %114, i64 0, i64 %116
  %118 = load i32*, i32** %117, align 8
  store i32* %118, i32** %11, align 8
  br label %119

; <label>:119:                                    ; preds = %111
  %120 = load i32, i32* %17, align 4
  %121 = add nsw i32 %120, 1
  store i32 %121, i32* %17, align 4
  br label %108

; <label>:122:                                    ; preds = %108
  %123 = load i32, i32* %16, align 4
  %124 = sext i32 %123 to i64
  %125 = getelementptr inbounds [10 x [10 x i32*]], [10 x [10 x i32*]]* %14, i64 0, i64 %124
  %126 = getelementptr inbounds [10 x i32*], [10 x i32*]* %125, i64 0, i64 1
  store i32* %2, i32** %126, align 8
  %127 = load i32*, i32** %11, align 8
  %128 = load i32, i32* %16, align 4
  %129 = sext i32 %128 to i64
  %130 = getelementptr inbounds [10 x [10 x i32*]], [10 x [10 x i32*]]* %14, i64 0, i64 %129
  %131 = getelementptr inbounds [10 x i32*], [10 x i32*]* %130, i64 0, i64 2
  store i32* %127, i32** %131, align 16
  %132 = load i32, i32* %16, align 4
  %133 = sext i32 %132 to i64
  %134 = getelementptr inbounds [10 x [10 x i32*]], [10 x [10 x i32*]]* %14, i64 0, i64 %133
  %135 = getelementptr inbounds [10 x i32*], [10 x i32*]* %134, i64 0, i64 3
  %136 = load i32*, i32** %135, align 8
  %137 = load i32**, i32*** %6, align 8
  store i32* %136, i32** %137, align 8
  %138 = load i32**, i32*** %7, align 8
  %139 = load i32*, i32** %138, align 8
  %140 = load i32, i32* %16, align 4
  %141 = sext i32 %140 to i64
  %142 = getelementptr inbounds [10 x [10 x i32*]], [10 x [10 x i32*]]* %14, i64 0, i64 %141
  %143 = getelementptr inbounds [10 x i32*], [10 x i32*]* %142, i64 0, i64 3
  store i32* %139, i32** %143, align 8
  br label %144

; <label>:144:                                    ; preds = %122
  %145 = load i32, i32* %16, align 4
  %146 = add nsw i32 %145, 1
  store i32 %146, i32* %16, align 4
  br label %104

; <label>:147:                                    ; preds = %104
  br label %161

; <label>:148:                                    ; preds = %89
  %149 = load i32*, i32** %11, align 8
  %150 = getelementptr inbounds [10 x i32*], [10 x i32*]* %13, i64 0, i64 2
  store i32* %149, i32** %150, align 16
  %151 = getelementptr inbounds %struct.PointerCase, %struct.PointerCase* %15, i32 0, i32 1
  %152 = load i32*, i32** %151, align 8
  %153 = getelementptr inbounds [10 x i32*], [10 x i32*]* %13, i64 0, i64 1
  store i32* %152, i32** %153, align 8
  %154 = getelementptr inbounds [10 x i32*], [10 x i32*]* %13, i64 0, i64 1
  store i32** %154, i32*** %7, align 8
  %155 = load i32**, i32*** %7, align 8
  %156 = load i32*, i32** %155, align 8
  %157 = getelementptr inbounds [10 x i32*], [10 x i32*]* %13, i64 0, i64 3
  store i32* %156, i32** %157, align 8
  %158 = getelementptr inbounds [10 x i32*], [10 x i32*]* %13, i64 0, i64 4
  %159 = load i32*, i32** %158, align 16
  %160 = load i32**, i32*** %6, align 8
  store i32* %159, i32** %160, align 8
  br label %161

; <label>:161:                                    ; preds = %148, %147
  br label %171

; <label>:162:                                    ; preds = %84
  %163 = getelementptr inbounds %struct.PointerCase, %struct.PointerCase* %15, i32 0, i32 3
  store i32** %9, i32*** %163, align 8
  %164 = getelementptr inbounds %struct.PointerCase, %struct.PointerCase* %15, i32 0, i32 0
  store i32** %164, i32*** %7, align 8
  %165 = getelementptr inbounds %struct.PointerCase, %struct.PointerCase* %15, i32 0, i32 1
  %166 = load i32*, i32** %165, align 8
  %167 = load i32**, i32*** %6, align 8
  store i32* %166, i32** %167, align 8
  %168 = load i32**, i32*** %7, align 8
  %169 = load i32*, i32** %168, align 8
  %170 = getelementptr inbounds %struct.PointerCase, %struct.PointerCase* %15, i32 0, i32 0
  store i32* %169, i32** %170, align 8
  br label %171

; <label>:171:                                    ; preds = %162, %161
  br label %172

; <label>:172:                                    ; preds = %196, %171
  %173 = load i32, i32* %2, align 4
  %174 = icmp sgt i32 %173, 0
  br i1 %174, label %175, label %197

; <label>:175:                                    ; preds = %172
  %176 = getelementptr inbounds [10 x i32*], [10 x i32*]* %13, i64 0, i64 0
  %177 = load i32*, i32** %176, align 16
  store i32* %177, i32** %9, align 8
  %178 = getelementptr inbounds [10 x i32*], [10 x i32*]* %13, i64 0, i64 1
  %179 = load i32*, i32** %178, align 8
  %180 = getelementptr inbounds %struct.PointerCase, %struct.PointerCase* %15, i32 0, i32 0
  store i32* %179, i32** %180, align 8
  %181 = load i32, i32* %2, align 4
  %182 = add nsw i32 %181, -1
  store i32 %182, i32* %2, align 4
  %183 = load i32, i32* %3, align 4
  %184 = icmp sgt i32 %183, 0
  br i1 %184, label %185, label %192

; <label>:185:                                    ; preds = %175
  %186 = load i32*, i32** %9, align 8
  %187 = load i32**, i32*** %6, align 8
  store i32* %186, i32** %187, align 8
  %188 = load i32**, i32*** %6, align 8
  %189 = load i32*, i32** %188, align 8
  store i32* %189, i32** %10, align 8
  store i32** %10, i32*** %8, align 8
  %190 = load i32*, i32** %11, align 8
  %191 = load i32**, i32*** %7, align 8
  store i32* %190, i32** %191, align 8
  br label %196

; <label>:192:                                    ; preds = %175
  %193 = load i32*, i32** %11, align 8
  %194 = load i32**, i32*** %8, align 8
  store i32* %193, i32** %194, align 8
  %195 = load i32*, i32** %10, align 8
  store i32* %195, i32** %9, align 8
  store i32* %3, i32** %11, align 8
  br label %196

; <label>:196:                                    ; preds = %192, %185
  br label %172

; <label>:197:                                    ; preds = %172
  %198 = call noalias i8* @malloc(i64 40) #4
  %199 = bitcast i8* %198 to i32*
  store i32* %199, i32** %18, align 8
  %200 = call i8* @_Znam(i64 40) #5
  %201 = bitcast i8* %200 to i32*
  store i32* %201, i32** %19, align 8
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
