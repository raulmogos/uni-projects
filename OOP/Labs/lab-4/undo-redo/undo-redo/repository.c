
#include "repository.h"
#include "domain.h"
#include <stdlib.h>
#include <stdio.h>
#include <string.h>


void resize(repository * repositoryOfItems);


repository * initiateRepository()
{
	repository * repositoryOfBots;

	// allocate space for the repository
	repositoryOfBots = (repository*)malloc(sizeof(repository)*1);

	// initiate the length 
	repositoryOfBots->length = 0;

	// initiate the capacity
	repositoryOfBots->capacity = 3;

	// allocate space for the for the bots array
	repositoryOfBots->bots = (bot**)malloc(sizeof(bot*)*repositoryOfBots->capacity);

	// return a pointer to the repositoryOfEntities
	return repositoryOfBots;
}

void add(repository * repositoryOfBots, bot * botToAdd)
{
	// the botToAdd has already a memory allocated 
	if (repositoryOfBots->length == repositoryOfBots->capacity - 1)
	{
		// resize
		resize(repositoryOfBots);
	}
	// we put the pointer bot into the dynamic array
	repositoryOfBots->bots[repositoryOfBots->length] = botToAdd;
	// we increase the length
	repositoryOfBots->length++;
}

void delete(repository * repositoryOfBots, char* serialNumber)
{
	for(int index =0; index<repositoryOfBots->length; index++)
		if (strcmp(repositoryOfBots->bots[index]->serialNumber, serialNumber)==0)
		{
			// we daclocate the memory
			destroyBot(repositoryOfBots->bots[index]);
			while (index < repositoryOfBots->length)
			{
				repositoryOfBots->bots[index] = repositoryOfBots->bots[index + 1];
				index++;
			}
			break;
		}
	// we decrease the length
	repositoryOfBots->length--;
}

void update(repository * repositoryOfBots, bot * botToUpdate)
{
	for (int index = 0; index < repositoryOfBots->length; index++)
		if (strcmp(repositoryOfBots->bots[index]->serialNumber, botToUpdate->serialNumber)== 0)
		{
			// we overwrite the bot
			destroyBot(repositoryOfBots->bots[index]);
			repositoryOfBots->bots[index] = botToUpdate;
			break;
		}
}

void resize(repository * repositoryOfItems)
{
	//printf("%s","memory increased\n");
	// we increase the capacity of the repository 
	repositoryOfItems->capacity = repositoryOfItems->capacity * 2;

	// we allocate new, bigger space for the repository->bots
	bot ** pointerToNewMemory = (bot **)malloc(sizeof(bot*) * repositoryOfItems->capacity);
	
	// we copy the old elements into the new memory
	for (int index = 0; index < repositoryOfItems->length; index++)
	{
		// copy the pointers
		//*(pointerToNewMemory + index) = *(repositoryOfItems->bots + index);
		pointerToNewMemory[index] = repositoryOfItems->bots[index];
	}

	// we free the memory of the old ones
	free(repositoryOfItems->bots);

	// no update the vector with the new memory
	repositoryOfItems->bots = pointerToNewMemory;
}

void destroyRepository(repository * repositoryOfElements)
{
	if (repositoryOfElements == NULL)
		return;
	
	for (int index = 0; index < repositoryOfElements->length; index++)
	{
		//printf("bot destroy rp\n");
		destroyBot(repositoryOfElements->bots[index]);
	}
	free(repositoryOfElements->bots);
	//repositoryOfElements->bots = NULL;
	free(repositoryOfElements);
}

//void destroyOnlyRepository(repository * repositoryOfElements)
//{
//	// here we destory only the array and not the bots
//	free(repositoryOfElements->bots);
//	free(repositoryOfElements);
//}



repositoryOperations * initiateRepositoryOperations()
{
	repositoryOperations * repositoryOfOperations;
	repositoryOfOperations = (repositoryOperations *)malloc(sizeof(repositoryOperations));
	repositoryOfOperations->length = 0;
	repositoryOfOperations->index = -1;
	return repositoryOfOperations;
}

void addOpeartion(repositoryOperations * repositoryOfOperations, operation * operationToAdd)
{
	if (repositoryOfOperations->index < repositoryOfOperations->length - 1)
		for (int index = repositoryOfOperations->index + 1; index < repositoryOfOperations->length; index++)
		{
			printf("delete operatinon at index %d\n", index);
			destroyOperation(repositoryOfOperations->operations[index]);
		}
	if (repositoryOfOperations->index == -1)
	{
		repositoryOfOperations->length = 1;
		repositoryOfOperations->index = 0;
		repositoryOfOperations->operations[0] = operationToAdd;
	}
	else
	{
		repositoryOfOperations->length = repositoryOfOperations->index + 2;
		repositoryOfOperations->operations[repositoryOfOperations->index + 1] = operationToAdd;
		repositoryOfOperations->index++;	
	}
}


void destroyRepositoryOperations(repositoryOperations * repositoryOfOperations)
{
	if (repositoryOfOperations == NULL)
		return;
	for (int index = 0;index < repositoryOfOperations->length; index++) 
	{
		// printf("operation destroy rp\n");
		destroyOperation(repositoryOfOperations->operations[index]);
	}
	free(repositoryOfOperations);
}