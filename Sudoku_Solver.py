sudoku=[
    [0,0,0,0,4,0,0,0,0],
    [1,0,0,0,0,0,0,6,0],
    [0,9,0,8,0,7,3,0,0],
    [0,0,6,2,0,4,0,3,0],
    [0,0,0,0,9,0,4,0,0],
    [0,2,0,0,5,0,0,0,0],
    [0,8,0,3,0,2,7,0,0],
    [0,0,0,5,0,0,0,0,0],
    [0,0,9,0,0,0,0,0,8]
]

def print_sudo(sudoku):
    for i in range(9):
        for j in range(9):
            print(sudoku[i][j], end=" ")
            if ((j + 1) % 3 == 0):
                print('|', end=" ")
        if ((i + 1) % 3 == 0):
            print('\n------------------------', end=" ")
        print("\n", end="")

print_sudo(sudoku)

print("solution of the puzzle is below")

def nex_empty_cur(sudoku):
    for row in range(9):
        for col in range(9):
            if sudoku[row][col]==0:
                return row,col
    return None,None

def validate_sudoku(sudoku,guess,r,c):
    rows=sudoku[r]
    if guess in rows:
        return False
    cols=[sudoku[i][c] for i in range(9)]
    if guess in cols:
        return False
    grid=[]
    #grid validation
    for i in range((r//3)*3,(r//3)*3+3):
        for j in range((c//3)*3,(c//3)*3+3):
            grid.append(sudoku[i][j])

    if guess in grid:
        return False


    return True

def sudoku_solver(sudoku):
    r,c=nex_empty_cur(sudoku)
    #print(r,c)
    if(r==None):
        return True

    for guess in range(1,10):
        #print("Check1",)
        if(validate_sudoku(sudoku,guess,r,c)):
            sudoku[r][c]=guess
            if(sudoku_solver(sudoku)):
                return True
        else:
            sudoku[r][c]=0


if(sudoku_solver(sudoku)):
    print_sudo(sudoku)
else:
    print("Puzzle is unsolvable")





