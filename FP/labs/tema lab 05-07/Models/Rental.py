'''

'''


class Rental:
    '''
    class for rental
    '''

    def __init__(self, rentalID, bookID, clientID, rented_date, due_date, returned_date):
        self.__rentalID = rentalID
        self.__bookID = bookID
        self.__clientID = clientID
        self.__rented_date = rented_date
        self.__due_date = due_date
        self.__returned_date = returned_date

    def __str__(self):
        return str(self.__rentalID)+', '+str(self.__bookID)+', '+str(self.__clientID)+', '+str(self.__rented_date)+', '+str(self.__due_date)+', '+str(self.__returned_date)

    def __eq__(self, other):
        return self.__rentalID == other.__rentalID

    def get_rental_id(self):
        return self.__rentalID

    def get_book_id(self):
        return self.__bookID

    def get_client_id(self):
        return self.__clientID

    def get_rented_date(self):
        return self.__rented_date

    def get_due_date(self):
        return self.__due_date

    def get_returned_date(self):
        return self.__returned_date

    def set_rental_id(self, value):
        self.__rentalID = value

    def set_book_id(self, value):
        self.__bookID = value

    def set_client_id(self, value):
        self.__clientID = value

    def set_rented_date(self, value):
        self.__rented_date = value

    def set_due_date(self, value):
        self.__due_date = value

    def set_returned_date(self, value):
        self.__returned_date = value

    '''
    rentalID = property(get_rental_id, set_rental_id, None, None)
    bookID = property(get_book_id, set_book_id, None, None)
    clientID = property(get_client_id, set_client_id, None, None)
    rented_date = property(get_rented_date, set_rented_date, None, None)
    due_date = property(get_due_date, set_due_date, None, None)
    returned_date = property(get_returned_date, set_returned_date, None, None)
    '''



