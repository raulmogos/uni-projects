from Repository.repo import RepoData
from Models.Client import Client

class FileClientRepository(RepoData):

    def __init__(self, fileName):
        RepoData.__init__(self)
        self.__fileName = fileName
        self.__readAllFromFile()

    def __readAllFromFile(self):
        try:
            with open(self.__fileName, "r") as file:
                lines = file.readlines()
                for line in lines:
                    words = line.strip().split(',')
                    if len(words) == 2:
                        client_id = int(words[0].strip())
                        client_name = words[1].strip()
                        client = Client(client_id, client_name)
                        RepoData.add(self, client)
        except FileNotFoundError:
            print("Inexistent file : " + self.__fileName)

    def __writeAllToFile(self):
        try:
            with open(self.__fileName, "w") as file:
                for client in self._lst:
                    file.write(str(client) + "\n")
        except FileNotFoundError:
            print("Inexistent file : " + self.__fileName)

    def add(self, client):
        RepoData.add(self, client)
        self.__writeAllToFile()

    def remove(self, client):
        RepoData.remove(self, client)
        self.__writeAllToFile()
