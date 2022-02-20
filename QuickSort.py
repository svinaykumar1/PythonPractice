def swap(l,a,b):
    if(a!=b):
        temp = l[a]
        l[a] = l[b]
        l[b] = temp


def partitions(l,start,end):
    pivot_ind = start
    pivot=l[pivot_ind]
    start_ind = start
    end_ind = end
    while end_ind > start_ind:
        while (start_ind <=len(l)-1 and l[start_ind]<=l[pivot_ind]):
            start_ind += 1
        while(l[end_ind]>l[pivot_ind]):
            end_ind -= 1

        if (start_ind < end_ind):
            swap(l, start_ind, end_ind)
            #start_ind,end_ind=end_ind,start_ind

    swap(l,pivot_ind,end_ind)

    return end_ind


def quicksort_func(l,start,end):
    if(start<end):
        pi=partitions(l,start,end)
        quicksort_func(l,start,pi-1)
        quicksort_func(l,pi+1,end)


if __name__=='__main__':
    temp=[[11, 9,29,7,2,15,28 ],
          [3,7,9,11],[25,22,21,10],[29,15,28],[],[6]]
    for l in temp:
        quicksort_func(l,0,len(l)-1)
        print(l)




