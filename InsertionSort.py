l=[2,3,5,7,9,12,6,4,1,15,8]

def find_def_first_sort(l):

    for i in range(len(l)-1):
        if(l[i]<l[i+1]):
            i=i+1
        else:
            break
    return i

def insertion_sort(l,i,j):
    for k in range(j,len(l)):
        #print(k)
        m=i
        while(m>=0):
            #print(m,l[m],l[k])
            if(l[m]>l[k]):
                if(m==0):
                    c=l.pop(k)
                    l.insert(0,c)
                    i=i+1
                    #print("Checkpoint 1")
                    break
                elif(l[m]>l[k] and l[m-1]<l[k]):
                    c=l[k]
                    l.pop(k)
                    l.insert(m,c)
                    i=i+1
                    #print("checkpoint 2")
                    break

            m=m-1
    return(l)



i=find_def_first_sort(l)
print(i)
if(i+1<len(l)-1):
    j=i+1
    print(insertion_sort(l,i,j))
else:
    print("List is already sorted",l)




