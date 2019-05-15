#include<stdio.h>
int main()
{
    int a,b,c,d;
    int **e,**f,**q;
    int *g,*h,*p;
    
    a=1;
    b=2;
    c=3;
    d = a+b+c;
    d = a -b;
    c= d*a;
    b = c+1;
    e =f;
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


    return 0;
}