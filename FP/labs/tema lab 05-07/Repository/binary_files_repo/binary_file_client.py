from Repository.repo import RepoData
from Models.Client import Client
import pickle

class FileClientRepositoryBinary(RepoData):

    def __init__(self, file_name):
        RepoData.__init__(self)
        self.__file_name = file_name
        self.__readAllBinaryFromFile()

    def __readAllBinaryFromFile(self):
        try:
            with open(self.__file_name, "rb") as binary_file:
                list_of_clients = pickle.load(binary_file)
            for client in list_of_clients:
                RepoData.add(self, client)
        except FileNotFoundError:
            print("Inexistent file : " + self.__file_name)

    def __writeAllBinaryToFile(self):
        try:
            with open(self.__file_name, "wb") as binary_file:
                pickle.dump(self._lst, binary_file)
        except FileNotFoundError:
            print("Inexistent file : " + self.__file_name)

    def add(self, client):
        RepoData.add(self, client)
        self.__writeAllBinaryToFile()

    def remove(self, client):
        RepoData.remove(self, client)
        self.__writeAllBinaryToFile()

'''
ahah = FileClientRepositoryBinary('clients.pickle')
for i in ahah.getAll():
    print(i)

b = Client(999,'gigi')

ahah.remove(b)

for i in ahah.getAll():
    print(i)
'''