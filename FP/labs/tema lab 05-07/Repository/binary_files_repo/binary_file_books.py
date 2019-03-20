from Repository.repo import RepoData
from Models.Book import Book
import pickle


class FileBookRepositoryBinary(RepoData):

    def __init__(self, file_name):
        RepoData.__init__(self)
        self.file_name = file_name
        self.__readBinaryFromFile()

    def __readBinaryFromFile(self):
        try:
            with open(self.file_name, "rb") as binary_file:
                list_of_books = pickle.load(binary_file)
            for book in list_of_books:
                RepoData.add(self, book)
        except FileNotFoundError:
            print("Inexistent file : " + self.file_name)

    def __writeBinaryToFile(self):
        try:
            with open(self.file_name, "wb") as binary_file:
                pickle.dump(self._lst, binary_file)
        except FileNotFoundError:
            print("Inexistent file : " + self.file_name)

    def add(self, book):
        RepoData.add(self, book)
        self.__writeBinaryToFile()

    def remove(self, book):
        RepoData.remove(self, book)
        self.__writeBinaryToFile()

'''
ahah = FileBookRepositoryBinary('books.pickle')
for i in ahah.getAll():
    print(i)

b = Book(999,'1','123456', 'dnsodc', True)

ahah.remove(b)

for i in ahah.getAll():
    print(i)
'''