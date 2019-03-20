from Repository.repo import RepoData
from Models.Rental import Rental
from errors.Errors import RepoFileTxtError
from datetime import date
import pickle

class FileRentalRepositoryBinary(RepoData):

    def __init__(self, file_name):
        RepoData.__init__(self)
        self.__file_name = file_name
        self.__readAllBinaryFromFile()

    def __readAllBinaryFromFile(self):
        '''
        we read all reantals from the file
        :return:
        '''
        try:
            with open(self.__file_name, "rb") as binary_file:
                list_of_rentals = pickle.load(binary_file)
            for rentals in list_of_rentals:
                RepoData.add(self, rentals)
        except FileNotFoundError:
            print("Inexistent file : " + self.__file_name)
        except EOFError:
            list_of_rentals = []

    def __writeAllBinaryToFile(self):
        try:
            with open(self.__file_name, "wb") as binary_file:
                pickle.dump(self._lst, binary_file)
        except FileNotFoundError:
            print("Inexistent file : " + self.__file_name)

    def __computeDateFromBinaryFile(self, list):
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
        self.__writeAllBinaryToFile()

    def remove(self, rental):
        RepoData.remove(self, rental)
        self.__writeAllBinaryToFile()
