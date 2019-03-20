from unittest import TestCase
from undo_redo.Unod_Redo import *

class TestUndoService(TestCase):

    def incr(self,a):
        a+=1

    def decr(self,a):
        a-=1

    def setUp(self):
        self.__var = 5
        redo = FunctionCall(self.incr,self.__var)
        undo = FunctionCall(self.decr,self.__var)
        operation = Operation(undo ,redo)
        self.serviceUndo = UndoService()
        self.serviceUndo.add_operation(operation)

    def test_add_operation(self):
        self.assertEqual(self.serviceUndo.get_list_lenght(),0)
        redo = FunctionCall(self.incr, self.__var+1)
        undo = FunctionCall(self.decr, self.__var+1)
        operation = Operation(undo, redo)
        self.serviceUndo.add_operation(operation)
        self.assertEqual(self.serviceUndo.get_list_lenght(),1)

    def test_undo(self):
        self.serviceUndo.undo()
        self.assertEqual(self.serviceUndo.get_list_lenght(),-1)

    def test_redo(self):
        self.serviceUndo.undo()
        self.assertEqual(self.serviceUndo.get_list_lenght(), -1)
        self.serviceUndo.redo()
        self.assertEqual(self.serviceUndo.get_list_lenght(), 0)
