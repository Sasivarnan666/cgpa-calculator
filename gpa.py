from data import GRADE_POINTS
from utils import get_valid_grade
from data import ALL_SEMESTERS
def calculate_gpa(sem):
    if sem not in ALL_SEMESTERS:
        print("Invalid semester!")
        return None, None

    subjects = ALL_SEMESTERS[sem]

    grade_points = {
        "O": 10, "A+": 9, "A": 8,
        "B+": 7, "B": 6, "C": 5, "U": 0
    }

    total_points = 0
    total_credits = 0

    print(f"\nEnter grades for Semester {sem}:")

    for subject, credit in subjects:
        grade = input(f"{subject} ({credit} credits): ").upper()

        if grade not in grade_points:
            print("Invalid grade! Try again.")
            return None, None

        point = grade_points[grade]
        total_points += point * credit
        total_credits += credit

    gpa = total_points / total_credits
    return gpa, total_credits