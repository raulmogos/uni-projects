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

void UI::deleteWhiteSpacesFromBeginning(std::string& string)
{
	while (string[0] == ' ')
		for (unsigned int i = 0; i < string.size(); i++)
			string[i] = string[i+1];
	
	// TODO: and erase white spaces at end
}

void UI::dump(std::string s)
{
	for (unsigned int n = 0; n < s.length(); ++n)
	{
		char c = s[n];
		std::cout << (char)c << ",";
	}
	std::cout << std::endl;

}

// administrator functions

void UI::addUi()
{
	//LABEL:

	std::string title, location, timeOfCreation, timesAccessed, footagePreview;

	std::getline(std::cin, title, ',');
	std::getline(std::cin, location, ',');
	std::getline(std::cin, timeOfCreation, ',');
	std::getline(std::cin, timesAccessed, ',');
	std::getline(std::cin, footagePreview, '\n');
	

	this->deleteWhiteSpacesFromBeginning(title);
	this->deleteWhiteSpacesFromBeginning(location);
	this->deleteWhiteSpacesFromBeginning(timeOfCreation);
	this->deleteWhiteSpacesFromBeginning(timesAccessed);
	this->deleteWhiteSpacesFromBeginning(footagePreview);
	
	if (!isdigit(timesAccessed[0]))
		return;

	bool response = this->controller.addRecording(title, location, timeOfCreation, timesAccessed, footagePreview);

	if (response == true)
		std::cout << "added succesfully \n";
	else
		std::cout << "add -- something went wrong\n";
}

void UI::removeUi()
{
	std::string title;
	std::getline(std::cin, title, '\n');
	if (title == "")
		return;
	
	this->deleteWhiteSpacesFromBeginning(title);

	bool response = this->controller.removeRecording(title);

	if (response == true)
		std::cout << "removed succesfully \n";
	else
		std::cout << "remove -- something went wrong\n";
}

void UI::updateUi()
{
	std::string title, location, timeOfCreation, timesAccessed, footagePreview;

	std::getline(std::cin, title, ',');
	std::getline(std::cin, location, ',');
	std::getline(std::cin, timeOfCreation, ',');
	std::getline(std::cin, timesAccessed, ',');
	std::getline(std::cin, footagePreview, '\n');

	this->deleteWhiteSpacesFromBeginning(title);
	this->deleteWhiteSpacesFromBeginning(location);
	this->deleteWhiteSpacesFromBeginning(timeOfCreation);
	this->deleteWhiteSpacesFromBeginning(timesAccessed);
	this->deleteWhiteSpacesFromBeginning(footagePreview);

	std::cout << timesAccessed[0] << std::endl;
	if (!isdigit(timesAccessed[0]))
		return;

	bool response = this->controller.updateRecording(title, location, timeOfCreation, timesAccessed, footagePreview);
	
	if (response == true)
		std::cout << "updated succesfully \n";
	else
		std::cout << "update -- something went wrong\n";
}

void UI::listUi()
{
	DynamicArray<Entity> vectorToList = this->controller.listOfEntities();
	for (int i = 0; i < this->controller.getSize(); i++)
		std::cout << vectorToList[i].toString();
}


// user functions 

void UI::nextUi()
{
	Entity v = *this->controller.nextRecording();
	std::cout << v.toString();
}

void UI::saveUi()
{
	std::string title;
	std::getline(std::cin, title, '\n');
	if (title == "")
		return;

	this->deleteWhiteSpacesFromBeginning(title);

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
	this->deleteWhiteSpacesFromBeginning(location);
	this->deleteWhiteSpacesFromBeginning(timesAccessed);

	//filter
	DynamicArray<Entity> vector = this->controller.filterRepositoryByLocationAndTimesAccessed(location, timesAccessed);

	for (int i = 0;i < vector.getSize(); i++)
		std::cout << vector[i].toString();
}

void UI::listUserModeUi()
{
	for (int i = 0; i < this->controller.getMyList().getSize(); i++)
		std::cout << this->controller.getMyList()[i].toString();
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