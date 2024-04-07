# CIS 2348 Final Project Part 1.
# Maimuna Murad
# 2065973

import csv
from datetime import datetime

class Student:
    def __init__(self, student_id, last_name, first_name, major, gpa, graduation_date, disciplinary_action):
        self.student_id = student_id
        self.last_name = last_name
        self.first_name = first_name
        self.major = major
        self.gpa = gpa
        self.graduation_date = graduation_date
        self.disciplinary_action = disciplinary_action

def load_data():
    students = {}
    with open('StudentsMajorsList.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            student_id, last_name, first_name, major = row[:4]
            disciplinary_action = row[4] if len(row) > 4 else ''
            students[student_id] = Student(student_id, last_name, first_name, major, None, None, disciplinary_action)

    with open('GPAList.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            student_id, gpa = row
            students[student_id].gpa = float(gpa)

    with open('GraduationDatesList.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            student_id, graduation_date = row
            students[student_id].graduation_date = graduation_date

    return students

def write_full_roster(students):
    with open('FullRoster.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Student ID', 'Major', 'First Name', 'Last Name', 'GPA', 'Graduation Date', 'Disciplinary Action'])
        for student in sorted(students.values(), key=lambda x: x.last_name):
            writer.writerow([student.student_id, student.major, student.first_name, student.last_name,
                             student.gpa, student.graduation_date, student.disciplinary_action])

def write_major_files(students):
    major_students = {}
    for student in students.values():
        major = student.major.replace(' ', '') + 'Students.csv'
        if major not in major_students:
            major_students[major] = []
        major_students[major].append(student)
    for major, students_list in major_students.items():
        with open(major, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Student ID', 'Last Name', 'First Name', 'Graduation Date', 'Disciplinary Action'])
            for student in sorted(students_list, key=lambda x: x.student_id):
                writer.writerow([student.student_id, student.last_name, student.first_name,
                                 student.graduation_date, student.disciplinary_action])

def write_scholarship_candidates(students):
    eligible_students = []
    for student in students.values():
        if student.gpa > 3.8 and not student.graduation_date and not student.disciplinary_action:
            eligible_students.append(student)
    eligible_students.sort(key=lambda x: x.gpa, reverse=True)
    with open('ScholarshipCandidates.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Student ID', 'Last Name', 'First Name', 'Major', 'GPA'])
        for student in eligible_students:
            writer.writerow([student.student_id, student.last_name, student.first_name, student.major, student.gpa])

def write_disciplined_students(students):
    disciplined_students = []
    for student in students.values():
        if student.disciplinary_action:
            disciplined_students.append(student)
    disciplined_students.sort(key=lambda x: datetime.strptime(x.graduation_date, '%m/%d/%Y'))
    with open('DisciplinedStudents.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Student ID', 'Last Name', 'First Name', 'Graduation Date'])
        for student in disciplined_students:
            writer.writerow([student.student_id, student.last_name, student.first_name, student.graduation_date])

def main():
    students = load_data()
    write_full_roster(students)
    write_major_files(students)
    write_scholarship_candidates(students)
    write_disciplined_students(students)

if __name__ == "__main__":
    main()
