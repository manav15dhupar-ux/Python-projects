print("======= Welcome To krina Store Calculator =======")
add=0
amt_list=[]

while True:
    num=input("\nEnter the amount or press q to exit:\n")
    if (num.lower()=='q'):
        break
    if(num.replace('.','',1).isdigit()):
        print("Enter a valid amount")
        total=float(num)
        add=add+total
        print(f"Total so far {add}")
        amt_list.append(float(num))
    else:
        print("Enter a valid amount:")

print("\n======MANAV GENERAL STORE======\n")
for i in amt_list:
    print(f"Rs.{i}")
print(f"Total amount Rs.{add} , Thanks for coming 😁 Visit Again 🙏")

