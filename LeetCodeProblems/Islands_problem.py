grid=[
    [1,1,1,1,0,0],
    [1,1,0,1,0,0],
    [1,1,0,0,1,0],
    [0,0,0,0,0,1]
]

grid=[
    [0,0,0,0,0],
    [1,1,0,0,0],
    [1,1,0,1,1],
    [0,0,0,1,0]
]


def dfs_island(grid,r,c,islands=[]):
    grid[r][c]=0
    #path=[(r-1,c),(r,c-1),(r+1,c),(r,c+1)] #Corner are not considered for island
    path=[(r-1,c),(r,c-1),(r+1,c),(r,c+1),(r-1,c-1),(r-1,c+1),(r+1,c+1),(r+1,c-1)]#if cornors considered for islands
    for (i,j) in path:
        if(i>-1 and i<len(grid) and j>-1 and j<len(grid[r]) and grid[i][j]==1):
            islands.append((i,j))
            dfs_island(grid,i,j,islands)

    return islands

def island_solver(grid):
    island_number=0

    islands_list={}
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if(grid[r][c]==1):
                #print(grid)
                islands_list[island_number+1]=(dfs_island(grid,r,c,islands=[(r,c)]))
                island_number=island_number+1

    return islands_list

print(island_solver(grid))