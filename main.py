from storage import load_data
from student import student_menu
from bus import bus_menu
from route import route_menu
from booking import booking_menu, view_bookings
from report import transport_report

students, buses, routes, bookings = load_data()

while True:
    print("\n======================================")
    print("     SMART CAMPUS TRANSPORT SYSTEM")
    print("======================================")
    print("1. Student Management")
    print("2. Bus Management")
    print("3. Route Management")
    print("4. Search Student")
    print("5. Bus Booking")
    print("6. View Bookings")
    print("7. Transport Report")
    print("8. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        student_menu(students, buses, routes, bookings)
    elif choice == "2":
        bus_menu(buses, students, routes, bookings)
    elif choice == "3":
        route_menu(routes, students, buses, bookings)
    elif choice == "4":
        search_roll = input("Enter roll number: ").strip()
        found = False
        for student in students:
            if student.get("roll_no") == search_roll:
                print("\nStudent Found!")
                print("Name:", student["name"])
                print("Roll No:", student["roll_no"])
                print("Hostel:", student["hostel"])
                found = True
                break
        if not found:
            print("Student not found.")
    elif choice == "5":
        booking_menu(students, buses, routes, bookings)
    elif choice == "6":
        view_bookings(students, buses, bookings)
    elif choice == "7":
        transport_report(students, buses, routes)
    elif choice == "8":
        print("\nThank you for using Smart Campus Transport System!")
        break
    else:
        print("Invalid choice. Please try again.")
