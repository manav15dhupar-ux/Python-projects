n = int(input("Enter The Number Of Employees: "))
data = []

while True:
    print("\n====== EMPLOYEE DATABASE ======")
    print("1. ADD")
    print("2. VIEW ALL")
    print("3. SEARCH")
    print("4. CHANGE")
    print("5. EXIT\n")

    ch = int(input("Enter Your Choice: "))

    # ---------- ADD ----------
    if ch == 1:
        for i in range(n):
            name = input("Enter The Name Of Employee: ")
            b_sal = float(input("Enter Basic Salary (IN THOUSAND): "))
            h_rent = float(input("Enter House Rent Allowance (IN THOUSAND): "))
            c_neance = float(input("Enter Conveyance Allowance (IN THOUSAND): "))

            total = b_sal + h_rent + c_neance

            employee = {
                "NAME": name,
                "BASIC SALERY": b_sal,
                "HOUSE RENT": h_rent,
                "CONVEYANCE": c_neance,
                "TOTAL SALERY": total
            }

            data.append(employee)

        print("\nEmployee details recorded successfully.\n")

    # ---------- VIEW ALL ----------
    elif ch == 2:
        if len(data) == 0:
            print("No Information Available. Please add employees.")
        else:
            count = 1
            for emp in data:
                print(f"\n{count}. NAME: {emp['NAME']}")
                print("BASIC SALARY:", emp["BASIC SALERY"])
                print("HOUSE RENT:", emp["HOUSE RENT"])
                print("CONVEYANCE:", emp["CONVEYANCE"])
                print("TOTAL SALARY:", emp["TOTAL SALERY"])
                count += 1

    # ---------- SEARCH ----------
    elif ch == 3:
        name1 = input("Enter the name of employee to search: ")
        found = False

        for emp in data:
            if emp["NAME"].lower() == name1.lower():
                print("\nEmployee Found\n")
                print("NAME:", emp["NAME"])
                print("BASIC SALARY:", emp["BASIC SALERY"])
                print("HOUSE RENT:", emp["HOUSE RENT"])
                print("CONVEYANCE:", emp["CONVEYANCE"])
                print("TOTAL SALARY:", emp["TOTAL SALERY"])
                found = True
                break

        if not found:
            print("Employee does not exist")

    # ---------- CHANGE ----------
    elif ch == 4:
        name2 = input("Enter Employee Name To Change: ")
        found = False

        for emp in data:
            if emp["NAME"].lower() == name2.lower():
                found = True

                print("\n===== UPDATE MENU =====")
                print("1. Basic Salary")
                print("2. House Rent Allowance")
                print("3. Conveyance Allowance")

                choice = int(input("Enter your choice: "))

                if choice == 1:
                    print("Current Basic Salary:", emp["BASIC SALERY"])
                    emp["BASIC SALERY"] = float(input("Enter new Basic Salary: "))
                elif choice == 2:
                    print("Current House Rent:", emp["HOUSE RENT"])
                    emp["HOUSE RENT"] = float(input("Enter new House Rent: "))
                elif choice == 3:
                    print("Current Conveyance:", emp["CONVEYANCE"])
                    emp["CONVEYANCE"] = float(input("Enter new Conveyance: "))
                else:
                    print("Invalid choice")

                # Recalculate total salary
                emp["TOTAL SALERY"] = (
                    emp["BASIC SALERY"]
                    + emp["HOUSE RENT"]
                    + emp["CONVEYANCE"]
                )

                print("\nEmployee details updated successfully.\n")
                break

        if not found:
            print("Employee not found")

    # ---------- EXIT ----------
    elif ch == 5:
        print("Exiting program...")
        break

    else:
        print("Invalid input. Try again.")