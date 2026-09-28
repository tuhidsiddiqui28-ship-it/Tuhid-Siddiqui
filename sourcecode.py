class Student:
    def __init__(self, student_id, name, age, course, marks):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks

    def display(self):
        print("\nStudent ID :", self.student_id)
        print("Name       :", self.name)
        print("Age        :", self.age)
        print("Course     :", self.course)
        print("Marks      :", self.marks)
        print("Grade      :", self.grade())

    def grade(self):
        if self.marks >= 90:
            return "A+"
        elif self.marks >= 80:
            return "A"
        elif self.marks >= 70:
            return "B"
        elif self.marks >= 60:
            return "C"
        elif self.marks >= 50:
            return "D"
        else:
            return "F"


class StudentManagementSystem:
    def __init__(self):
        self.students = {}

    def add_student(self):
        student_id = input("Enter Student ID: ")

        if student_id in self.students:
            print("Student already exists.")
            return

        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        course = input("Enter Course: ")
        marks = float(input("Enter Marks: "))

        student = Student(student_id, name, age, course, marks)
        self.students[student_id] = student

        print("Student added successfully.")

    def view_students(self):
        if not self.students:
            print("No students found.")
            return

        for student in self.students.values():
            student.display()

    def search_student(self):
        student_id = input("Enter Student ID to search: ")

        if student_id in self.students:
            self.students[student_id].display()
        else:
            print("Student not found.")

    def update_student(self):
        student_id = input("Enter Student ID to update: ")

        if student_id not in self.students:
            print("Student not found.")
            return

        student = self.students[student_id]

        student.name = input(f"Enter Name [{student.name}]: ") or student.name
        student.age = int(input(f"Enter Age [{student.age}]: ") or student.age)
        student.course = input(
            f"Enter Course [{student.course}]: "
        ) or student.course
        student.marks = float(
            input(f"Enter Marks [{student.marks}]: ") or student.marks
        )

        print("Student updated successfully.")

    def delete_student(self):
        student_id = input("Enter Student ID to delete: ")

        if student_id in self.students:
            del self.students[student_id]
            print("Student deleted successfully.")
        else:
            print("Student not found.")

    def calculate_average(self):
        if not self.students:
            print("No students available.")
            return

        total = sum(student.marks for student in self.students.values())
        average = total / len(self.students)

        print(f"Average Marks: {average:.2f}")

    def menu(self):
        while True:
            print("\n========== STUDENT MANAGEMENT SYSTEM ==========")
            print("1. Add Student")
            print("2. View All Students")
            print("3. Search Student")
            print("4. Update Student")
            print("5. Delete Student")
            print("6. Calculate Average Marks")
            print("7. Exit")
            print("===============================================")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_student()

            elif choice == "2":
                self.view_students()

            elif choice == "3":
                self.search_student()

            elif choice == "4":
                self.update_student()

            elif choice == "5":
                self.delete_student()

            elif choice == "6":
                self.calculate_average()

            elif choice == "7":
                print("Thank you for using Student Management System.")
                break

            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    system = StudentManagementSystem()
    system.menu()
