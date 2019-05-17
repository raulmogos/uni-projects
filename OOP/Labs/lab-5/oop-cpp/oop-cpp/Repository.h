#pragma once
#include "DynamicArray.h"
#include "Recording.h"

typedef Recording TElement;

class Repository
{
private: 
	
	DynamicArray<TElement> array;
	//DynamicArray<TElement>::iterator it;
	
public:
	Repository();
	~Repository();

	bool add(const TElement& element);
	bool remove(const TElement& element);
	bool update(const TElement& element);

	DynamicArray<TElement> getArray() { return this->array; }

	std::string toString();

	int getSize() const;
};
