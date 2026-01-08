#------Load Previous Data------

def load_data():
    global tup,names
    try:
        with open("data.txt","r") as f:
            for line in f:
                data = line.strip().split("|")
                name = data[0]
                t_marks = int(data[1])
                avg = float(data[2])

                tup += ((name,t_marks,avg),)
                names.append(name)
    except FileNotFoundError:
        pass

#------Save New Data------


def save_data(name, t_marks, avg):
    with open("data.txt", "a") as f:
        f.write(f"{name}|{t_marks}|{avg}\n")

#------Enter New Data------
tup=()
names=[]
load_data() # Fetching Previous Data

n=int(input("Enter number of students:"))

for i in range(n):
    name=input("Name:")

    if name in names:
        print("Student already exists")
        continue

    t_marks=int(input("Enter Total Marks:"))
    avg=t_marks/3

    tup+=((name,t_marks,avg),)
    names.append(name)
    save_data(name,t_marks,avg) # Saving New Data

#------Main Menu------

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
            print(i[0], "\t", i[1], "\t\t", round(i[2], 2))

    elif ch == 3:
        sr = input("Enter name to search: ")
        found = False
        for i in tup:
            if i[0].lower() == sr.lower():
                print("Name:", i[0])
                print("Total Marks:", i[1])
                print("Average:", i[2])
                found = True
                break
        if not found:
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