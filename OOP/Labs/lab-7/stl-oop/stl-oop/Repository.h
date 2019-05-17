#pragma once
#include <vector>
#include "Recording.h"

typedef Recording Entity;

class Repository
{
protected: 
	
	std::vector<Entity> array;
	std::vector<Entity>::iterator iteratorForRepository;
	
public:
	Repository();
	~Repository();

	virtual bool add(const Entity& element);
	virtual bool remove(const Entity& element);
	virtual bool update(const Entity& element);

	std::vector<Entity> getListOfData();

	std::vector<Entity>::iterator next();

	int getSize() const;
};
