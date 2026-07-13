class Person:
    def __init__(self, name, uid, department):
        self.name = name
        self.id = uid
        self.department = department

    def display_information(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.id}")
        print(f"Department: {self.department}")

    def update_information(self):
        print(f"\n--- Updating Information for {self.name} ---")
        self.name = input("Enter new name: ")
        self.department = input("Enter new department: ")
        print("Information updated successfully!")


class Student(Person):
    def register(self):
        print("Student registered successfully!")


class Teacher(Person):
    def register(self):
        print("Teacher registered successfully!")

class Course:
    def __init__(self, name, uid, department):
        self.name = name
        self.id = uid
        self.department = department

    def register(self):
        print("Course registered successfully!")

    def display_information(self):
        print(f"Course Name: {self.name}")
        print(f"Course ID: {self.id}")
        print(f"Department: {self.department}")

    def update_information(self):
        print(f"\n--- Updating Course: {self.name} ---")
        self.name = input("Enter new course name: ")
        self.department = input("Enter new department: ")
        print("Course updated successfully!")


students = []
teachers = []
courses = []

def save_data():
    try:
        with open("school_data.txt", "w") as file:
            file.write("[STUDENTS]\n")
            for s in students:
                file.write(f"{s.name},{s.id},{s.department}\n")

            file.write("[TEACHERS]\n")
            for t in teachers:
                file.write(f"{t.name},{t.id},{t.department}\n")

            file.write("[COURSES]\n")
            for c in courses:
                file.write(f"{c.name},{c.id},{c.department}\n")
    except Exception as e:
        print("Error saving data:", e)


def load_data():
    global students, teachers, courses
    try:
        with open("school_data.txt", "r") as file:
            section = None
            for line in file:
                line = line.strip()
                if not line:
                    continue

                if line == "[STUDENTS]":
                    section = "students"
                    continue
                elif line == "[TEACHERS]":
                    section = "teachers"
                    continue
                elif line == "[COURSES]":
                    section = "courses"
                    continue

                parts = line.split(",")
                if len(parts) == 3:
                    name, uid, dept = parts
                    if section == "students":
                        students.append(Student(name, uid, dept))
                    elif section == "teachers":
                        teachers.append(Teacher(name, uid, dept))
                    elif section == "courses":
                        courses.append(Course(name, uid, dept))
    except FileNotFoundError:
        pass 
    except Exception as e:
        print("Error loading data:", e)

def register_student():
    try:
        print("\n--- Register Student ---")
        name = input("Student Name: ")
        sid = input("Student ID: ")
        dept = input("Department: ")

        student = Student(name, sid, dept)
        student.register()
        students.append(student)
        save_data()
    except Exception as e:
        print("Failed to register student:", e)


def view_students():
    if not students:
        print("\nNo students registered.")
        return
    print("\n------ Students ------")
    for student in students:
        student.display_information()
        print("-" * 25)


def register_teacher():
    try:
        print("\n--- Register Teacher ---")
        name = input("Teacher Name: ")
        tid = input("Teacher ID: ")
        dept = input("Department: ")

        teacher = Teacher(name, tid, dept)
        teacher.register()
        teachers.append(teacher)
        save_data()
    except Exception as e:
        print("Failed to register teacher:", e)


def view_teachers():
    if not teachers:
        print("\nNo teachers registered.")
        return
    print("\n------ Teachers ------")
    for teacher in teachers:
        teacher.display_information()
        print("-" * 25)


def register_course():
    try:
        print("\n--- Register Course ---")
        name = input("Course Name: ")
        cid = input("Course ID: ")
        dept = input("Department: ")

        course = Course(name, cid, dept)
        course.register()
        courses.append(course)
        save_data()
    except Exception as e:
        print("Failed to register course:", e)


def view_courses():
    if not courses:
        print("\nNo courses registered.")
        return
    print("\n------ Courses ------")
    for course in courses:
        course.display_information()
        print("-" * 25)


load_data()

while True:
    print("\n===== SCHOOL MANAGEMENT SYSTEM =====")
    print("1. Register Student")
    print("2. View Students")
    print("3. Register Teacher")
    print("4. View Teachers")
    print("5. Register Course")
    print("6. View Courses")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        register_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        register_teacher()
    elif choice == "4":
        view_teachers()
    elif choice == "5":
        register_course()
    elif choice == "6":
        view_courses()
    elif choice == "7":
        print("Thank you for using the system. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")