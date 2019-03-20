#pragma once

#include "domain.h"



typedef struct repository
{
	int length;
	int capacity;
	bot ** bots;
}repository;

repository * initiateRepository();

void add(repository * repositoryOfBots, bot * botToAdd);
void delete(repository * repositoryOfBots, char * serialNumber);
void update(repository * repositoryOfBots, bot * botToUpdate);

void destroyRepository(repository * repositoryOfElements);



typedef struct repositoryOperations
{
	int length;
	int index;
	operation * operations[200];
}repositoryOperations;

repositoryOperations * initiateRepositoryOperations();

void addOpeartion(repositoryOperations * repositoryOfOperations, operation * operationToAdd);
void deleteLastOperation(repositoryOperations * repositoryOfOperations);

void destroyRepositoryOperations(repositoryOperations * repositoryOfOperations);