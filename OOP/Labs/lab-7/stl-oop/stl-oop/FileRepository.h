#pragma once

#include "Repository.h"



class FileRepository : public Repository
{
private:

	std::string fileName;

public:

	FileRepository();
	FileRepository(std::string InputFileName);
	~FileRepository();

	void setFileNameRepository(const std::string file_name);

	void readDataFromFile();

private:

	void writeDataToFile();
};

