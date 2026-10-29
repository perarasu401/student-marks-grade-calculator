def calculate_bill(units):
    if units <= 100:
        bill = units * 1.50
    elif units <= 200:
        bill = 100 * 1.50 + (units - 100) * 2.50
    elif units <= 500:
        bill = 100 * 1.50 + 100 * 2.50 + (units - 200) * 4.00
    else:
        bill = 100 * 1.50 + 100 * 2.50 + 300 * 4.00 + (units - 500) * 6.00
    return bill


def electricity_billing_demo():
    n = int(input("Enter number of customers: "))
    for i in range(1, n + 1):
        print(f"\nCustomer {i}")
        name = input("Enter customer name: ")
        units = float(input("Enter units consumed: "))
        bill = calculate_bill(units)

        print("Customer Name :", name)
        print("Units :", units)
        print("Bill Amount : Rs.", round(bill, 2))


# Menu-Driven Student Information System
students = {}


def add_student():
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    dept = input("Enter Department: ")
    students[roll] = {"Name": name, "Department": dept}
    print("Student added successfully.")


def view_students():
    if not students:
        print("No student records found.")
        return
    print("\n--- Student Records ---")
    for roll, data in students.items():
        print(
            "Roll No:", roll,
            "| Name:", data["Name"],
            "| Department:", data["Department"],
        )


def search_student():
    roll = input("Enter Roll No to search: ")
    if roll in students:
        print(students[roll])
    else:
        print("Student not found.")


def delete_student():
    roll = input("Enter Roll No to delete: ")
    if roll in students:
        del students[roll]
        print("Student deleted successfully.")
    else:
        print("Student not found.")


def student_menu():
    while True:
        print("\n1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice.")


# Student Record Management with List, Tuple, Dictionary and CSV
import csv

students_list = [
    {"RollNo": "101", "Name": "Anitha", "Department": "CSE", "Mark": 86},
    {"RollNo": "102", "Name": "Bala", "Department": "CSE", "Mark": 91},
    {"RollNo": "103", "Name": "Chitra", "Department": "ECE", "Mark": 78},
]

# Tuple example: fixed course details
course = ("Python", 4)
print("Course Tuple:", course)

# Write text file
with open("students.txt", "w") as file:
    for student in students_list:
        file.write(str(student) + "\n")

# Write CSV file
with open("students.csv", "w", newline="") as file:
    fields = ["RollNo", "Name", "Department", "Mark"]
    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()
    writer.writerows(students_list)

# Read CSV file
print("\n--- Records from CSV ---")
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["RollNo"], row["Name"], row["Department"], row["Mark"])


if __name__ == "__main__":
    electricity_billing_demo()
    student_menu()
