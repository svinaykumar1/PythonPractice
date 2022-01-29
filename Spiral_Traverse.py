import numpy as np

n=int(input("Input an Integer:"))

print(n)
a=np.zeros(shape=(n,n))
print(a)

k=1
mode='f'

while k<n*n:
    if(k==1 and mode=='f'):
        i=0
        j=0
        a[i][j]=k
        #k=k+1
        #j=j+1
    if(mode=='f'):
        j=j+1
        k=k+1
        if(j==n):
            j=j-1
            k=k-1
            mode='d'
        elif(j<n and a[i][j]==0):
            a[i][j]=k
            #k=k+1
            #j=j+1
        elif(j<n and a[i][j]!=0):
            j = j - 1
            k = k - 1
            mode = 'd'
    if(mode=='d'):
        i = i + 1
        k = k + 1
        if (i == n):
            i = i - 1
            k = k - 1
            mode = 'b'
        elif (i < n and a[i][j] == 0):
            a[i][j] = k
            #k = k + 1
            #i = i + 1
        elif (i < n and a[i][j] != 0):
            i = i - 1
            k = k - 1
            mode = 'b'

    if(mode=='b'):
        j = j - 1
        k = k + 1
        if (j == -1):
            j = j + 1
            k = k - 1
            mode = 't'
        elif (j > -1 and a[i][j] == 0):
            a[i][j] = k
            #k = k + 1
            #j = j - 1
        elif (i > -1 and a[i][j] != 0):
            j = j + 1
            k = k - 1
            mode = 't'

    if (mode=='t'):
        i = i - 1
        k = k + 1
        if (i == -1):
            i = i + 1
            k = k - 1
            mode = 'f'
        elif (i > -1 and a[i][j] == 0):
            a[i][j] = k
            #k = k + 1
            #i = i - 1
        elif (i > -1 and a[i][j] != 0):
            i = i + 1
            k = k - 1
            mode = 'f'





'''def next_dir(s):
    move_dir = ['f', 'd', 'b', 't']
    for str in range(len(move_dir)):
        if(s==move_dir[-1]):
            s=move_dir[0]
            return s
        elif(s==move_dir[str]):
            s=move_dir[str+1]
            return s'''
print(a)

s='f'

'''
while(k<=n*n):
    if(i==0 and j==0):
        k=1
        a[i][j]=1
    if(s=='f'):
        a[i][j]=k
        k=k+1
        j=j+1
        if (j == n):
            j = j - 1
            s = next_dir(s)
        elif (a[i][j + 1] != 0):
            j = j - 1
            s = next_dir(s)

    if (s == b):
        a[i][j] = k
        k = k + 1
        j = j + 1
        if (j == n):
            j = j - 1
            s = next_dir(s)
        elif (a[i][j + 1] != 0):
            j = j - 1
            s = next_dir(s)'''

