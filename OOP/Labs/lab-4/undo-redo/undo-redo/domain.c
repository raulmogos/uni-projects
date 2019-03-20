#include "domain.h"
#include <string.h>
#include <stdlib.h>


bot * createBot(char * serialNumber, char * state, char * specialization, int energyCostToRepair)
{
	bot * botToCreate;

	// we allocate space for the new created bot
	botToCreate = (bot*)malloc(sizeof(bot)*1);
	botToCreate->serialNumber = (char*)malloc(sizeof(char)*(strlen(serialNumber) + 1));
	botToCreate->state = (char*)malloc(sizeof(char)*(strlen(state)+1));
	botToCreate->specialization = (char*)malloc(sizeof(char)*(strlen(specialization)+1));
	botToCreate->energyCostToRepair = (int*)malloc(sizeof(int));

	// we give it the values
	strcpy(botToCreate->serialNumber, serialNumber);
	strcpy(botToCreate->state, state);
	strcpy(botToCreate->specialization, specialization);
	*(botToCreate->energyCostToRepair) = energyCostToRepair;

	return botToCreate;
}

void destroyBot(bot * botToDestroy)
{
	if (botToDestroy == NULL)
		return;
	// we deallocate the memory of the fields
	free(botToDestroy->serialNumber);
	free(botToDestroy->state);
	free(botToDestroy->specialization);
	free(botToDestroy->energyCostToRepair);
	// we deallocate the memory of the struct bot
	free(botToDestroy);
	//botToDestroy == NULL;
}

bot * deepCopyBot(bot * botToCopy)
{
	if (botToCopy == NULL)
		return NULL;

	bot * newBot = createBot(botToCopy->serialNumber, botToCopy->state, botToCopy->specialization, *(botToCopy->energyCostToRepair));
	return newBot;
}



operation * createOperation(char * operationName, bot * dataBot)
{
	operation * operationToCreate = (operation *)malloc(sizeof(operation));
	operationToCreate->operationName = (char*)malloc(sizeof(char)*(strlen(operationName) + 1));
	strcpy(operationToCreate->operationName, operationName);
	operationToCreate->dataBot = deepCopyBot(dataBot);
	return operationToCreate;
}

void destroyOperation(operation * operationToDestroy)
{
	if (operationToDestroy == NULL)
		return;
	free(operationToDestroy->operationName);
	destroyBot(operationToDestroy->dataBot);
	free(operationToDestroy);
}