#include<stdio.h>
#include<malloc.h>
int *globalA;
int **globalB;

int *fun1(int n, int *ptr, int **pptr)
{
    globalA = ptr;
    pptr = globalB;
    *globalB = ptr;
    pptr = &globalA;
    globalA = *globalB;

    return globalA;
}

int **fun2(int n, int *ptr, int **pptr, int *ptr1)
{
    if(n>0)
    {
        globalA = &n;
        *pptr = ptr;
        ptr1 = *pptr;
        ptr = ptr1;
        return pptr;
    }
    else
    {
        globalB = &ptr1;
        ptr = &n;
        *globalB = ptr;
        ptr1 = *pptr;
        return globalB;
    }
}

void fun3(int n, int *ptr)
{
    ptr = &n;
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
    int ***s;
    int ****t;

    int ArrayTmp[10];
    int *PointerArray[10];
    int *PointerDouleArray[10][10];
    struct PointerCase pointerCase;

    a = 1;
    b = 2;
    c = 3;
    d = a + b + c;
    d = a - b;
    c = d * a;
    b = c + 1;
    e = f;
    globalA = *e;
    if(b > 0)
    {
        *e = g;
        h = *e;
        q = &h;
        *f = p;
        p = ***t;
        f = *s;
        e = **t;
    }
    else
    {
        *q = p;
        g = h;
        p = &b;
    }

    while (a != 0)
    {
        h = *q;
        g = p;
    }
    
    if (d > 0)
    {
        p = fun1(a,g,e);
    }
    else
    {
        e = fun2(b,h,q,p);
    }
    fun3(c,g);
    if (c != 1)
    {
        pointerCase.a = g;
        h = pointerCase.b;
        *pointerCase.d = p;
        h = *pointerCase.e;
        if (a > 0)
        {
            p = &ArrayTmp[2];
            for ( int i = 0; i < 10; i++)
            {
                g = PointerArray[i];
                for (int j = 0; j < 10; j++)
                {
                    p = PointerDouleArray[i][j];
                }
                
                PointerDouleArray[i][1] = &a;
                PointerDouleArray[i][2] = p;
                *e = PointerDouleArray[i][3];
                PointerDouleArray[i][3] = *f;
            }
            
        }
        else
        {
            PointerArray[2] = p;
            PointerArray[1] = pointerCase.b;
            f = &PointerArray[1];
            PointerArray[3] = *f;
            *e = PointerArray[4];
        }
        
    }
    else
    {
        pointerCase.e = &g;
        f = &pointerCase.a;
        *e = pointerCase.b;
        pointerCase.a = *f;
    }

    while (a > 0)
    {
        /* code */
        g = PointerArray[0];
        pointerCase.a = PointerArray[1];
        a--;
        if(b > 0)
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
        
    }

    int *newP;
    newP = (int *)malloc(sizeof(int)*10);
    int *newP1;
    newP1 = new int[10];

    return 0;
    
    
    
}

