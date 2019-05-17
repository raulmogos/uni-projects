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


int Controller::getSize() const
{
	return this->repositoryRecordings.getSize();
}

DynamicArray<Entity> Controller::listOfEntities()
{
	return  this->repositoryRecordings.getListOfData();
}


bool Controller::saveToMyList(const std::string & title)
{
	DynamicArray<Entity> array = this->repositoryRecordings.getListOfData();
	Entity emptyEntity { title, "", "", -1, "" };

	for (int i=0; i< this->repositoryRecordings.getSize(); i++)
		if (emptyEntity == array[i])
		{
			this->myList.add(array[i]);
			return true;
		}
	return false;
}

DynamicArray<Entity> Controller::getMyList()
{
	DynamicArray<Entity> listToReturn{};
	for (int i = 0;i < this->myList.getSize(); i++)
		listToReturn.add(this->myList[i]);
	return listToReturn;
}


//-----------------------------------------------------------------------------------------------


DynamicArray<Entity>::iterator Controller::nextRecording()
{
	return this->repositoryRecordings.next();
}

// filtering 

DynamicArray<Entity> Controller::filterRepositoryByLocationAndTimesAccessed(const std::string locationToFilterBy, std::string timesAccessed)
{

	DynamicArray<Entity> vector;

	DynamicArray<Entity> vectorToReturn;

	int times_Accessed = std::stoi(timesAccessed);

	for (int i = 0;i < this->repositoryRecordings.getSize(); i++)
		vector.add(this->repositoryRecordings.getListOfData()[i]);

	for (int i = 0;i < this->repositoryRecordings.getSize();i++)
	{
		std::string stringLocation = vector[i].getLocation();
		if (vector[i].getTimesAccessed() < times_Accessed && strcmp(stringLocation.c_str(), locationToFilterBy.c_str()) == 0)
		{
			vectorToReturn.add(vector[i]);
		}
	}

	return vectorToReturn;
}


