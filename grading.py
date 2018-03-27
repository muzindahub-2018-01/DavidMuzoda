Dee = {
    "name": "Dee",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
Mark = {
    "name": "Mark",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
Arthur = {
    "name": "Arthur",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

# Addition of functions
def average(numbers):
    total = sum(numbers)
    total = float(total)
    return total / len(numbers)


def get_average(student):
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])
    return 0.1 * homework + 0.2 * quizzes + 0.7 * tests


def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

print("The grades for Dee, Mark and Arthur respectively are as follows: ")
  
print(get_letter_grade(get_average(Dee)))

print(get_letter_grade(get_average(Mark)))

print(get_letter_grade(get_average(Arthur)))
