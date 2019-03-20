#pragma once

typedef struct bot
{
	char * serialNumber;
	char * state;
	char * specialization;
	int * energyCostToRepair;
}bot;

bot * createBot(char * serialNumber, char * state, char * specialization, int energyCostToRepair);
void destroyBot(bot * botToDestroy);

bot * deepCopyBot(bot * botToCopy);


typedef struct operation
{
	char * operationName;
	bot * dataBot;
}operation;

operation * createOperation(char * operationName, bot * dataBot);
void destroyOperation(operation * operationToDestroy);