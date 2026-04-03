from gpa import calculate_gpa
from cgpa import calculate_cgpa
from data import ALL_SEMESTERS
import json,os

print("\n" + "="*40)
print("🎓 CGPA CALCULATOR SYSTEM")
print("="*40)


def save_data(data):
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)

def load_data():
    if os.path.exists("data.json"):
        with open("data.json", "r") as file:
            return json.load(file)
    return {}

def main():
    semester_data = load_data()


    while True:
        print("\n===== MENU =====")
        print("1. Calculate GPA")
        print("2. Calculate CGPA")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                sem = int(input("Enter semester (1-8): "))
                if sem not in ALL_SEMESTERS:
                    print("Invalid semester!")
                    continue
            except ValueError:
                print("Please enter a number!")
                continue

            if str(sem) in semester_data:
                confirm = input("Already calculated. Recalculate? (y/n): ")
                if confirm.lower() != 'y':
                    continue

            gpa, credits = calculate_gpa(sem)

            if gpa is not None:
                semester_data[str(sem)] = {
                    "gpa": gpa,
                    "credits": credits
                }
                save_data(semester_data)

                print(f"Semester {sem} GPA: {gpa:.2f}")

        elif choice == "2":
        
            if not semester_data:
                print("⚠️  No data available. Calculate GPA first.")
            else:
                print("\n📊 Stored Data:")
                for sem, data in semester_data.items():
                    print(f"Semester {sem} → GPA: {data['gpa']:.2f}")
                
                cgpa = calculate_cgpa(list(semester_data.values()))
                print(f"CGPA: {cgpa:.2f}")

        elif choice == "3":
            print("Exiting...")
            break

                  
        else:
            print("Invalid choice.")

main()