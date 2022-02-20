import copy


def max_sub_array(l):
    max_sum=0
    max_sub_ar=[]
    for i in range(len(l)):
        temp_sum=l[i]
        temp_sub_ar=[l[i]]

        while(i<len(l)-1):
            i=i+1
            temp_sum=temp_sum+l[i]
            temp_sub_ar.append(l[i])
            if (temp_sum > max_sum):
                max_sum = temp_sum
                max_sub_ar =copy.deepcopy(temp_sub_ar)
            #print(max_sum,max_sub_ar,temp_sum,temp_sub_ar)

    if (temp_sum > max_sum):
        max_sum = temp_sum
        max_sub_ar = temp_sub_ar
    return max_sum,max_sub_ar







print(max_sub_array([-2,1,-3,4,-1,2,1,-5,4]))
print(max_sub_array([1]))
print(max_sub_array([5,4,-1,7,8]))