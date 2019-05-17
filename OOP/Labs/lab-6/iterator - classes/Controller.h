#pragma once

#include "Repository.h"

typedef Recording Entity;



class Controller
{
	private:

		Repository repositoryRecordings;

		// list saved recordings
		DynamicArray<Entity> myList;
		// iterator for myList;

	public:

		Controller (const Repository &repository);
		~Controller();

		// repo functions
		bool addRecording(const std::string& title, const std::string& location, const std::string& timeOfCreation, const std::string& timesAccessed, const std::string& footagePreview);
		bool removeRecording(const std::string& title);
		bool updateRecording(const std::string& title, const std::string& location, const std::string& timeOfCreation, const std::string& timesAccessed, const std::string& footagePreview);


		int getSize() const;
		DynamicArray<Entity> listOfEntities() ;
		
		// next 
		DynamicArray<Entity>::iterator nextRecording();
		// addToMylist
		bool saveToMyList(const std::string& title);
		//bool next();
		DynamicArray<Entity> getMyList();
		// recordings for a given location having the number of times accessed smaller than 
		// the second given amount.  --- > filter
		DynamicArray<Entity> filterRepositoryByLocationAndTimesAccessed(const std::string location, std::string timesAccessed);
};

