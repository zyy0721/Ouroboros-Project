#include<stdio.h>

struct PointerCase
{
    int *a,*b;
    int **d,**e;
    int g;

};


int main()
{
    int *aa,*bb;
    int **dd,**ee;
    int gg;
    int ArrayTmp[10];
    int *PointerArray[10];
    struct PointerCase pointerCase;
    gg = 1;
    pointerCase.a = aa;
    pointerCase.d = ee;
    bb = pointerCase.a;
    *pointerCase.d = bb;
    pointerCase.e = & aa;
    dd = &pointerCase.a;
    *ee = pointerCase.b;
    bb = *pointerCase.e;
    pointerCase.a = *dd;
    if(gg != 0)
    {
        gg = ArrayTmp[0];
        aa = PointerArray[0];
        bb = PointerArray[1];
    }
    else
    {
        int i = 2;
        gg = ArrayTmp[i];
        aa = PointerArray[i];
    }
    


    return 0;
}