def add_student():
    print("=== Add Student ===")


print("===== Student Management System =====")

print("1. Add Student")
print("2. View Students")
print("3. Search Student")
print("4. Exit")

choice = input("Choose an option: ")

if choice == "1":
    add_student()

elif choice == "2":
    print("View Students")

elif choice == "3":
    print("Search Student")

elif choice == "4":
    print("Good Bye")

else:
    print("Invalid Choice")