#include<stdio.h>

void fun(int a, int* b, int **c)
{
	a = 1;
	b = NULL;
	c = NULL;
}

int main()
{
	int *a,*b;
	*a = *b;
	int **e,**f;
	*e = *f;
	**e = **f;
	int aa;
	fun(aa,b,e);
}
