import getpass as gp

print("password")
p=gp.getpass()

if(p==123):
    "password is correct"
else:
    "wrong password"



def exam_func(x):
    l.append(5)

l='BANANA'

print(l.count('AN'))

l=[]
print(l)
exam_func(l)
print(l)

class temp(object):
    def __init__(self,veh,mod):
        self.veh=veh
        self.mod=mod

    def print_det(self):
        print(self.veh,self.mod)

a=temp('Honda',1940)
a.print_det()
