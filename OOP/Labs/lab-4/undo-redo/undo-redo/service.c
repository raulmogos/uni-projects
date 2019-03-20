#include <string.h>

#include "domain.h"
#include "repository.h"
#include "service.h"

bot * searchBotBySerialNumber(repository * repositoryOfBots, char * serialNumber)
{
	// we search a bot by its serial number
	for (int index = 0; index < repositoryOfBots->length; index++)
	{
		if (strcmp(serialNumber, repositoryOfBots->bots[index]->serialNumber) == 0)
			return repositoryOfBots->bots[index]; // it is in the repository
	}
	// we return -1 if the bot is NOT in the repository
	//return -1; // it is not in the repository
}

int isBotInRepository(repository * repositoryOfBots, char * serialNumber)
{
	// we search a bot by its serial number
	for (int index = 0; index < repositoryOfBots->length; index++)
	{
		// we return 1 if the bot is in the repository
		if (strcmp(serialNumber, repositoryOfBots->bots[index]->serialNumber) == 0)
			return 1; // it is in the repository
	}
	// we return -1 if the bot is NOT in the repository
	return -1; // it is not in the repository
}

repository * filterByEnergyCostToRepairAndSortByState(repository * repositoryOfBots, int maximumEnergyCostToRepair)
{
	repository * repositoryNew = initiateRepository();
	for (int index = 0; index < repositoryOfBots->length; index++)
		if ( *(repositoryOfBots->bots[index]->energyCostToRepair) < maximumEnergyCostToRepair) {
			add(repositoryNew, deepCopyBot(repositoryOfBots->bots[index]));
		}

	// now we sort by state
	for(int index = 0; index< repositoryNew->length - 1; index++)
		for(int index2 = index+1; index2< repositoryNew->length; index2++)
			if (strcmp(repositoryNew->bots[index]->state, repositoryNew->bots[index2]->state) > 0)
			{
				bot * aux = repositoryNew->bots[index];
				repositoryNew->bots[index] = repositoryNew->bots[index2];
				repositoryNew->bots[index2] = aux;
			}

	return repositoryNew;
}

int addBot(repositoryOperations* repositoryOfOperations, repository * repositoryOfBots, bot * botToAdd)
{
	// verify if it is already in the repository
	if (isBotInRepository(repositoryOfBots, botToAdd->serialNumber) == 1)
		return -1;
	// we add it in the repository 
	add(repositoryOfBots, botToAdd);
	operation * op = createOperation("add", botToAdd);
	addOpeartion(repositoryOfOperations, op);
	return 1;
}

int deleteBot(repositoryOperations* repositoryOfOperations, repository * repositoryOfBots, char * serialNumber)
{
	// verify if it is already in the repository
	if (isBotInRepository(repositoryOfBots, serialNumber) == 1)
	{
		// we delete it
		for (int index=0; index<repositoryOfBots->length; index++)
			if (strcmp(serialNumber, repositoryOfBots->bots[index]->serialNumber) == 0)
			{
				// here we add the operatinon for undo-redo 
				operation * op = createOperation("delete", repositoryOfBots->bots[index]);
				addOpeartion(repositoryOfOperations, op);
				delete(repositoryOfBots, repositoryOfBots->bots[index]->serialNumber);
				return 1; // bot was deleted
			}
	}
	return -1; // the bot does not exist in the repository
}

int updateBot(repositoryOperations* repositoryOfOperations, repository * repositoryOfBots, bot * botToUpdate)
{
	// check if the bot is in repository
	if (isBotInRepository(repositoryOfBots, botToUpdate->serialNumber) == 1)
	{

		for (int index=0; index<repositoryOfBots->length; index++)
			if (strcmp(repositoryOfBots->bots[index]->serialNumber, botToUpdate->serialNumber) == 0)
			{
				// operation
				operation * op = createOperation("update", repositoryOfBots->bots[index]);
				addOpeartion(repositoryOfOperations, op);
				break;
			}

		update(repositoryOfBots, botToUpdate);
		return 1; // the bot was updated
	}
	else
		return -1; // the bot does not exist in the repository
}

repository * filterBySpecialization(repository * repositoryOfBots, char * specialization)
{
	repository * listBotsSameSpecialisation = initiateRepository();

	// we filter 
	for (int index=0; index<repositoryOfBots->length; index++)
		if (strcmp(repositoryOfBots->bots[index]->specialization, specialization) == 0)
		{
			// copy the pointer 
			bot * newBot = deepCopyBot(repositoryOfBots->bots[index]);
			add(listBotsSameSpecialisation, newBot);
		}
	return listBotsSameSpecialisation;
}

int undo(repositoryOperations* repositoryOfOperations, repository * repositoryOfBots)
{
	if (repositoryOfOperations->index == -1)
		return -1;

	if (strcmp(repositoryOfOperations->operations[repositoryOfOperations->index]->operationName, "add") == 0)
	{ 
		delete(repositoryOfBots, repositoryOfOperations->operations[repositoryOfOperations->index]->dataBot->serialNumber);
	}
	else if (strcmp(repositoryOfOperations->operations[repositoryOfOperations->index]->operationName, "delete") == 0)
	{
		add(repositoryOfBots, deepCopyBot(repositoryOfOperations->operations[repositoryOfOperations->index]->dataBot));
	}
	else if (strcmp(repositoryOfOperations->operations[repositoryOfOperations->index]->operationName, "update") == 0)
	{
		// here we interchange
		bot * botToChange = deepCopyBot(searchBotBySerialNumber(repositoryOfBots, repositoryOfOperations->operations[repositoryOfOperations->index]->dataBot->serialNumber));
		update(repositoryOfBots, deepCopyBot(repositoryOfOperations->operations[repositoryOfOperations->index]->dataBot));
		destroyBot(repositoryOfOperations->operations[repositoryOfOperations->index]->dataBot);
		repositoryOfOperations->operations[repositoryOfOperations->index]->dataBot = botToChange;
	}
	repositoryOfOperations->index--;
	return 1;
}

int redo(repositoryOperations* repositoryOfOperations, repository * repositoryOfBots)
{
	if (repositoryOfOperations->index == repositoryOfOperations->length - 1)
		return -1;
	if (strcmp(repositoryOfOperations->operations[repositoryOfOperations->index+1]->operationName, "add") == 0)
	{
		add(repositoryOfBots, deepCopyBot(repositoryOfOperations->operations[repositoryOfOperations->index+1]->dataBot));
	}
	else if (strcmp(repositoryOfOperations->operations[repositoryOfOperations->index+1]->operationName, "delete") == 0)
	{
		delete(repositoryOfBots, repositoryOfOperations->operations[repositoryOfOperations->index+1]->dataBot->serialNumber);
	}
	else if (strcmp(repositoryOfOperations->operations[repositoryOfOperations->index + 1]->operationName, "update") == 0)
	{
		// here we interchange
		bot * botToChange = deepCopyBot(searchBotBySerialNumber(repositoryOfBots, repositoryOfOperations->operations[repositoryOfOperations->index+1]->dataBot->serialNumber));
		update(repositoryOfBots, deepCopyBot(repositoryOfOperations->operations[repositoryOfOperations->index + 1]->dataBot));
		destroyBot(repositoryOfOperations->operations[repositoryOfOperations->index+1]->dataBot);
		repositoryOfOperations->operations[repositoryOfOperations->index+1]->dataBot = botToChange;
	}
	repositoryOfOperations->index++;
	return 1;
}

void exitApplication(repository * repositoryOfBots, repositoryOperations* repositoryOfOperations)
{
	//  we destroy the repository
	destroyRepository(repositoryOfBots);
	//_CrtDumpMemoryLeaks();
	// we destroy the undo redo repository
	destroyRepositoryOperations(repositoryOfOperations);
	//_CrtDumpMemoryLeaks();
}
