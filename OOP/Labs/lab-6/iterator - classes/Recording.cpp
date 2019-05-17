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
	str = str + "\t" + this->title + " " + this->location + " " + this->timeOfCreation + " " + std::to_string(this->timesAccessed)  + " " +this->footagePreview + "\n";
	return str;
}
