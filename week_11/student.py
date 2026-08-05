def get_student():
    print("========Computer Lab Access========")

    name = input("Student Name: ")
    student_id = input("Student ID: ")

    registered = input("Registered for today's lab? (Y/N): ").strip().upper() == "Y"
    lab_open = input("Is the lab open? (Y/N): ").strip().upper() == "Y"
    comp_available = input("Computer Available? (Y/N): ").strip().upper() == "Y"

    return name, student_id, registered, lab_open, comp_available