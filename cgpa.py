def calculate_cgpa(sem_data):
    total_points = 0
    total_credits = 0

    for sem in sem_data:
        total_points += sem["gpa"] * sem["credits"]
        total_credits += sem["credits"]

    cgpa = total_points / total_credits
    return cgpa