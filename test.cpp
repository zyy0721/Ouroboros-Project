#include <stdio.h>

int main()
{
	
	int**a ,**b,**c,**d,**e,**f;
	int*g,*h,*p;
	
	a=b;
	c=a;
	e=c;
	a=d;
	e=f;
	*e=g;
	h=*e;
	*e=p;

	printf("Hello World!");
	return 0;
}
