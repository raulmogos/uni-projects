#define _CRTDBG_MAP_ALLOC

#include <assert.h>
#include <iostream>
#include <crtdbg.h>
#include "Repository.h"
#include "Controller.h"
#include "UI.h"
#include "Recording.h"
#include <string>


#include <ctype.h>


int main()
{
	system("mode con:cols=170 lines=30");
	system("color a");
	

	system("CLS");
	{

		Repository repository{};
		Controller ctrl{ repository };
		UI ui{ ctrl };

		ui.run();
	}
	
	
	_CrtDumpMemoryLeaks();
	//system("pause");
	return 0;
}