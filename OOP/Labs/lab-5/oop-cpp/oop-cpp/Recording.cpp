#pragma once
#include "Recording.h"
#include <string.h>


Recording::Recording() : title(""), location(""), timeOfCreation(""),  timesAccessed(-1), footagePreview("") {}

Recording::Recording(const std::string&  title, const std::string& location, const std::string& timeOfCreation, const int timesAccessed, const std::string& footagePreview)
{
	this->title = title;
	this->location = location;
	this->timeOfCreation = timeOfCreation;
	this->timesAccessed = timesAccessed;
	this->footagePreview = footagePreview;
}

Recording::~Recording() {}



void Recording::setTitle(std::string& title)
{
	this->title = title;
}
void Recording::setLocation(std::string& location) 
{
	this->location = location;
}
void Recording::setTimeOfCreation(std::string& timeOfCreation)
{
	this->timeOfCreation = timeOfCreation;
}
void Recording::setTimesAccessed(int timesAccessed)
{
	this->timesAccessed = timesAccessed;
}
void Recording::setFootagePreview(std::string& footagePreview)
{
	this->footagePreview = footagePreview;
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
