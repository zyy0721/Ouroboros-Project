#include<stdio.h>
int main()
{
    int **e,**f,**q;
    int *g,*h,*p;

    e =f;
    *e = g;
    h = *e;
    q = &h;
    *f = p;
    *q = p;
    g = h;
    return 0;
}