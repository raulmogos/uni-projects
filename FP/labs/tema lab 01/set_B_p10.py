import math




def product(n):
    '''
        product of proper factors of n 
    '''

    sq=int(math.sqrt(n)) #the square root of n - integer
    p=1
    nr=0
    
    for i in range (2,sq+1):
        if n%i==0: nr+=1

    p=n**nr #the product is n to the power of nr

    if sq==math.sqrt(n) : #checks if it is perfect square
        p=int(p/sq)
        
    return p


def run_ui():
    while True:
        x = input("enter a number: ")
        x = int(x)
        print(product(x))



def test():
    assert product(2) == 1
    assert product(12) == 144
    assert product(16) == 64
    assert product(8) == 8
    assert product(9) == 3




test()
run_ui()





