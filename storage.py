import json

FILE_NAME = "data.json"

def load_data():
    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)

        return (
            data.get("students", []),
            data.get("buses", []),
            data.get("routes", []),
            data.get("bookings", [])
        )

    except (FileNotFoundError, json.JSONDecodeError):
        return [], [], [], []

def save_data(students, buses, routes, bookings):
    data = {
        "students": students,
        "buses": buses,
        "routes": routes,
        "bookings": bookings
    }

    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)
