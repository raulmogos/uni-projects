
from Repository.binary_files_repo.binary_file_books import FileBookRepositoryBinary
from Repository.binary_files_repo.binary_file_client import FileClientRepositoryBinary
from Repository.binary_files_repo.binary_file_rentals import FileRentalRepositoryBinary

from ui_package.ui_console_module import Console

from Service.book_service import BookService
from Service.client_service import ClientService
from Service.rental_service import RentalService

from undo_redo.Unod_Redo import UndoService

from Repository.repo import RepoData
from Repository.txt_files_repo.FileRepoBook import FileBookRepository
from Repository.txt_files_repo.FileRepoClient import FileClientRepository
from Repository.txt_files_repo.FileRepoRental import FileRentalRepository

from Validation.Validator import Validator



class Settings:

    def __init__(self, file_name_settings):
        self.__file_name_settings = file_name_settings
        self.__readAllFromFileTxt()

    def __readAllFromFileTxt(self):
        try:
            with open(self.__file_name_settings, "r") as file:
                lines = file.readlines()
                dict_of_lines = {}
                for line in lines:
                    lst = line.split("=")
                    dict_of_lines[lst[0].strip()] = lst[1].strip().strip('"')
        except FileNotFoundError:
            print("Inexistent file : " + self.__file_name_settings)

        if dict_of_lines['repository'] == 'inmemory':
            pass
        elif dict_of_lines['repository'] == 'text files':
            bookRepo = FileBookRepository(dict_of_lines['books'])
            clientRepo = FileClientRepository(dict_of_lines['clients'])
            rentalRepo = FileRentalRepository(dict_of_lines['rentals'])
        elif dict_of_lines['repository'] == 'binary files':
            bookRepo = FileBookRepositoryBinary(dict_of_lines['books'])
            clientRepo = FileClientRepositoryBinary(dict_of_lines['clients'])
            rentalRepo = FileRentalRepositoryBinary(dict_of_lines['rentals'])

        valid = Validator()
        undoService = UndoService()

        serviceBook = BookService(valid, bookRepo, undoService, rentalRepo)
        serviceClient = ClientService(valid, clientRepo, undoService, rentalRepo, bookRepo)
        serviceRental = RentalService(valid, rentalRepo, serviceBook, serviceClient, undoService)

        if dict_of_lines['ui'] == 'gui':
            ui = Console(serviceBook, serviceClient, serviceRental, undoService)
        else:
            ui = Console(serviceBook, serviceClient, serviceRental, undoService)
        ui.runUI()