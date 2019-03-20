#define _CRTDBG_MAP_ALLOC

#include <crtdbg.h>
#include <stdio.h>
#include <stdlib.h>

#include "domain.h"
#include "repository.h"
#include "ui.h"

int main()
{
	repositoryOperations * repositoryOfOperations = initiateRepositoryOperations();
	repository * repositoryOfBots = initiateRepository();

	runUI(repositoryOfBots, repositoryOfOperations);
	
	_CrtDumpMemoryLeaks();
	// system("pause");
	return 0;
}