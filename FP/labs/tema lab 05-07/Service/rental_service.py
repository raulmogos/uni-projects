from datetime import datetime
from datetime import date
from datetime import timedelta
from Models.Book import Book
from Models.Client import Client
from Models.Rental import Rental
from errors.Errors import *
from Models.MostActiveClients import MostActiveClientsDTO
from Models.MostRentedBooks import MostRentedBooksDTO
from Models.MostRentedAuthor import MostRentedAuthorDTO
from Models.LateRentals import LateRentalsDTO
from undo_redo.Unod_Redo import FunctionCall, Operation


class RentalService:

    def __init__(self, valid, rentalRepo, bookService, clientService, undoService):
        self.__valid = valid
        self.__rentalRepo = rentalRepo
        self.__bookService = bookService
        self.__clientService = clientService
        self.__undoService = undoService
        self.setBooksAvailabilityAcordingly()

    def createRental(self, rental_id, book_id, client_id):

        book_repo = self.__bookService.getAllBooks()
        client_repo = self.__clientService.getAllClients()
        # we create a new client in order to see if client_id valid or not
        client = Client(client_id, 'None')
        self.__valid.checkClientExistence(client, client_repo)

        # we create a new book in order to see if the book_is valid or not
        book = Book(book_id, 'None', 'None', 'None', None)
        self.__valid.checkBookExistenceAndAvailability(book, book_repo)

        # need to check the book if it is available

        current_date = datetime.now()
        current_day = current_date.day               # int
        current_month = current_date.month           # int
        current_year = current_date.year             # int
        rented_date = date(current_year, current_month, current_day)

        #rented_date = []            # rented_date will be a list
        #rented_date.append(current_day)
        #rented_date.append(current_month)
        #rented_date.append(current_year)

        # we need to create the due date
        due_date_p = current_date + timedelta(days=14)
        due_date_day = due_date_p.day                 # int
        due_date_month = due_date_p.month             # int
        due_date_year = due_date_p.year               # int
        due_date = date(due_date_year, due_date_month, due_date_day)

        #due_date = []               # due_date will be a list
        #due_date.append(due_date_day)
        #due_date.append(due_date_month
        #due_date.append(due_date_year)

        returned_date = 0

        rental = Rental(rental_id, book_id, client_id, rented_date, due_date, returned_date)
        return rental

    def getAllRentals(self):
        return self.__rentalRepo.getAll()

    def addRental(self, rental):
        self.__bookService.setBookUnavailable(rental.get_book_id())
        self.__rentalRepo.add(rental)
        # the undo for the add rental
        undo = FunctionCall(self.deleteRental, rental.get_rental_id())
        redo = FunctionCall(self.addRental, rental)
        operation = Operation(undo, redo)
        self.__undoService.add_operation(operation)

    def updateRental(self, rental_id, new_book_id, new_client_id):
        rental_new = self.createRental(rental_id, new_book_id, new_client_id)
        rental_old = self.searchRentalById(rental_id)

        book_new = self.__bookService.searchBookById(new_book_id)

        self.__valid.checkBookExistenceAndAvailability(book_new, self.__bookService.getAllBooks())
        self.__bookService.setBookAvailable(rental_old.get_book_id())
        self.__bookService.setBookUnavailable(rental_new.get_book_id())
        self.__rentalRepo.update(rental_old, rental_new)

        # the undo
        undo = FunctionCall(self.updateRental, rental_id, rental_old.get_book_id(), rental_old.get_client_id())
        redo = FunctionCall(self.updateRental, rental_id, new_book_id, new_client_id)
        operation = Operation(undo, redo)
        self.__undoService.add_operation(operation)

    def returnBook(self, book_id):
        book = Book(book_id, None, None, None, None)
        self.__valid.checkBookExistence(book, self.__bookService.getAllBooks())
        self.__bookService.setBookAvailable(book_id)
        rental = self.searchRentalByBookId(book_id)

        # setting the returned date
        current_date = datetime.now()
        returned_date = date(current_date.year, current_date.month, current_date.day)

        rental.set_returned_date(returned_date)

        #the undo
        undo = FunctionCall(self.undoReturnBook, book_id)
        redo = FunctionCall(self.returnBook, book_id)
        operation = Operation(undo, redo)
        self.__undoService.add_operation(operation)

    def undoReturnBook(self, book_id):
        book = Book(book_id, None, None, None, None)
        self.__valid.checkBookExistence(book, self.__bookService.getAllBooks())
        self.__bookService.setBookUnavailable(book_id)
        rental = self.searchRentalByBookId(book_id)
        rental.set_returned_date(0)

    def setBooksAvailabilityAcordingly(self):
        for rental in self.__rentalRepo.getAll():
            book_id = rental.get_book_id()
            for book in self.__bookService.getAllBooks():
                if book_id == book.get_book_id():
                    book.set_availability(False)


    ##############################################################

    def deleteRental(self, rental_id):
        rental = self.searchRentalById(rental_id)
        self.__valid.checkRentalExistence(rental, self.__rentalRepo.getAll())
        self.__bookService.setBookAvailable(rental.get_book_id())
        self.__rentalRepo.remove(rental)

    def searchRentalById(self, rental_id):
        rental = Rental(rental_id, None, None, None, None, None)
        self.__valid.checkRentalExistence(rental, self.__rentalRepo.getAll())
        for i in self.__rentalRepo.getAll():
            if i.get_rental_id() == rental_id:
                return i

    def searchRentalByBookId(self, book_id):
        '''
        funtion that search a rental by a book id
        :param book_id: int object
        :return: the rental
        '''
        repo_rental = self.__rentalRepo.getAll()
        for rental in repo_rental:
            if book_id == rental.get_book_id():
                return rental
        raise RepoError('this book is not rented')

    ###############################################################

    def mostRentedBooks(self):
        '''
        we look in every rental and count how many times a book had been rented
        '''
        dict = {}
        for rental in self.getAllRentals():
            book_id = rental.get_book_id()
            book = self.__bookService.searchBookById(book_id)
            if book_id not in dict.keys():
                nr = 0
                dict[book_id] = [book.get_title(), nr]
            dict[book_id][1] += 1

        lst = []
        for key in dict.keys():
            book_id = key
            book_title = dict[key][0]
            times_rented = dict[key][1]
            lst.append(MostRentedBooksDTO(book_id, book_title, times_rented))
        #lst.sort(key=lambda x: x.get_times_rented(), reverse=True)
        self.shellSort(lst, MostRentedBooksDTO.get_times_rented)
        return lst

    def mostActiveClients(self):
        '''

        :return:
        '''
        dict = {}
        for rental in self.getAllRentals():
            client_id = rental.get_client_id()
            client = self.__clientService.searchClientById(client_id)
            if client_id not in dict.keys():
                nr = 0
                dict[client_id] = [client.get_name(), nr]
            dict[client_id][1] += 1

        lst = []
        for key in dict.keys():
            client_id = key
            client_name = dict[key][0]
            nr_of_books_rented = dict[key][1]
            lst.append(MostActiveClientsDTO(client_id, client_name, nr_of_books_rented))

        #lst.sort(key=lambda x: x.get_nr_of_books_rented(), reverse=True)
        self.shellSort(lst, MostActiveClientsDTO.get_nr_of_books_rented)
        return lst

    def mostRentedAuthor(self):
        dict = {}
        for rental in self.getAllRentals():
            book_id = rental.get_book_id()
            book = self.__bookService.searchBookById(book_id)
            author = book.get_author()
            if author not in dict.keys():
                dict[author] = 0
            dict[author] += 1
        lst = []
        for key in dict.keys():
            author = key
            nr_of_times_rented = dict[key]
            lst.append(MostRentedAuthorDTO(author, nr_of_times_rented))
        #lst.sort(key=lambda x: x.get_nr_of_times_rented(), reverse=True)
        self.shellSort(lst, MostRentedAuthorDTO.get_nr_of_times_rented)
        return lst

    def lateRentals(self):
        '''
        function that return a sorted list of late rentals
        :return:
        '''
        dict = {}
        for rental in self.getAllRentals():
            if rental.get_returned_date() != 0:
                #date(yyyy,mm,dd)
                returned_date = date(rental.get_returned_date()[2], rental.get_returned_date()[1], rental.get_returned_date()[0])
                due_date = date(rental.get_due_date()[2], rental.get_due_date()[1], rental.get_due_date()[0])
                if returned_date > due_date:
                    dict[rental.get_rental_id()] = int((returned_date - due_date).days)
        lst = []
        for key in dict.keys():
            rental_id = key
            book_id = self.searchRentalById(rental_id).get_book_id()
            book_title = self.__bookService.searchBookById(book_id).get_title()
            client_id = self.searchRentalById(rental_id).get_client_id()
            client_name = self.__clientService.searchClientById(client_id).get_name()
            nr_of_days_of_delay = dict[key]
            lst.append(LateRentalsDTO(rental_id, book_id, book_title, client_id, client_name, nr_of_days_of_delay))
        #lst.sort(key=lambda x: x.get_nr_of_days_of_delay(), reverse=True)
        self.shellSort(lst, LateRentalsDTO.get_nr_of_days_of_delay)
        return lst

    def shellSort(self, arr, func):

        # Start with a big gap, then reduce the gap
        n = len(arr)
        gap = n // 2

        # Do a gapped insertion sort for this gap size.
        # The first gap elements a[0..gap-1] are already in gapped
        # order keep adding one more element until the entire array
        # is gap sorted
        while gap > 0:

            for i in range(gap, n):

                # add a[i] to the elements that have been gap sorted
                # save a[i] in temp and make a hole at position i
                temp = arr[i].func()

                # shift earlier gap-sorted elements up until the correct
                # location for a[i] is found
                j = i
                while j >= gap and arr[j - gap].func() < temp:
                    arr[j] = arr[j - gap]
                    j -= gap

                    # put temp (the original a[i]) in its correct location
                arr[j] = temp
            gap //= 2


    def filter(self, arr, nr_top):
        if nr_top < 10:
            return arr
        arr_1 = []
        for i in range(0,10):
            arr_1.append(arr[i])
        return arr_1