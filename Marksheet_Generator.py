marks = []
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