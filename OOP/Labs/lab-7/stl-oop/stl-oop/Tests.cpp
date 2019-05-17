#include "Tests.h"
#include "Recording.h"
#include "Repository.h"
#include "Controller.h"
#include "FileRepository.h"

#include <assert.h>
#include <fstream>



void Tests::testAll()
{
	std::cout << "tests are running\n";
	testRecording();
	testRepository();
	testFileRepository();
	testController();
}

void Tests::testRecording()
{
	// teste getters
	// test constructor 
	{
		Recording recording1{ "op", "arad", "3-3", 32, "qwer" };
		assert(recording1.getTitle() == "op");
		assert(recording1.getLocation() == "arad");
		assert(recording1.getTimeOfCreation() == "3-3");
		assert(recording1.getTimesAccessed() == 32);
		assert(recording1.getFootagePreview() == "qwer");
	}

	// test default constructor
	{
		Recording recording2;
		assert(recording2.getTitle() == "");
		assert(recording2.getLocation() == "");
		assert(recording2.getTimeOfCreation() == "");
		assert(recording2.getTimesAccessed() == -1);
		assert(recording2.getFootagePreview() == "");
	}

	// test copy constructor
	{
		Recording recording1{ "op", "arad", "3-3", 32, "qwer" };
		Recording recording3(recording1);
		assert(recording3.getTitle() == "op");
		assert(recording3.getLocation() == "arad");
		assert(recording3.getTimeOfCreation() == "3-3");
		assert(recording3.getTimesAccessed() == 32);
		assert(recording3.getFootagePreview() == "qwer");
	}
	// test setters
	{
		Recording recording4;
		std::string title{ "ha" };
		recording4.setTitle(title);
		std::string location{ "asa" };
		recording4.setLocation(location);
		std::string time_of_creation{ "joi" };
		recording4.setTimeOfCreation(time_of_creation);
		recording4.setTimesAccessed(3);
		std::string footage{ "hagi" };
		recording4.setFootagePreview(footage);
	}

	// test == operator
	{
		Recording recording1{ "op", "arad", "3-3", 32, "qwer" };
		Recording recording3(recording1);
		assert((recording1 == recording3) == true);
	}

	// test to string 
	{
		Recording recording1{ "op", "arad", "3-3", 32, "qwer" };
		assert(recording1.toString() == "op arad 3-3 32 qwer\n");
	}

	// test << and >> operators
	{
		Recording recording5{ "  ha  ", "ha", "ha", 9, "ha" }, rec6;
		std::ofstream fout("test-recording-file.txt");
		fout << recording5;
		fout.close();
		std::ifstream fin("test-recording-file.txt");
		fin >> rec6;
		assert(rec6.getTitle() == "ha");
		assert(rec6.getLocation() == "ha");
		assert(rec6.getTimeOfCreation() == "ha");
		assert(rec6.getTimesAccessed() == 9);
		assert(rec6.getFootagePreview() == "ha");
		fin.close();
	}

	// test = operator 
	{
		Recording recording5{ "ha", "ha", "ha", 9, "ha" }, recording6;
		recording6 = recording5;
		assert(recording6.getTitle() == "ha");
		assert(recording6.getLocation() == "ha");
		assert(recording6.getTimeOfCreation() == "ha");
		assert(recording6.getTimesAccessed() == 9);
		assert(recording6.getFootagePreview() == "ha");
	}
}

void Tests::testRepository()
{
	Repository repository{};

	// test size 
	// test add 
	{
		Recording recording{ "ha", "ha", "ha", 99, "ha" };
		bool response = repository.add(recording);
		assert(response == true);
		assert(repository.getSize() == 1);
		response = repository.add(recording);
		assert(response == false);
		assert(repository.getSize() == 1);
	}

	// test remove 
	{		
		Recording rec{ "ha", "ha", "ha", 99, "ha" };
		assert(repository.getSize() == 1);
		bool r = repository.remove(rec);
		assert(r == true);
		assert(repository.getSize() == 0);
		r = repository.remove(rec);
		assert(r == false);
		assert(repository.getSize() == 0);
	}

	// test update 
	{
		Recording rec{ "ha", "ha", "ha", 99, "ha" };
		assert(repository.getSize() == 0);
		repository.add(rec);
		bool r = repository.update(Recording{ "ha", "qw","qw", 11, "qw" });
		assert(r == true);

		assert(repository.getListOfData()[0].getTitle() == "ha");
		assert(repository.getListOfData()[0].getLocation() == "qw");
		assert(repository.getListOfData()[0].getTimeOfCreation() == "qw");
		assert(repository.getListOfData()[0].getTimesAccessed() == 11);
		assert(repository.getListOfData()[0].getFootagePreview() == "qw");

		r = repository.update(Recording{ "qw", "qw","qw", 11, "qw" });
		assert(r == false);
		
		repository.remove(rec);
	}

	// test next
	{
		assert(repository.getSize() == 0);
		Recording recording1{ "1", "1", "1", 1, "1" };
		Recording recording2{ "2", "2", "2", 2, "2" };
		Recording recording3{ "3", "3", "3", 3, "3" };
		repository.add(recording1);
		repository.add(recording2);
		repository.add(recording3);

		Recording current;

		current = *repository.next();
		assert(current == recording1);
		current = *repository.next();
		assert(current == recording2);
		current = *repository.next();
		assert(current == recording3);
		current = *repository.next();
		assert(current == recording1);
		current = *repository.next();
		assert(current == recording2);
		current = *repository.next();
		assert(current == recording3);
		current = *repository.next();
		assert(current == recording1);
	}


}

void Tests::testFileRepository()
{
	// test read + write
	{
		FileRepository repository;
		repository.setFileNameRepository("test-file-repo.txt");

		Recording recording1{ "1", "1", "1", 1, "1" };
		Recording recording2{ "2", "2", "2", 2, "2" };
		Recording rec3{ "3", "3", "3", 3, "3" };
		repository.add(recording1);
		repository.add(recording2);
		repository.add(rec3);
	}

	{
		FileRepository repo("test-file-repo.txt");
		repo.readDataFromFile();

		Recording rec1{ "1", "1", "1", 1, "1" };
		Recording rec2{ "2", "2", "2", 2, "2" };
		Recording rec3{ "3", "3", "3", 3, "3" };

		assert(repo.getListOfData()[0] == rec1);
		assert(repo.getListOfData()[1] == rec2);
		assert(repo.getListOfData()[2] == rec3);

	}
}

void Tests::testController()
{
	// add 
	{
		FileRepository repo("test-file-repo.txt");
		Controller controller{ repo };

		Recording rec1{ "1", "1", "1", 1, "1" };
		Recording rec2{ "2", "2", "2", 2, "2" };
		Recording rec3{ "3", "3", "3", 3, "3" };

		controller.addRecording(rec1);
		assert(true);

		try { controller.addRecording(rec1); }
		catch (std::exception& add_error) { assert(strcmp(add_error.what(), "existing recording")==0); assert(true); }
	}
	// test add case 2
	{
		FileRepository repo("test-file-repo.txt");
		Controller controller{ repo };

		assert(controller.addRecording("1", "1", "1", "1", "1")==true);
		assert(controller.addRecording("1", "2", "2", "2", "2")==false);
	}
	
	// update
	{
		FileRepository repo("test-file-repo.txt");
		Controller controller{ repo };

		Recording rec1{ "1", "1", "1", 1, "1" };
		Recording rec2{ "1", "2", "2", 2, "2" };
		Recording rec3{ "3", "3", "3", 3, "3" };

		controller.addRecording(rec1);

		controller.updateRecording(rec2);
		assert(true);
		
		try { controller.updateRecording(rec3); }
		catch (std::exception& update_error) { assert(strcmp(update_error.what(), "inexisting recording") == 0); assert(true); }
	}
	// test update case 2
	{
		FileRepository repo("test-file-repo.txt");
		Controller controller{ repo };

		assert(controller.addRecording("1", "1", "1", "1", "1") == true);
		assert(controller.updateRecording("1", "2", "2", "2", "2") == true);
		assert(controller.updateRecording("112", "2", "2", "2", "2") == false);
	}

	// remove 
	{
		FileRepository repo("test-file-repo.txt");
		Controller controller{ repo };

		Recording rec1{ "1", "1", "1", 1, "1" };

		controller.addRecording(rec1);

		controller.removeRecording(rec1.getTitle());
		assert(true);

		assert(controller.removeRecording("2") == false);
	}


	// test get size
	{
		FileRepository repo("test-file-repo.txt");
		Controller controller{ repo };

		Recording rec1{ "1", "1", "1", 1, "1" };

		controller.addRecording(rec1);
		assert(controller.getSize() == 1);
	}

	// test list of entities 
	{
		FileRepository repo("test-file-repo.txt");
		Controller controller{ repo };

		Recording rec1{ "1", "1", "1", 1, "1" };
		Recording rec2{ "2", "2", "2", 2, "2" };
		Recording rec3{ "3", "3", "3", 3, "3" };

		controller.addRecording(rec1);
		controller.addRecording(rec2);
		controller.addRecording(rec3);

		assert(controller.listOfEntities()[0] == rec1);
		assert(controller.listOfEntities()[1] == rec2);
		assert(controller.listOfEntities()[2] == rec3);
	}

	// save to my list
	{
		FileRepository repo("test-file-repo.txt");
		Controller controller{ repo };

		Recording rec1{ "1", "1", "1", 1, "1" };
		Recording rec2{ "2", "2", "2", 2, "2" };
		Recording rec3{ "3", "3", "3", 3, "3" };

		controller.addRecording(rec1);
		controller.addRecording(rec2);
		controller.addRecording(rec3);

		assert(controller.saveToMyList("1") == true);
		assert(controller.saveToMyList("4") == false);
	}

	// get my list
	{
		FileRepository repo("test-file-repo.txt");
		Controller controller{ repo };

		Recording rec1{ "1", "1", "1", 1, "1" };
		Recording rec2{ "2", "2", "2", 2, "2" };
		Recording rec3{ "3", "3", "3", 3, "3" };

		controller.addRecording(rec1);
		controller.addRecording(rec2);
		controller.addRecording(rec3);

		controller.saveToMyList("1");
		controller.saveToMyList("2");
		controller.saveToMyList("3");

		assert(controller.getMyList()[0] == rec1);
		assert(controller.getMyList()[1] == rec2);
		assert(controller.getMyList()[2] == rec3);
	}

	// test nextRecording
	{
		FileRepository repo("test-file-repo.txt");
		Controller controller{ repo };

		Recording rec1{ "1", "1", "1", 1, "1" };
		Recording rec2{ "2", "2", "2", 2, "2" };
		Recording rec3{ "3", "3", "3", 3, "3" };

		controller.addRecording(rec1);
		controller.addRecording(rec2);
		controller.addRecording(rec3);

		controller.saveToMyList("1");
		controller.saveToMyList("2");
		controller.saveToMyList("3");

		assert(*controller.nextRecording() == rec1);
		assert(*controller.nextRecording() == rec2);
		assert(*controller.nextRecording() == rec3);
		assert(*controller.nextRecording() == rec1);
		assert(*controller.nextRecording() == rec2);
		assert(*controller.nextRecording() == rec3);
	}

	// test filterRepositoryByLocationAndTimesAccessed
	{
		FileRepository repo("test-file-repo.txt");
		Controller controller{ repo };

		Recording rec1{ "1", "1", "1", 1, "1" };
		Recording rec2{ "2", "2", "2", 2, "2" };
		Recording rec3{ "3", "2", "3", 3, "3" };
		Recording rec4{ "5", "5", "5", 5, "5" };

		std::vector<Entity> filteredList = controller.filterRepositoryByLocationAndTimesAccessed("2", "5");

		assert(filteredList.size() == 0);
	
		controller.addRecording(rec1);
		controller.addRecording(rec2);
		controller.addRecording(rec3);
		controller.addRecording(rec4);

		filteredList = controller.filterRepositoryByLocationAndTimesAccessed("2", "5");

		assert(filteredList.size() == 2);

		assert(filteredList[0] == rec2);
		assert(filteredList[1] == rec3);
	}

	// test setFileNameForRepository
	{
		FileRepository repo("test-file-repo.txt");
		Controller controller{ repo };

		controller.setFileNameForRepository("test-file-repo.txt");
	}
}