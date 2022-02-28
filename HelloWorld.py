print("Hello World")
print("This is my first program")

sudoku=[
    [0,0,7,0,0,6,8,0,2],
    [0,0,0,2,0,8,7,0,0],
    [2,8,0,0,0,3,1,0,6],
    [6,7,2,5,0,0,9,0,0],
    [0,4,9,8,0,0,6,0,0],
    [0,3,1,0,4,9,0,5,0],
    [0,1,0,9,0,0,3,7,8],
    [0,6,3,0,0,5,0,2,0],
    [9,0,0,3,0,0,5,0,0]
]

#print (5//3,5/3,5%3)

l=[1,3,2,0,0,5,0,6]

for j in range(len(l)):
    for i in range(len(l) - 1):
        if (l[i] == 0):
            c = l[i + 1]
            l[i + 1] = l[i]
            l[i] = c

print(l)

str1="Hello World how are you"

for i in str1.split(' '):
    print(i)

l=[1,1,1,2,2,2,3,4,6,8,8,9]
x=[]
for i in l:
    if i not in x:
        x.append(i)

print(x)

s="   ****Hello world how are you doing*****   "
#print(s)
print(s.strip(),'\n',s.strip().strip('*'))
print(s.find('o'))
print(s.count('o'))
print(s)


a=9
a=str(a)
print(int(a)+int(a+a)+int(a+a+a)+int(a+a+a+a))

import itertools

for i in itertools.permutations([1,2,3]):
    print(i)

l=[12,24,35,24,88,120,155,88,120,155]
l1=[x for x in sorted(list(set(l)))]
print(sorted(list(set(l)))[::-1])

import zlib
s='helloworld!helloworld!helloworld!helloworld!'
#t=zlib.compress(s)
#print(bin(t))
#k=zlib.decompress(t)
#print(k)

class temp(object):
    def __init__(self,a):
        self.a=a

    def __add__(c,b):
        return c.a*b.a


O=temp(5)
O1=temp(6)
print(O+O1)

def numGenerator(n):
    for i in range(n+1):
        if(i%5==0 and i%7==0):
            yield i

a=numGenerator(500)

for i in a:
    print(i)


import re
str1='vinaya@gmail.com has rama@yahoo.com'
patn="(\w+)@(\w+).(\w+)"
x=re.findall("(\w+)@(\w+).(\w+)",str1)
print(x)

import functools as f

l=[1,2,3,4,5,6]
print(f.reduce(lambda x,y:x+y,l))

#401,403

print([3]+[4]+[5,7])

class node(object):
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

    def add_left_node(self,left1):
        self.left=left1

    def add_right_node(self,right1):
        self.right=right1

    def print_tree(self):
        if(self.left==None):
            self.left.val=None
        if (self.right==None):
            self.right.val = None
        print(self.val,self.left.val,self.right.val)



a=node(1)
b=node(2)
c=node(3)
d=node(4)
a.add_left_node(b)
a.add_right_node(c)
b.add_right_node(d)
#b.print_tree()

(a,b,_,_)=(5,6,7,8)

print(a,b,_)

import numpy as np
x=np.ones(20).reshape(4,5)

#print(s)
x[0][3]=5

if (5 in x[:1]):
    print(x[:1])