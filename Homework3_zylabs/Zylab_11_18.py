# Maimuna Murad
# 2065973
# Lab 11.18 Filter and sort a list

integers = input().split()

non_negative_int = []

for num in integers:
    num = int(num)

    if num >= 0:

        non_negative_int.append(num)

non_negative_int.sort()

for i in non_negative_int:
    print(i, end=' ')