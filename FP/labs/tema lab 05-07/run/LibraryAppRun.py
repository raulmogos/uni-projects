
'''
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
'''
from settings.read_settings_txt import Settings
#we read from file the files an the we run
settings = Settings("settings.txt")