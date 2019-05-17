#pragma once

#include "Controller.h"


class UI
{
private:

	Controller controller;

public:

	UI( const Controller &controller);
	void run();
	~UI();

private:

	void printMenuUser();
	void printMenuAdministrator();

	void addUi();
	void removeUi();
	void updateUi();
	void listUi();

	void nextUi();
	void saveUi();
	void filterUserUi();
	void listUserModeUi();

	void runModeAdministrator();
	void runModeUser();

	void deleteWhiteSpacesFromBeginning(std::string& string);
	void dump(std::string);
};

