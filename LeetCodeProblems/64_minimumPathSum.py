import copy

grid=[[1,3,1],
      [1,5,1],
      [4,2,1]]
li_copy=copy.deepcopy(grid)
#grid[0][0]=-1
#print(grid,li_copy,id(grid),id(li_copy))
path_dict={}

for row in range(len(grid)):
      for col in range(len(grid[row])):
            if(row==0 and col==0):
                  pass
                  #path_dict[(0,0)]=list((0,0))


            if(row==0 and col>0):
                  grid[row][col]=grid[row][col]+grid[row][col-1]
                  if((row,col-1)) in path_dict.keys():
                        pass
                        #path_dict[(row, col)] = list(path_dict[(row, col-1)]).append((row,col))

                  else:
                        path_dict[(row, col)] = list((row, col - 1))

            elif(row>0 and col==0):
                  grid[row][col]+=grid[row-1][col]
                  if (row-1,col) in path_dict.keys():
                        pass
                        #path_dict[(row,col)]=list(path_dict[(row-1,col)]).append((row,col))

                  else:
                        path_dict[(row,col)]=list((row,col))
                  #path_dict[(row,col)]=list(path_dict.get((row-1,col),[])).append((row,col))
            elif(row>0 and col>0):
                  grid[row][col]+=min(grid[row-1][col],grid[row][col-1])
                  c=[]
                  if(grid[row][col-1]<grid[row-1][col]):
                        #c=(row,col-1)
                        if((row,col-1) in path_dict.keys()):
                              c.append(path_dict[(row,col-1)])
                  else:
                        if((row-1,col) in path_dict.keys()):
                              c.append(path_dict[(row-1,col)])

                  #path_dict[(row,col)]=c.append((row,col))


print(grid[row][col])
print(grid,path_dict)


'''
def minimum_path_sum(grid):
      #print(id(l),id(grid))
      for i in range(len(grid)):
            for j in range(len(grid[i])):
                  #if(l[i][j]!=-1):
                        #print(grid[i][j],l[i][j])
                        if (i == 0 and j == 0):
                              #min_sum = grid[i][j]
                              #l[i][j] = -1
                              pass
                        elif (i-1 > -1 and j-1 >-1):
                              if (grid[i - 1][j] < grid[i][j - 1]):
                                    grid[i][j] = grid[i][j] + grid[i - 1][j]
                                    #l[i][j]=-1
                              else:
                                    grid[i][j] =grid[i][j]+grid[i][j-1]
                                    #l[i][j]=-1
                        elif(i-1>-1 and j-1<=-1):
                              grid[i][j]=grid[i][j]+grid[i-1][j]
                              #l[i][j]=-1
                        elif(i-1<=-1 and j-1>-1):
                              grid[i][j]=grid[i][j]+grid[i][j-1]
                              #l[i][j]=-1
                        #print(grid)

      return grid'''




#print(minimum_path_sum(grid))