def merger(l1,l2):
    i=0
    j=0
    k=0
    l3=[]
    while(k<len(l1)+len(l2)):
        if(l1[i]<l2[j]):
            l3.append(l1[i])
            k=k+1
            i=i+1
        elif(i<len(l1) and j<len(l2)):
            #print(k,j)
            l3.append(l2[j])
            k=k+1
            j=j+1

        if(i==len(l1)):
            l3.extend(l2[j:])
            break
        elif(j==len(l2)):
            l3.extend(l1[i:])
            break
    return l3

def sort_data_func(l1,i,j):
    #print(l1)
    if (len(l1)==2):
        if (l1[1] < l1[0]):
            return [l1[1], l1[0]]
        else:
            return l1
    elif(len(l1)==1):
        return l1
    elif(len(l1)>2):
        mid = len(l1) // 2
        l2 = l1[i:mid]
        l3 = l1[mid:]
        #print(l2,l3)
        l=merger(sort_data_func(l2,0,mid),sort_data_func(l3,0,len(l3)-1))
        return l

l1=[5,3,4,9,10,25,13,12,8,6,76,25,38,26,23,44]
print(sort_data_func(l1,0,len(l1)-1))
#print(merger([3,5,7,9,10],[2,5,6,8,13,15]))