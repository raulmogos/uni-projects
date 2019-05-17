#pragma once
#include <iostream>




template <typename TElement>
class DynamicArray
{

private:
	int capacity;
	int size;
	TElement* elements;

public:
	DynamicArray<TElement>();
	// copy constructor
	DynamicArray<TElement> (const DynamicArray<TElement> & dynamic_array);
	~DynamicArray();

	void add(const TElement & element);
	void deleteFromPosition(int index);

	int getSize() const;
	TElement getElement(int index);

	TElement * getElements() const;

	TElement& operator[](int index);

	//
	DynamicArray<TElement>& operator=(const DynamicArray<TElement>& array);

	DynamicArray<TElement>* operator*();

private:
	// functions
	void resize();
	void shiftElementsToLeft(int index);

public:
	class iterator
	{
	private:
		TElement * pointer;

	public:
		// comstructor
		iterator() : pointer(NULL) {};
		iterator(TElement * pointerToData)
		{
			this->pointer = pointerToData;
		} 
		// pre ++ operator
		iterator operator++()
		{
			this->pointer++;
			return this->pointer;
		}
		//post ++ operator
		iterator operator++(int)
		{
			iterator old = this->pointer;
			this->pointer++;
			return old;
		}
		// deref  * operator
		TElement operator*()
		{
			return *this->pointer;
		}
		// != operator
		bool operator!=(iterator it)
		{
			return this->pointer != it.pointer;
		}
		// = operator
		iterator operator=(TElement * pointerToData)
		{
			this->pointer = pointerToData;
			return this->pointer;
		}
		bool operator==(TElement * pointerToData)
		{
			return this->pointer == pointerToData;
		}
		bool operator>(TElement * pointerToData)
		{
			return this->pointer > pointerToData;
		}

	};

	TElement * begin() { return this->elements; }
	TElement * end() { return this->elements + this->size; }

};



//////////////////////////////////////////////////////////////////////////////////////////////////////

template <typename TElement>
DynamicArray<TElement>::DynamicArray()
{
	this->capacity = 4;
	this->size = 0;
	this->elements = new TElement[4];
}

template<typename TElement>
DynamicArray<TElement>::DynamicArray(const DynamicArray<TElement> & dynamic_array)
{
	this->size = dynamic_array.size;
	this->capacity = dynamic_array.capacity;

	this->elements = new TElement[this->capacity];

	for (int i = 0; i < dynamic_array.size; i++)
		this->elements[i] = dynamic_array.elements[i];
}

template <typename TElement>
DynamicArray<TElement>::~DynamicArray()
{	
	delete[] this->elements;
}

template <typename TElement>
void DynamicArray<TElement>::add(const TElement & element)
{
	if (this->size == this->capacity - 1)
		this->resize();

	TElement el{element};

	this->elements[this->size] = el;
	this->size++;
}

template <typename TElement>
void DynamicArray<TElement>::deleteFromPosition(int index)
{
	this->shiftElementsToLeft(index);
	this->size--;
}

template <typename TElement>
int DynamicArray<TElement>::getSize() const
{
	return this->size;
}

template <typename TElement>
TElement DynamicArray<TElement>::getElement(int index)
{
	return this->elements[index];
}

template <typename TElement>
TElement * DynamicArray<TElement>::getElements() const
{
	return this->elements;
}

template <typename TElement>
TElement&  DynamicArray<TElement>::operator[](int index)
{
	return this->elements[index];
}


template <typename TElement> 
DynamicArray<TElement>& DynamicArray<TElement>::operator=(const DynamicArray<TElement>& array)
{
	if (this == &array)
		return *this;

	this->size = array.size;
	this->capacity = array.capacity;
	
	delete[] this->elements;
	this->elements = new TElement[this->capacity];

	for (int i = 0;i < this->size; i++)
		this->elements[i] = array.elements[i];
	
	return *this;
}

template <typename TElement>
void DynamicArray<TElement>::resize()
{
	this->capacity = this->capacity * 2;
	TElement * new_dynamic_vector = new TElement[this->capacity];

	for (int i = 0;i < this->size; i++)
	{
		new_dynamic_vector[i] = this->elements[i];
	}

	delete[] this->elements;
	elements = new_dynamic_vector;
}

template <typename TElement>
void DynamicArray<TElement>::shiftElementsToLeft(int index)
{
	for (int i = index; i < this->size - 1; i++)
	{
		this->elements[i] = this->elements[i + 1];
	}
}

template <typename TElement>
DynamicArray<TElement>* DynamicArray<TElement>::operator*()
{
	return this;
}