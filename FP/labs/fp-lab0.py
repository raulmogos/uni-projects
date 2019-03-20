def e_prim(x):

    '''
        funtion for deteminig prime numbers
        IMPUT: X- INTEGER
        PRECONDITIONS: X>0
        OUTPUT: R-BOOLEAN
        POSTCONDITIONS: R-TRUE IF X IS PRIME
                         FLASE OHTERWISE

        !!! test driven development 
    '''
    
    if x<2:
        return False
    if x==2:
        return True

    if x%2==0:
        return False
    
    i=3
    #WE ONLY GO TO THE SQUARE ROOT OF X FOR OPTIMISATIONS
    while i*i<=x:
        if x%2==0:
            return False
        i+=2
    return False

def afisiaza_prim(x,r):

     '''
        funtion prints the answer
        IMPUT: X- INTEGER
        PRECONDITIONS: X>0
        

        !!! test driven development 
    '''
    if r:
        print(str(x)+"is prime")
    else
        print(str(x)+"not is prime")

def ui_print():
     x=int(x)
     r = e_prim(x)
     afisiaza_prim(x,r)

def run():
    while True:
       x = imput("please give a number")
    try
            x=int(x)
            r = e_prim(x)
            afisiaza_prim(x,r)
        except ValueError as v:
            print("imput invalid")

       x=int(x)
       print(type(x))


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
