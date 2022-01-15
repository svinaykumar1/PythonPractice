l=[1,2,5,1,3,4]
Sum1=8
List_sum=[]

for i in range(len(l)):
    for j in range(len(l)):
        if(i!=j):
            if(l[i]+l[j]==Sum1):
                List_sum.append( (l[i],l[j] ))

print(List_sum)

