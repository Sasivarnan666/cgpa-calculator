from data import GRADE_POINTS

def get_valid_grade(subject_name, credit):
    while True:
        grade = input(f"Enter grade for {subject_name} ({credit} credits): ").strip().upper()
        if grade in GRADE_POINTS:
            return grade
        else:
            print("❌ Invalid grade. Try again.")