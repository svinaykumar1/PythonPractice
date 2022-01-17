#l=[2,4,6,3,9,11,12,10,13,18,25,23,24,26,29,28,27,19,20,22,21]
l=[2,4,6,3,9,11,12,10,13,18,25,23,14]

def sort_list(l):
    for i in range(len(l)-1):
        for j in range(len(l)-1):
            if (l[j]>l[j+1]):
                c=l[j]
                l[j]=l[j+1]
                l[j+1]=c

    return l

def max_cons_ele_seq(l):
    cons_arr=[]
    length1 = 0
    final_len = 0
    final_list = []
    for i in range(len(l)-1):
        if(l[i+1]-l[i]==1):
            #print(l[i],l[i+1])
            if len(cons_arr)==0:
                cons_arr=[l[i],l[i+1]]
                length1=2
            else:
                cons_arr.append(l[i+1])
                length1=length1+1
        else:
            if(len(cons_arr)>len(final_list)):
                final_list=cons_arr
                final_len=length1
            length1 = 0
            cons_arr = []

    if (len(cons_arr) > len(final_list)):
        final_list = cons_arr
        final_len = length1
    length1 = 0
    cons_arr = []
    return final_list,final_len



l=sort_list(l)
print(l)

print(max_cons_ele_seq(l))




