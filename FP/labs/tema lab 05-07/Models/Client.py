'''

'''

class Client:
    '''
    class for client
    '''
    def __init__(self, clientID, name):
        self.__clientID = clientID
        self.__name = name

    def __str__(self):
        return str(self.__clientID)+', '+self.__name

    def __eq__(self, other):
        return self.__clientID == other.__clientID

    def get_client_id(self):
        return self.__clientID


    def get_name(self):
        return self.__name


    def set_client_id(self, value):
        self.__clientID = value


    def set_name(self, value):
        self.__name = value

    '''
    clientID = property(get_client_id, set_client_id, None, None)
    name = property(get_name, set_name, None, None)
    '''
