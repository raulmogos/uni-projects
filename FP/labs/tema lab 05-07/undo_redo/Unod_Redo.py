


class UndoService:

    def __init__(self):
        self.__undo_list = []
        self.__index = -1
        self.__during_undo = False

    def add_operation(self, operation):
        '''
        add an operation
        :return:
        '''
        # test if the function - add is called during an undo process
        if self.__during_undo == True:
            return
        # ... we delete the previous undos
        self.__undo_list = self.__undo_list[:self.__index + 1]
        # if no we add it to the list
        self.__undo_list.append(operation)
        # we modify the index, in order to control better switching between undo and redo
        self.__index = len(self.__undo_list) - 1
        #print(self.__index)
        #print(len(self.__undo_list))

    def undo(self):
        '''
        we do undo
        :return:
        '''
        if self.__index < 0:
            return False
        self.__during_undo = True
        self.__undo_list[self.__index].undo()
        self.__index -= 1
        #print(self.__index)
        #print(len(self.__undo_list))
        #print(self.__undo_list)
        self.__during_undo = False
        return True

    def redo(self):
        '''
        we do redo
        :return:
        '''
        if self.__index+1 >= len(self.__undo_list):
            return False
        self.__during_undo = True
        self.__index += 1
        self.__undo_list[self.__index].redo()
        #print(self.__index)
        #print(len(self.__undo_list))
        self.__during_undo = False
        return True

    def get_list_lenght(self):
        return self.__index

class FunctionCall:

    def __init__(self, function, *params):
        self.__function = function
        self.__params = params

    def call(self):
        self.__function(*self.__params)


class Operation:

    def __init__(self, undo, redo):
        self.__undo = undo
        self.__redo = redo

    def undo(self):
        self.__undo.call()

    def redo(self):
        self.__redo.call()

class CascadeOperations:
    def __init__(self):
        self.__list_operartions = []

    def add(self, operation):
        self.__list_operartions.append(operation)
        #print(len(self.__list_operartions))

    def undo(self):
        for op in self.__list_operartions:
            op.undo()

    def redo(self):
        for op in self.__list_operartions:
            print(op)
            op.redo()
