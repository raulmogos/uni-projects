

class MostRentedAuthorDTO:

    def __init__(self, author, nr_of_times_rented):
        self.__author = author
        self.__nr_of_times_rented = nr_of_times_rented

    def __str__(self):
        return str(self.__author)+"     "+str(self.__nr_of_times_rented)

    def get_nr_of_times_rented(self):
        return self.__nr_of_times_rented