from logic_functions import *


def tests():
    c={4:5}
    assert getReal(c) == 4
    c = {0: 6}
    assert getReal(c) == 0
    c = {-9: 5}
    assert getReal(c) == -9

    c = {4: 5}
    assert getImag(c) == 5
    c = {9:9}
    assert getImag(c) == 9
    c = {9:0}
    assert getImag(c) == 0

    c = {3:4}
    assert getModulo(c) == 5
    c = {-3: 0}
    assert getModulo(c) == 3
    c = {0: -14}
    assert getModulo(c) == 14

    c = {8:0}
    assert isReal(c) == True
    c = {78: -776}
    assert isReal(c) == False

    assert creatComplex(5,6) == {5:6}

    #assert sumOfComponents(lst,start_position,end_position)





