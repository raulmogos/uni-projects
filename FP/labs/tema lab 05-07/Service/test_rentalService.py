from unittest import TestCase
from Validation.Validator import Validator
from Repository.repo import RepoData
from Service.client_service import *
from Service.book_service import *
from Service.rental_service import *
from undo_redo.Unod_Redo import *


class TestRentalService(TestCase):
    def setUp(self):
        self.bookRepo = RepoData()
        self.clientRepo = RepoData()
        self.rentalRepo = RepoData()
        self.valid = Validator()
        self.undoService = UndoService()
        self.serviceBook = BookService(self.valid, self.bookRepo, self.undoService, self.rentalRepo)
        self.serviceClient = ClientService(self.valid, self.clientRepo, self.undoService, self.rentalRepo,
                                           self.bookRepo)
        self.serviceRental = RentalService(self.valid, self.rentalRepo, self.serviceBook, self.serviceClient,
                                           self.undoService)

    def test_createRental(self):
        self.bookRepo.add(Book(12, 'qwert', 'asdfgh', 'zxcvbn', True))
        self.clientRepo.add(Client(43, 'MOhl ojsddan'))
        rental = self.serviceRental.createRental(777, 12, 43)
        self.assertEqual(777, rental.get_rental_id())
        self.assertEqual(12, rental.get_book_id())
        self.assertEqual(43, rental.get_client_id())

        current_date = datetime.now()
        due_date = current_date + timedelta(days=14)

        day = current_date.day
        month = current_date.month
        year = current_date.year
        date_p = date(year, month, day)

        self.assertEqual(date_p, rental.get_rented_date())
        day = due_date.day
        month = due_date.month
        year = due_date.year
        t = date(year, month, day)
        self.assertEqual(t, rental.get_due_date())
        self.assertEqual(0, rental.get_returned_date())

    def test_getAllRentals(self):
        self.bookRepo.add(Book(12, 'qwert', 'asdfgh', 'zxcvbn', True))
        self.bookRepo.add(Book(56, 'mara', 'op', 'slavici', True))
        self.clientRepo.add(Client(43, 'MOhl ojsddan'))
        self.clientRepo.add(Client(99, 'gicu jnjnj'))
        rental1 = self.serviceRental.createRental(777, 12, 43)
        self.serviceRental.addRental(rental1)
        self.assertEqual(1, len(self.serviceRental.getAllRentals()))
        rental2 = self.serviceRental.createRental(888, 56, 99)
        self.serviceRental.addRental(rental2)
        self.assertEqual(2, len(self.serviceRental.getAllRentals()))

    def test_addRental(self):
        self.bookRepo.add(Book(12, 'qwert', 'asdfgh', 'zxcvbn', True))
        self.bookRepo.add(Book(56, 'mara', 'op', 'slavici', True))
        self.clientRepo.add(Client(43, 'MOhl ojsddan'))
        self.clientRepo.add(Client(99, 'gicu jnjnj'))
        rental1 = self.serviceRental.createRental(777, 12, 43)
        self.serviceRental.addRental(rental1)
        self.assertEqual(1, len(self.serviceRental.getAllRentals()))
        rental2 = self.serviceRental.createRental(888, 56, 99)
        self.serviceRental.addRental(rental2)
        self.assertEqual(2, len(self.serviceRental.getAllRentals()))

    def test_deleteRental(self):
        self.bookRepo.add(Book(12, 'qwert', 'asdfgh', 'zxcvbn', True))
        self.bookRepo.add(Book(56, 'mara', 'op', 'slavici', True))
        self.clientRepo.add(Client(43, 'MOhl ojsddan'))
        self.clientRepo.add(Client(99, 'gicu jnjnj'))
        rental1 = self.serviceRental.createRental(777, 12, 43)
        self.serviceRental.addRental(rental1)
        rental2 = self.serviceRental.createRental(888, 56, 99)
        self.serviceRental.addRental(rental2)
        self.assertEqual(2, len(self.serviceRental.getAllRentals()))
        self.serviceRental.deleteRental(888)
        self.assertEqual(1, len(self.serviceRental.getAllRentals()))

    def test_searchRentalById(self):
        self.bookRepo.add(Book(12, 'qwert', 'asdfgh', 'zxcvbn', True))
        self.bookRepo.add(Book(56, 'mara', 'op', 'slavici', True))
        self.clientRepo.add(Client(43, 'MOhl ojsddan'))
        self.clientRepo.add(Client(99, 'gicu jnjnj'))
        rental1 = self.serviceRental.createRental(777, 12, 43)
        self.serviceRental.addRental(rental1)
        rental2 = self.serviceRental.createRental(888, 56, 99)
        self.serviceRental.addRental(rental2)

        rental = self.serviceRental.searchRentalById(777)
        self.assertEqual(rental, rental1)
        rental = self.serviceRental.searchRentalById(888)
        self.assertEqual(rental, rental2)

    def test_searchRentalByBookId(self):
        self.bookRepo.add(Book(12, 'qwert', 'asdfgh', 'zxcvbn', True))
        self.bookRepo.add(Book(56, 'mara', 'op', 'slavici', True))
        self.clientRepo.add(Client(43, 'MOhl ojsddan'))
        self.clientRepo.add(Client(99, 'gicu jnjnj'))
        rental1 = self.serviceRental.createRental(777, 12, 43)
        self.serviceRental.addRental(rental1)
        rental2 = self.serviceRental.createRental(888, 56, 99)
        self.serviceRental.addRental(rental2)

        rental = self.serviceRental.searchRentalByBookId(12)
        self.assertEqual(rental, rental1)
        rental = self.serviceRental.searchRentalByBookId(56)
        self.assertEqual(rental, rental2)

    def test_returnBook(self):
        book1 = Book(12, 'qwert', 'asdfgh', 'zxcvbn', True)
        self.serviceBook.addBook(book1)
        book2 = Book(56, 'mara', 'op', 'slavici', True)
        self.serviceBook.addBook(book2)
        self.serviceClient.addClient(Client(43, 'MOhl ojsddan'))
        self.serviceClient.addClient(Client(99, 'gicu jnjnj'))
        rental1 = self.serviceRental.createRental(777, 12, 43)
        rental2 = self.serviceRental.createRental(888, 56, 99)
        self.serviceRental.addRental(rental1)
        self.serviceRental.addRental(rental2)
        book3 = self.serviceBook.searchBookById(rental1.get_book_id())
        self.assertEqual(book3.get_availability(), False)
        self.serviceRental.returnBook(12)
        book3 = self.serviceBook.searchBookById(rental1.get_book_id())
        self.assertEqual(book3.get_availability(), True)
        book3 = self.serviceBook.searchBookById(rental2.get_book_id())
        self.assertEqual(book3.get_availability(), False)
        self.serviceRental.returnBook(56)
        book3 = self.serviceBook.searchBookById(rental2.get_book_id())
        self.assertEqual(book3.get_availability(), True)

    def test_updateRental(self):
        self.bookRepo.add(Book(12, 'qwert', 'asdfgh', 'zxcvbn', True))
        self.serviceBook.addBook(Book(56, 'mara', 'op', 'slavici', True))
        self.serviceClient.addClient(Client(43, 'MOhl ojsddan'))
        self.serviceClient.addClient(Client(99, 'gicu jnjnj'))
        rental1 = self.serviceRental.createRental(777, 12, 43)
        self.serviceRental.addRental(rental1)
        self.serviceRental.updateRental(777,56,43)
        self.assertEqual(56, self.serviceRental.getAllRentals()[0].get_book_id())
        self.assertEqual(43, self.serviceRental.getAllRentals()[0].get_client_id())
