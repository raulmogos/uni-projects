'''
Raul Mogos
lab02

1. Read a list of complex numbers (in z = a + bi form) from the keyboard.
2. Print the entire list of numbers.
3. Print to console the longest sequence that observes a given property. Each student will receive
2 of the properties from the list provided below.
4. Exit the application

schimba din tuple in lista
    getReal
    getImag
    setReal
    setImag
    createComplex
    

'''
def distinct_numbers_ui(t_tuple):
    print('the sequence of disctinct numbers is ')
    print(t_tuple)

def distinct_numbers(t_tuple):
    '''
        this function computes the longest sequence of disctinct numbers
        
        INPUT: A TUPLE OF COMPLEX NUMBERS
        OUTPUT: THE LONGEST SEQUENCE OF DISTINCT NUMBERS 
    '''
    
    k=0
    maxi=0
    p=0
    for i in range(0,len(t_tuple)-1):
        if t_tuple[i]!=t_tuple[i+1]:
            k+=1
        else:
            k+=1
            maxi_vechi=maxi
            maxi=max(maxi_vechi,k)
            k=0

            if maxi_vechi!=maxi:
                i_final = i
                i_initial = i - maxi +1

    # we do this in case the longest sequence is in the end 
    k+=1
    maxi_vechi=maxi
    maxi=max(maxi_vechi,k)
    k=0
    if maxi_vechi!=maxi:
        i_final = len(t_tuple)-1
        i_initial = len(t_tuple) - maxi

    # we do this in order to print it corectly
    i_final+=1

    return t_tuple[i_initial:i_final]

        

def getter (x):
    return x.real

def setter(x):
    return x.imag

def real_numbers_ui(t_tuple):
    print('the longest sequence of real numbers: ')
    print(t_tuple)

def real_numbers(t_tuple):
    '''
        this function computes the longest sequence of real numbers
        
        INPUT: A TUPLE OF COMPLEX NUMBERS
        OUTPUT: THE LONGEST SEQUENCE OF REAL NUMBERS 
    '''
    k=0
    maxi=0
    for i in range(0,len(t_tuple)):
        if setter(t_tuple[i]) == 0:
            k+=1
        else:
            #at the end of the sequence we sotore all the information
            maxi_vechi=maxi
            maxi=max(maxi_vechi,k)
            k=0

            # we check if we have a longer sequence, if so, we store the info
            if maxi_vechi!=maxi:
                i_final=i-1
                i_initial=i-maxi
                
    #we repeat this in case the longest sequence is at the end 
    maxi_vechi=maxi
    maxi=max(maxi_vechi,k)
    if maxi_vechi!=maxi:
        i_final=len(t_tuple)
        i_initial=len(t_tuple)-maxi

    # we do this in order to print it corectly
    i_final+=1

    # we call the ui 
    return t_tuple[i_initial:i_final]
    
def fix_complex_numbers(complex_number):
    '''
        WE CHANGE THE COMPLEX NUMBER SO THAT PYTHON CAN UNDERSTAND IT
        INPUT: A STRING
        OUTPUT A CHANGED STRING
    '''
    complex_number = complex_number.replace('i','j')
    complex_number = complex_number.replace(' ','')
    return complex_number

def append_to_tuple(complex_number,t_tuple):
    '''
        WE ADD A COMPLEX TO A TUPLE
        INPUT: COMPLEX NUMBER, TUPLE
        OUTPUT: THE TUPLE +COMPLEX NUMBER
    '''
    t_tuple = t_tuple + (complex_number,)
    return t_tuple


def add_complex(pp,tt_tuple):
    '''
        WE CONVERT THE STRING TO A COMPLEX
        INPUT
        OUTPUT
    '''

    #we replace i with j because python
    pp = fix_complex_numbers(pp)
    
    try:
        pp=complex(pp)
    except ValueError:
        print ('Oops!  That was not a complex number.  Try again...')

    tt_tuple = append_to_tuple(pp,tt_tuple)
    
    return tt_tuple

    

def read(t_tuple):
    while True:
        try:
            x = int(input('Please enter a positive number: '))
            if x>0 :break
        except ValueError:
            print ('Oops!  That was no valid number.  Try again...')

    for i in range(0,x):
        p=input('enter a complex number: ')
        t_tuple = add_complex(p,t_tuple)
        
    return t_tuple



def ui_run():
    complex_numbers_tuple= ()
    while True:
        x = input('please insert a valid comand >>')
        if x=='read':
            complex_numbers_tuple = read(complex_numbers_tuple)
        elif x=='print':
            print(complex_numbers_tuple)
            print(type(complex_numbers_tuple[0]))
        elif x=='exit':
            exit()
        elif x=='1':
            real_numbers_ui(real_numbers(complex_numbers_tuple))
        elif x=='2':
            distinct_numbers_ui(distinct_numbers(complex_numbers_tuple))
 



'''
///////////////////////////////////////////////////////////////////////////////////////////////////////
'''
#tuple_example = ((4+77j),(4+7j),(5-3j),(5-0j),(4-0j),(9-9j),(5-6j),(77+4j),(797+4j),(7+4j))



def test_real_numbers():
    tuple_example_1 = ((1-9j),(4+7j),(9+0j),(5-0j),(3-0j),(9-9j),(5-0j),(3-0j),(9-4j),(7+4j))
    assert real_numbers(tuple_example_1) == ((9+0j),(5-0j),(3-0j))
    
    tuple_example_2 = ((1-9j),(4+7j),(9+0j),(5-0j),(3-0j),(9-9j),(5-0j),(5-0j),(9-0j),(7+0j))
    assert real_numbers(tuple_example_2) == ((5-0j),(5-0j),(9-0j),(7+0j))
    
    tuple_example_3 = ((1-9j),(4+7j),(9+0j),(5-9j),(3-0j),(9-9j),(5-0j),(5-9j),(9-0j),(7+0j))
    assert real_numbers(tuple_example_3) == ((9-0j),(7+0j))

    tuple_example_2 = ((1-9j),(4+7j),(9+0j),(5-0j),(3-0j),(9-9j),(5-0j),(5-0j),(9-0j),(7+0j))
    assert real_numbers(tuple_example_2) == ((5-0j),(5-0j),(9-0j),(7+0j))

def test_distinct_numbers():
    tuple_example_1 = ((1-9j),(4+7j),(9+0j),(5-0j),(5-0j),(9-9j),(5-0j),(3-0j),(9-4j),(9-4j))
    assert distinct_numbers(tuple_example_1) == ((5-0j),(9-9j),(5-0j),(3-0j),(9-4j))

    tuple_example_2 = ((1-9j),(4+7j),(9+0j),(5-0j),(5-0j),(9-9j),(5-0j),(3-0j),(9-4j),(7+4j))
    assert distinct_numbers(tuple_example_2) == ((5-0j), (9-9j), (5-0j), (3-0j), (9-4j), (7+4j))

    tuple_example_3 = ((1-9j),(4+7j),(9+0j),(5-0j),(9-4j),(7+4j))
    assert distinct_numbers(tuple_example_3) == ((1-9j),(4+7j),(9+0j),(5-0j),(9-4j),(7+4j))


ui_run()

test_real_numbers()

test_distinct_numbers()





























