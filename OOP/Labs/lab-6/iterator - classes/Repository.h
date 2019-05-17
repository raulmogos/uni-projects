#pragma once
#include "DynamicArray.h"
#include "Recording.h"

typedef Recording Entity;

class Repository
{
private: 
	
	DynamicArray<Entity> array;
	DynamicArray<Entity>::iterator iteratorForRepository;
	
public:
	Repository();
	~Repository();

	bool add(const Entity& element);
	bool remove(const Entity& element);
	bool update(const Entity& element);

	DynamicArray<Entity> getListOfData();

	DynamicArray<Entity>::iterator next();

	int getSize() const;
};
