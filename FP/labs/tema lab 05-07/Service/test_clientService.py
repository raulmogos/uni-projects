from unittest import TestCase
from Validation.Validator import Validator
from Service.client_service import ClientService
from Repository.repo import RepoData
from undo_redo.Unod_Redo import UndoService, FunctionCall


class TestClientService(TestCase):
    def setUp(self):
        self.clientRepo = RepoData()
        self.valid = Validator()
        self.UndoService = UndoService()
        self.rentalRepo = RepoData()
        self.bookRepo = RepoData()
        self.serviceClient = ClientService(self.valid, self.clientRepo, self.UndoService, self.rentalRepo,
                                           self.bookRepo)

    def test_createClient(self):
        client = self.serviceClient.createClient(765, 'gigi')
        self.assertEqual(765, client.get_client_id())
        self.assertEqual('gigi', client.get_name())

    def test_addClient(self):
        client1 = self.serviceClient.createClient(765, 'gigi')
        client2 = self.serviceClient.createClient(769, 'popa')
        self.serviceClient.addClient(client1)
        self.serviceClient.addClient(client2)
        self.assertEqual(2, len(self.serviceClient.getAllClients()))

    def test_getAllClients(self):
        client1 = self.serviceClient.createClient(765, 'gigi')
        client2 = self.serviceClient.createClient(769, 'popa')
        self.serviceClient.addClient(client1)
        self.assertEqual(1, len(self.serviceClient.getAllClients()))
        self.serviceClient.addClient(client2)
        self.assertEqual(2, len(self.serviceClient.getAllClients()))

    def test_deleteClient(self):
        client1 = self.serviceClient.createClient(765, 'gigi')
        client2 = self.serviceClient.createClient(769, 'popa')
        self.serviceClient.addClient(client1)
        self.serviceClient.addClient(client2)
        self.assertEqual(2, len(self.serviceClient.getAllClients()))
        self.serviceClient.deleteClient(765)
        self.assertEqual(1, len(self.serviceClient.getAllClients()))

    def test_searchClientById(self):
        client1 = self.serviceClient.createClient(765, 'gigi')
        client2 = self.serviceClient.createClient(769, 'popa')
        self.serviceClient.addClient(client1)
        self.serviceClient.addClient(client2)
        client = self.serviceClient.searchClientById(769)
        self.assertEqual(client, client2)

    def test_searchClientByName(self):
        client1 = self.serviceClient.createClient(765, 'gigi')
        client2 = self.serviceClient.createClient(769, 'popa')
        self.serviceClient.addClient(client1)
        self.serviceClient.addClient(client2)
        client = self.serviceClient.searchClientByName('popa')
        self.assertEqual(client, client2)

    def test_updateClient(self):
        client1 = self.serviceClient.createClient(765, 'gigi')
        self.clientRepo.add(client1)
        self.serviceClient.updateClient(765,'hagi')
        self.assertEqual('hagi', self.serviceClient.getAllClients()[0].get_name())
