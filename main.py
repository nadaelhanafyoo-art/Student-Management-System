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

    name = input("Enter student name: ").strip()
    age = input("Enter student age: ").strip()
    grade = input("Enter student grade: ").strip()

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


def search_student():
    print("\n===== Search Student =====")

    search_name = input("Enter student name: ").strip()

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

    if not found:
        print("Student not found.")


def delete_student():
    print("\n===== Delete Student =====")

    delete_name = input("Enter student name: ").strip()

    found = False

    for student in students:
        if student["name"].lower() == delete_name.lower():

            students.remove(student)

            save_students()

            print("Student deleted successfully!")

            found = True
            break

    if not found:
        print("Student not found.")


def edit_student():
    print("\n===== Edit Student =====")

    edit_name = input("Enter student name: ").strip()

    found = False

    for student in students:
        if student["name"].lower() == edit_name.lower():

            print("\nEnter new data")

            student["name"] = input("New name: ").strip()
            student["age"] = input("New age: ").strip()
            student["grade"] = input("New grade: ").strip()

            save_students()

            print("\nStudent updated successfully!")

            found = True
            break

    if not found:
        print("Student not found.")


load_students()

while True:

    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Edit Student")
    print("6. Exit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        edit_student()

    elif choice == "6":
        print("Good Bye")
        break

    elif choice == "":
        continue

    else:
        print("Invalid Choice") 