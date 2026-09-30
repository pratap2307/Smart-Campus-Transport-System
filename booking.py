from storage import save_data


def _find_by_key(items, key, value):
    for item in items:
        if item.get(key) == value:
            return item
    return None


def booking_menu(students, buses, routes, bookings):
    print("\n--- Bus Booking ---")

    roll_no = input("Enter student roll number: ").strip()
    bus_no = input("Enter bus number: ").strip()

    if not roll_no or not bus_no:
        print("Student roll number and bus number are required.")
        return

    student = _find_by_key(students, "roll_no", roll_no)
    bus = _find_by_key(buses, "bus_no", bus_no)

    if student is None:
        print("Student not found.")
        return

    if bus is None:
        print("Bus not found.")
        return

    for booking in bookings:
        if booking.get("roll_no") == roll_no and booking.get("bus_no") == bus_no:
            print("This booking already exists.")
            return

    try:
        capacity = int(bus.get("capacity", 0))
    except (TypeError, ValueError):
        print("Bus capacity is invalid. Please correct the bus record first.")
        return

    if capacity <= 0:
        print("This bus has no available capacity.")
        return

    current_bookings = sum(
        1 for booking in bookings if booking.get("bus_no") == bus_no
    )
    if current_bookings >= capacity:
        print("This bus is full. Booking cannot be created.")
        return

    bookings.append({"roll_no": roll_no, "bus_no": bus_no})
    save_data(students, buses, routes, bookings)
    print("\nBus Booked Successfully!")


def view_bookings(students, buses, bookings):
    print("\n--- Bus Bookings ---")

    if not bookings:
        print("No bookings available.")
        return

    for booking in bookings:
        student = _find_by_key(students, "roll_no", booking.get("roll_no"))
        bus = _find_by_key(buses, "bus_no", booking.get("bus_no"))

        student_name = student["name"] if student else "Unknown"
        driver_name = bus["driver"] if bus else "Unknown"
        route_name = bus["route"] if bus else "Unknown"

        print("Student Name:", student_name)
        print("Roll No:", booking.get("roll_no"))
        print("Bus No:", booking.get("bus_no"))
        print("Driver:", driver_name)
        print("Route:", route_name)
        print("--------------------")
