from errors.Errors import RepoError
from errors.Errors import ValidError
from Models.Book import Book
from Repository.repo import RepoData


class Validator:

    def __init__(self):
        pass

    ###############################################################

    def checkBookExistenceAndAvailability(self, book, repo_book):
        '''
        function that checks if the book exists and if it is available
        :param book: the object book
        :param repo_book: the object - list in which are all the books in the library
        :return: if the book does not exist - repoError('inexsting book')
                 if the book exists:  -- if the book is available - pass
                                         if the book is not available - repoError('unavailable book ')
        '''
        rep = repo_book
        if book not in rep:
            raise RepoError('inexisting book id !')
        for i in rep:
            if book == i:
                if i.get_availability() == False:
                    raise RepoError('unavailable book !')
                '''
                else:
                    i.set_availability(False)
                '''

    def checkBookExistence(self, book, repo_book):
        '''
        function that checks if the book exists
        :param book: a object
        :param repo_book: a list of objects(books)
        :return: RepoError  if the book does not exists
        '''
        if book not in repo_book:
            raise RepoError('book inexistent !')

    ################################################################

    def checkClientExistence(self, client, repo_client):
        '''

        :param client:
        :param repo_client:
        :return:
        '''
        rep = repo_client
        if client not in rep:
            raise RepoError('inexisting client id !')

    ################################################################

    def checkRentalExistence(self, rental, rental_repo):
        '''

        :param rental:
        :param rental_repo:
        :return:
        '''
        if rental not in rental_repo:
            raise RepoError('inexisting reantal !')

    ##########################################################################