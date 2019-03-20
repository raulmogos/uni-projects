from unittest import TestCase

from errors.Errors import *
from Models.Book import Book
from Models.Client import Client
from Repository.repo import RepoData


class TestValidator(TestCase):

    def setUp(self):
        self.repoBook = RepoData()
        self.repoClient = RepoData()
        self.repoRentals = RepoData()

    def test_checkBookExistenceAndAvailability(self):
        s = 'hello world'
        with self.assertRaises(TypeError):
            s.split(2)

    def test_checkBookExistence(self):
        pass

    def test_checkClientExistence(self):
        pass

    def test_checkRentalExistence(self):
        pass
