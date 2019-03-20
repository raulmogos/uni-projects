from Repository.repo import RepoData
from Models.Rental import Rental
from errors.Errors import RepoFileTxtError
from datetime import date

class FileRentalRepository(RepoData):

    def __init__(self, fileName):
        RepoData.__init__(self)
        self.__fileName = fileName
        self.__readAllFromFile()

    def __readAllFromFile(self):
        '''
        we read all reantals from the file
        :return:
        '''
        try:
            with open(self.__fileName, "r") as file:
                lines = file.readlines()
                for line in lines:
                    if line != "":
                        words = line.strip().split(",")
                        if len(words) == 6:
                            rental_id = int(words[0].strip())
                            book_id = int(words[1].strip())
                            client_id = int(words[2].strip())
                            rented_date = self.__computeDateFromFile(words[3].strip())
                            due_date = self.__computeDateFromFile(words[4].strip())
                            returned_date = self.__computeDateFromFile(words[5].strip())
                            rental = Rental(rental_id, book_id, client_id, rented_date, due_date, returned_date)
                            RepoData.add(self, rental)
        except FileNotFoundError:
            print("Inexistent file : " + self.__fileName)

    def __writeAllToFile(self):
        try:
            with open(self.__fileName, "w") as file:
                for rental in self._lst:
                    file.write(str(rental) + "\n")
        except FileNotFoundError:
            print("Inexistent file : " + self.__fileName)

    def __computeDateFromFile(self, list):
        '''
        function that takes care of the date
        :param list: a list of char: [dd,mm,yyyy]
        :return: a list of int: [dd,mm,yyyy]
        '''
        if list[0] == '0' and len(list) == 1:
            return 0
        lst = list.split("-")
        if len(lst) == 3:
            new_date = date(int(lst[0]), int(lst[1]), int(lst[2]))
            return new_date
        else:
            raise RepoFileTxtError('bad date in rental txt file')

    def add(self, rental):
        RepoData.add(self, rental)
        self.__writeAllToFile()

    def remove(self, rental):
        RepoData.remove(self, rental)
        self.__writeAllToFile()
