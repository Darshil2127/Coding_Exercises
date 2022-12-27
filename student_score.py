students_score = {"Aneri" : 91, "Darshil" : 83, "Jay" : 76, "Smit" : 56, "Ravi" : 66}

students_grades = {}

for student in students_score:
    grades = students_score[student]
    if grades > 90:
        students_grades[student] = "Outstanding"
    elif grades > 81:
        students_grades[student] = "Exceed expectation"
    elif grades > 71:
        students_grades[student] = "Acceptable"
    else:
        students_grades[student] = "Fail"

print(students_grades)