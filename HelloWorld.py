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

str1="HelloWorld"

for i in enumerate(s):
    print(i)


