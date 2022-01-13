l=[0, -1, 2, -3, 1]

def func_triplets(l):
    for i in range(len(l)):
        for j in range(len(l)):
            for k in range(len(l)):
                if(i!=j and j!=k):
                    if(l[i]+l[j]+l[k]==0):
                        c=[l[i],l[j],l[k]]
                        for m in range(len(c)-1):
                            for n in range(len(c)-1):
                                if c[m]<c[n]:
                                    x=c[n]
                                    c[n]=c[m]
                                    c[m]=x
                        triplets.append(c)



triplets=[]
func_triplets(l)
dedup_triplets=[]
for i in triplets:
    if(i not in dedup_triplets):
        dedup_triplets.append(i)
print(triplets)
print(dedup_triplets)
#print(fin_triplet)

