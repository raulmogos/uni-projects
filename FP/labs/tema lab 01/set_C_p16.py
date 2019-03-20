def gen(n):
    '''
        program that generates the largest number smaller than n
    '''

    n=n-1 # the number must be smaller
    
    while perfect_number(n)==False and n>0:
        n=n-1

    if n==0 : return False

    return n

def perfect_number(p):
    '''
        checks if a number p is perfect or not 
    '''
    s=1
    t=p
    for i in range(2,p):
        if p%i==0 : s=s+i
    if p==s : return True
    return False





def run_ui():
    while True:
        N = input("enter a number : ")
        N = int(N)

        if gen(N)==False:
            print ('there is not a such number ')
        else : print (gen(N))


def test():
    assert perfect_number(6)==True
    assert perfect_number(5)==False
    assert perfect_number(8)==False


test()
run_ui()





