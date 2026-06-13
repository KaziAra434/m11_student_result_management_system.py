# Student Result Management System

file_name = "students.txt"


# Grade Function
def calculate_grade(py, html, db, avg):

    if py < 50 or html < 50 or db < 50:
        return "F"

    elif avg >= 80:
        return "A+"

    elif avg >= 70:
        return "A"

    elif avg >= 60:
        return "B"

    elif avg >= 50:
        return "C"

    else:
        return "F"


# Add Student
def add_student():

    total_students = int(input("How many students do you want to add? "))

    for i in range(total_students):

        print(f"\nStudent {i+1}")

        student_id = input(
            "Enter Student ID (4 digits, Example: 1234): "
        )

        while len(student_id) != 4 or not student_id.isdigit():
            student_id = input(
                "Invalid ID! Enter 4 digits only: "
            )

        name = input("Enter Student Name: ")

        python_marks = float(input("Python Marks: "))
        html_marks = float(input("HTML Marks: "))
        database_marks = float(input("Database Marks: "))

        total = python_marks + html_marks + database_marks
        average = total / 3

        grade = calculate_grade(
            python_marks,
            html_marks,
            database_marks,
            average
        )

        with open(file_name, "a") as file:

            file.write(
                f"{student_id},{name},{python_marks},"
                f"{html_marks},{database_marks},"
                f"{total},{average:.2f},{grade}\n"
            )

    print(f"\n{total_students} student(s) result have been added.\n")


# View Results
def view_results():

    try:
        with open(file_name, "r") as file:

            print("\nID\tName\tTotal\tAverage\tGrade")
            print("-" * 40)

            for line in file:

                data = line.strip().split(",")

                print(
                    f"{data[0]}\t{data[1]}\t{data[5]}"
                    f"\t{data[6]}\t{data[7]}"
                )

            print()

    except FileNotFoundError:
        print("No records found.\n")


# Search Student
def search_student():

    search_id = input(
        "Enter Student ID to search (Example: 1234): "
    )

    found = False

    try:
        with open(file_name, "r") as file:

            for line in file:

                data = line.strip().split(",")

                if data[0] == search_id:

                    print("\nStudent Found")
                    print("ID:", data[0])
                    print("Name:", data[1])
                    print("Total:", data[5])
                    print("Average:", data[6])
                    print("Grade:", data[7])

                    found = True
                    break

        if found == False:
            print("Student not found.\n")

    except FileNotFoundError:
        print("No records found.\n")


# Summary Report
def summary_report():

    try:
        with open(file_name, "r") as file:

            records = file.readlines()

        total_students = len(records)

        averages = []

        grade_count = {
            "A+": 0,
            "A": 0,
            "B": 0,
            "C": 0,
            "F": 0
        }

        for line in records:

            data = line.strip().split(",")

            averages.append(float(data[6]))

            grade = data[7]
            grade_count[grade] += 1

        print("\nSummary Report")
        print("--------------")
        print("Total Students:", total_students)
        print("Highest Average:", max(averages))
        print("Lowest Average:", min(averages))

        print("\nGrade Count")

        for grade in grade_count:
            print(grade, ":", grade_count[grade])

        print()

    except FileNotFoundError:
        print("No records found.\n")


# Main Menu
while True:

    print("===== Student Result Management System =====")
    print("1. Add Student Result")
    print("2. View All Results")
    print("3. Search Student Result")
    print("4. Generate Summary Report")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_results()

    elif choice == "3":
        search_student()

    elif choice == "4":
        summary_report()

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice! Please enter 1-5.\n")