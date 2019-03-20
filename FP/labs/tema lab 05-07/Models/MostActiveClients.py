

class MostActiveClientsDTO:

    def __init__(self, client_id, client_name, nr_of_books_rented):
        self.__client_id = client_id
        self.__client_name = client_name
        self.__nr_of_books_rented = nr_of_books_rented

    def __str__(self):
        return str(self.__client_id)+"     "+str(self.__client_name)+"     "+str(self.__nr_of_books_rented)

    def get_nr_of_books_rented(self):
        return self.__nr_of_books_rented