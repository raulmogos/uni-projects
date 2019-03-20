#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv)
{
	int maxValue = 0, lastFibonaciNumber = 0, beforeLastFibonaciNumber = 1, beforeBeforeLastFibonaciNumber = 0, sumOfFibonaciEvenNumbers = 0;

	printf("n= ");scanf_s("%d", &maxValue);

	lastFibonaciNumber = beforeLastFibonaciNumber + beforeBeforeLastFibonaciNumber;

	while (lastFibonaciNumber <= maxValue)
	{
		if (lastFibonaciNumber % 2 == 0) // if last is even
			sumOfFibonaciEvenNumbers = sumOfFibonaciEvenNumbers + lastFibonaciNumber;

		beforeBeforeLastFibonaciNumber = beforeLastFibonaciNumber;
		beforeLastFibonaciNumber = lastFibonaciNumber;
		lastFibonaciNumber = beforeLastFibonaciNumber + beforeBeforeLastFibonaciNumber;
	}

	printf("%d", sumOfFibonaciEvenNumbers);

	return 0;
}