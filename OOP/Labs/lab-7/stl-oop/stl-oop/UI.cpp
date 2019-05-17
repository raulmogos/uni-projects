#include "UI.h"
#include "Controller.h"

#include <iostream>
#include <sstream>
#include <string>
#include <algorithm>

// constructor + destructor

UI::UI(const Controller &controller) : controller(controller) {}

UI::~UI() {}


// menus

void UI::printMenuUser()
{
	std::cout << " menu B: \n";
	std::cout << " next \n";
 	std::cout << " list location, timesAccessed(list deck D sector X1423, 5) \n";
	std::cout << " mylist \n";
	std::cout << " exit \n";
	std::cout << " \n\n\n";
}

void UI::printMenuAdministrator()
{
	std::cout << " menu A: \n";
	std::cout << " add title, location, timeOfCreation, timesAccessed, footagePreview ";
	std::cout << " (eg. add anomaly, deck D sector X1423, 01-13-3248, 5, prev123.mp15) \n";
	std::cout << " update title, newLocation, newTimeOfCreation, newTimesAccessed, newFootagePreview ";
	std::cout << " (eg. update anomaly, deck E sector X1423, 01-14-3248, 14, prev124.mp15)\n";
	std::cout << " delete title (eg. delete anomaly) \n";
	std::cout << " list \n";
	std::cout << " exit \n";
	std::cout << " \n\n\n";
}


// helper functions

void UI::deleteWhiteSpacesBeginningAndEnd(std::string& stringToCompute)
{
	while (stringToCompute[0] == ' ')
	{
		stringToCompute.erase(stringToCompute.begin());
	}
	while (stringToCompute[stringToCompute.size()-1] == ' ')
	{
		stringToCompute.erase(stringToCompute.size()-1);
	}
}

// administrator functions

void UI::addUi()
{
	Recording rec;
	std::cin >> rec;

	try
	{
		this->controller.addRecording(rec);
	}
	catch (std::exception& error)
	{
		std::cout << error.what() << '\n';
	}
}

void UI::removeUi()
{
	std::string title;
	std::getline(std::cin, title, '\n');
	if (title == "")
		return;
	
	this->deleteWhiteSpacesBeginningAndEnd(title);

	bool response = this->controller.removeRecording(title);

	if (response == true)
		std::cout << "removed succesfully \n";
	else
		std::cout << "remove -- something went wrong\n";
}

void UI::updateUi()
{
	Recording recordingToUpdate;
	std::cin >> recordingToUpdate;

	try
	{
		this->controller.updateRecording(recordingToUpdate);
	}
	catch (std::exception& error)
	{
		std::cout << error.what() << '\n';
	}
}

void UI::listUi()
{
	for (auto entity : this->controller.listOfEntities())
		std::cout << entity << '\n';
}


// user functions 

void UI::nextUi()
{
	Entity currentEntity = *this->controller.nextRecording();
	std::cout << currentEntity;
}

void UI::saveUi()
{
	std::string title;
	std::getline(std::cin, title, '\n');
	if (title == "")
		return;

	this->deleteWhiteSpacesBeginningAndEnd(title);

	bool response = this->controller.saveToMyList(title);

	if (response == true)
		std::cout << "saved succesfully \n";
	else
		std::cout << "save -- something went wrong\n";
}

void UI::filterUserUi()
{
	std::string location, timesAccessed;
	std::getline(std::cin, location, ',');
	std::getline(std::cin, timesAccessed, '\n');
	// delete white spaces
	this->deleteWhiteSpacesBeginningAndEnd(location);
	this->deleteWhiteSpacesBeginningAndEnd(timesAccessed);

	//filter
	std::vector<Entity> filteredVector = this->controller.filterRepositoryByLocationAndTimesAccessed(location, timesAccessed);

	for (auto i : filteredVector)
		std::cout << i << '\n';
}

void UI::listUserModeUi()
{
	for (auto i : this->controller.getMyList())
		std::cout << i << '\n';
}


// run modes

void UI::runModeAdministrator()
{
	system("cls");
	this->printMenuAdministrator();

	std::string firstCommand;
	
	int switchMode = 0;

	while (true)
	{
		std::cout << "admin >> ";
		std::cin >> firstCommand;

		if (firstCommand == "add")
			this->addUi();
		else if (firstCommand == "update")
			this->updateUi();
		else if (firstCommand == "delete" || firstCommand == "remove")
			this->removeUi();
		else if (firstCommand == "list")
			this->listUi();
		else if (firstCommand == "mode")
		{
			switchMode = 1; break;
		}
		else if (firstCommand == "exit")
			return;
		else
		{
			std::cout << "invalid command! \n";
		}
	}

	if (switchMode == 1)
		this->runModeUser();
}

void UI::runModeUser()
{
	system("cls");
	this->printMenuUser();

	std::string firstCommand;

	int switchMode = 0;

	while (true)
	{
		std::cout << "user >> ";
		std::cin >> firstCommand;

		if (firstCommand == "next")
			this->nextUi();
		else if (firstCommand == "save")
			this->saveUi();
		else if (firstCommand == "list")
			this->filterUserUi();
		else if (firstCommand == "mylist")
			this->listUserModeUi();
		else if (firstCommand == "mode")
		{
			switchMode = 1; break;
		}
		else if (firstCommand == "exit")
			return ;
		else
		{
			std::cout << "invalid command! \n";
		}
	}

	if(switchMode==1)
		this->runModeAdministrator();
}


// main run

void UI::run()
{
	std::string InputMode;
	std::string fileLocation, command;

	while (true)
	{
		std::cout << "enter fileLocation \n"; 
		std::cout << ">> ";
		std::cin >> command;
		std::getline(std::cin,fileLocation, '\n');

		this->deleteWhiteSpacesBeginningAndEnd(fileLocation);

		std::cout <<"file Location selected: "<< fileLocation << "\n";
		
		if (command == "fileLocation")
		{
			// set the file name
			this->controller.setFileNameForRepository(fileLocation);
			break;
		}
		std::cout << "\n";
	}

	while ( true )
	{
		std::cout << "choose a mode [A/B] \n";
		std::cout << "\n MODE: ";
		std::cin >> InputMode;
		std::cout <<"mode "<< InputMode;
		if (InputMode == "A" || InputMode == "B" || InputMode == "a" || InputMode == "b")
			break;
		else if (InputMode == "exit")
			return;
	}

	if (InputMode == "A" || InputMode == "a")
		this->runModeAdministrator();
	else if (InputMode == "B" || InputMode == "b")
		this->runModeUser();
}