

def add_two_num(l1,l2):
    sum_list=[]
    if(len(l1)>len(l2)):
        l1,l2=l2,l1

    #print(l1, l2)

    r=0
    for i in range(len(l1)):

        val=l1[i]+l2[i]+r
        if(val>=10):
            c=val-10
            r=1
        else:
            c=val
            r=0
        #print(c,r)
        sum_list.append(c)
        #print(sum_list)

    for j in range(len(l1),len(l2)):
        val = l2[j]  + r
        if (val >= 10):
            c = val - 10
            r = 1
        else:
            c = val
            r = 0
        sum_list.append(c)

    if(r!=0):
        sum_list.append(r)

    #print(sum_list)

    return sum_list



print(add_two_num([2,4,3],[5,6,4]))
print(add_two_num([0],[0]))
print(add_two_num([9,9,9,9,9,9,9],[9,9,9,9]))