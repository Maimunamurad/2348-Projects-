# Maimuna Murad
# 2065973
# Lab 14.13 Sorting user IDs

# Global variable
num_calls = 0

# Partitioning algorithm
def partition(user_ids, i, k):
    # Pick middle element as pivot
    pivot_index = (i + k) // 2
    pivot_value = user_ids[pivot_index]

    # Initialize low and high indices
    l = i
    h = k

    # Partitioning
    while True:
        # Move l to the right until a value >= pivot is found
        while user_ids[l] < pivot_value:
            l += 1
        # Move h to the left until a value <= pivot is found
        while user_ids[h] > pivot_value:
            h -= 1
        if l >= h:
            # If pointers crossed, partitioning is done
            return h
        # Swap elements at l and h
        user_ids[l], user_ids[h] = user_ids[h], user_ids[l]
        l += 1
        h -= 1

# Quicksort algorithm
def quicksort(user_ids, i, k):
    global num_calls
    num_calls += 1
    if i < k:
        # Partition the array
        j = partition(user_ids, i, k)
        # Recursively sort the subarrays
        quicksort(user_ids, i, j)
        quicksort(user_ids, j + 1, k)

if __name__ == "__main__":
    user_ids = []
    user_id = input()
    while user_id != "-1":
        user_ids.append(user_id)
        user_id = input()

    # Initial call to quicksort
    quicksort(user_ids, 0, len(user_ids) - 1)

    # Print number of calls to quicksort
    print(num_calls)

    # Print sorted user ids
    for user_id in user_ids:
        print(user_id)
