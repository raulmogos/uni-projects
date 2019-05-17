#include "FileRepository.h"
#include <fstream>
#include <iostream>


FileRepository::FileRepository() {}

FileRepository::FileRepository(std::string InputFileName) : fileName(InputFileName)
{
	//this->readDataFromFile();
}

FileRepository::~FileRepository() 
{
	this->writeDataToFile();
}

void FileRepository::setFileNameRepository(const std::string file_name)
{
	this->fileName = file_name;
}

void FileRepository::readDataFromFile()
{
	std::ifstream file_in;

	file_in.open(this->fileName);

	if (file_in.fail()) 
	{
		// file could not be opened
		file_in.close();
	}
	else 
	{
		Entity inputRecording;
		while (!file_in.eof())
		{
			file_in >> inputRecording;
			this->add(inputRecording);
		}
		file_in.close();
	}
}

void FileRepository::writeDataToFile()
{
	std::ofstream file_out(this->fileName);

	for (int i=0; i<this->array.size(); i++)
	{
		if (i == this->array.size() - 1)
		{
			file_out << this->array[i];
			break;
		}
		file_out << this->array[i] << '\n';
	}

	file_out.close();
}



