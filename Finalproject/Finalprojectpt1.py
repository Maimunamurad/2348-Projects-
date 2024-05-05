import csv
from collections import defaultdict

def read_csv(file_name):
    """Reads data from a CSV file."""
    data = []
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    return data

def write_csv(file_name, data):
    """Writes data to a CSV file."""
    with open(file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)

def sort_by_last_name(student_id):
    """Sorts student data by last name."""
    return student_data[student_id]['last_name']

def sort_by_student_id(student):
    """Sorts student data by student ID."""
    return student[0]

# Load data from CSV files
students_majors = read_csv('StudentsMajorsList-3.csv')
gpa_list = read_csv('GPAList-1.csv')
graduation_dates = read_csv('GraduationDatesList-1.csv')
full_roster = read_csv('FullRoster-1.csv')

# Initialize data structures
student_data = {}
disciplinary_action = set()

# Populate student data from CSV
for row in students_majors:
    student_id = row[0]
    student_data[student_id] = {
        'last_name': row[1],
        'first_name': row[2],
        'major': row[3],
        'disciplinary': row[4] if len(row) > 4 else ""
    }

# Track students with disciplinary actions
for row in full_roster:
    if row[-1].upper() == 'Y':
        disciplinary_action.add(row[0])

# Update student data with GPA and graduation date
for student_id, gpa in gpa_list:
    student_data[student_id]['gpa'] = float(gpa)

for student_id, grad_date in graduation_dates:
    student_data[student_id]['grad_date'] = grad_date

# Generate FullRoster.csv
full_roster_output = [['Student ID', 'Major', 'First Name', 'Last Name', 'GPA', 'Graduation Date', 'Disciplinary Action']]
sorted_student_ids = sorted(student_data.keys(), key=sort_by_last_name)

for student_id in sorted_student_ids:
    info = student_data[student_id]
    full_roster_output.append([
        student_id, info['major'], info['first_name'], info['last_name'],
        info['gpa'], info['grad_date'], 'Y' if student_id in disciplinary_action else ''
    ])

write_csv('FullRoster.csv', full_roster_output)

# Generate separate CSV files for each major
major_students = defaultdict(list)
for student_id, info in student_data.items():
    major = info['major'].replace(' ', '')
    major_students[major].append([
        student_id, info['last_name'], info['first_name'], info['grad_date'],
        'Y' if student_id in disciplinary_action else ''
    ])

for major, students in major_students.items():
    file_name = f"{major}Students.csv"
    header = ['Student ID', 'Last Name', 'First Name', 'Graduation Date', 'Disciplinary Action']
    students.sort(key=sort_by_student_id)
    students.insert(0, header)
    write_csv(file_name, students)

# Generate ScholarshipCandidates.csv
eligible_students = [(id, info) for id, info in student_data.items() if id not in disciplinary_action and 'grad_date' in info and info['gpa'] > 3.8]
eligible_students.sort(key=sort_by_student_id)  # Sort by student ID
scholarship_candidates = [['Student ID', 'Last Name', 'First Name', 'Major', 'GPA']]
for student_id, info in eligible_students:
    scholarship_candidates.append([student_id, info['last_name'], info['first_name'], info['major'], info['gpa']])

write_csv('ScholarshipCandidates.csv', scholarship_candidates)

# Generate DisciplinedStudents.csv
disciplined_students = [['Student ID', 'Last Name', 'First Name', 'Graduation Date']]
for student_id in sorted(disciplinary_action):
    info = student_data[student_id]
    disciplined_students.append([student_id, info['last_name'], info['first_name'], info['grad_date']])

write_csv('DisciplinedStudents.csv', disciplined_students)
