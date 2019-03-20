
def e_prim(x):
    '''
    FUNCTION FOR DETERMINING IF THE GIVEN PARAMETER X (INTEGER) IS PRIME OR NOT
    INPUT : X - INTEGER
    PRECONDITION : -
    OUTPUT: R - BOOLEAN
    POSTCONDITION: R = True IF X IS PRIME
                       False OTHERWISE
    '''
    if x<2:
        return False
    if x==2:
        return True
    if x % 2 == 0:
        return False
    i=3
    #WE ONLY GO TO THE SQUARE ROOT OF X FOR OPTIMIZATION PURPOSES 
    while i*i<=x:
        if x % i == 0:
            return False
        i+=2
    return True

def invers(x):
    rez = 0
    while x>0:
        u = x % 10 
        rez = rez*10 + u
        x //= 10
    return rez

def e_palin(x):
    '''
    FUNCTION FOR DETERMINING IF THE GIVEN PARAMETER X (INTEGER) IS PALINDROME OR NOT
    INPUT : X - INTEGER
    PRECONDITION : -
    OUTPUT: R - BOOLEAN
    POSTCONDITION: R = True IF X IS PRIME
                       False OTHERWISE
    '''
    return x==invers(x)
    

def afiseaza_prim(x,r):
    '''
    FUNCTION THAT, GIVEN A NUMBER X (INTEGER) AND THE RESULT R OF A PRIMALITY TEST (BOOL)
    PRINTS WHETHER THE NUMBER X IS PRIME OR NOT TO THE STD OUTPUT
    INPUT : X - INTEGER, R - BOOLEAN
    PRECONDITION : R = True IF X IS PRIME
                       False OTHERWISE
    OUTPUT: -
    POSTCONDITION: -
    '''
    if r:
        print(str(x)+"is prime")
    else:
        print(str(x)+"is NOT prime")

def afiseaza_palin(x,r):
    '''
    FUNCTION THAT, GIVEN A NUMBER X (INTEGER) AND THE RESULT R OF A PALIN TEST (BOOL)
    PRINTS WHETHER THE NUMBER X IS PALIN OR NOT TO THE STD OUTPUT
    INPUT : X - INTEGER, R - BOOLEAN
    PRECONDITION : R = True IF X IS PRIME
                       False OTHERWISE
    OUTPUT: -
    POSTCONDITION: -
    '''
    if r:
        print(str(x)+"is palin")
    else:
        print(str(x)+"is NOT palin")


def ui_prime():
    try:
        x = input("Please give a number:")
        x = int(x)
        r = e_prim(x)
        afiseaza_prim(x,r)
    except ValueError as v:
        print("invalid input!")

def ui_palin():
    try:
        x = input("Please give a number:")
        x = int(x)
        r = e_palin(x)
        afiseaza_palin(x,r)
    except ValueError as v:
        print("invalid input!")

        
def run():
    while True:
        x = input("Please give a valid command:")
        if x=="exit":
            return
        if x == "prime":
            ui_prime()
        if x == "palin":
            ui_palin()
        

def test_e_prim():
    assert e_prim(13)==True
    assert e_prim(0)==False
    assert e_prim(-2)==False
    assert e_prim(1)==False
    assert e_prim(-5)==False
    assert e_prim(2)==True
    assert e_prim(4)==False

test_e_prim()
run()

