//#include "DynamicArray.h"
//#include <iostream>
//
//template <typename TElement>
//DynamicArray<TElement>::DynamicArray()
//{
//	this->capacity = 9;
//	this->size = 0;
//	this->elements = new TElement[9];
//}
//
//template <typename TElement>
//DynamicArray<TElement>::~DynamicArray()
//{
//	delete[] this->elements;
//}
//
//template <typename TElement>
//void DynamicArray<TElement>::add(TElement element)
//{
//	if (this->size == this->capacity - 1)
//		this->resize();
//
//	this->elements[this->size] = element;
//	this->size++;
//}
//
//template <typename TElement>
//void DynamicArray<TElement>::deleteFromPosition(int index)
//{
//	this->shiftElementsRigth(index);
//	this->size--;
//}
//
//template <typename TElement>
//int DynamicArray<TElement>::getSize() const
//{
//	return this->size;
//}
//
//template <typename TElement>
//TElement DynamicArray<TElement>::getElement(int index)
//{
//	return this->elements[index];
//}
//
//template <typename TElement>
//TElement&  DynamicArray<TElement>::operator[](int index)
//{
//	return this->elements[index];
//}
//
//template <typename TElement>
//void DynamicArray<TElement>::resize()
//{
//	this->capacity = this->capacity * 2;
//	TElement * new_dynamic_vector = new TElement[this->capacity];
//
//	for (int i = 0;i < this->size; i++) 
//	{
//		new_dynamic_vector[i] = this->elements[i];
//	}
//
//	delete[] this->elements;
//	elements = new_dynamic_vector;
//}
//
//template <typename TElement>
//void DynamicArray<TElement>::shiftElementsRigth(int index)
//{
//	for (int i = index; i < this->size-1; i++)
//	{
//		this->elements[i] = this->elements[i + 1];
//	}
//}
//
