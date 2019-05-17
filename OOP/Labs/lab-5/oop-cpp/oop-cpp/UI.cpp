#include "UI.h"
#include "Controller.h"

#include <iostream>
#include <sstream>
#include <string>

// constructor + destructor

UI::UI(const Controller &controller) : controller(controller) {}

UI::~UI() {}


// menus

void UI::printMenuUser()
{
	std::cout << " menu B: \n";
	std::cout << " next \n";
	std::cout << " save title(eg.save anomaly) \n";
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
	
	// + erase white spaces at end
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
/*
	std::cout << title <<'-';
	std::cout << location << '-';
	std::cout << timeOfCreation << '-';
	std::cout << timesAccessed << '-';
	std::cout << footagePreview << '-';*/
	
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
	std::cout << this->controller.dataToString() << '\n';
}


// user functions 

void UI::nextUi()
{

}

void UI::saveUi()
{
	
}

void UI::filterUserUi()
{

}

void UI::listUserModeUi()
{

}


// run modes

void UI::runModeAdministrator()
{
	system("cls");
	this->printMenuAdministrator();

	std::string firstCommand;
	
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
		else if (firstCommand == "exit")
			break;
	}

}

void UI::runModeUser()
{
	system("cls");
	this->printMenuUser();

	std::string firstCommand;

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
		else if (firstCommand == "exit")
			break;
	}
}


// main run

void UI::run()
{
	std::string mode;

	while ( true )
	{
		std::cout << "choose a mode [A/B] \n";
		std::cout << "\n MODE: ";
		std::cin >> mode;
		std::cout <<"mode "<< mode;
		if (mode == "A" || mode == "B" || mode == "a" || mode == "b")
			break;
		else if (mode == "exit")
			return;
	}

	if (mode == "A" || mode == "a")
		this->runModeAdministrator();
	else if (mode == "B" || mode == "b")
		this->runModeUser();
}