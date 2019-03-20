from errors.Errors import RepoError
from Repository.iterable_repo import IterableData

class RepoData:

    def __init__(self):
        '''
        we initialize a list
        '''
        self._lst = []
        #bug
        #self._lst = IterableData()

    def __len__(self):
        '''
        return the lenght of the list
        :return: the lenght(int)
        '''
        return len(self._lst)

    def add(self, element):
        '''
        we add a new element to the list
        :param element: object
        :return:
        '''
        if element in self._lst:
            raise RepoError('existing element')
        self._lst.append(element)

    def remove(self, element):
        '''
        we remove an element from the list
        :param element:
        :return:
        '''
        if element not in self._lst:
            raise RepoError('inexisting element')
        self._lst.remove(element)

    def update(self, old_element, new_element):
        self.remove(old_element)
        self.add(new_element)

    def getAll(self):
        '''
        :return: a copy of the list
        '''
        return self._lst[:]