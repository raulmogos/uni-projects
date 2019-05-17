#pragma once

#include "Repository.h"



Repository::Repository(){}

Repository::~Repository() {}



bool Repository::add(const Entity& element)
{
	for (int i=0; i<this->array.getSize(); i++)
		if(element==this->array[i])
			return false;
	this->array.add(element);
	this->iteratorForRepository = NULL;
	return true;
}

bool Repository::remove(const Entity& element)
{
	for(int i=0;i<this->array.getSize(); i++)
		if (element == this->array[i])
		{
			this->array.deleteFromPosition(i);
			this->iteratorForRepository = NULL;
			return true;
		}
	return false;
}

bool Repository::update(const Entity& element)
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



DynamicArray<Entity>  Repository::getListOfData()
{
	Entity* elementsFromDynamicArray = this->array.getElements();

	DynamicArray<Entity> vector;

	for (int i = 0;i < this->array.getSize(); i++)
		vector.add(this->array[i]);

	return vector;
}

DynamicArray<Entity>::iterator Repository::next()
{
	DynamicArray<Entity>::iterator iteratorToReturn;
	
	if (this->iteratorForRepository == NULL)
		this->iteratorForRepository = this->array.begin();
	else if (this->iteratorForRepository != this->array.end())
		this->iteratorForRepository++;
	
	if (this->iteratorForRepository == this->array.end())
		this->iteratorForRepository = this->array.begin();

	iteratorToReturn = this->iteratorForRepository;

	return iteratorToReturn;
}
