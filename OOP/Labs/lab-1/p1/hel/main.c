#include <stdio.h>
#include <stdlib.h>

int main()
{
    char line[10003];

    scanf("%[^\n]", line);

    printf(line);

    return 0;
}
