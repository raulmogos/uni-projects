#pragma once

#include "Repository.h"

class Controller
{
	private:

		Repository repositoryRecordings;

	public:

		Controller (const Repository &repository);
		~Controller();

		bool addRecording(const std::string& title, const std::string& location, const std::string& timeOfCreation, const std::string& timesAccessed, const std::string& footagePreview);
		bool removeRecording(const std::string& title);
		bool updateRecording(const std::string& title, const std::string& location, const std::string& timeOfCreation, const std::string& timesAccessed, const std::string& footagePreview);

		std::string dataToString() ;
};

