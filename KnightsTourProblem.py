n=int(input("Enter Integer:"))

l=[]
x=[]

l=[[-1 for j in range(n)] for k in range(n)]
#l[0][0]=0
#l[0][0]=1
#pos=1
for a in l:
    print(a)

def next_empty(l):
    for i in range(len(l)):
        for j in range(len(l)):
            if(l[i][j]==-1):
                return i,j
    return None

def next_move_pos(l,i,j):
    move_list=[]
    for a in range(i-2,i+3):
        for b in range(j-2,j+3):
            if(abs(a-i)+abs(b-j)==3):
                if(a<n and a>=0 and b<n and b>=0):
                    move_list.append((a, b))

    return move_list

def board_validation(l,a,b):
    for x,y in next_move_pos(l,a,b):
        if(l[x][y]==-1):
            return True
    return False


def knight_solver(l,a,b,pos):
    if(next_empty(l)==None):
        return l
    else:
        #print(next_move_pos(l,a,b))
        for x,y in next_move_pos(l,a,b):
            if(l[x][y]==-1):
                l[x][y]=pos+1
                pos=pos+1
                #print(x,y,l,board_validation(l,x,y))
                if(board_validation(l,x,y)):
                    knight_solver(l,x,y,pos)
                else:
                    l[x][y]=-1
                    #pos=pos-1
        return l

l[0][0]=1
knight_solver(l,0,0,1)
#print(next_move_pos(l,1,2))

for a in l:
    print(a)


'''

def arrange_knight(l):
    if (next_empty(l) == None):
        print(l)
    else:
        a, b = next_empty(l)
        if (a == 0 and b == 0):
            l[a][b] = pos
            pos=pos+1
        else:'''



