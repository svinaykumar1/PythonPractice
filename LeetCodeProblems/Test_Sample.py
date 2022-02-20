def find_i_val(l):
    j=0
    for i in range(len(l)-1):
        if(l[i]<l[i+1]):
            j=j+1
        else:
            break
    return(j)

def ins_sort_func(l,a,b):
    for i in range(b,0,-1):
        if(b<len(l) and l[i]>l[b] and l[i-1]<l[b] ):
            x=l[b]
            l.remove(b)
            l.insert(x,i)
            a=a+1
            b=b+1
            break

    print(l)



if __name__=='__main__':
    l=[7,15,2,28,33,1,8,4,-5]
    i=find_i_val(l)
    print(i)
    ins_sort_func([7,15,2,28,33,1,8,4,-5],i,i+1)