# Maimuna Murad
# 2065973
# Lab 14.11 Descending selection sort with output during execution

def selection_sort_descend_trace(numbers):
    for i in range(len(numbers) - 1):
        t = i
        for j in range(i + 1, len(numbers)):
            if numbers[t] < numbers[j]:
                t = j
        numbers[i], numbers[t] = numbers[t], numbers[i]
        for value in numbers:
            print(value, end=" ")
        print()

if __name__ == "__main__":
    numbers = [int(x) for x in input().split()]
    selection_sort_descend_trace(numbers)
