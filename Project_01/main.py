# Expense Tracker Project 

expensesList = [] #list of expenses in form of dictionary 
print(" \nWelcome to Expense Tracker : \n")

while True:
    print("====MENU====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Khrcha")
    print("4. Exit")

    choice= int(input("\nPlease Enter Your Choice : "))

#ADD Expense
    if(choice == 1):
        date= input("Enter Date of expense: ")
        category= input("Enter type of expence (Food, Travel, Makeup, Books): ")
        description= input("Describe/Brief about expence:: ")
        amount= float(input("Enter the amount: "))

        expense= {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expensesList.append(expense)
        print(" \n Expense is added succesfully \n")

# 2. VIEW ALL EXPENSES 
    elif(choice == 2):
        if( len(expensesList)==0 ):
            print("No Expenses Added.")
        else:
           print("===== Total Expense ======")
           count= 1
           for eachKharcha in expensesList:
                print(f"\nExpense Number {count}:\n DATE:{eachKharcha["date"]}\nCATEGORY:{eachKharcha["category"]}\nDESCRIPTION: {eachKharcha["description"]}\nAMOUNT: {eachKharcha["amount"]} \n")
                count= count+1

# 3. View TOtal Spending 
    elif(choice == 3):
        total= 0
        for eachKrcha in expensesList:
            total = total + eachKrcha["amount"]

        print(f"\nTOTAL EXPENSE: {total}\n")

#4. EXIT 
    elif(choice == 4):
        print("\nThank You For Using Our Expense Tracker\n")
        break

    else:
        print("INVALID CHOICE. TRY AGAIN")