#pragma once

#include <iostream>

#include "Controller.h"

#include <algorithm>

#include "Exception.h"



Controller::Controller(const FileRepository &repository) : repositoryRecordings(repository) {}

Controller::~Controller() {}

void Controller::addRecording(Entity recording)
{
	bool response = this->repositoryRecordings.add(recording);
	if (response == false)
	{
		throw std::exception("existing recording");
	}
}

void Controller::updateRecording(Entity recording)
{
	bool response = this->repositoryRecordings.update(recording);
	if (response == false)
	{
		throw std::exception("inexisting recording");
	}
}


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

std::vector<Entity> Controller::listOfEntities()
{
	return  this->repositoryRecordings.getListOfData();
}



bool Controller::saveToMyList(const std::string & title)
{
	std::vector<Entity> vector = this->repositoryRecordings.getListOfData();
	std::string new_title(title.c_str());

	Entity ent { new_title, "", "", -1, "" };
	

	auto found = std::find(vector.begin(), vector.end(), ent);

	if (found != vector.end())
	{
		this->myList.push_back(*found);
		return true;
	}

	return false;
}

std::vector<Entity> Controller::getMyList()
{
	std::vector<Entity> listToReturn;

	listToReturn = this->myList;

	//for (auto i : this->myList)
	//	list.push_back(i);
	return listToReturn;
}


//-----------------------------------------------------------------------------------------------


std::vector<Entity>::iterator Controller::nextRecording()
{
	return this->repositoryRecordings.next();
}

// filtering 

std::vector<Entity> Controller::filterRepositoryByLocationAndTimesAccessed(const std::string locationToFilterBy, std::string timesAccessed)
{

	std::vector<Entity> vectorOfAllData = repositoryRecordings.getListOfData();

	std::vector<Entity> vectorToReturn(vectorOfAllData.size());

	int times_Accessed = std::stoi(timesAccessed);

	auto it = std::copy_if(vectorOfAllData.begin(), vectorOfAllData.end(), vectorToReturn.begin(), [times_Accessed, locationToFilterBy](Entity i) 
		{return (i.getTimesAccessed() < times_Accessed && strcmp(i.getLocation().c_str(), locationToFilterBy.c_str()) == 0);});

	vectorToReturn.resize(std::distance(vectorToReturn.begin(),it));

	return vectorToReturn;
}

void Controller::setFileNameForRepository(const std::string fileNameToSet)
{
	this->repositoryRecordings.setFileNameRepository(fileNameToSet);
	this->repositoryRecordings.readDataFromFile();
}


