# CIS 2348 Final Project Part 1.
# Maimuna Murad
# 2065973

import csv
from collections import defaultdict


# Function to read CSV files
def read_csv(file_name):
    """
    Read data from a CSV file and return it as a list of rows.

    Args:
        file_name (str): The name of the CSV file to read.

    Returns:
        list: A list containing each row of the CSV file as a list.
    """
    data = []
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    return data


# Function to write data to CSV files
def write_csv(file_name, data):
    """
    Write data to a CSV file.

    Args:
        file_name (str): The name of the CSV file to write.
        data (list): The data to write to the CSV file.
    """
    with open(file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)


# Sorting function for sorting by last name
def sort_by_last_name(student_id, student_data):
    """
    Sorting function to sort student data by last name.

    Args:
        student_id (str): The student ID.
        student_data (dict): Dictionary containing student data.

    Returns:
        str: The last name of the student corresponding to the given student ID.
    """
    return student_data[student_id]['last_name']


# Sorting function for sorting by student ID
def sort_by_student_id(student):
    """
    Sorting function to sort students by student ID.

    Args:
        student (tuple): A tuple containing student information.

    Returns:
        str: The student ID.
    """
    return student[0]


# Read CSV files
students_majors = read_csv('StudentsMajorsList-3.csv')
gpa_list = read_csv('GPAList-1.csv')
graduation_dates = read_csv('GraduationDatesList-1.csv')
full_roster = read_csv('FullRoster-1.csv')

# Process data
student_data = {}
disciplinary_action = set()

# Populate student data dictionary
for row in students_majors:
    # Extract student information from the row
    student_id = row[0]
    last_name = row[1]
    first_name = row[2]
    major = row[3]
    disciplinary = row[4] if len(row) > 4 else ""

    # Store student information in the student_data dictionary
    student_data[student_id] = {'last_name': last_name, 'first_name': first_name, 'major': major,
                                'disciplinary': disciplinary}

# Populate disciplinary action set
for row in full_roster:
    # Extract student ID and disciplinary action from the row
    student_id = row[0]
    disciplinary = row[-1]
    # Check if the student has disciplinary action and add them to the set
    if disciplinary.upper() == 'Y':
        disciplinary_action.add(student_id)

# Update student data with GPA and graduation date
for student_id, gpa in gpa_list:
    # Convert GPA to float and store it in the student data
    student_data[student_id]['gpa'] = float(gpa)

for student_id, grad_date in graduation_dates:
    # Store graduation date in the student data
    student_data[student_id]['grad_date'] = grad_date

# Generate List per major files
major_students = defaultdict(list)
for student_id, data in student_data.items():
    major = data['major'].replace(' ', '')
    last_name = data['last_name']
    first_name = data['first_name']
    grad_date = data['grad_date']
    disciplinary = 'Y' if student_id in disciplinary_action else ''
    major_students[major].append([student_id, last_name, first_name, grad_date, disciplinary])

for major, students in major_students.items():
    # Create file for each major
    file_name = f"{major}Students.csv"
    header = ['Student ID', 'Last Name', 'First Name', 'Graduation Date', 'Disciplinary Action']
    students.sort(key=sort_by_student_id)
    students.insert(0, header)
    # Write student information to the file
    write_csv(file_name, students)

# Generate DisciplinedStudents.csv
disciplined_students = [['Student ID', 'Last Name', 'First Name', 'Graduation Date']]
for student_id in sorted(disciplinary_action):
    # Extract student information
    data = student_data[student_id]
    last_name = data['last_name']
    first_name = data['first_name']
    grad_date = data['grad_date']
    # Append disciplined student information to the list
    disciplined_students.append([student_id, last_name, first_name, grad_date])

# Write DisciplinedStudents.csv
write_csv('DisciplinedStudents.csv', disciplined_students)

# Generate FullRoster.csv
full_roster_output = [
    ['Student ID', 'Major', 'First Name', 'Last Name', 'GPA', 'Graduation Date', 'Disciplinary Action']]
sorted_student_ids = sorted(student_data.keys(), key=lambda student_id: sort_by_last_name(student_id, student_data))
for student_id in sorted_student_ids:
    # Extract student information
    data = student_data[student_id]
    last_name = data['last_name']
    first_name = data['first_name']
    major = data['major']
    gpa = data['gpa']
    grad_date = data['grad_date']
    disciplinary = 'Y' if student_id in disciplinary_action else ''
    # Append student information to the output list
    full_roster_output.append([student_id, major, first_name, last_name, gpa, grad_date, disciplinary])

# Write FullRoster.csv
write_csv('FullRoster.csv', full_roster_output)

# Generate ScholarshipCandidates.csv
eligible_students = [(student_id, data) for student_id, data in student_data.items() if
                     student_id not in disciplinary_action and 'grad_date' in data and data['gpa'] > 3.8]
eligible_students.sort(key=lambda student: sort_by_student_id(student))  # Sort by student ID
scholarship_candidates = [['Student ID', 'Last Name', 'First Name', 'Major', 'GPA']]
for student_id, data in eligible_students:
    # Extract student information
    last_name = data['last_name']
    first_name = data['first_name']
    major = data['major']
    gpa = data['gpa']
    # Append student information to the list of scholarship candidates
    scholarship_candidates.append([student_id, last_name, first_name, major, gpa])

# Write ScholarshipCandidates.csv
write_csv('ScholarshipCandidates.csv', scholarship_candidates)
