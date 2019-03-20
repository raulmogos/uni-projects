from Repository.repo import RepoData
from Models.Book import Book

class FileBookRepository(RepoData):

    def __init__(self, fileName):
        #RepoData.__init__(self)
        self.__fileName = fileName
        self.__readAllFromFile()

    def __readAllFromFile(self):
        '''
        we read all books from the file
        :return:
        '''
        try:
            with open(self.__fileName, "r") as file:
                lines = file.readlines()
                for line in lines:
                    if line != "":
                        words = line.strip().split(",")
                        if len(words) == 5:
                            book_id = int(words[0].strip())
                            book_title = words[1].strip()
                            book__description = words[2].strip()
                            book_author = words[3].strip()
                            availability = bool(words[4].strip())
                            book = Book(book_id, book_title, book__description, book_author, availability)
                            RepoData.add(self, book)
        except FileNotFoundError:
            print("Inexistent file : " + self.__fileName)

    def __writeAllToFile(self):
        try:
            with open(self.__fileName, "w") as file:
                for book in self._lst:
                    file.write(str(book) + "\n")
        except FileNotFoundError:
            print("Inexistent file : " + self.__fileName)

    def add(self, book):
        RepoData.add(self, book)
        self.__writeAllToFile()

    def remove(self, book):
        RepoData.remove(self, book)
        self.__writeAllToFile()
