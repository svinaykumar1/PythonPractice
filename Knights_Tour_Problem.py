import numpy as np
n=6
list1=[[0 for i in range(n)] for j in range(n)]
#a=np.zeros(n*n).reshape(n,n)
a=np.array(list1)
print(a)
'''
def path(a,i,j):
    val=[(i-2,j-1),(i-2,j+1),(i+2,j-1),(i+2,j+1),(i-1,j-2),(i+1,j-2),(i-1,j+2),(i+1,j+2)]
    path_val=[(c,d) for (c,d) in val if c>-1 and c<n and d>-1 and d<n and a[c][d]==0 ]
    if(path_val==[]):
        return[(-1,-1)]
    return path_val
'''

def knights_problem_solver(n,a,i,j,k):
    if k==n*n:
        return True
    if (i<0 or i>=n or j<0 or j>=n or a[i][j]!=0):
        return False
    a[i][j]=k
    for i_move,j_move in zip([2,2,1,1,-1,-1,-2,-2],[1,-1,2,-2,2,-2,1,-1]):
        if(knights_problem_solver(n,a,i+i_move,j+j_move,k+1)):
            return True
    a[i][j]=0

knights_problem_solver(n,a,0,0,0)
print(a)
