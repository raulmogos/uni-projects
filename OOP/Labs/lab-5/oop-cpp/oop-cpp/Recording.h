#pragma once

#include <string>


class Recording
{
private:

	std::string title; 
	std::string location;
	std::string timeOfCreation;
	int  timesAccessed;
	std::string footagePreview;

public:
	Recording();
	Recording(const std::string& title, const std::string& location, const std::string& timeOfCreation, const int timesAccessed, const std::string& footagePreview);
	// desctructor 
	~Recording();
	// asigment operatot
	//Recording operator=(const Recording& rec);
	//// copy constructor
	//Recording(const Recording& rec);

	std::string getTitle() const { return this->title; }
	std::string getLocation() const { return this->location; }
	std::string getTimeOfCreation() const { return this->timeOfCreation; }
	int getTimesAccessed() const { return this->timesAccessed; }
	std::string getFootagePreview() const { return this->footagePreview; }

	void setTitle(std::string& title);
	void setLocation(std::string& location);
	void setTimeOfCreation(std::string& timeOfCreation);
	void setTimesAccessed(int timesAccessed);
	void setFootagePreview(std::string& footagePreview);

	bool operator==(const Recording& recording) const;

	std::string toString();
};

