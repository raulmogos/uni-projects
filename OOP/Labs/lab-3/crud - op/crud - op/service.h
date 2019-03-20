#pragma once

#include <string.h>

#include "repository.h"


int addBot(bot botToAdd)
{
	for(int index=0; index<botRepository.lengthOfTheList;index++)
		if (strcmp(botToAdd.serialNumber, botRepository.bots[index].serialNumber)==0)
		{
			return -1;
		}
	botRepository.lengthOfTheList++;
	botRepository.bots[botRepository.lengthOfTheList-1] = botToAdd;
	return 1;
}

int updateBot(bot botToUpdate)
{
	for (int index = 0; index < botRepository.lengthOfTheList; index++)
	{
		if (strcmp(botRepository.bots[index].serialNumber, botToUpdate.serialNumber)==0)
		{
			botRepository.bots[index] = botToUpdate;
			return 1;
		}
	}
	return -1;
}

int deleteBot(char *serialNumber)
{
	/*function that removes a bot from the list*/
	
	for (int index = 0; index < botRepository.lengthOfTheList; index++)
	{
		if (strcmp( botRepository.bots[index].serialNumber, serialNumber)==0)
		{
			// now we overwrite
			while (index <= botRepository.lengthOfTheList)
			{
				botRepository.bots[index] = botRepository.bots[index + 1];
				index++;
			}
			botRepository.lengthOfTheList--;
			return 1;
		}
	}
	return -1;
}