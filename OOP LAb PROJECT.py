# Class for Student
class Student:
    def __init__(self, student_id, name, email):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.enrollments = []

    def enroll_course(self, course):
        self.enrollments.append(course)
        print(f"{self.name} has been enrolled in {course.title}.")

    def list_enrollments(self):
        if not self.enrollments:
            print(f"{self.name} is not enrolled in any courses.")
        else:
            print(f"{self.name}'s Enrolled Courses:")
            for course in self.enrollments:
                print(f"- {course.title}")


# Class for Instructor
class Instructor:
    def __init__(self, instructor_id, name, expertise):
        self.instructor_id = instructor_id
        self.name = name
        self.expertise = expertise
        self.courses = []

    def assign_course(self, course):
        self.courses.append(course)
        print(f"Instructor {self.name} has been assigned to the course: {course.title}")

    def list_courses(self):
        if not self.courses:
            print(f"Instructor {self.name} is not assigned to any courses.")
        else:
            print(f"{self.name}'s Courses:")
            for course in self.courses:
                print(f"- {course.title}")


# Class for Course
class Course:
    def __init__(self, course_id, title, instructor=None):
        self.course_id = course_id
        self.title = title
        self.instructor = instructor
        self.assignments = []

    def add_assignment(self, assignment):
        self.assignments.append(assignment)
        print(f"Assignment '{assignment.title}' has been added to the course: {self.title}.")

    def list_assignments(self):
        if not self.assignments:
            print(f"No assignments available for the course: {self.title}.")
        else:
            print(f"Assignments for {self.title}:")
            for assignment in self.assignments:
                print(f"- {assignment.title}")


# Class for Assignment
class Assignment:
    def __init__(self, assignment_id, title, description):
        self.assignment_id = assignment_id
        self.title = title
        self.description = description


# Class for Enrollment
class Enrollment:
    def __init__(self, student, course):
        self.student = student
        self.course = course

    def enroll(self):
        self.student.enroll_course(self.course)


# Function to create a student with user input
def create_student():
    student_id = int(input("Enter Student ID: "))
    name = input("Enter Student Name: ")
    email = input("Enter Student Email: ")
    return Student(student_id, name, email)


# Function to create an instructor with user input
def create_instructor():
    instructor_id = int(input("Enter Instructor ID: "))
    name = input("Enter Instructor Name: ")
    expertise = input("Enter Instructor Expertise: ")
    return Instructor(instructor_id, name, expertise)


# Function to create a course with user input
def create_course(instructors):
    course_id = int(input("Enter Course ID: "))
    title = input("Enter Course Title: ")
    print("Available Instructors:")
    for i, instructor in enumerate(instructors, start=1):
        print(f"{i}. {instructor.name} ({instructor.expertise})")
    choice = int(input("Select Instructor by Number: ")) - 1
    instructor = instructors[choice] if 0 <= choice < len(instructors) else None
    if instructor:
        course = Course(course_id, title, instructor)
        instructor.assign_course(course)
        return course
    else:
        print("Invalid instructor selection.")
        return None


# Function to create an assignment with user input
def create_assignment():
    assignment_id = int(input("Enter Assignment ID: "))
    title = input("Enter Assignment Title: ")
    description = input("Enter Assignment Description: ")
    return Assignment(assignment_id, title, description)


# Function to enroll a student in a course
def enroll_student(students, courses):
    print("Available Students:")
    for i, student in enumerate(students, start=1):
        print(f"{i}. {student.name}")
    student_choice = int(input("Select Student by Number: ")) - 1

    print("Available Courses:")
    for i, course in enumerate(courses, start=1):
        print(f"{i}. {course.title}")
    course_choice = int(input("Select Course by Number: ")) - 1

    if 0 <= student_choice < len(students) and 0 <= course_choice < len(courses):
        student = students[student_choice]
        course = courses[course_choice]
        enrollment = Enrollment(student, course)
        enrollment.enroll()
    else:
        print("Invalid selection.")


# Main Function to Run the E-Learning Platform
def main():
    students = []
    instructors = []
    courses = []

    while True:
        print("\nE-Learning Platform Menu:")
        print("1. Register Student")
        print("2. Register Instructor")
        print("3. Register Course")
        print("4. Add Assignment to a Course")
        print("5. Enroll Student in a Course")
        print("6. List of Courses for an Instructor")
        print("7. List of Enrolled Student in a Course")
        print("8. List of Assignments for a Course")
        print("9. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            students.append(create_student())
        elif choice == 2:
            instructors.append(create_instructor())
        elif choice == 3:
            course = create_course(instructors)
            if course:
                courses.append(course)
        elif choice == 4:
            print("Available Courses:")
            for i, course in enumerate(courses, start=1):
                print(f"{i}. {course.title}")
            course_choice = int(input("Select Course by Number: ")) - 1
            if 0 <= course_choice < len(courses):
                assignment = create_assignment()
                courses[course_choice].add_assignment(assignment)
            else:
                print("Invalid course selection.")
        elif choice == 5:
            enroll_student(students, courses)
        elif choice == 6:
            print("Available Instructors:")
            for i, instructor in enumerate(instructors, start=1):
                print(f"{i}. {instructor.name}")
            instructor_choice = int(input("Select Instructor by Number: ")) - 1
            if 0 <= instructor_choice < len(instructors):
                instructors[instructor_choice].list_courses()
            else:
                print("Invalid instructor selection.")
        elif choice == 7:
            print("Available Students:")
            for i, student in enumerate(students, start=1):
                print(f"{i}. {student.name}")
            student_choice = int(input("Select Student by Number: ")) - 1
            if 0 <= student_choice < len(students):
                students[student_choice].list_enrollments()
            else:
                print("Invalid student selection.")
        elif choice == 8:
            print("Available Courses:")
            for i, course in enumerate(courses, start=1):
                print(f"{i}. {course.title}")
            course_choice = int(input("Select Course by Number: ")) - 1
            if 0 <= course_choice < len(courses):
                courses[course_choice].list_assignments()
            else:
                print("Invalid course selection.")
        elif choice == 9:
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


# Run the program
if __name__ == "__main__":
    main()