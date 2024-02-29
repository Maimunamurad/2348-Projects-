def strengthen_password(password):
    strengthened_password = ""

    for char in password:
        if char == 'i':
            strengthened_password += '!'
        elif char == 'a':
            strengthened_password += '@'
        elif char == 'm':
            strengthened_password += 'M'
        elif char == 'B':
            strengthened_password += '8'
        elif char == 'o':
            strengthened_password += '.'
        else:
            strengthened_password += char

    strengthened_password += "q*s"
    return strengthened_password

simple_password = input()

stronger_password = strengthen_password(simple_password)

print(stronger_password)
