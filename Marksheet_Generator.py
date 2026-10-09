
marksheet = []


def calculate_result(name, marks):
    total = sum(marks)
    percentage = (total / 500) * 100

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    if percentage >= 50:
        status = "PASS"
    else:
        status = "FAIL"

    student = {
        "name": name,
        "marks": marks,
        "total": total,
        "percentage": percentage,
        "grade": grade,
        "status": status
    }

    marksheet.append(student)


name = input("Enter student name: ")

marks = []
subjects = ["Math", "Physics", "Chemistry", "English", "Computer"]

for subject in subjects:
    while True:
        try:
            mark = int(input(f"Enter {subject} marks (0-100): "))

            if 0 <= mark <= 100:
                marks.append(mark)
                break
            else:
                print("Marks must be between 0 and 100.")

        except ValueError:
            print("Please enter a valid whole number.")

calculate_result(name, marks)

for student in marksheet:
    print("\n===== MARKSHEET =====")
    print("Name:", student["name"])
    print("Marks:", student["marks"])
    print("Total:", student["total"], "/ 500")
    print("Percentage:", round(student["percentage"], 2), "%")
    print("Grade:", student["grade"])
    print("Status:", student["status"])
    print("=====================")
