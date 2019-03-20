from Models.Client import Client
from errors.Errors import *
from undo_redo.Unod_Redo import FunctionCall, Operation, CascadeOperations

class ClientService:

    def __init__(self, valid, repo, undoService, rentalRepo, bookRepo):
        self.__valid = valid
        self.__repoClient = repo
        self.__undoService = undoService
        self.__rentalRepo = rentalRepo
        self.__bookRepo = bookRepo

    def createClient(self, client_id, name):
        client = Client(client_id, name)
        return client

    def addClient(self, client):
        self.__repoClient.add(client)
        # undo for add
        undo = FunctionCall(self.deleteClient, client.get_client_id())
        redo = FunctionCall(self.addClient, client)
        operation = Operation(undo, redo)
        self.__undoService.add_operation(operation)

    def updateClient(self, client_id, client_new_name):
        client_new = self.createClient(client_id, client_new_name)
        client_old = self.searchClientById(client_id)
        self.__repoClient.update(client_old, client_new)
        # undo for the update
        undo = FunctionCall(self.updateClient, client_id, client_old.get_name())
        redo = FunctionCall(self.updateClient, client_id, client_new_name)
        operation = Operation(undo, redo)
        self.__undoService.add_operation(operation)

    def getAllClients(self):
        return self.__repoClient.getAll()

    def deleteClient(self, client_id):
        client = self.searchClientById(client_id)
        self.__repoClient.remove(client)
        # undo for delete
        undo = FunctionCall(self.addClient, client)
        redo = FunctionCall(self.deleteClient, client_id)
        operation = Operation(undo, redo)

        co = CascadeOperations()
        co.add(operation)

        rent = []
        for rental in self.__rentalRepo.getAll():
            if client_id == rental.get_client_id():
                rent.append(rental)

        for rental in rent:
            self.removeRentalForUndo(rental)

        if len(rent) != 0:
            for rental in rent:
                undo = FunctionCall(self.addRentalForUndo, rental)
                redo = FunctionCall(self.removeRentalForUndo, rental)
                operation_cas = Operation(undo, redo)
                co.add(operation_cas)
        self.__undoService.add_operation(co)


    def removeRentalForUndo(self, rental):
        if rental not in self.__rentalRepo.getAll():
            return
        self.__rentalRepo.remove(rental)
        for book in self.__bookRepo.getAll():
            if book.get_book_id() == rental.get_book_id():
                book.set_availability(True)
                return

    def addRentalForUndo(self, rental):
        self.__rentalRepo.add(rental)
        for book in self.__bookRepo.getAll():
            if book.get_book_id() == rental.get_book_id():
                book.set_availability(False)
                return


    def searchClientById(self, client_id):
        client = Client(client_id, 'None')
        self.__valid.checkClientExistence(client, self.__repoClient.getAll())
        for cl in self.__repoClient.getAll():
            if cl.get_client_id() == client_id:
                return cl

    def searchClientByName(self, client_name):
        for cl in self.__repoClient.getAll():
            if cl.get_name() == client_name:
                return cl
        raise RepoError('no such a name')