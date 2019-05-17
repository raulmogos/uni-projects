#pragma once

#include "Repository.h"
#include <algorithm>



Repository::Repository(){}

Repository::~Repository() {}



bool Repository::add(const Entity& element)
{
	auto found = std::find(this->array.begin(), this->array.end(), element);

	if (found != this->array.end())
	{
		return false;
	}

	this->array.push_back(element);
	this->iteratorForRepository = this->array.begin();
	return true;
}

bool Repository::remove(const Entity& element)
{
	auto found = std::find(this->array.begin(), this->array.end(), element);

	if (found != this->array.end())
	{
		this->array.erase(found);
		this->iteratorForRepository = this->array.begin();
		return true;
	}
	return false;
}

bool Repository::update(const Entity& element)
{
	auto found = std::find(this->array.begin(), this->array.end(), element);

	if (found != this->array.end())
	{
		std::replace(this->array.begin(), this->array.end(), element, element);
		this->iteratorForRepository = this->array.begin();
		return true;
	}
	return false;
}

int Repository::getSize() const
{
	return this->array.size();
}

std::vector<Entity>  Repository::getListOfData()
{
	std::vector<Entity> vector(this->array);
	return vector;
}

std::vector<Entity>::iterator Repository::next()
{
	std::vector<Entity>::iterator v;

	if (this->iteratorForRepository == this->array.end())
	{
		this->iteratorForRepository = this->array.begin();
		this->iteratorForRepository++;
		return this->array.begin();
	}
	else if (this->iteratorForRepository == this->array.begin())
	{
		this->iteratorForRepository = this->array.begin() + 1;
		return this->array.begin();
	}
	else if (this->iteratorForRepository != this->array.end())
		this->iteratorForRepository++;

	v = this->iteratorForRepository - 1;
	return v;
}
