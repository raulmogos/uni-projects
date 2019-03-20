'''

'''

class Book:
    '''
    class for book

    create a field-true/false = available/not available

    '''
    def __init__(self, bookID, title, description, author, availability):
        self.__bookID = bookID
        self.__title = title
        self.__description = description
        self.__author = author
        self.__availability = availability

    def __str__(self):
        return str(self.__bookID)+', '+self.__title+', '+self.__description+', '+self.__author+', '+self.__available_to_str(self.__availability)


    def __eq__(self, value):
        return self.__bookID == value.__bookID


    def get_book_id(self):
        return self.__bookID


    def get_title(self):
        return self.__title


    def get_description(self):
        return self.__description


    def get_author(self):
        return self.__author


    def set_book_id(self, value):
        self.__bookID = value


    def set_title(self, value):
        self.__title = value


    def set_description(self, value):
        self.__description = value


    def set_author(self, value):
        self.__author = value

    def set_availability(self, value):
        self.__availability = value

    def get_availability(self):
        return self.__availability

    def __available_to_str(self, state):
        if state == True:
            return 'available'
        return 'unavailable'

    '''
    bookID = property(get_book_id, set_book_id, None, None)
    title = property(get_title, set_title, None, None)
    description = property(get_description, set_description, None, None)
    author = property(get_author, set_author, None, None)
    '''