from unittest import TestCase
from ObstructionGame import Square, Board, Game


class TestSquare(TestCase):
    def setUp(self):
        self.__sq = Square(1, 2)

    def test_row(self):
        self.assertEqual(1, self.__sq.row)

    def test_col(self):
        self.assertEqual(2, self.__sq.col)


class TestBoard(TestCase):
    def setUp(self):
        self.__board = Board(5,5)

    def test_move(self):
        self.__board.move(Square(1,1),'X')
        #print(self.__board.getBoard())
        self.assertEqual(self.__board.getBoard()[1][1],'X')

    def test_getEmptySquares(self):
        self.__board = Board(3, 3)
        self.__board.move(Square(1,1),'X')
        #l = self.__board.getEmptySquares(), []
        self.assertEqual(self.__board.getEmptySquares(), [])

    def test_isWon(self):
        self.__board = Board(3, 3)
        self.__board.move(Square(1, 1), 'X')
        self.assertEqual(True, self.__board.isWon())
        self.__board = Board(4, 4)
        self.__board.move(Square(1, 1), 'X')
        self.assertEqual(False, self.__board.isWon())