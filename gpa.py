from data import GRADE_POINTS
from utils import get_valid_grade

def calculate_gpa(subjects):
    total_points = 0
    total_credits = 0

    for subject in subjects:
        grade = get_valid_grade(subject["name"], subject["credit"])
        grade_point = GRADE_POINTS[grade]
        credit = subject["credit"]

        contribution = grade_point * credit
        total_points += contribution
        total_credits += credit

        print(f"{subject['name']} → {grade_point} × {credit} = {contribution}")

    gpa = total_points / total_credits
    print(f"\n🎯 GPA: {gpa:.2f}")

    return gpa, total_credits