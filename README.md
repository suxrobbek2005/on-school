# On-School - Online School System

## Overview
On-School is a simple terminal-based Python application that simulates an online school system. It allows students to register, log in, view available courses, enroll in courses, view their enrolled courses, and check grades.

This project is aimed at providing a basic implementation of user interaction in an educational system with static data, making it ideal for learning Python basics, such as functions, loops, data structures, and user input handling.

## Project Structure
```
on_school/
├── main.py               # Entry point of the application
├── school/               # Folder for school management modules
│   ├── __init__.py       # Marks this directory as a Python package
│   ├── courses.py        # Course management functions
│   ├── students.py       # Student management functions
│   ├── grades.py         # Grade management functions
├── utils/               # Folder for school management modules
│   ├── __init__.py       # Marks this directory as a Python package
│   ├── filters.py 
```

## Features
1. **User Registration**: Users can register by providing their name, email, and password.
2. **User Login**: Registered users can log in with their email and password.
3. **View Available Courses**: Users can view a list of available courses.
4. **Enroll in a Course**: Users can enroll in a course by selecting from available options.
5. **View Enrolled Courses**: Users can view a list of courses they are enrolled in.
6. **Check Grades**: Users can check their grades for the courses they are enrolled in.
7. **Logout**: Users can log out, returning to the main menu.

## Static Data
The system is initialized with static data:

- **Courses**: A predefined list of courses with details (name, instructor, and duration).
- **Students**: A list of registered students with name, email, and password.
- **Grades**: A dictionary to store grades for students based on their email.

### Running the Application
1. Navigate to the `on-school` directory in your terminal.
2. Run the application using the following command:
   ```bash
   python main.py
   ```

## File Descriptions

### `main.py`
This file is the entry point of the application and contains the main loop that handles user interaction. It imports functions from other modules to allow users to register, log in, view and enroll in courses, and check grades.

### `courses.py`
Contains functions related to course management, such as:
- Viewing available courses.

### `students.py`
Handles student registration, login, and course enrollment functionality. The `register_student`, `login_student`, and `enroll_in_course` functions are included here.

### `grades.py`
Contains the `check_grades` function, which allows users to view their grades for enrolled courses.

## Example Terminal Interaction

### Register a New User
```plaintext
=== Welcome to On-School ===
1. Register
2. Login
3. Exit
Select an option: 1
Enter your name: Alice Smith
Enter your email: alice@example.com
Enter your password: password123
Registration successful! Welcome, Alice Smith.
```

### Log in to the System
```plaintext
=== Welcome to On-School ===
1. Register
2. Login
3. Exit
Select an option: 2
Enter your email: alice@example.com
Enter your password: password123
Login successful! Welcome back, Alice Smith.
```

### View Available Courses
```plaintext
Available Courses:
1. Python Basics (Duration: 8 weeks, Instructor: John Doe)
2. Data Science 101 (Duration: 10 weeks, Instructor: Jane Smith)
```

### Enroll in a Course
```plaintext
Select a course number to enroll: 1
Successfully enrolled in Python Basics!
```

### View Enrolled Courses
```plaintext
My Courses:
1. Python Basics (Instructor: John Doe)
```

### Check Grades
```plaintext
My Grades:
Python Basics: Not graded yet
```

### Logout
```plaintext
Goodbye, Alice Smith!
```

# Example
```plaintext
=== Welcome to On-School ===
1. Register
2. Login
3. Exit
Select an option: 1
Enter your name: Alice Smith
Enter your email: alice@example.com
Enter your password: password123
Registration successful! Welcome, Alice Smith.

=== Welcome to On-School ===
1. Register
2. Login
3. Exit
Select an option: 2
Enter your email: alice@example.com
Enter your password: password123
Login successful! Welcome back, Alice Smith.

--- Main Menu for Alice Smith ---
1. View Available Courses
2. Enroll in a Course
3. View My Courses
4. Check My Grades
5. Logout
Choose an option: 1

Available Courses:
1. Python Basics (Duration: 8 weeks, Instructor: John Doe)
2. Data Science 101 (Duration: 10 weeks, Instructor: Jane Smith)

--- Main Menu for Alice Smith ---
1. View Available Courses
2. Enroll in a Course
3. View My Courses
4. Check My Grades
5. Logout
Choose an option: 2
Select a course number to enroll: 1
Successfully enrolled in Python Basics!

--- Main Menu for Alice Smith ---
1. View Available Courses
2. Enroll in a Course
3. View My Courses
4. Check My Grades
5. Logout
Choose an option: 3

My Courses:
1. Python Basics (Instructor: John Doe)

--- Main Menu for Alice Smith ---
1. View Available Courses
2. Enroll in a Course
3. View My Courses
4. Check My Grades
5. Logout
Choose an option: 4

My Grades:
Python Basics: Not graded yet
```
