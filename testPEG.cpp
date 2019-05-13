#include<stdio.h>
int main()
{
    int **e,**f,**q;
    int *g,*h,*p;
    int a;

    e =f;
    *e = g;
    h = *e;
    q = &h;
    *f = p;
    *q = p;
    g = h;
    a = 1;
    p = &a;
    return 0;
}