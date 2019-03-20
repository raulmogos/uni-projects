#include "domain.h"
#include "repository.h"


int addBot(repositoryOperations* repositoryOfOperations, repository * repositoryOfBots, bot * botToAdd);
int deleteBot(repositoryOperations* repositoryOfOperations, repository * repositoryOfBots, char * serialNumber);
int updateBot(repositoryOperations* repositoryOfOperations, repository * repositoryOfBots, bot * botToUpdate);

repository * filterBySpecialization(repository * repositoryOfBots, char * specialization);

int undo(repositoryOperations* repositoryOfOperations, repository * repositoryOfBots);
int redo(repositoryOperations* repositoryOfOperations, repository * repositoryOfBots);

void exitApplication(repository * repositoryOfBots, repositoryOperations* repositoryOfOperations);