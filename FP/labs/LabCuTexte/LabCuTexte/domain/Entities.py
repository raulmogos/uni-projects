class Balla(object):
    
    
    def __init__(self, ident, name, value):
        self.__ident = ident
        self.__name = name
        self.__value = value

    def __str__(self):
        return str(self.__ident)+","+self.__name+","+str(self.__value)


    def get_ident(self):
        return self.__ident


    def get_name(self):
        return self.__name


    def get_value(self):
        return self.__value


    def set_name(self, value):
        self.__name = value


    def set_value(self, value):
        self.__value = value

    ident = property(get_ident, None, None, None)
    name = property(get_name, set_name, None, None)
    value = property(get_value, set_value, None, None)
    
    



