#pragma once

#include "Repository.h"
#include "FileRepository.h"

typedef Recording Entity;



class Controller
{
	private:

		FileRepository repositoryRecordings;
		
		// list saved recordings
		std::vector<Entity> myList;

	public:

		Controller (const FileRepository &repository);
		~Controller();

		// repo functions
		void addRecording(Entity recording);
		void updateRecording(Entity recording);

		bool addRecording(const std::string& title, const std::string& location, const std::string& timeOfCreation, const std::string& timesAccessed, const std::string& footagePreview);
		bool removeRecording(const std::string& title);
		bool updateRecording(const std::string& title, const std::string& location, const std::string& timeOfCreation, const std::string& timesAccessed, const std::string& footagePreview);


		int getSize() const;
		std::vector<Entity> listOfEntities() ;
		
		// next 
		std::vector<Entity>::iterator nextRecording();
		// addToMylist
		bool saveToMyList(const std::string& title);
		//bool next();
		std::vector<Entity> getMyList();
		// recordings for a given location having the number of times accessed smaller than 
		// the second given amount.  --- > filter
		std::vector<Entity> filterRepositoryByLocationAndTimesAccessed(const std::string location, std::string timesAccessed);

		void setFileNameForRepository(const std::string fileNameToSet);
};

