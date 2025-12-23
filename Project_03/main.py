n = int(input("Enter number of students: "))
tup = ()
names = []

for i in range(n):
    name = input("Name: ")
    names.append(name)
    t_marks = int(input("Enter Total Marks: "))
    avg = t_marks / 3   # assuming 3 subjects
    tup += ((name, t_marks, avg),)

while True:
    print("\n===== MENU =====")
    print("1. Pass/Fail")
    print("2. Display")
    print("3. Search")
    print("4. Merit List")
    print("5. Exit")

    ch = int(input("Enter your Choice: "))

    if ch == 1:
        for i in tup:
            if i[2] >= 32:
                print(i[0], "Result: Pass")
            else:
                print(i[0], "Result: Fail")

    elif ch == 2:
        print("Name\tTotal Marks\tAverage")
        for i in tup:
            print(i[0], "\t", i[1], "\t", round(i[2], 2))

    elif ch == 3:
        sr = input("Enter name to search: ")
        if sr in names:
            pos = names.index(sr)
            print("Name:", tup[pos][0])
            print("Total Marks:", tup[pos][1])
            print("Average:", tup[pos][2])
        else:
            print("Name not found")

    elif ch == 4:
        print("====== MERIT LIST ======")
        for i in tup:
            if i[2] >= 75:
                print(i[0])

    elif ch == 5:
        break
    else:
        print("Invalid Choice")