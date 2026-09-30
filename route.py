from storage import save_data


def route_menu(routes, students, buses, bookings):
    print("\n--- Route Management ---")
    print("1. Add Route")
    print("2. View Routes")
    print("3. Back")

    choice = input("Enter route choice: ").strip()

    if choice == "1":
        route_name = input("Enter route name: ").strip()
        start = input("Enter starting point: ").strip()
        destination = input("Enter destination: ").strip()
        bus_no = input("Enter bus number: ").strip()

        if not route_name or not start or not destination or not bus_no:
            print("All route fields are required.")
            return

        if not any(bus.get("bus_no") == bus_no for bus in buses):
            print("Bus not found. Add the bus first.")
            return

        if any(route.get("route_name") == route_name for route in routes):
            print("This route name is already registered.")
            return

        routes.append({
            "route_name": route_name,
            "start": start,
            "destination": destination,
            "bus_no": bus_no
        })
        save_data(students, buses, routes, bookings)
        print("\nRoute Added Successfully!")

    elif choice == "2":
        print("\n--- Route List ---")
        if not routes:
            print("No routes available.")
        else:
            for route in routes:
                print("Route:", route["route_name"])
                print("Start:", route["start"])
                print("Destination:", route["destination"])
                print("Bus No:", route["bus_no"])
                print("--------------------")

    elif choice == "3":
        print("Going back to main menu.")
    else:
        print("Invalid choice.")
