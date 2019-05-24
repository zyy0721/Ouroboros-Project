#include<stdio.h>
int main()
{
	int *a,*b;
	*a = *b;
	int **e,**f;
	*e = *f;
	**e = **f;
}
