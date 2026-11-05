# Student Management System - By Injarapu Sailaja

students = []

def add_student():
    name = input("Enter Name: ")
    roll = input("Enter Roll No: ")
    marks = input("Enter Marks: ")
    students.append({"Name": name, "Roll": roll, "Marks": marks})
    print("Student Added Successfully!")

def view_students():
    if not students:
        print("No Students Found!")
    else:
        for s in students:
            print(s)

def search_student():
    roll = input("Enter Roll No to Search: ")
    for s in students:
        if s["Roll"] == roll:
            print("Found:", s)
            return
    print("Student Not Found!")

def delete_student():
    roll = input("Enter Roll No to Delete: ")
    for s in students:
        if s["Roll"] == roll:
            students.remove(s)
            print("Deleted Successfully!")
            return
    print("Not Found!")

while True:
    print("\n1. Add  2. View  3. Search  4. Delete  5. Exit")
    choice = input("Enter Choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Thank You!")
        break
    else:
        print("Invalid Choice!")