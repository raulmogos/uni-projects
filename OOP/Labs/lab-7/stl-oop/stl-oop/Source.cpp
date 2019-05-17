#define _CRTDBG_MAP_ALLOC

#include <assert.h>
#include <iostream>
#include <crtdbg.h>

#include "Repository.h"
#include "FileRepository.h"
#include "Controller.h"
#include "UI.h"
#include "Recording.h"

#include "Tests.h"

#include <ctype.h>


int main()
{

	//Tests::testAll();

	system("mode con:cols=170 lines=30");
	system("color a");
	system("CLS");


	


	{
		FileRepository repository{};
		Controller ctrl{ repository };
		UI ui{ ctrl };

		ui.run();
	}
	
	
	_CrtDumpMemoryLeaks();
	system("pause");
	return 0;
}