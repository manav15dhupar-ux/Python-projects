import random

def ux(user,computer):
        print(f"Your choice:{choices[user]}")
        print(f"Computer choise:{choices[computer]}")
        
print("======Welcome To Snake,Water,Gun======")

choices={
    1:"Snake",
    2:"Water",
    3:"Gun"
}
while True:
    computer=random.randint(1,3)
    print("===MENU===")
    print("1.Snake\n2.Water\n3.Gun\n4.Exit\n")

    user=int(input("Enter your choise:"))

    if user not in [1,2,3,4]:
        print("invalid choise")
        continue

    if user==4:
         print("Tanks for Visiting")
         break


    if(user==computer):
        ux(user,computer)
        print("Tie")
       
    elif((user==1 and computer==2)or(user==2 and computer==3)or(user==3 and computer==1)):
        ux(user,computer)
        print("user won")

    else:
        ux(user,computer)
        print("computer won")
   

