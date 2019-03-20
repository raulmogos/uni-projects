from unittest import TestCase
from Service.book_service import BookService
from Repository.repo import RepoData
from Validation.Validator import Validator
from Models.Book import Book
from undo_redo.Unod_Redo import *


class TestBookService(TestCase):
    def setUp(self):
        self.valid = Validator()
        self.bookRepo = RepoData()
        self.undoService = UndoService()
        self.rentalRepo = RepoData()
        self.book_service = BookService(self.valid, self.bookRepo, self.undoService, self.rentalRepo)

    def test_createBook(self):
        book = self.book_service.createBook(432, 'mara', 'op', 'slavici')
        self.assertEqual(book.get_book_id(), 432)
        self.assertEqual(book.get_author(), 'slavici')
        self.assertEqual(book.get_description(), 'op')
        self.assertEqual(book.get_title(), 'mara')
        self.assertEqual(book.get_availability(), True)

    def test_addBook(self):
        book1 = self.book_service.createBook(432, 'mara', 'op', 'slavici')
        book2 = self.book_service.createBook(442, 'mora cu noroc', 'super', 'slavici')
        self.book_service.addBook(book1)
        self.book_service.addBook(book2)
        self.assertEqual(len(self.bookRepo.getAll()), 2)

    def test_getAllBooks(self):
        book1 = self.book_service.createBook(432, 'mara', 'op', 'slavici')
        book2 = self.book_service.createBook(442, 'mora cu noroc', 'super', 'slavici')
        self.book_service.addBook(book1)
        self.book_service.addBook(book2)
        self.assertEqual(len(self.bookRepo.getAll()), 2)
        self.book_service.deleteBook(book2.get_book_id())
        self.assertEqual(len(self.bookRepo.getAll()), 1)

    def test_searchBookById(self):
        book1 = self.book_service.createBook(432, 'mara', 'op', 'slavici')
        book2 = self.book_service.createBook(442, 'mora cu noroc', 'super', 'slavici')
        self.book_service.addBook(book1)
        self.book_service.addBook(book2)
        book = self.book_service.searchBookById(432)
        self.assertEqual(book, book1)

    def test_deleteBook(self):
        book1 = self.book_service.createBook(432, 'mara', 'op', 'slavici')
        book2 = self.book_service.createBook(442, 'mora cu noroc', 'super', 'slavici')
        self.book_service.addBook(book1)
        self.book_service.addBook(book2)
        self.assertEqual(len(self.bookRepo.getAll()), 2)
        self.book_service.deleteBook(book2.get_book_id())
        self.assertEqual(len(self.bookRepo.getAll()), 1)
        self.book_service.addBook(book2)
        self.assertEqual(len(self.bookRepo.getAll()), 2)

    def test_setBookAvailable(self):
        book1 = self.book_service.createBook(432, 'mara', 'op', 'slavici')
        self.book_service.addBook(book1)
        self.book_service.setBookUnavailable(book1.get_book_id())
        self.assertEqual(False, book1.get_availability())
        self.book_service.setBookAvailable(book1.get_book_id())
        self.assertEqual(True, book1.get_availability())

    def test_searchBookByName(self):
        book1 = self.book_service.createBook(432, 'mara', 'op', 'slavici')
        book2 = self.book_service.createBook(442, 'mora cu noroc', 'super', 'slavici')
        self.book_service.addBook(book1)
        self.book_service.addBook(book2)
        book_lst = self.book_service.searchBookByName('mara')
        #print(book_lst[0].get_title())
        self.assertEqual(book_lst, [book1])

    def test_searchBookByAuthor(self):
        book1 = self.book_service.createBook(432, 'mara', 'op', 'slavici')
        book2 = self.book_service.createBook(442, 'mora cu noroc', 'super', 'slavici')
        self.book_service.addBook(book1)
        self.book_service.addBook(book2)
        book = self.book_service.searchBookByAuthor('slavici')
        self.assertEqual(book, book1)

    def test_searchBookByDescription(self):
        book1 = self.book_service.createBook(432, 'mara', 'op', 'slavici')
        book2 = self.book_service.createBook(442, 'mora cu noroc', 'super', 'slavici')
        self.book_service.addBook(book1)
        self.book_service.addBook(book2)
        book = self.book_service.searchBookByDescription('super')
        self.assertEqual(book, book2)

    def test_setBookUnavailable(self):
        book1 = self.book_service.createBook(432, 'mara', 'op', 'slavici')
        self.book_service.addBook(book1)
        self.book_service.setBookUnavailable(book1.get_book_id())
        self.assertEqual(False, book1.get_availability())

    def test_updateBook(self):
        book1 = self.book_service.createBook(432, 'mara', 'op', 'slavici')
        self.book_service.addBook(book1)
        self.book_service.updateBook(432, 'haha', 'gigi', 'oop')
        self.assertEqual(self.book_service.getAllBooks()[0].get_title(), 'haha')
        self.assertEqual(self.book_service.getAllBooks()[0].get_description(), 'gigi')
        self.assertEqual(self.book_service.getAllBooks()[0].get_author(), 'oop')
        #print(self.book_service.getAllBooks()[0])
        #self.fail()