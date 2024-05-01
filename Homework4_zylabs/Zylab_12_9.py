# Maimuna Murad
# 2065973
# Lab 12.9 Exception handling to detect input string vs. integer

# Split input into 2 parts: name and age
parts = input().split()
name = parts[0]
while name != '-1':
    try:
        # Attempt to convert the second part to an integer and increment it
        age = int(parts[1]) + 1
    except ValueError:  # Catch ValueError exception
        age = 0  # Set age to 0 if conversion fails
    print(f'{name} {age}')

    # Get next line
    parts = input().split()
    name = parts[0]
