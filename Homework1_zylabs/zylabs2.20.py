# MaimunaMurad
# 2065973

lemon_juice_cups = float(input("Enter amount of lemon juice (in cups):\n"))
water_cups = float(input("Enter amount of water (in cups):\n"))
agave_nectar_cups = float(input("Enter amount of agave nectar (in cups):\n"))

num_servings = int(input("How many servings does this make?\n"))

print("\nLemonade ingredients - yields {:.2f} servings".format(num_servings))
print("{:.2f} cup(s) lemon juice".format(lemon_juice_cups))
print("{:.2f} cup(s) water".format(water_cups))
print("{:.2f} cup(s) agave nectar".format(agave_nectar_cups))

desired_servings = int(input("\nHow many servings would you like to make?\n"))

adjusted_lemon_juice_cups = (desired_servings / num_servings) * lemon_juice_cups
adjusted_water_cups = (desired_servings / num_servings) * water_cups
adjusted_agave_nectar_cups = (desired_servings / num_servings) * agave_nectar_cups

print("\nLemonade ingredients - yields {:.2f} servings".format(desired_servings))
print("{:.2f} cup(s) lemon juice".format(adjusted_lemon_juice_cups))
print("{:.2f} cup(s) water".format(adjusted_water_cups))
print("{:.2f} cup(s) agave nectar".format(adjusted_agave_nectar_cups))

gallons_per_cup = 1 / 16  # 1 gallon = 16 cups

adjusted_lemon_juice_gallons = adjusted_lemon_juice_cups * gallons_per_cup
adjusted_water_gallons = adjusted_water_cups * gallons_per_cup
adjusted_agave_nectar_gallons = adjusted_agave_nectar_cups * gallons_per_cup

print("\nLemonade ingredients - yields {:.2f} servings".format(desired_servings))
print("{:.2f} gallon(s) lemon juice".format(adjusted_lemon_juice_gallons))
print("{:.2f} gallon(s) water".format(adjusted_water_gallons))
print("{:.2f} gallon(s) agave nectar".format(adjusted_agave_nectar_gallons))
