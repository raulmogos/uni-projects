

class LateRentalsDTO:

    def __init__(self, rental_id, book_id, book_title, client_id, client_name, nr_of_days_of_delay):
        self.__rental_id = rental_id
        self.__book_id = book_id
        self.__book_title = book_title
        self.__client_id = client_id
        self.__client_name = client_name
        self.__nr_of_days_of_delay = nr_of_days_of_delay

    def __str__(self):
        return str(self.__rental_id)+"   "+str(self.__book_id)+" "+str(self.__book_title)+"   "+str(self.__client_id)+" "+str(self.__client_name)+"   "+str(self.__nr_of_days_of_delay)

    def get_nr_of_days_of_delay(self):
        return self.__nr_of_days_of_delay