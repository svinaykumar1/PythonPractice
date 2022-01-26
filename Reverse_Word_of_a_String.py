str1=input("Enter a String:")

str2=str1[::-1]
print(str2)

str3=''

for i in str1:
    if(str3==''):
        str3=i
    else:
        str3=i+str3

print(str3)
