# ========== Info ========#
# This file contain mainly function to creating list of random numbers to sort

# ========= Directories ==========#
import random


# Function 1 - random numbers generating
# Function will return a list of random numbers. Its size, and boundaries will be provide by user.
def rand_number(size, boundary):
    rand_list = []

    for item in range(0, size):
        rand_list.append(random.randint(0, boundary-1))

    return rand_list


# Function 2 - list of numbers
# Function will return list of sorted numbers. Its size will be provide by user.
def list_of_numbers(reach):
    input_list = []

    for item in range(0, reach):
        input_list.append(item)

    return input_list


# Function 3 - list of random, unique numbers
def unique_rand_numbers(size, reach):
    input_list = []

    while len(input_list) != size:
        generated_number = random.randint(1, reach)

        if generated_number not in input_list:
            input_list.append(generated_number)

    return input_list
