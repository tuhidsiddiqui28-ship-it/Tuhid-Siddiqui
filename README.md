

# Student Management System

A simple **Student Management System** developed in Python using **Object-Oriented Programming (OOP)** concepts.

This project allows users to add, view, search, update, and delete student records. It can also calculate the average marks of all registered students and automatically assign grades based on marks.

## Features

* Add a new student
* View all students
* Search for a student by Student ID
* Update student information
* Delete a student record
* Calculate average marks
* Automatically calculate student grades
* Simple menu-driven interface
* Uses Python OOP concepts

## Technologies Used

* **Programming Language:** Python 3
* **Concepts:** Object-Oriented Programming (OOP)
* **Data Structure:** Dictionary

## Project Structure

```text
Student-Management-System/
│
├── student_management.py
└── README.md
```

## Student Information

The system stores the following information for each student:

* Student ID
* Name
* Age
* Course
* Marks
* Grade

## Grading System

|    Marks | Grade |
| -------: | :---: |
|   90–100 |   A+  |
|    80–89 |   A   |
|    70–79 |   B   |
|    60–69 |   C   |
|    50–59 |   D   |
| Below 50 |   F   |

## How to Run

### 1. Install Python

Make sure Python 3 is installed on your computer.

You can check your Python version using:

```bash
python --version
```

### 2. Save the Program

Save the Python code in a file such as:

```text
student_management.py
```

### 3. Run the Program

Open a terminal in the project folder and run:

```bash
python student_management.py
```

## Menu Options

When the program starts, the following menu is displayed:

```text
========== STUDENT MANAGEMENT SYSTEM ==========
1. Add Student
2. View All Students
3. Search Student
4. Update Student
5. Delete Student
6. Calculate Average Marks
7. Exit
===============================================
```

### 1. Add Student

Enter the student's:

* Student ID
* Name
* Age
* Course
* Marks

The system creates a student record and stores it in the system.

### 2. View All Students

Displays all students currently stored in the system, including their automatically calculated grade.

### 3. Search Student

Enter a Student ID to find and display a particular student's information.

### 4. Update Student

Enter the Student ID and provide new information.

If you leave a field empty, the existing value is retained.

### 5. Delete Student

Enter the Student ID to remove that student's record from the system.

### 6. Calculate Average Marks

The system calculates the average marks of all registered students.

For example:

```text
Average Marks: 78.50
```

### 7. Exit

Closes the Student Management System.

## OOP Concepts Used

### Class

The project contains two classes:

```python
class Student:
```

and

```python
class StudentManagementSystem:
```

### Constructor

The `__init__()` method initializes objects and their attributes.

```python
def __init__(self, student_id, name, age, course, marks):
```

### Encapsulation

Student information is stored inside the `Student` object using attributes such as:

```python
self.student_id
self.name
self.age
self.course
self.marks
```

### Methods

The program uses methods to perform different operations, such as:

```python
add_student()
view_students()
search_student()
update_student()
delete_student()
calculate_average()
```

### Dictionary

Student records are stored in a dictionary:

```python
self.students = {}
```

The Student ID is used as the dictionary key.

## Example

### Adding a Student

```text
Enter your choice: 1
Enter Student ID: 101
Enter Name: Rahul
Enter Age: 20
Enter Course: BCA
Enter Marks: 85
Student added successfully.
```

### Viewing the Student

```text
Student ID : 101
Name       : Rahul
Age        : 20
Course     : BCA
Marks      : 85.0
Grade      : A
```

## Limitations

This is a basic educational project. Student records are stored only in memory while the program is running.

When the program is closed, the data is lost because no database or file storage is currently used.

## Future Improvements

The project can be extended by adding:

* File-based data storage
* SQLite/MySQL database
* Login and authentication
* Student attendance management
* Subject-wise marks
* Report card generation
* GUI using Tkinter
* Input validation
* Sorting and filtering students
* Exporting student records to CSV or Excel

