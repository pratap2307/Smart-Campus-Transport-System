from storage import save_data


def student_menu(students, buses, routes, bookings):
    print("\n--- Student Management ---")
    print("1. Register Student")
    print("2. Back")

    choice = input("Enter choice: ").strip()

    if choice == "1":
        name = input("Enter student name: ").strip()
        roll_no = input("Enter roll number: ").strip()
        hostel = input("Enter hostel/block: ").strip()

        if not name or not roll_no or not hostel:
            print("All student fields are required.")
            return

        for student in students:
            if student.get("roll_no") == roll_no:
                print("This roll number is already registered.")
                return

        students.append({"name": name, "roll_no": roll_no, "hostel": hostel})
        save_data(students, buses, routes, bookings)
        print("\nStudent Registered Successfully!")

    elif choice == "2":
        print("Going back to main menu.")
    else:
        print("Invalid choice.")
