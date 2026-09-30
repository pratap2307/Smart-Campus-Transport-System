from storage import save_data
from validation import required_text, positive_integer


def bus_menu(buses, students, routes, bookings):
    print("\n--- Bus Management ---")
    print("1. Add Bus")
    print("2. View Buses")
    print("3. Back")

    choice = input("Enter bus choice: ").strip()

    if choice == "1":
        bus_no = input("Enter bus number: ").strip()
        driver = input("Enter driver name: ").strip()
        route = input("Enter bus route: ").strip()
        capacity_text = input("Enter bus capacity: ").strip()

        if not required_text(bus_no, driver, route, capacity_text):
            print("All bus fields are required.")
            return

        try:
            capacity = positive_integer(capacity_text)
        except (TypeError, ValueError):
            print("Capacity must be a positive whole number.")
            return

        for bus in buses:
            if bus.get("bus_no") == bus_no:
                print("This bus number is already registered.")
                return

        buses.append({
            "bus_no": bus_no,
            "driver": driver,
            "route": route,
            "capacity": capacity
        })
        save_data(students, buses, routes, bookings)
        print("\nBus Added Successfully!")

    elif choice == "2":
        print("\n--- Bus List ---")
        if not buses:
            print("No buses available.")
        else:
            for bus in buses:
                print("Bus No:", bus["bus_no"])
                print("Driver:", bus["driver"])
                print("Route:", bus["route"])
                print("Capacity:", bus["capacity"])
                print("--------------------")

    elif choice == "3":
        print("Going back to main menu.")
    else:
        print("Invalid choice.")
