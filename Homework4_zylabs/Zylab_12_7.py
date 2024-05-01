# Maimuna Murad
# 2065973
# Lab 12.7 Fat-burning heart rate

def get_age():
    age = int(input())
    if age < 18 or age > 75:
        raise ValueError("Invalid age.")
    return age

def fat_burning_heart_rate(age):
    heart_rate = 0.70 * (220 - age)
    return heart_rate

if __name__ == "__main__":
    try:
        age = get_age()
        fb_heart_rate = fat_burning_heart_rate(age)
        print(f"Fat burning heart rate for a {age} year-old: {fb_heart_rate:.1f} bpm")
    except ValueError as ve:
        print("Invalid age.")
        print("Could not calculate heart rate info.\n") # Newline added here
