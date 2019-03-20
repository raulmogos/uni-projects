'''

7) Generate all subsequences of length 2n+1, formed only by 0, -1 or 1, such that 𝑎1 = 0, ..., 𝑎2𝑛+1= 0
and |𝑎𝑖+1 - 𝑎𝑖| = 1 or 2, for any 1 ≤ i ≤ 2n

sol:
'''



ret_lst = [0]

def back(n):
    lst = [0, 1, -1]
    for i in lst:
        ret_lst.append(i)
        if consistent(ret_lst) == True:
            if solution(ret_lst, n) == True:
                print_solution(ret_lst)
            else: back(n)
        ret_lst.pop()


def print_solution(lst):
    print(lst[1:])
    #lst.pop()

def consistent(lst):
    for i in range(1, len(lst)):
        if i%2!=0: # daca e impar
            if lst[i]!=0: # si daca e nenul
                return False # e inconsistent
    for i in range(1, len(lst)-1):
        if abs(lst[i+1] - lst[i]) not in [1,2]:
            return False
    return True


def solution(lst, n):
    if len(lst) == 2*n+1:
        return True
    return False


def test():
    pass


n = int(input('n='))
back(n)