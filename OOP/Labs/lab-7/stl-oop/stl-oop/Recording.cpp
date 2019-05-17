#pragma once

#include "Recording.h"
#include <string.h>


Recording::Recording() : title(""), location(""), timeOfCreation(""),  timesAccessed(-1), footagePreview("") {}

Recording::Recording(const std::string&  inputTitle, const std::string& InputLocation, const std::string& InputTimeOfCreation, const int InputTimesAccessed, const std::string& InputFootagePreview)
{
	this->title = inputTitle;
	this->location = InputLocation;
	this->timeOfCreation = InputTimeOfCreation;
	this->timesAccessed = InputTimesAccessed;
	this->footagePreview = InputFootagePreview;
}

 Recording::~Recording() {}

 Recording Recording::operator=(const Recording & rec)
 {
	 this->title = rec.title;
	 this->location = rec.location;
	 this->timesAccessed = rec.timesAccessed;
	 this->timeOfCreation = rec.timeOfCreation;
	 this->footagePreview = rec.footagePreview;
	 return *this;
 }

 Recording::Recording(const Recording & rec)
 {
	 this->title = rec.title;
	 this->location = rec.location;
	 this->timesAccessed = rec.timesAccessed;
	 this->timeOfCreation = rec.timeOfCreation;
	 this->footagePreview = rec.footagePreview;
 }



void Recording::setTitle(std::string& newTitle)
{
	title = newTitle;
}
void Recording::setLocation(std::string& newLocation) 
{
	location = newLocation;
}
void Recording::setTimeOfCreation(std::string& newTimeOfCreation)
{
	timeOfCreation = newTimeOfCreation;
}
void Recording::setTimesAccessed(int newTimesAccessed)
{
	timesAccessed = newTimesAccessed;
}
void Recording::setFootagePreview(std::string& newFootagePreview)
{
	footagePreview = newFootagePreview;
}

bool Recording::operator==(const Recording& recording) const
{
	return this->title == recording.title;
}

std::string Recording::toString()
{
	std::string str;
	str = str + this->title + " " + this->location + " " + this->timeOfCreation + " " + std::to_string(this->timesAccessed)  + " " +this->footagePreview + "\n";
	return str;
}


std::istream & operator>>(std::istream & stream, Recording & recording)
{
	std::string times_Accessed;
	std::getline(stream, recording.title, ',');
	while (recording.title[0] == ' ')
	{
		recording.title.erase(recording.title.begin());
	}

	while (recording.title.size()>0 && recording.title[recording.title.size() - 1] == ' ')
	{
		recording.title.erase(recording.title.size() - 1);
	}
	std::getline(stream, recording.location, ',');
	std::getline(stream, recording.timeOfCreation, ',');
	std::getline(stream, times_Accessed, ',');
	recording.timesAccessed = std::atoi(times_Accessed.c_str());
	std::getline(stream, recording.footagePreview, '\n');
	return stream;
}

std::ostream & operator<<(std::ostream & stream, const Recording & recording)
{
	stream << recording.title;
	stream << ",";
	stream << recording.location;
	stream << ",";
	stream << recording.timeOfCreation;
	stream << ",";
	stream << recording.timesAccessed;
	stream << ",";
	stream << recording.footagePreview;
	return stream;
}


// -------------------------------private ----------------------

//void Recording::deleteWhiteSpacesBeginningAndEnd(std::string & stringToCompute)
//{
//	while (stringToCompute[0] == ' ')
//	{
//		stringToCompute.erase(stringToCompute.begin());
//	}
//	while (stringToCompute[stringToCompute.size() - 1] == ' ')
//	{
//		stringToCompute.erase(stringToCompute.size() - 1);
//	}
//}
