print("====== WELCOME TO PHONE DIRECTORY ======")

phone = {}
n = int(input("Enter the Number Of Entries: "))

for i in range(n):
    name = input("Enter Name: ")
    if name in phone:
        print("The name already exist")
        continue
    
       
    ph = input("Enter Phone Number: ")
    if ph in phone.values():
        print("phone number already exist.")
        continue
   
       

    if ph.isdigit() and len(ph)==10:
        phone[name] = ph
    else:
        print("Enter a valid number, start again")
        break

while True:
    print("\n====== SEARCH LIST ======")
    print("1. Contact List")
    print("2. Find")
    print("3. Add")
    print("4. Discard")
    print("5. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        for key in phone:
            print(key)

    elif ch == 2:
        find = input("Enter the name to find contact: ")
        if find in phone:
            print(find, ":", phone[find])
        else:
            print("Contact not found. Choose option 3 to add.")

    elif ch == 3:
        name_=input("Enter the name:")
        ph_=input("Enter the phone number:")

        if name_ in phone:
            print("The name already exist")
            continue
  
    
        if ph_ in phone.values():
            print("phone number already exist.")
            continue


        if ph_.isdigit() and len(ph_)==10:
            phone[name_] = ph_
            print("Contact added successfully.")
        else:
            print("Enter a valid phone number")

    elif ch == 4:
        name_dis = input("Enter name of contact to discard: ")
        if name_dis in phone:
            phone.pop(name_dis)
            print("Contact removed successfully.")
        else:
            print("The contact does not exist.")

    elif ch == 5:
        break

    else:
        print("Choose a correct option")