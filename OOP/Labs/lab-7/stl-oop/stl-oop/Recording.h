#pragma once

#include <string>
#include <iostream>
#include <sstream>


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
	Recording operator=(const Recording& rec);
	// copy constructor
	Recording(const Recording& rec);

	std::string getTitle() const { return title; }
	std::string getLocation() const { return location; }
	std::string getTimeOfCreation() const { return timeOfCreation; }
	int getTimesAccessed() const { return timesAccessed; }
	std::string getFootagePreview() const { return footagePreview; }

	void setTitle(std::string& title);
	void setLocation(std::string& location);
	void setTimeOfCreation(std::string& timeOfCreation);
	void setTimesAccessed(int timesAccessed);
	void setFootagePreview(std::string& footagePreview);

	bool operator==(const Recording& recording) const;

	std::string toString();

	friend std::istream & operator >> (std::istream & stream, Recording & recording);
	friend std::ostream & operator << (std::ostream & stream, const Recording & recording);

private:

	//void deleteWhiteSpacesBeginningAndEnd(std::string& stringToCompute);
};

