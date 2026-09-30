def transport_report(students, buses, routes):
    print("\n--- Transport Report ---")
    print("Total Students:", len(students))
    print("Total Buses:", len(buses))
    print("Total Routes:", len(routes))

    print("\n--- Student Details ---")
    if len(students) == 0:
        print("No students registered.")
    else:
        for student in students:
            print("Name:", student["name"])
            print("Roll No:", student["roll_no"])
            print("Hostel:", student["hostel"])
            print("--------------------")

    print("\n--- Bus Details ---")
    if len(buses) == 0:
        print("No buses available.")
    else:
        for bus in buses:
            print("Bus No:", bus["bus_no"])
            print("Driver:", bus["driver"])
            print("Route:", bus["route"])
            print("Capacity:", bus["capacity"])
            print("--------------------")

    print("\n--- Route Details ---")
    if len(routes) == 0:
        print("No routes available.")
    else:
        for route in routes:
            print("Route:", route["route_name"])
            print("Start:", route["start"])
            print("Destination:", route["destination"])
            print("Bus No:", route["bus_no"])
            print("--------------------")
