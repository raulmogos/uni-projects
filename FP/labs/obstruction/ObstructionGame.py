from texttable import Texttable
from random import randint

class GameException(Exception):
    pass

class Square():
    def __init__(self, row, col):
        self.__row = row
        self.__col = col
    @property
    def row(self):
        return self.__row
    @property
    def col(self):
        return self.__col

class Board():
    def __init__(self, no_of_rows, no_of_columns):
        '''

        :param no_of_rows:
        :param no_of_columns:
        '''
        self.__rows = no_of_rows
        self.__columns = no_of_columns
        self.__data = [[0 for i in range(self.__columns)] for j in range(self.__rows)]
        self.__rows_list = []
        for i in range(self.__rows):
            self.__rows_list.append(i)
        self.__columns_list = []
        for i in range(self.__columns):
            self.__columns_list.append(i)

    def move(self, square, symbol):
        '''
            input : square - Square instance
                    symbol - a character : 'x' or 'o'
            output: sets the board acordingly
        '''

        if square.row not in self.__rows_list or square.col not in self.__columns_list:
            raise GameException("Move outside board!")
        if symbol not in ['X', 'O']:
            raise GameException("Invalid symbol!")
        if self.__data[square.row][square.col] != 0:
            raise GameException("Square already taken!")

        self.__data[square.row][square.col] = symbol
        if square.row+1 in self.__rows_list and self.__data[square.row+1][square.col]==0:
            self.__data[square.row + 1][square.col] = '+'
        if square.row-1 in self.__rows_list and self.__data[square.row-1][square.col]==0:
            self.__data[square.row - 1][square.col] = '+'
        if square.col+1 in self.__columns_list and self.__data[square.row][square.col+1]==0:
            self.__data[square.row][square.col+1] = '+'
        if square.col-1 in self.__columns_list and self.__data[square.row][square.col-1]==0:
            self.__data[square.row][square.col-1] = '+'
        if square.col - 1 in self.__columns_list and square.row - 1 in self.__rows_list and self.__data[square.row - 1][square.col - 1] == 0:
            self.__data[square.row - 1][square.col - 1] = '+'
        if square.col - 1 in self.__columns_list and square.row + 1 in self.__rows_list and self.__data[square.row + 1][square.col - 1] == 0:
            self.__data[square.row + 1][square.col - 1] = '+'
        if square.col + 1 in self.__columns_list and square.row + 1 in self.__rows_list and self.__data[square.row + 1][square.col + 1] == 0:
            self.__data[square.row + 1][square.col + 1] = '+'
        if square.col + 1 in self.__columns_list and square.row - 1 in self.__rows_list and self.__data[square.row - 1][square.col + 1] == 0:
            self.__data[square.row - 1][square.col + 1] = '+'

    def getEmptySquares(self):
        '''
        function that return a list with the empty equares
        :return: list of squares
        '''
        empty_squares = []
        for i in range(self.__rows):
            for j in range(self.__columns):
                if self.__data[i][j] == 0:
                    empty_squares.append(Square(i,j))
        return empty_squares

    def isWon(self):
        '''
        function that checks if the game finishes
        :return:
        '''
        if self.getEmptySquares() == []:
            return True
        return False

    def __str__(self):
        '''
        function that returns the str
        :return:
        '''
        t = Texttable()
        p = []
        p.append(' ')
        p = p + self.__columns_list
        #t.header(p)
        t.add_row(p)
        ds = {0:' ', '+':'+', 'X':'X', 'O':'O'}
        for i in self.__rows_list:
            rez = self.__data[i][:]
            for j in self.__columns_list:
                rez[j] = ds[rez[j]]
            l = []
            l.append(i)
            l = l + rez
            t.add_row(l)

        return t.draw()
    def getBoard(self):
        return self.__data

class Game():
    def __init__(self, no_of_rows=6, no_of_columns=6):
        self.__board = Board(no_of_rows, no_of_columns)
    def movePlayerOne(self, square):
        self.__board.move(square, 'X')
    def moveComputer(self):
        '''
        computer moves randomly
        :return:
        '''
        square_nr = randint(0, len(self.board.getEmptySquares()))
        self.__board.move(self.board.getEmptySquares()[square_nr], 'O')
    @property
    def board(self):
        return self.__board

class UI():
    def __init__(self, game):
        self.__game = game

    def readMove(self):
        while True:
            move = input("Enter the square(row, column): ")
            mv = move.strip().split(' ')
            try:
                row = int(mv[0].strip())
                col = int(mv[1].strip())
                break
            except ValueError:
                print("Invaild move!")
        return Square(row, col)

    def start(self):
        while True:
            try:
                n = input("Enter the size of the board: ")
                size = n.strip().split(' ')
                self.__game = Game(int(size[0].strip()), int(size[1].strip()))
                break
            except ValueError:
                print("Invalid size!")

        move_palyer_bool = 1
        while self.__game.board.isWon() == False:
            print(self.__game.board)
            try:
                if move_palyer_bool%2==1:
                    #moves playes one
                    move_square = self.readMove()
                    self.__game.movePlayerOne(move_square)
                else:
                    #moves player two
                    self.__game.moveComputer()
            except GameException as ge:
                print(ge)
                move_palyer_bool -= 1
            move_palyer_bool+=1

        print(self.__game.board)
        #print(self.__game.board.isWon())
        #print(move_palyer_bool)
        if move_palyer_bool%2==1:
            print("Computer wins!")
            print("Player one has lost!")
        else:
            print("Player one won!")
            print("Computer has lost!")
