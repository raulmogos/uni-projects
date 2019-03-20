#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#pragma once
#include "service.h"
#include "domain.h"
#include "repository.h"
#include "service.h"

void printString(char *string)
{
	printf("%s\n", string);
}

void printABot(bot * botToPrint)
{
	/*function that prints a bot on the screen*/

	printf("serial number: %10s  ", botToPrint->serialNumber);
	printf("state: %10s  ", botToPrint->state);
	printf("specialization: %10s  ", botToPrint->specialization);
	printf("energy cost to repair: %10d  ", *(botToPrint->energyCostToRepair));
	printf("\n");
}

void printRepositoryOfBots(repository * repositoryOfBots)
{
	if (repositoryOfBots->length >= 1)
		for (int index = 0; index < repositoryOfBots->length; index++)
			printABot(repositoryOfBots->bots[index]);
	else
		printString("empty repository");

	//printf("length:    %5d \n", repositoryOfBots->length);
	//printf("capacity:  %5d \n", repositoryOfBots->capacity);
}

void printRepositoryOfOperations(repositoryOperations * repositoryOfOperations)
{
	for (int index = 0; index < repositoryOfOperations->length; index++)
	{
		printf("%s\n", repositoryOfOperations->operations[index]->operationName);
		printABot(repositoryOfOperations->operations[index]->dataBot);
	}
	printf("index:  %d\n", repositoryOfOperations->index);
	printf("length:  %d\n", repositoryOfOperations->length);
}


bot * convertDataToBot(char *serialNumber, char *state, char *specialization, char * energyCostToRepair)
{
	/*function that converts data to a bot type*/
	bot * botToReturn;
	// we convert str into int
	int numberenergyCostToRepair = atoi(energyCostToRepair);
	botToReturn = createBot(serialNumber, state, specialization, numberenergyCostToRepair);
	return botToReturn;
}

void computeInput(char *sentence, char **listOfWords, int *numberOfWords)
{
	char *word;

	int index = 0;

	word = strtok(sentence, " ,");
	while (word != NULL)
	{
		//printf("%s ", token);
		//printf("%d", index);
		strcpy(listOfWords[index], word);
		index++;
		word = strtok(NULL, " ,");
	}
	*numberOfWords = index;
	//printf("%d", index);
}



void runUI(repository * repositoryOfBots, repositoryOperations * repositoryOfOperations)
{
	char input_commands[204];
	char **listOfCommands;

	// alocate space 
	listOfCommands = (char**)malloc(sizeof(char*) * 50);
	for (int i = 0; i < 50; i++)
	{
		listOfCommands[i] = (char*)malloc(sizeof(char) * 50);
	}

	printf("Enter a command: \n");

	int numberOfCommands = 0;

	strcpy(input_commands, "");
	while (strcmp(input_commands, "") == 0)
	{
		printf(">> ");

		// read from the console command line
		fgets(input_commands, 204, stdin);
		// we delete the '\n' from the input string
		input_commands[strlen(input_commands) - 1] = '\0';
		// here we compute the list of commands and the number of words
		computeInput(input_commands, listOfCommands, &numberOfCommands);

		// test commands
		if (strcmp(listOfCommands[0], "add") == 0)
		{
			if (numberOfCommands != 5)
			{
				printString("invalid parameters!");
				printString("add serialNumber state specialization energyCostToRepair");
			}
			else
			{
				bot * botToAdd = convertDataToBot(listOfCommands[1], listOfCommands[2], listOfCommands[3], listOfCommands[4]);

				//add a bot
				int response = addBot(repositoryOfOperations, repositoryOfBots, botToAdd);

				if (response == 1)
					printString("added successfully");
				else
					printString("the bot is already in the repository");
			}
		}
		else if (strcmp(listOfCommands[0], "delete") == 0 || strcmp(listOfCommands[0], "remove") == 0)
		{
			if (numberOfCommands != 2)
			{
				printString("invalid parameters!");
				printString("delete <serialNumber>");
			}
			else
			{
				// delete a bot	
				int reponse = deleteBot(repositoryOfOperations, repositoryOfBots, listOfCommands[1]);
				
				if (reponse == 1)
					printString("bot removed successfully");
				else
					printString("the bot is not in the repository");
			}
		}
		else if (strcmp(listOfCommands[0], "update") == 0)
		{
			if (numberOfCommands != 5)
			{
				printString("invalid parameters!\n");
				printString("update serialNumber state specialization energyCostToRepair\n");
			}
			else
			{
				// update the bot 
				bot * botToUpdate = convertDataToBot(listOfCommands[1], listOfCommands[2], listOfCommands[3], listOfCommands[4]);
				int response = updateBot(repositoryOfOperations, repositoryOfBots, botToUpdate);
				if (response == 1)
					printString("updated successfully");
				else
					printString("invalid serial number"); 
			}
		}
		else if (strcmp(listOfCommands[0], "list") == 0)
		{
			if (numberOfCommands == 1)
				printRepositoryOfBots(repositoryOfBots);
			else if (numberOfCommands == 2)
			{
				if (atoi(listOfCommands[1])!=0)
				{
					// here we list
					printString("hei list");
					int maximumEnergyCostToRepair = atoi(listOfCommands[1]);
					printf("%d \n", maximumEnergyCostToRepair);
					repository * repositoryMaximumEnergyCostToRepair = filterByEnergyCostToRepairAndSortByState(repositoryOfBots, maximumEnergyCostToRepair);
					printRepositoryOfBots(repositoryMaximumEnergyCostToRepair);
					destroyRepository(repositoryMaximumEnergyCostToRepair);
				}
				else 
				{
					repository * repositoryBotsSameSpecialization = filterBySpecialization(repositoryOfBots, listOfCommands[1]);
					printRepositoryOfBots(repositoryBotsSameSpecialization);
					destroyRepository(repositoryBotsSameSpecialization);
				}
			}
			else
				printString("invalid command");
		}
		else if (strcmp(listOfCommands[0], "exit") == 0)
		{
			if (numberOfCommands != 1)
			{
				printString("Command 'exit' has no parameters!\n");
			}
			else
			{
				exitApplication(repositoryOfBots, repositoryOfOperations); 
				printString("You've exited successfully\n");
				break;
			}
		}
		else if (strcmp(listOfCommands[0], "undo") == 0)
		{
			int response = undo(repositoryOfOperations, repositoryOfBots);
			if (response == 1)
				printString("UNdoing correctly");
			else
				printString("No more undo's");
		}
		else if (strcmp(listOfCommands[0], "redo") == 0)
		{
			int response = redo(repositoryOfOperations, repositoryOfBots);
			if (response == 1)
				printString("REdoing correctly");
			else
				printString("No more redo's");
		}
		else // this is for invalid commands
		{
			printString("Invalid command!\n");
			printString("Commands available: 'add', 'delete', 'update', 'list', 'exit'. \n");
		}

		// update the input commands so that the while loop goes on
		strcpy(input_commands, "");

		
		/*printString("\n------list of bots -------\n");
		printRepositoryOfBots(repositoryOfBots);
		printString("\n------list of operations -------\n");
		printRepositoryOfOperations(repositoryOfOperations);*/
	}

	// free
	for (int i = 0;i < 50;i++)
		free(listOfCommands[i]);
	free(listOfCommands);
}
