#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#pragma once
#include "service.h"


void printABot(bot botToPrint)
{
	/*function that prints a bot on the screen*/

	printf("serial number: %10s  ", botToPrint.serialNumber);
	printf("state: %10s  ", botToPrint.state);
	printf("specialization: %10s  ", botToPrint.specialization);
	printf("energy cost to repair: %10d  ", botToPrint.energyCostToRepair);
	printf("\n");
}

bot convertDataToBot(char *serialNumber, char *state, char *specialization, char *energyCostToRepair)
{
	/*function that converts data to a bot type*/

	bot botToReturn;

	strcpy( botToReturn.serialNumber, serialNumber);
	strcpy( botToReturn.state, state);
	strcpy( botToReturn.specialization, specialization);
	botToReturn.energyCostToRepair = atoi(energyCostToRepair);

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

void printString(char *string)
{
	printf("%s", string);
}

void listAllBots()
{
	if (botRepository.lengthOfTheList == 0)
	{
		printString("There are no bots.\n");
	}
	else
		for (int index = 0; index < botRepository.lengthOfTheList; index++)
		{
			printABot(botRepository.bots[index]);
		}
}

void printAListOfBotsWithTheSameSpecialization(char * specialization)
{
	for (int index = 0; index < botRepository.lengthOfTheList; index++)
		if (strcmp(specialization, botRepository.bots[index].specialization) == 0)
		{
			printABot(botRepository.bots[index]);
		}
}

void runUI()
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
	while ( strcmp(input_commands, "")==0 )
	{
		printf(">> ");

		// read from the console command line
		fgets(input_commands, 204, stdin);
		// we delete the '\n' from the input string
		input_commands[strlen(input_commands) - 1] = '\0';

		// here we compute the list of commands and the number of words
		computeInput(input_commands, listOfCommands, &numberOfCommands);

		// test the first command
		if (strcmp(listOfCommands[0], "add") == 0)
		{
			if (numberOfCommands != 5)
			{
				printString("invalid parameters!\n");
				printString("add serialNumber state specialization energyCostToRepair\n");
			}
			else
			{
				//add a bot
				bot botToAdd = convertDataToBot(listOfCommands[1], listOfCommands[2], listOfCommands[3], listOfCommands[4]);
				int message = addBot(botToAdd);
				if (message == 1)
				{
					printString("You've added successfully\n");
				}
				else
				{
					printString("serial number error\n");
				}
			}
		}
		else if (strcmp(listOfCommands[0], "delete") == 0 || strcmp(listOfCommands[0], "remove") == 0)
		{
			if (numberOfCommands != 2)
			{
				printString("invalid parameters!\n");
				printString("delete serialNumber\n");
			}
			else
			{
				int message = deleteBot(listOfCommands[1]);
				if (1 == message)
				{
					printString("You've deleted successfully\n");
				}
				else
				{
					printString("invalid serial number \n");
				}
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
				bot botToUpdate = convertDataToBot(listOfCommands[1], listOfCommands[2], listOfCommands[3], listOfCommands[4]);
				int returnMessage = updateBot(botToUpdate);

				if (returnMessage == 1)
				{
					printString("You've updated successfully\n");
				}
				else
				{
					printString("Ivalid serial number\n");
				}
			}
		}
		else if (strcmp(listOfCommands[0], "list") == 0)
		{
			if (numberOfCommands == 1)
			{
				listAllBots();
				//printString("Listed successfully!\n");
			}
			else if (numberOfCommands == 2)
			{
				printAListOfBotsWithTheSameSpecialization(listOfCommands[1]);
			}
			else
			{
				printString("Command 'list' has no parameters or has too many! \n");
			}
		}
		else if (strcmp(listOfCommands[0], "exit") == 0)
		{
			if (numberOfCommands != 1)
			{
				printString("Command 'exit' has no parameters!\n");
			}
			else
			{
				printString("You've exited successfully\n");
				break;
			}
		}
		else // this is for invalid commands
		{
			printString("Invalid command!\n");
			printString("Commands available: 'add', 'delete', 'update', 'list', 'exit'. \n");
		}
		
		// update the input commands so that the while loop goes on
		strcpy(input_commands, "");
	}
	// free
	for (int i = 0;i < 50;i++)
		free(listOfCommands[i]);
	free(listOfCommands);
}
