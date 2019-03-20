'''
    ui functions
'''

from logic_functions import *



def addUI(lst):
    '''
    :param lst:
    :return:
    '''
    while True:
        try:
            real = int(input('please enter the real part of the number real= '))
            break
        except ValueError as ve:
            print('that is not a number ')
    while True:
        try:
            imag = int(input('please enter the imaginary part of the number imag= '))
            break
        except ValueError as ve:
            print('that is not a number ')

    addToList(lst, creatComplex(real, imag))


def insertUI(lst):
    '''
    :param lst:
    :return:
    '''
    while True:
        try:
            real = int(input('please enter the real part of the number real= '))
            break
        except ValueError as ve:
            print('that is not a number ')
    while True:
        try:
            imag = int(input('please enter the imaginary part of the number imag= '))
            break
        except ValueError as ve:
            print('that is not a number ')
    number = creatComplex(real, imag)
    while True:
        try:
            position = int(input('please enter the position p= '))
            break
        except ValueError as ve:
            print('that is not an integer number ')

    insertToList(position, number, lst)


def removeOneUI(lst):
    while True:
        position = input('please enter the position p= ')
        try:
            position = int(position)
            removeElementAtPosition(position, lst)
            break
        except ValueError as ve:
            print('that is not an integer number ')
        except IndexError as we:
            print('number bigger than list lenght ')


def removeMoreUI(lst):
    while True:
        start_position = input('please enter the start position start= ')
        end_position = input('please enter the end position end= ')
        try:
            start_position = int(start_position)
            end_position = int(end_position)
            removeMore(start_position, end_position, lst)
            break
        except ValueError as ve:
            print('that is not an integer number ')
        except IndexError as ie:
            print('number bigger than list lenght ')


def removeUI(lst):
    print('\t one ')
    print('\t more ')
    while True:
        comand = input('Enter a comand: ')
        comand = comand.replace(' ', '')

        if comand == 'one':
            removeOneUI(lst)
            break
        elif comand == 'more':
            removeMoreUI(lst)
            break
        else:
            print('enter a valid comand ')


def replaceUI(lst):
    while True:
        try:
            real = int(input('please enter the real part of the number you want to replace real= '))
            break
        except ValueError as ve:
            print('that is not a number ')
    while True:
        try:
            imag = int(input('please enter the imaginary part of the number you want to replace imag= '))
            break
        except ValueError as ve:
            print('that is not a number ')
    number_to_remove = creatComplex(real, imag)
    while True:
        try:
            real = int(input('please enter the real part of the number you want to replace with real= '))
            break
        except ValueError as ve:
            print('that is not a number ')
    while True:
        try:
            imag = int(input('please enter the imaginary part of the number you want to replace with imag= '))
            break
        except ValueError as ve:
            print('that is not a number ')
    number_to_add = creatComplex(real, imag)
    replace_X_With_Y(number_to_remove, number_to_add, lst)


def printList(lst):
    print(lst)


def listRealUI(lst):
    while True:
        try:
            start_position = int(input('please enter the start position s= '))
            break
        except ValueError as ve:
            print('this is not a number ')

    while True:
        try:
            end_position = int(input('please enter the end position e= '))
            break
        except ValueError as ve:
            print('this is not a number ')

    if end_position > len(lst):
        end_position = len(lst)
    else:
        end_position += 1

    for i in range(start_position, end_position):
        if isReal(lst[i]) == True:
            print(lst[i])


def smaller_nr(lst, nr):
    for i in lst:
        if getModulo(i) < nr:
            print(i)


def equal_nr(lst, nr):
    for i in lst:
        if getModulo(i) == nr:
            print(i)


def bigger_nr(lst, nr):
    for i in lst:
        if getModulo(i) > nr:
            print(i)


def listModuloUI(lst):
    dict_operator = {'<': smaller_nr, '=': equal_nr, '>': bigger_nr}
    print('\t   <  =  >  ')
    operator = input('enter an operator ')

    operator.replace(' ', '')
    if operator == '<' or operator == '=' or operator == '>':
        pass
    else:
        listModuloUI(lst)

    while True:
        try:
            nr = int(input('please enter anumber  n = '))
            break
        except ValueError as ve:
            print('this is not a number ')

    if operator in dict_operator:
        dict_operator[operator](lst, nr)


def ListUI(lst):
    print('\t list ')
    print('\t real ')
    print('\t modulo')

    while True:
        comand = input('Enter a comand: ')
        comand = comand.replace(' ', '')

        if comand == 'list':
            printList(lst)
            break
        elif comand == 'real':
            listRealUI(lst)
            break
        elif comand == 'modulo':
            listModuloUI(lst)
            break
        else:
            print('enter a valid comand ')


def sumUI(lst):
    while True:
        try:
            start_position  = int(input('please enter the start position p_i= '))
            valid_position(lst,start_position)
            break
        except ValueError as ve:
            print(ve)
    while True:
        try:
            end_position  = int(input('please enter the end position p_e= '))
            valid_position(lst,end_position)
            break
        except ValueError as ve:
            print(ve)
    print('the sum is: ',sumOfComponents(lst,start_position,end_position))


def productUI(lst):
    while True:
        try:
            start_position  = int(input('please enter the start position p_i= '))
            valid_position(lst,start_position)
            break
        except ValueError as ve:
            print(ve)
    while True:
        try:
            end_position  = int(input('please enter the end position p_e= '))
            valid_position(lst,end_position)
            break
        except ValueError as ve:
            print(ve)
    print('the product is: ',productOfComponents(lst,start_position,end_position))


def filterModuloUI(lst):
    print('\t < ')
    print('\t =')
    print('\t > ')
    while True:
        command = input('please input a command: ')
        if command == '<' :
            while True:
                try:
                    number = int(input('enter a number n= '))
                    filterSmallerThan(lst,number)
                except ValueError as ve:
                    print(ve)
                break
            break
        elif command == '=' :
            while True:
                try:
                    number = int(input('enter a number n= '))
                    filterEqualTo(lst,number)
                except ValueError as ve:
                    print(ve)
                break
            break
        elif command == '>' :
            while True:
                try:
                    number = int(input('enter a number n= '))
                    filterBiggerThan(lst,number)
                except ValueError as ve:
                    print(ve)
                break
            break
        else:
            print('please input a valid command')


def filterUI(lst):
    print('\t real ')
    print('\t modulo')
    while True:
        command = input('please input a command: ')
        if command == 'real' :
            filterReal(lst)
            break
        elif command == 'modulo' :
            filterModuloUI(lst)
            break
        else:
            print('please input a valid command')


def printUndo(undo_list):
    print(undo_list)

'''
//////////////////////////////////////////////
'''



def printMenu():
    print('\t add ')
    print('\t insert ')
    print('\t remove ')
    print('\t replace ')
    print('\t list ')
    print('\t sum ')
    print('\t product')
    print('\t filter')
    print('\t undo')
