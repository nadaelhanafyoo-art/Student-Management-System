import json

students = []

def load_students():
    global students

    try:
        with open("students.json", "r") as file:
            students = json.load(file)
    except:
        students = []

def save_students():
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)

def add_student():
    print("\n===== Add Student =====")

    name = input("Enter student name: ")
    age = input("Enter student age: ")
    grade = input("Enter student grade: ")

    student = {
        "name": name,
        "age": age,
        "grade": grade
    }

    students.append(student)

    save_students()

    print("\nStudent added successfully!")

def view_students():
    print("\n===== Students List =====")

    if len(students) == 0:
        print("No students found.")
        return

    for student in students:
        print("----------------------")
        print("Name :", student["name"])
        print("Age  :", student["age"])
        print("Grade:", student["grade"])

load_students()

def search_student():

    print("\n===== Search Student =====")

    search_name = input("Enter student name: ")

    found = False

    for student in students:

        if student["name"].lower() == search_name.lower():

            print("\nStudent Found")
            print("----------------------")
            print("Name :", student["name"])
            print("Age  :", student["age"])
            print("Grade:", student["grade"])

            found = True
            break

    if found == False:
        print("Student not found.")

while True:

    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        print("Good Bye")
        break

    elif choice == "":
        continue

    else:
        print("Invalid Choice")