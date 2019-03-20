'''

'''
from errors.Errors import RepoError
from errors.Errors import ValidError

class Console(object):

    def __init__(self, serviceBook, serviceClient, serviceRental, undoService):
        self.__serviceBook = serviceBook
        self.__serviceClient = serviceClient
        self.__serviceRental = serviceRental
        self.__undoService = undoService

    ################################################################

    def __addBookUI(self):
        while True:
            try:
                book_id = int(input('book id: '))
                book_title = input('book title: ')
                book_description = input('book descprition: ')
                book_author = input('book author: ')
                book = self.__serviceBook.createBook(book_id, book_title, book_description, book_author)
                self.__serviceBook.addBook(book)
                break
            except RepoError as re:
                print(re)
            except ValidError as ve:
                print(ve)
            except ValueError as ve:
                print(ve)

    def __addClientUI(self):
        while True:
            try:
                client_id = int(input('client id: '))
                book_name = input('client name: ')
                client = self.__serviceClient.createClient(client_id, book_name)
                self.__serviceClient.addClient(client)
                break
            except RepoError as re:
                print(re)
            except ValidError as ve:
                print(ve)
            except ValueError as ve:
                print(ve)

    def __addRentalUI(self):
        '''
        we add a new rental = the client rents a book
        :return:
        '''
        while True:
            try:
                print('the client basically rents now a book ')
                rental_id = int(input('rental id: '))
                book_id = int(input('book id: '))
                client_id = int(input('client id: '))
                rental = self.__serviceRental.createRental(rental_id, book_id, client_id)
                self.__serviceRental.addRental(rental)
                break
            except RepoError as re:
                print(re)
            except ValidError as ve:
                print(ve)
            except ValueError as ve:
                print(ve)

    #################################################################

    def __removeBookUI(self):
        '''
        use only id for removing
        :return:
        '''
        while True:
            try:
                book_id = int(input('book id: '))
                self.__serviceBook.deleteBook(book_id)
                break
            except RepoError as re:
                print(re)
            except ValidError as ve:
                print(ve)
            except ValueError as ve:
                print(ve)

    def __removeClientUI(self):
        '''
        use only id for removing
        :return:
        '''
        while True:
            try:
                client_id = int(input('client id: '))
                self.__serviceClient.deleteClient(client_id)
                break
            except RepoError as re:
                print(re)
            except ValidError as ve:
                print(ve)
            except ValueError as ve:
                print(ve)

    def __removeRentalUI(self):
        '''
        use only id for removing
        :return:
        '''
        while True:
            try:
                reantal_id = int(input('rental id: '))
                self.__serviceRental.deleteRental(reantal_id)
                break
            except RepoError as re:
                print(re)
            except ValidError as ve:
                print(ve)
            except ValueError as ve:
                print(ve)

    ###########################################

    def __updateBookUI(self):
        while True:
            try:
                book_id = int(input('book id: '))
                book_new_title = input('book new title')
                book_new_description = input('book new description: ')
                book_new_author = input('book new author: ')
                self.__serviceBook.updateBook(book_id, book_new_title, book_new_description, book_new_author)
                break
            except RepoError as re:
                print(re)
            except ValidError as ve:
                print(ve)
            except ValueError as ve:
                print(ve)

    def __updateClientUI(self):
        while True:
            try:
                client_id = int(input('client id: '))
                client_new_name = input('client new name: ')
                self.__serviceClient.updateClient(client_id, client_new_name)
                break
            except RepoError as re:
                print(re)
            except ValidError as ve:
                print(ve)
            except ValueError as ve:
                print(ve)

    def __updateRentalUI(self):
        while True:
            try:
                rental_id = int(input('rental id: '))
                new_book_id = int(input('book id: '))
                new_client_id = int(input('client id: '))
                self.__serviceRental.updateRental(rental_id, new_book_id, new_client_id)
                break
            except RepoError as re:
                print(re)
            except ValidError as ve:
                print(ve)
            except ValueError as ve:
                print(ve)

    ###########################################

    def __returnBookUI(self):
        while True:
            try:

                book_id = int(input('book id: '))
                self.__serviceRental.returnBook(book_id)
                break
            except RepoError as re:
                print(re)
            except ValidError as ve:
                print(ve)
            except ValueError as ve:
                print(ve)


    ###########################################

    def __searchBookUI(self):
        print("1 -- by id\n"
              "2 -- by title\n"
              "3 -- by description\n"
              "4 -- by author\n")
        cmd = int(input('>> '))
        if cmd == 1:
            self.__searchBookByIdUI()
        elif cmd == 2:
            self.__searchBookByTitleUI()
        elif cmd == 3:
            self.__searchBookByDescriptionUI()
        elif cmd == 4:
            self.__searchBookByAuthorUI()
        else:
            return


    def __searchBookByIdUI(self):
        while True:
            try:
                book_id = int(input('book id: '))
                book = self.__serviceBook.searchBookById(book_id)
                break
            except RepoError as re:
                print(re)
            except ValidError as ve:
                print(ve)
            except ValueError as ve:
                print(ve)
        print(book)

    def __searchBookByTitleUI(self):
        while True:
            try:
                book_title = input('book title: ')
                book = self.__serviceBook.searchBookByName(book_title)
                break
            except RepoError as re:
                print(re)
            except ValidError as ve:
                print(ve)
            except ValueError as ve:
                print(ve)
        for bk in book:
            print(bk)

    def __searchBookByDescriptionUI(self):
        while True:
            try:
                book_description = input('book description: ')
                book = self.__serviceBook.searchBookByDescription(book_description)
                break
            except RepoError as re:
                print(re)
            except ValidError as ve:
                print(ve)
            except ValueError as ve:
                print(ve)
        print(book)

    def __searchBookByAuthorUI(self):
        while True:
            try:
                book_author = input('book author: ')
                book = self.__serviceBook.searchBookByAuthor(book_author)
                break
            except RepoError as re:
                print(re)
            except ValidError as ve:
                print(ve)
            except ValueError as ve:
                print(ve)
        print(book)


    ###########################################

    def __searchClientUI(self):
        print("1 -- by id\n"
              "2 -- by name\n")
        cmd = int(input('>> '))
        if cmd == 1:
            self.__searchClientByIdUI()
        elif cmd == 2:
            self.__searchClientByNameUI()

    def __searchClientByIdUI(self):
        while True:
            try:
                client_id = int(input('client id: '))
                client = self.__serviceClient.searchClientById(client_id)
                break
            except RepoError as re:
                print(re)
            except ValidError as ve:
                print(ve)
            except ValueError as ve:
                print(ve)
        print(client)

    def __searchClientByNameUI(self):
        while True:
            try:
                client_name = input('client name: ')
                client = self.__serviceClient.searchClientByName(client_name)
                break
            except RepoError as re:
                print(re)
            except ValidError as ve:
                print(ve)
            except ValueError as ve:
                print(ve)
        print(client)

    ###########################################

    def __printMenu(self):
        print("1  --  add\n"
              "2  --  remove\n"
              "3  --  update\n"
              "4  --  list\n"
              "5  --  search a book\n"
              "6  --  search a client\n"
              "7  --  return a book\n"
              "8  --  statistics\n"
              "9  --  undo\n"
              "10 --  redo\n"
              "else - exit")

    def __getInput2(self):
        while True:
            try:
                print("1  --  book\n"
                      "2  --  client\n"
                      "3  --  rental\n"
                      "else - exit")
                cmd2 = int(input('> '))
                break
            except ValueError as ve:
                print(ve)
        return cmd2

    def __listUI(self):
        print('###################     BOOKS     #######################')

        rep_book = self.__serviceBook.getAllBooks()
        if len(rep_book) == 0:
            print('empty book repo ')
        else:
            for i in rep_book:
                print(i)
        print('###################     CLIENTS     #######################')

        rep_client = self.__serviceClient.getAllClients()
        if len(rep_client) == 0:
            print('empty client repo ')
        else:
            for i in rep_client:
                print(i)
        print('###################     RENTALS     #######################')

        rep_rental = self.__serviceRental.getAllRentals()
        if len(rep_rental) == 0:
            print('empty rental repo ')
        else:
            for i in rep_rental:
                print(i)
        print('#########################################################')

    def __statisticsMenuUI(self):
        print("1  --  Most rented books.\n"
              "2  --  Most active clients.\n"
              "3  --  Most rented author.\n"
              "4  --  Late rentals.\n")

        nr = int(input('>'))
        if nr == 1:
            lst = self.__serviceRental.mostRentedBooks()
            for i in lst:
                print(i)
        if nr == 2:
            lst = self.__serviceRental.mostActiveClients()
            for i in lst:
                print(i)
        if nr == 3:
            lst = self.__serviceRental.mostRentedAuthor()
            for i in lst:
                print(i)
        if nr == 4:
            lst = self.__serviceRental.lateRentals()
            for i in lst:
                print(i)



    def __undo(self):
        undo = self.__undoService.undo()
        if not undo:
            print("No more Undo's!")

    def __redo(self):
        redo = self.__undoService.redo()
        if not redo:
            print("No more Redo's!")


    ###########################################

    def runUI(self):
        while True:
            try:
                self.__printMenu()
                cmd1 = int(input('> '))
            except ValueError as ve:
                print(ve)
            except RepoFileTxtError as rfte:
                print(rfte)

            if cmd1 == 1:
                cmd2 = self.__getInput2()
                if cmd2 == 1:
                    self.__addBookUI()
                elif cmd2 == 2:
                    self.__addClientUI()
                elif cmd2 == 3:
                    self.__addRentalUI()
                else:
                    return

            elif cmd1 == 2:
                cmd2 = self.__getInput2()
                if cmd2 == 1:
                    self.__removeBookUI()
                elif cmd2 == 2:
                    self.__removeClientUI()
                elif cmd2 == 3:
                    self.__removeRentalUI()
                else:
                    return

            elif cmd1 == 3:
                cmd2 = self.__getInput2()
                if cmd2 == 1:
                    self.__updateBookUI()
                elif cmd2 == 2:
                    self.__updateClientUI()
                elif cmd2 == 3:
                    self.__updateRentalUI()
                else:
                    return

            elif cmd1 == 4:
                self.__listUI()
            elif cmd1 == 5:
                self.__searchBookUI()
            elif cmd1 == 6:
                self.__searchClientUI()
            elif cmd1 == 7:
                self.__returnBookUI()
            elif cmd1 == 8:
                self.__statisticsMenuUI()
            elif cmd1 == 9:
                self.__undo()
            elif cmd1 == 10:
                self.__redo()
            else:
                return