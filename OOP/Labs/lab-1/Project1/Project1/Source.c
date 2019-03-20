#include <stdio.h>
#include <stdlib.h>
#include <conio.h>

int main()
{
	printf("Hello, OPP!\n");
	printf("Enter a string :\n");

	char input_string[51];

	gets(input_string);

	printf("%s", input_string);
	
	//_getch();
	return 0;
}