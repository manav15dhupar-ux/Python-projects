#------Loads Previous data------

def load_data():
    try:
        with open("ph.txt","r") as f:
            for line in f:
                name,ph=line.strip().split(',')
                phone[name]=ph

    except FileNotFoundError:
        pass

#------Add New Data To File------

def save_data():
    with open("ph.txt","w") as f:
        for name,ph in phone.items():
            f.write(f"{str(name)},{str(ph)}\n")

#------Main Menu------

phone = {}
load_data() # Fetching Previous Data

print("====== WELCOME TO PHONE DIRECTORY ======")

while True:
    print("\n====== SEARCH LIST ======")
    print("1. Contact List")
    print("2. Find")
    print("3. Add")
    print("4. Discard")
    print("5. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        found=False
        for key in phone:
            print(key)
            found=True
        if not found:
            print("No contact list exist")

    elif ch == 2:
        if(len(phone)!=0):
            find = input("Enter the name to find contact: ")
            if find in phone:
                print(f"{find}:{phone[find]}")
            else:
                print("Contact not found. Choose option 3 to add.")
        
        else:
            print("No contacts exist")

    elif ch == 3:
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
                save_data() # Stores New Data
            else:
                print("Enter a valid number, start again")
                break

    elif ch == 4:
        if(len(phone)!=0):
            name_dis = input("Enter name of contact to discard: ")
            if name_dis in phone:
                phone.pop(name_dis)
                save_data() # Removing Data From File
                print("Contact removed successfully.")
            else:
                print("The contact does not exist.")
        
        else:
            print("Contact list does not exist")

    elif ch == 5:
        break

    else:
        print("Choose a correct option")