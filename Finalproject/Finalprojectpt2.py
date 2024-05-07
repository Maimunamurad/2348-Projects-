import csv
from datetime import datetime

class Student:
    def __init__(self, student_id, last_name, first_name, major, gpa, disciplinary_action=False):
        # Initialize a new Student object with the provided details.
        self.student_id = student_id
        self.last_name = last_name
        self.first_name = first_name
        self.major = major
        self.gpa = float(gpa)
        self.disciplinary_action = bool(disciplinary_action)

    def __str__(self):
        # Return a string representation of the Student object.
        return f"{self.student_id}, {self.first_name} {self.last_name}, {self.major}, {self.gpa}"

class StudentRecordManager:
    def __init__(self):
        # Initialize the StudentRecordManager with empty lists and dictionaries for storing data.
        self.students = []
        self.gpa_records = {}
        self.graduation_dates = {}

    def load_student_records(self, students_file, gpa_file, graduation_file):
        # Load student records from CSV files. Handle various errors like missing files and bad data.
        try:
            with open(students_file, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) < 5:
                        print(f"Row too short in Students file: {row}")
                        continue
                    student_id, last_name, first_name, major = row[:4]
                    disciplinary_action = row[4].strip().lower() in ('true', '1', 'yes')
                    student = Student(student_id, last_name, first_name, major, 0.0, disciplinary_action)
                    self.students.append(student)

            with open(gpa_file, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) < 2:
                        print(f"Invalid row or value in GPA file: {row}")
                        continue
                    student_id, gpa = row[0], float(row[1])
                    self.gpa_records[student_id] = gpa

            with open(graduation_file, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) < 2:
                        print(f"Invalid row or value in Graduation Dates file: {row}")
                        continue
                    student_id, graduation_date_str = row[0], row[1]
                    graduation_date = datetime.strptime(graduation_date_str, '%m/%d/%Y')
                    self.graduation_dates[student_id] = graduation_date

        except FileNotFoundError as e:
            print(f"File not found: {e}")
        except Exception as e:
            print(f"Error reading CSV files: {e}")

        for student in self.students:
            student.gpa = self.gpa_records.get(student.student_id, 0.0)

    def is_graduated(self, student_id):
        # Check if the student has graduated by comparing the current date to their graduation date.
        graduation_date = self.graduation_dates.get(student_id)
        return graduation_date and graduation_date <= datetime.today()

    def find_students(self, major, gpa):
        # Find students matching a given major and GPA threshold.
        major, gpa = major.lower(), float(gpa)
        matching_students, closest_students = [], []
        for student in self.students:
            if student.major.lower() == major and not student.disciplinary_action and not self.is_graduated(student.student_id):
                if abs(gpa - student.gpa) <= 0.1:
                    matching_students.append(student)
                elif abs(gpa - student.gpa) <= 0.25:
                    closest_students.append(student)

        if matching_students:
            print("Your student(s):")
            for student in matching_students:
                print(student)
        if closest_students:
            print("You may also consider:")
            for student in closest_students:
                print(student)
        if not matching_students and not closest_students:
            print("No such student.")

def main():
    # Main function to manage the application flow.
    record_manager = StudentRecordManager()
    record_manager.load_student_records('StudentsMajorsList-3.csv', 'GPAList-1.csv', 'GraduationDatesList-1.csv')
    while True:
        query = input("Enter major and GPA or 'q' to quit: ").strip()
        if query.lower() == 'q':
            break
        try:
            *major_parts, gpa = query.rsplit(' ', 1)
            major = ' '.join(major_parts)
            float(gpa)  # This will raise ValueError if gpa is not a float
        except ValueError:
            print("Invalid input. Please provide major and GPA.")
            continue

        record_manager.find_students(major, gpa)

if __name__ == "__main__":
    main()
