class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    # Sort the student list based on CGPA in descending order
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students

# Test the function with different input lists of students
if __name__ == "__main__":
    students1 = [
        Student("Alice", "A123", 3.8),
        Student("Bob", "B456", 3.5),
        Student("Charlie", "C789", 3.9),
    ]

    students2 = [
        Student("David", "D101", 3.2),
        Student("Eva", "E202", 3.7),
        Student("Frank", "F303", 3.4),
    ]

    sorted_students1 = sort_students(students1)
    sorted_students2 = sort_students(students2)

    print("Sorted Students List 1:")
    for student in sorted_students1:
        print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")

    print("\nSorted Students List 2:")
    for student in sorted_students2:
        print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")