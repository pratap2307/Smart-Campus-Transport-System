# Smart Campus Transport System

A console-based Python application for managing campus transport records such as students, buses, routes and bus bookings.

**Author:** Rudra Pratap Singh Ranawat  
**Programme:** Integrated M.Tech CSE (Cyber Security)  
**University:** VIT Bhopal University

## Overview

The Smart Campus Transport System provides a simple menu-driven application for a campus transport administrator. It allows students to be registered, buses and routes to be managed, students to be searched, bus bookings to be made, and transport reports to be viewed.

The project uses a local `data.json` file for persistent storage.

## Features

- Student Management
- Bus Management
- Route Management
- Search Student
- Transport Report
- Bus Booking
- View Bookings
- JSON Persistent Storage
- Duplicate checking for roll numbers, bus numbers, route names and bookings
- Input validation for required fields and positive bus capacity
- Bus capacity enforcement during booking

## Technologies / Tools

- Python 3
- Python standard library
- JSON
- Command-line / terminal
- VS Code or any Python IDE

The application uses Python's standard library. Pytest is used only for automated testing.

## Project Structure

```text
Smart-Campus-Transport-System/
├── main.py
├── student.py
├── bus.py
├── route.py
├── booking.py
├── report.py
├── storage.py
├── data.json
├── README.md
├── statement.md
└── tests/
    ├── test_project.py
    └── test_validation.py
```

The program is divided into separate modules so that student, bus, route, booking, reporting and storage functions are easier to maintain.

## How to Run

1. Install Python 3.8 or newer.
2. Open the project folder in VS Code or a terminal.
3. Run:

```bash
python main.py
```

The program will load existing records from `data.json`.

## Main Menu

```text
1. Student Management
2. Bus Management
3. Route Management
4. Search Student
5. Transport Report
5. Bus Booking
6. View Bookings
7. Transport Report
8. Exit
```

## Testing

The project includes basic tests in `tests/test_project.py`.

The main manual tests include:
- Registering a student
- Adding and viewing buses
- Adding and viewing routes
- Searching for an existing and non-existing student
- Booking with valid and invalid student/bus details
- Viewing bookings
- Viewing the transport report
- Checking JSON persistence
- Checking duplicate roll numbers, bus numbers and bookings
- Checking required fields and positive bus capacity
- Checking that bookings cannot exceed bus capacity
- Checking that every route refers to an existing bus

## Future Improvements

- Add edit and delete options
- Add login/user authentication
- Add graphical or web interface
- Add GPS/live bus tracking


## Version Control

The project is prepared for Git-based version control. The repository should include the complete source code, documentation, tests, report assets and a `.gitignore` file. A typical workflow is:

```bash
git init
git add .
git commit -m "Initial Smart Campus Transport System submission"
```

## Design Documentation

The accompanying project report contains the problem statement, objectives, functional and non-functional requirements, system architecture, workflow, UML-style use case/class/sequence diagrams, JSON storage design, implementation details, testing results, challenges, learnings, future enhancements and references.
