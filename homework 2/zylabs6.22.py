a1 = int(input())
b1 = int(input())
c1 = int(input())
a2 = int(input())
b2 = int(input())
c2 = int(input())

solution_found = False
for x in range(-10, 11):
    for y in range(-10, 11):
        if a1 * x + b1 * y == c1 and a2 * x + b2 * y == c2:
            print(x, y)
            solution_found = True
            break

    if solution_found:
        break

if not solution_found:
    print("No solution")
