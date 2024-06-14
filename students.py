import os
import csv

student_all = []
current_student = []
marks = {'c1': 0, 'c2': 0, 'c3': 0, 'm1': 0, 'm2': 0, 'm3': 0, 'e1': 0, 'e2': 0, 'e3': 0, 'eng': 0, 'evs': 0}

def read_from_csv():
    rollno = input("Enter roll number of student to fetch data for: ")
    file_exists = os.path.isfile('students_data.csv')
    if not file_exists:
        print("File not found.")
        return
    with open('students_data.csv', mode='r', newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if str(row[1].strip()) == str(rollno):
                print(row)

def write_to_csv():
    global student_all  # Declare student_all as global to modify it inside the function
    file_exists = os.path.isfile('students_data.csv')
    with open('students_data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Name", "Roll No", "Percentage", "SGPA"])
        for i in student_all:
            writer.writerow(i)
    student_all = []  

def percentage(marks):
    total_marks = sum(marks.values())
    percentage = (total_marks / 600) * 100
    print(f"Result is {percentage}%\n")
    return percentage

def sgpa(per):
    sgpa = (per / 10) * 0.75
    print(f"Your SGPA is {sgpa}\n")
    return sgpa

def enter_data():
    global student_all
    name = input("Enter name: ")
    roll_no = int(input("Enter roll_no: "))
    print("Now enter marks")
    for key in marks:
        value = int(input(f"Enter the marks of {key}: "))
        marks[key] = value
    per = percentage(marks)
    sgp = sgpa(per)
    current_student = [name, roll_no, per, sgp]
    print(current_student)
    student_all.append(current_student)

def printall():
    for i, j in enumerate(student_all):
        print(f"{i}: {j}")

def display_menu():
    print("\nMenu")
    print("1. Enter data")
    print("2. Print all unsaved data")
    print("3. Write current data to CSV")
    print("4. Fetch data from CSV")
    print("5. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            enter_data()
        elif choice == '2':
            printall()
        elif choice == '3':
            write_to_csv()
        elif choice == '4':
            read_from_csv()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
