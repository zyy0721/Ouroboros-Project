#include<stdio.h>
#include<malloc.h>
int *globalA;
int **globalB;
void fun1(int n, int *ptr, int **pptr)
{
    globalA = ptr;
    pptr = globalB;
    *globalB = ptr;
    pptr = &globalA;
    globalA=*globalB;
}
void fun2(int n, int *ptr, int **pptr, int *ptr1)
{
    if(n>0)
    {
        globalA = &n;
        *pptr = ptr;
        ptr1 = *pptr;
        ptr = ptr1;
    }
    else
    {
        globalB = &ptr1;
        ptr = &n;
        *globalB = ptr;
        ptr1 = *pptr;
    }
    
}

struct PointerCase
{
    int *a,*b;
    int **d,**e;
    int g;

};

int main()
{
    int a,b,c,d;
    int **e,**f,**q;
    int *g,*h,*p;
    
    int ArrayTmp[10];
    int *PointerArray[10];
    struct PointerCase pointerCase;

    a=1;
    b=2;
    c=3;
    d = a+b+c;
    d = a -b;
    c= d*a;
    b = c+1;
    e =f;
    globalA=*e;
    if(b>0)
    {
        *e = g;
        h = *e;
        q = &h;
        *f = p;
    }
    else
    {
        *q = p;
        g = h;
        p = &b;
    }

    while(a!=0)
    {
        h = *q;
        g = p;
    }

    switch (c)
    {
        case 1:
            d = a + c;
            p = &d;
            break;
        case 2:
            a = d + (c - 1)*2;
            p = &a;
            break;
            
        default:
            break;
    }

    if(d>0)
    {
        fun1(a,g,e);
    }
    else
    {
        fun2(b,h,q,p);
    }
    
    if(c != 1)
    {
        pointerCase.a = g;
        h = pointerCase.b;
        *pointerCase.d = p;
        h = *pointerCase.e;

        
    }
    else
    {
        pointerCase.e = & g;
        f = &pointerCase.a;
        *e = pointerCase.b;
        pointerCase.a = *f;
    }
    
    while(a>0)
    {
        g = PointerArray[0];
        pointerCase.a = PointerArray[1];
        a--;
    }

    int * newP;
    newP = (int *)malloc(sizeof(int)*10);
    int *newPP;
    newPP = new int[10];

    return 0;
}