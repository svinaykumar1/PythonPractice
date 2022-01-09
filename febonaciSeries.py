def febi_ser(n):
    if n<=2:
        return 1
    else:
        return febi_ser(n-1)+febi_ser(n-2)

#Optimized febenoci series
feb_list={}
def feb_ser_new(n):
    if(n in feb_list.keys()):
        return feb_list[n]
    elif n<=2:
        feb_list[n]=1
        return feb_list[n]
    else:
        feb_list[n]= feb_ser_new(n-1)+feb_ser_new(n-2)
        return feb_list[n]



print(feb_ser_new(50))
print(feb_list)
#print(feb_ser_new(25))