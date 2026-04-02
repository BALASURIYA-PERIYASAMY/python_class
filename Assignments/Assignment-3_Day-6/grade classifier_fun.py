def get_grade(marks):
    if 90 <= marks <= 100:
        return "A"
    elif 75 <= marks <= 89:
        return "B"
    elif 60 <= marks <= 74:
        return "C"
    elif 45 <= marks <= 59:
        return "D"
    else:
        return "F"

students = {"rahul":90,"john":55,"anita":72,"priya":38,"sara":85}

for name, marks in students.items():
    grade = get_grade(marks)
    print(name, "→", grade)

