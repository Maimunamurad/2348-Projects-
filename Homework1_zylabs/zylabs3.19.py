# MaimunaMurad
# 2065973

import math

wall_height = float(input("Enter wall height (feet):\n"))
wall_width = float(input("Enter wall width (feet):\n"))

wall_area = int(wall_height * wall_width)
print("Wall area:", wall_area, "square feet")

paint_coverage_per_gallon = 350

paint_needed = wall_area / paint_coverage_per_gallon
print("Paint needed: {:.2f} gallons".format(paint_needed))

cans_needed = math.ceil(paint_needed)
print("Cans needed:", cans_needed, "can(s)")

paint_colors = {'red': 35, 'blue': 25, 'green': 23}
chosen_color = input("\nChoose a color to paint the wall:\n").lower()

if chosen_color in paint_colors:
    cost_per_can = paint_colors[chosen_color]
    total_cost = cost_per_can * cans_needed
    print("Cost of purchasing {} paint: ${}".format(chosen_color, total_cost))
else:
    print("Invalid color choice.")
