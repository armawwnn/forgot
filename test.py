
import random

def generate_random_sum(n, target_sum):
    # Generate n-1 random numbers between 0 and target_sum
    parts = [random.randint(0, target_sum) for _ in range(n - 1)]
    parts.sort()

    # Calculate the differences between consecutive parts
    differences = [parts[0]] + [parts[i] - parts[i - 1] for i in range(1, n - 1)] + [target_sum - parts[-1]]

    return differences


def descending_numbers(start=80, end=0):
    numbers = []
    for num in range(start, end - 1, -1):
        numbers.append(num)
    return numbers


import random

# Original array
arr = [1,2,3,4,5,6,7,8,9]

# Define the start and end indices of the part you want to shuffle
start_index = 0
end_index = 1

# Extract the part of the array you want to shuffle
part_to_shuffle = arr[start_index:end_index]
# Shuffle the extracted part
random.shuffle(part_to_shuffle)

# Put the shuffled part back into the original array
arr[start_index:end_index] = part_to_shuffle

