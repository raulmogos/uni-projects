'''
service for book
'''
from Models.Book import Book
from errors.Errors import *
from undo_redo.Unod_Redo import Operation, FunctionCall, CascadeOperations


class BookService:

    def __init__(self, valid, bookRepo, undoService, rentalRepo):
        self.__valid = valid
        self.__bookRepo = bookRepo
        self.__undoService = undoService
        self.__rentalRepo = rentalRepo

    def createBook(self, book_id, book_title, book_description, book_author):
        book = Book(book_id, book_title, book_description, book_author, True)
        return book

    def addBook(self, book):
        self.__bookRepo.add(book)
        # the undo+redo
        undo = FunctionCall(self.deleteBook, book.get_book_id())
        redo = FunctionCall(self.addBook, book)
        operation = Operation(undo, redo)
        self.__undoService.add_operation(operation)

    def generateBook(self):
        pass

    def getAllBooks(self):
        return self.__bookRepo.getAll()


    def deleteBook(self, book_id):
        '''

        :param book_id:
        :return:
        '''
        book = self.searchBookById(book_id)
        self.__bookRepo.remove(book)

        undo = FunctionCall(self.addBook, book)
        redo = FunctionCall(self.deleteBook, book_id)
        operation = Operation(undo, redo)

        co = CascadeOperations()
        co.add(operation)

        rent = []
        for rental in self.__rentalRepo.getAll():
            if rental.get_book_id() == book_id:
                rent.append(rental)

        for rental in rent:
            self.removeRentalForUndo(rental)

        if len(rent) != 0:
            for r in rent:
                undo = FunctionCall(self.addRentalForUndo, r)
                redo = FunctionCall(self.removeRentalForUndo, r)
                operation_cascaded = Operation(undo, redo)
                co.add(operation_cascaded)
        self.__undoService.add_operation(co)


    def addRentalForUndo(self, rental):
        self.__rentalRepo.add(rental)

    def removeRentalForUndo(self, rental):
        # we check first if the rental is already removed
        # because some of them were removed during the redo of the  function - deleteBook
        if rental not in self.__rentalRepo.getAll():
            return
        self.__rentalRepo.remove(rental)


    def updateBook(self, book_id, book_new_title, book_new_description, book_new_author):
        book_new = self.createBook(book_id, book_new_title, book_new_description, book_new_author)
        book_old = self.searchBookById(book_id)
        self.__bookRepo.update(book_old, book_new)

        undo = FunctionCall(self.updateBook, book_old.get_book_id(), book_old.get_title(), book_old.get_description(), book_old.get_author())
        redo = FunctionCall(self.updateBook, book_new.get_book_id(), book_new.get_title(), book_new.get_description(), book_new.get_author())
        operation = Operation(undo, redo)
        self.__undoService.add_operation(operation)

    '''
    #############################################################
    '''

    def setBookAvailable(self, book_id):
        book = self.searchBookById(book_id)
        book.set_availability(True)

    def setBookUnavailable(self, book_id):
        book = self.searchBookById(book_id)
        book.set_availability(False)

    '''
    #############################################################
    '''

    def searchBookById(self, book_id):
        '''

        :param book_id:
        :return:
        '''
        book = Book(book_id, 'None', 'None', 'None', None)
        self.__valid.checkBookExistence(book, self.__bookRepo.getAll())
        book_repo = self.__bookRepo.getAll()
        for book in book_repo:
            if book_id == book.get_book_id():
                return book

    def searchBookByName(self, book_title):
        repo = self.getAllBooks()
        book_lst = []
        for book in repo:
            if book_title in book.get_title():
                book_lst.append(book)
        if len(book_lst)!=0:
            return book_lst
        else:
            raise RepoError('book does not exists')

    def searchBookByDescription(self, book_description):
        repo = self.getAllBooks()
        for book in repo:
            if book.get_description() == book_description:
                return book
        raise RepoError('book does not exists')

    def searchBookByAuthor(self, book_author):
        repo = self.getAllBooks()
        for book in repo:
            if book.get_author() == book_author:
                return book
        raise RepoError('book does not exists')
