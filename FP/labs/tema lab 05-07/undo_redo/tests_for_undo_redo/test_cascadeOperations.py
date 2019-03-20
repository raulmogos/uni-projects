from unittest import TestCase
from undo_redo.Unod_Redo import *

class TestCascadeOperations(TestCase):

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
        self.co = CascadeOperations()

    def test_add(self):
        redo = FunctionCall(self.incr, self.__var+1)
        undo = FunctionCall(self.decr, self.__var+1)
        operation1 = Operation(undo, redo)
        redo = FunctionCall(self.incr, self.__var+2)
        undo = FunctionCall(self.decr, self.__var+2)
        operation2 = Operation(undo, redo)
        self.co.add(operation1)
        self.co.add(operation2)
        self.serviceUndo.add_operation(self.co)
        self.assertEqual(1, self.serviceUndo.get_list_lenght())

    def test_undo(self):
        redo = FunctionCall(self.incr, self.__var + 1)
        undo = FunctionCall(self.decr, self.__var + 1)
        operation1 = Operation(undo, redo)
        redo = FunctionCall(self.incr, self.__var + 2)
        undo = FunctionCall(self.decr, self.__var + 2)
        operation2 = Operation(undo, redo)
        self.co.add(operation1)
        self.co.add(operation2)
        self.serviceUndo.add_operation(self.co)
        self.serviceUndo.undo()
        self.assertEqual(0, self.serviceUndo.get_list_lenght())

    def test_redo(self):
        redo = FunctionCall(self.incr, self.__var + 1)
        undo = FunctionCall(self.decr, self.__var + 1)
        operation1 = Operation(undo, redo)
        redo = FunctionCall(self.incr, self.__var + 2)
        undo = FunctionCall(self.decr, self.__var + 2)
        operation2 = Operation(undo, redo)
        self.co.add(operation1)
        self.co.add(operation2)
        self.serviceUndo.add_operation(self.co)
        self.serviceUndo.undo()
        self.assertEqual(0, self.serviceUndo.get_list_lenght())
        self.serviceUndo.redo()
        self.assertEqual(1, self.serviceUndo.get_list_lenght())
