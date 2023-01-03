#include <stdio.h>
int main() {
	int num1, num2 ;
	scanf("%d %d", &num1, &num2);
	if ((num1 > 0) && (num2 > 0))
	{
		printf("1\n");
	}
	else if ((num1 < 0) && (num2 > 0))
	{
		printf("2\n");
	}
	else if ((num1 < 0) && (num2 < 0))
	{
		printf("3\n");
	}
	else {
		printf("4\n");
		return 0;
	}
}