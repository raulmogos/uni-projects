'''
        THE LOGIC MODULE
'''

import copy

def creatComplex(real,imag):
    '''
    :param real:
    :param imag:
    :return: a dictionary which is a complex
    '''
    return {real:imag}



def removeElementAtPosition(index,lst):
    '''
    :param index: position which will be deleted
    :param lst:
    :return:
    '''
    try:
        del lst[index]
    except:
        raise IndexError('index too big ')

def insertToList(index,number,lst):
    '''
    we insert a number at a given position
    :param index:  integer
    :param number: dictionary-complex
    :param lst: list
    :return:
    '''
    lst.insert(index,number)

def addToList(lst,n):
    '''
    we put a new element at edn of the list
    :param lst:
    :param n:
    :return:
    '''
    lst.append(n)

def removeMore(start_index,end_index,lst):
    '''
    we remove a sequence from star_index to end_index
    :param start_index: integer
    :param end_index: integer
    :param lst: list
    :return: modified list
    '''
    del lst[start_index:end_index+1]

def replace_X_With_Y(x,y,lst):
    '''
    we replace x with y in list lst
    :param x: integer
    :param y: integer
    :param lst: list
    :return: modified list
    '''
    for i in range(0,len(lst)):
        if lst[i] == x:
            insertToList(i,y,lst)
            removeElementAtPosition(i+1,lst)



def getReal(number):
    '''
    we get the real part of the complex dict
    :param number: complex dict
    :return: real part
    '''
    for key in number.keys():
        return key

def getImag(number):
    '''
    we get the imaginary part
    :param number: dict complex
    :return: imaginary part
    '''
    for key in number.keys():
        return number[key]
        

def getModulo(number):
    '''
    :param number: dict complex
    :return: modulo of complex
    '''
    return int((getImag(number)*getImag(number) + getReal(number)*getReal(number))**(1/2))

def isReal(number):
    '''
    we qsk if it is real or not
    :param number:
    :return:
    '''
    if int(getImag(number)) == 0 :
        return True
    return False



def sumOfComponents(lst,start_position,end_position):
    '''
    we comput the sum from start_postion to end_position
    :param lst: list
    :param start_position: intiger
    :param end_position: imteger
    :return: sum
    '''
    s_imag = 0
    s_real = 0
    if end_position + 1 <= len(lst):
        end_position+=1
    for i in range(start_position,end_position):
        s_real = s_real + getReal(lst[i])
        s_imag = s_imag + getImag(lst[i])
    return creatComplex(s_real,s_imag)

def valid_position(lst,position):
    '''
    we ask if it is a valid number or not
    :param lst:
    :param position:
    :return:
    '''
    if position > len(lst):
        raise ValueError('this value is bigger than the lenght of the list')

def productOfComponents(lst,start_position,end_position):
    '''
    we comput the product
    :param lst:
    :param start_position: integer
    :param end_position:integer
    :return:product
    '''
    Product = 1
    if end_position + 1 <= len(lst):
        end_position+=1
    for i in range(start_position,end_position):
        Product = Product * complex(getReal(lst[i]),getImag(lst[i]))
    return Product



def filterReal(lst):
    '''
    we remove all elements that are not real
    :param lst: list
    :return: list modified
    '''
    list_object = list(filter(isReal,lst))
    '''
    aur => lst[:] = copy.deepcopy(l)
    '''
    lst[:] = copy.deepcopy(list_object)

def filterSmallerThan(lst,number):
    '''
    <
    we eliminate all the elements that are bigger than number
    :param lst:
    :param number:
    :return:
    '''
    list_oject = list(filter(lambda x: getModulo(x)<number ,lst))
    lst[:] = copy.deepcopy(list_oject)

def filterEqualTo(lst,number):
    '''
    we eliminate all the numbers that are not equal to number
    :param lst:
    :param number:
    :return: lst modified
    '''
    list_oject = list(filter(lambda x: getModulo(x) == number, lst))
    lst[:] = copy.deepcopy(list_oject)

def filterBiggerThan(lst,number):
    '''
    >
    we eliminate all numbers that are smaller than number
    :param lst: list
    :param number:
    :return:
    '''
    list_oject = list(filter(lambda x: getModulo(x) > number, lst))
    lst[:] = copy.deepcopy(list_oject)



def addCommandToUndoList(lst,undo_list):
    '''
    we add the curent list to the undo list
    :param lst: curent list
    :param undo_list:
    :return: undo_list modified
    '''
    undo_list.append(copy.deepcopy(lst))

def undo(lst, undo_list):
    '''
    we undo the last operation made on the list
    :param lst:
    :param undo_list:
    :return: lst modified
    '''
    del undo_list[-1]
    try:
        lst[:] = copy.deepcopy(undo_list[-1])
    except IndexError as ie:
        print(ie)
