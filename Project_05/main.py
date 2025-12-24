n=int(input("Enter The Number Of Employes:"))
data=[]
count=1

while True:
    print("======EMPLOYE DATABASE======")
    print("\n1.ADD")
    print("2.VIEW ALL")
    print("3.SEARCH")
    print("4.CHANGE")
    print("5.EXIT\n")

    ch=int(input("Enter Your choise:"))

    if(ch==1):
        for i in range(n):

            name=input("Enter The Name Of Employe:")
            b_sal=float(input("Enter Basic Salery (IN THOUSAND):"))
            h_rent=float(input("Enter House Reant Allowlance (IN THOUSAND):"))
            c_neance=float(input("Enter Conveyance Allowlance (IN THOUSAND):"))
            total=b_sal+h_rent+c_neance

            employe={
                "NAME":name,
                "BASIC SALERY":b_sal,
                "HOUSE RENT":h_rent,
                "CONVEYANCE":c_neance,
                "TOTAL SALERY":total
            }

            data.append(employe)
        print("\nEmploye details have been recorded successfully.\n")

    elif(ch==2):
        if(len(data)==0):
            print("No Information Is There, Click 1 To Add")
        else:
            for view in data:  
                print(f"{count}.NAME:{view["NAME"]}\nBASIC SALERY:{view["BASIC SALERY"]}\nHOUSE RENT:{view["HOUSE RENT"]}\nCONVEYANCE:{view["CONVEYANCE"]}\nTOTAL SALERY:{view["TOTAL SALERY"]}")
                count=count+1

    elif(ch==3):
        name1 = input("Enter the name of employee: ")

        for emp in data:

            if emp["NAME"].lower() == name1.lower():
                print("\nEmployee Found\n")
                print("NAME:", emp["NAME"])
                print("BASIC SALARY:", emp["BASIC SALERY"])
                print("HOUSE RENT:", emp["HOUSE RENT"])
                print("CONVEYANCE:", emp["CONVEYANCE"])
                print("TOTAL SALARY:", emp["TOTAL SALERY"])
                break

            else:
                print("Employee does not exist")
    
    elif ch == 4:
        name2 = input("Enter Employee Name To Change/Remove: ")

        for emp in data:
            if emp["NAME"].lower() == name2.lower():

                print("\n===== UPDATE MENU =====")
                print("1. Basic Salary")
                print("2. House Rent Allowance")
                print("3. Conveyance Allowance")

                choice = int(input("Enter your choice: "))

                if choice == 1:
                    print(f"BASIC SALERY is {emp["BASIC SALERY"]}.")
                    emp["BASIC SALERY"] = float(input("Enter new Basic Salary: "))
                elif choice == 2:
                    print(f"HOUSE RENT is {emp["HOUSE RENT"]}.")
                    emp["HOUSE RENT"] = float(input("Enter new House Rent: "))
                elif choice == 3:
                    print(f"CONVEYANCE is {emp["CONVEYANCE"]}.")
                    emp["CONVEYANCE"] = float(input("Enter new Conveyance: "))
                else:
                    print("Invalid choice")

                emp["TOTAL SALERY"] = (
                    emp["BASIC SALERY"]
                    + emp["HOUSE RENT"]
                    + emp["CONVEYANCE"]
                )

                print("\nEmployee details updated successfully.\n")
                break

            else:
                print("Employee not found.")

    elif(ch==5):
        break
    else:
        print("Invalid input try again")

