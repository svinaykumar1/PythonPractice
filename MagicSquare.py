import random

import numpy as np

n=int(input("input integer:"))

num_list=[i for i in range(1,n*n+1,1)]
print(num_list)

#a=np.zeros(shape=(n,n))
#print(a)

b=[[0 for i in range(n)] for j in range(n)]

def print_mat(mat):
    for i in mat:
        print(i)

def nex_empty_slot(a):
    for i in range(n):
        for j in range(n):
            if(a[i][j]==0):
                return i,j
    return None,None

def arrange_a(a):
    num_list = [i for i in range(1, n * n + 1, 1)]
    for i in range(n):
        for j in range(n):
            c=random.choice(num_list)
            a[i][j]=c
            num_list.remove(c)

    return(a)

def val_magic_sq(a,non_sol):
    temp_list=[]
    for i in range(n):
        for j in range(3):
            temp_list.append(a[i][j])

    if(temp_list in non_sol):
        return False
    else:
        sum=0
        for i in a:
            sum(i)


#def magic_sq_solver(a,non_sol):
print(print_mat(arrange_a(b)))
