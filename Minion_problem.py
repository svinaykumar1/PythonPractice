str1='BANANA'

player1_list=[]
player2_list=[]

for st1 in str1:
    if st1 in ["A","E","I","O","U"]:
            if st1 not in player1_list:
                player1_list.append(st1)

    else:
        if st1 not in player2_list:
            player2_list.append(st1)

print(player1_list)
print(player2_list)

def count_cal(lis1,str1):
    t_dict={}
    t_set=set()
    for j in lis1:
        for i in range(len(str1)+1):
            for k,l in enumerate(str1):
                #print(k,l)
                if(j==l):
                    t_set.add(str1[k:k+i])
    t_set.remove('')
    #for i in t_set:
        #t_dict[i]=t_dict.get(i,0)+str1.count(i)

    for i in t_set:
        for j in range(len(str1)):
            #print(i,str1[j:len(i)+j])
            if(i==str1[j:len(i)+j]):
                t_dict[i] = t_dict.get(i, 0) + 1

    #print (t_dict)
    sum=0
    for i in t_dict.values():
        sum=sum+i

    return t_dict,sum


    #t_set.remove('')
    return t_set

player1_dict,player1_cnt=count_cal(player1_list,str1)
player2_dict,player2_cnt=count_cal(player2_list,str1)

print(player1_dict,player2_dict)

if(player1_cnt>player2_cnt):
    print("Player 1 wins")
elif(player2_cnt>player1_cnt):
    print("Player 2 wins")
else:
    print("Drawn")

