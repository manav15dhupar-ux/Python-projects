#------save New Data------

def save_data(data,date,name):
    with open("sales.txt","a") as f:
        f.write(f"Rs.{str(data)},{str(date)},{str(name)}\n")

#---Store Date------

def get_date():
    date_pur=input("Enter The Date(DD/MM/YY):")
    return date_pur

#------Store Name------

def costomer_details():
    name=input("Enter Name:")
    return name

#------Main Menu------

print("======= Welcome To krina Store Calculator =======")
add=0
amt_list=[]
today_date=get_date()
custom=costomer_details()

while True:
    num=input("\nEnter the amount or press q to exit:\n")
    if (num.lower()=='q'):
        break
    if(num.replace('.','',1).isdigit()):
        total=float(num)
        add=add+total
        print(f"Total so far {add}")
        amt_list.append(total)

    else:
        print("Enter a valid amount:")

#------Final Output------

print("\n======MANAV GENERAL STORE======\n")
for i in amt_list:
    print(f"Rs.{i}")
print(f"Total amount Rs.{add} , Thanks for coming 😁 Visit Again 🙏")
save_data(add,today_date,custom) # save all changes

