#pragma once

#include "Controller.h"


Controller::Controller(const Repository &repository) : repositoryRecordings(repository) {}

Controller::~Controller() {}


bool Controller::addRecording(const std::string& title, const std::string& location, const std::string& timeOfCreation, const std::string& timesAccessed, const std::string& footagePreview)
{
	int times_Accessed = stoi(timesAccessed);
	// exception thrown
	Recording recording { title, location, timeOfCreation, times_Accessed, footagePreview };
	return this->repositoryRecordings.add(recording);
}

bool Controller::removeRecording(const std::string& title)
{
	Recording recording{ title, "", "", -1, ""};
	return this->repositoryRecordings.remove(recording);
}

bool Controller::updateRecording(const std::string& title, const std::string& location, const std::string& timeOfCreation, const std::string& timesAccessed, const std::string& footagePreview)
{
	int times_Accessed = stoi(timesAccessed);
	// handel exception
	Recording recording{ title, location, timeOfCreation, times_Accessed, footagePreview };
	return this->repositoryRecordings.update(recording);
}

std::string Controller::dataToString() 
{
	std::string string;

	string = this->repositoryRecordings.toString();

	return string;
}
