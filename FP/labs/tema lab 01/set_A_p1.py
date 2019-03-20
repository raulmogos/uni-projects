'''
    PROGRAM THAT GENERATES THE FIRTS PRIME NUMBER AFTER A NUMBER N
    INPUT: N - a natural number
    OUTPU: P - THE FIRTS PRIME NUMBER AFTER N
'''


def e_prim(x):
    '''
        FUNCTION THAT CHECKS IF X PRIME OR NOT
        INPUT: X -  a number
        OUTPUT: TRUE - IF X IS PRIEM
                FALSE - OTHERWISE
    '''
    if x<2 :
        return False
    if x==2:
        return True
    if x%2==0:
        return False

    i=3
    while i*i<=x :
        if x%i==0: return False
        i+=2

    return True


def gen(n):
    '''
        FUNCTION THAT GENERATE THE FIRST PRIME NUMBER AFTER n
    '''
    if e_prim(n)==True:
        n+=1

    if n%2==0:
        n+=1
    
    while e_prim(n)==False:
        n+=2
     
    return n



def run_ui():
    while True:
        N = input("Enter a number : ")
        N = int(N)
        P = gen(N)
        print("the first prime number larger than ",N," is : ",P)




def test_e_prim():
    assert e_prim(13)==True
    assert e_prim(0)==False
    assert e_prim(-2)==False
    assert e_prim(1)==False
    assert e_prim(-5)==False
    assert e_prim(2)==True
    assert e_prim(4)==False

def test_gen():
    assert gen(10)==11
    assert gen(14)==17




test_e_prim()
test_gen()
run_ui()





























