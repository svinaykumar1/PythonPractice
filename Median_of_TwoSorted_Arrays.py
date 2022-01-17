l1=[2, 3, 5, 6, 10, 12,28]
l2=[1, 5, 11, 15, 18, 22, 45,58,72]

l3=[]
i=0
j=0

while (i<len(l1) and j<len(l2)):

    if (l1[i] < l2[j]):
        l3.append(l1[i])
        i = i + 1
    else:
        l3.append(l2[j])
        j = j + 1

    if (i == (len(l1) - 1)):
        l3.extend(l2[j:])
        break
    if (j == (len(l2) - 1)):
        l3.extend(l1[i:])
        break

print(l3)

if(len(l3)%2==0):
    median=(l3[len(l3)//2-1]+l3[len(l3)//2])/2
else:
    median=l3[len(l3)//2]
print(median)

