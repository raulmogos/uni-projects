'''
        Raul Mogos
        assigment 3-4
'''

import copy
from test_module import *
from logic_functions import *
from UI_module import *

'''
///////////////////////////////////////////////////////////////////////////////////////////////////////////////
'''

def start():
    '''
    list_rational_numbers = [{4:5}, {-77:0}, {78:9}, {-77:0}, {65:0}, {23:-43}]
    undo_l = [[{4:5}, {-77:0}, {78:9}, {-77:0}, {65:0}, {23:-43}]]
    '''
    list_rational_numbers = [{'re':4,'im':5}, {'re':-77,'im':0}, {'re':78,'im':9}, {'re':-77,'im':0}, {'re':65,'im':0}, {'re':23,'im':-43}]
    undo_l = [{'re':4,'im':5}, {'re':-77,'im':0}, {'re':78,'im':9}, {'re':-77,'im':0}, {'re':65,'im':0}, {'re':23,'im':-43}]
    undo_list = []
    undo_list[:] = copy.deepcopy(undo_l)

    dict_comands = {
        'add':addUI,
        'insert':insertUI,
        'remove':removeUI,
        'replace': replaceUI,
        'list':ListUI ,
        'sum':sumUI,
        'product':productUI,
        'filter':filterUI
        }
    while True:
        print(list_rational_numbers)
        #printUndo(undo_list)
        printMenu()
        input_comand = input('>')

        input_comand = input_comand.replace(' ','')

        if input_comand in dict_comands.keys():
            dict_comands[input_comand](list_rational_numbers)
            addCommandToUndoList(list_rational_numbers, undo_list)
        elif input_comand == 'undo':
            undo(list_rational_numbers, undo_list)
        elif input_comand == 'exit':
            return
        else:
            print('Please enter a valid comand! ')


tests()
start()

'''
+ comentarii
+ teste
'''

