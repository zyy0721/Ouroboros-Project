#include<stdio.h>

int *global;

void fun1(int *ptr)
{
    global = ptr;
}
void fun2(int **ptr)
{
    *ptr = global;
}

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
    global=*e;
    if(b>0)
    {
        *e = g;
        h = *e;
        q = &h;//h is address taken
        *f = p;
    }
    else
    {
        *q = p;
        g = h;
        p = &b;//b is address taken
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
            p = &d;//d is address taken
            break;
        case 2:
            a = d + (c - 1)*2;
            p = &a;//a is address taken addressTaken
            break;
            
        default:
            break;
    }

    if(d>0)
    {
        fun1(h);
    }
    else
    {
        fun2(e);
    }
    


    return 0;
}