import csv
import pandas as pd

def view_all():
 df = pd.read_csv('student_data.csv')
 print(df)


def addnew():
    name = input("Enter the name: ")
    maths = input("Enter maths marks: ")
    science = input("Enter science marks: ")
    english = input("Enter english marks: ")

    maths = int(maths)
    science = int(science)
    english = int(english)

    with open("student_data.csv", "a", newline='', encoding="utf-8") as myfile:
        writer = csv.writer(myfile)
        writer.writerow([name, maths, science, english])
    print("New student record added!\n")

def highest_score():
    top_scorer = None
    highest_marks = -1
    students = []

    with open("student_data.csv", "r", encoding="utf-8") as file:
        data = csv.reader(file)
        next(data) 
        for row in data:
            name = row[0]
            maths = int(row[1])
            science = int(row[2])
            english = int(row[3])

            total = maths + science + english
            average = total / 3

            students.append([name, maths, science, english, total, average])

            if total > highest_marks:
                highest_marks = total
                top_scorer = name

    for student in students:
        print(f"For {student[0]}:")
        print(f"Maths: {student[1]}, Science: {student[2]}, English: {student[3]}")
        print(f"Total: {student[4]}, Average: {student[5]}")

    print(f" Highest scorer is {top_scorer} with total marks {highest_marks}.")

def menu():
    while True:
        print("=== Student Report Card Menu ===")
        print("1. View All Records")
        print("2. Add New Record")
        print("3. Show Topper")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            view_all()
        elif choice == '2':
            addnew()
        elif choice == '3':
            highest_score()
        elif choice == '4':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-4.")
menu()