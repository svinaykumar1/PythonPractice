import random
import datetime





Name=input("Enter Your Name:")

option= input("Hi {},How are you doing? Do you want to solve some problems?(y/n)".format(Name))
option=option.lower()
if(option not in ('y','n')):
    print("Sorry {} you have entered a wrong option. Bye!".format(Name))
else:
    num_probs=int(input("How many problems do you want solve"))
    print("Lets Start your test")

i=1
Score=0

#print(randint(20))
t1=datetime.datetime.now()
while (i<num_probs+1):
    a=random.randint(1,20)
    b=random.randint(1,10)
    Ans=int(input("Problem {}: {}x{} \n Answer:".format(i,a,b)))
    i=i+1
    if(Ans==a*b):
        #print("Your Answer is correct")
        Score=Score+1
        print("{} score is :{}".format(Name,Score))

    else:
        print("You got it wrong.Correct answer is {}. {} score is : {}".format(a*b,Name,Score))

t2=datetime.datetime.now()
print("Total time taken for test {} sec".format(t2-t1))
print("Thanks for your support. Your Final score is {}/{}".format(Score,num_probs))


