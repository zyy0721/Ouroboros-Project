#include <stdio.h>

int main()
{
	int a = 3;
	int b = 0;
	int i = 0;
	for(;i<3;i++)
	{
		a = a + 3;
	}
	if(a < 10)
		a = a-2;
	else
		b = b +2;
	return 0;
}
