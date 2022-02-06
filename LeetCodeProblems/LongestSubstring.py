#lenght of longest substring with non repeating characters
s='ababcdead'

def long_sub_str(s):
    long_str=''
    for i in range(len(s)):
        #print(i)
        temp_str=s[i]
        for j in s[i+1:]:
            #print(j)
            if j in temp_str:
                temp_str=''
                break
            else:
                temp_str=temp_str+j
                #print(temp_str)

            if (len(temp_str) > len(long_str)):
                long_str = temp_str



    return(long_str)


print(long_sub_str(s))

