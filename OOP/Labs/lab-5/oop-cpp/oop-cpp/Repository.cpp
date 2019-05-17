#pragma once
#include "Repository.h"

Repository::Repository()
{
}

Repository::~Repository()
{
}

bool Repository::add(const TElement& element)
{
	for (int i=0; i<this->array.getSize(); i++)
		if(element==this->array[i])
			return false;
	this->array.add(element);
	return true;
}

bool Repository::remove(const TElement& element)
{
	for(int i=0;i<this->array.getSize(); i++)
		if (element == this->array[i])
		{
			this->array.deleteFromPosition(i);
			return true;
		}
	return false;
}

bool Repository::update(const TElement& element)
{
	for (int i = 0;i < this->array.getSize(); i++)
		if (element == this->array[i])
		{
			this->array[i] = element;
			return true;
		}
	return false;
}

int Repository::getSize() const
{
	return this->array.getSize();
}

std::string Repository::toString()
{
	std::string string;
	for (int i = 0; i < this->array.getSize(); i++)
		string = string + this->array[i].toString();
	return string;
}