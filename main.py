from gpa import calculate_gpa
from cgpa import calculate_cgpa
from data import sem1_subjects, sem2_subjects

def main():
    semester_data = {}

    while True:
        print("\n===== MENU =====")
        print("1. Calculate Semester 1 GPA")
        print("2. Calculate Semester 2 GPA")
        print("3. Calculate CGPA")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            gpa, credits = calculate_gpa(sem1_subjects)
            semester_data[1] = {"gpa": gpa, "credits": credits}

        elif choice == "2":
            gpa, credits = calculate_gpa(sem2_subjects)
            semester_data[2] = {"gpa": gpa, "credits": credits}

        elif choice == "3":
            if not semester_data:
                print("⚠️ No data available. Calculate GPA first.")
            else:
                cgpa = calculate_cgpa(list(semester_data.values()))
                print(f"🏆 CGPA: {cgpa:.2f}")

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice.")

main()