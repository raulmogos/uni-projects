#define _CRTDBG_MAPALLOC

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