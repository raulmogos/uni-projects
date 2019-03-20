

class MostRentedBooksDTO:

    def __init__(self, book_id, book_title, times_rented):
        self.__book_id = book_id
        self.__book_title = book_title
        self.__times_rented = times_rented

    def __str__(self):
        return str(self.__book_id)+"     "+str(self.__book_title)+"     "+str(self.__times_rented)

    def get_times_rented(self):
        return self.__times_rented