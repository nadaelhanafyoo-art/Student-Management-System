students = []

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

    print("\nStudent added successfully!")
    print(students)


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

print("===== Student Management System =====")

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
    print("Search Student")

elif choice == "4":
    print("Good Bye")

else:
    print("Invalid Choice")