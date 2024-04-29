import random

def shuffle_random_part(arr):
    # Choose a random index within the array
    start_index = random.randint(0, len(arr) - 1)
    
    # Decide the length of the random part (can be varied)
    part_length = random.randint(1, min(len(arr) - start_index, 4))

    # Extract the random part
    random_part = arr[start_index:start_index + part_length]

    # Shuffle the random part
    random.shuffle(random_part)

    # Update the original array with the shuffled part
    arr[start_index:start_index + part_length] = random_part

    return arr

# Example array
arr = [1,2,3,4,5,6,7,8]

# Shuffle random part of the array
result = shuffle_random_part(arr)

