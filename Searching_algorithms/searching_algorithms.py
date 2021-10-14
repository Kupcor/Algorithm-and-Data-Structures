# ========== Info ========#
# This file contain some searching functions

# ========= Directories and files ========#
import math
from Soritng_algorithms import sorting_algorithms


# Function 1 - linear search
# 1. Start at the beginning of the list/range
# 2. Compare the current number/values with the value you are looking for
# 3. If this is the wanted number then stop searching
# 4. If this is not the wanted number then go to the next value
# 5. Go to step 2

# Function will return the index position of the wanted number/target if found, else return None

def linear_search(wanted_number, _list=[]):
    input_list = sorting_algorithms.bubble_sort(_list)

    for i in range(0, len(input_list)):
        if input_list[i] == wanted_number:
            return i

    print("Wanted number is not found. It is probably out of range.")
    return None


# Function 2 - binary search
# Input precondition - values have to be sorted
# 1. Go to the middle of the list/range
# 2. Compare the current number/values with the value you are looking for
# 3. If this is the wanted number then stop searching
# 4. If wanted number is greater than current value than define new range of searching:
#       (first value = current value, end of range>
# 5. If wanted number is lower than current values than define new range of searching:
#       (first value, end of range = current value
# 6. Go to step 1

# Function will return the index position of the wanted number/target if found, else return None

def binary_search(wanted_number, _list=[]):
    input_list = _list

    max_range = len(input_list) - 1  # last element of the input_list; position of last element of the input_list
    min_range = 0  # first element of the input_list; position of the first element of the input_list
    current_position = int((max_range - min_range) / 2)  # current position of the compared value

    while current_position != max_range or current_position != min_range:

        if input_list[current_position] == wanted_number:
            return current_position  # position of the wanted item

        else:
            if current_position >= wanted_number:
                max_range = current_position
                current_position = (max_range + min_range) / 2
                current_position = math.floor(current_position)
            elif current_position <= wanted_number:
                min_range = current_position
                current_position = (max_range + min_range) / 2
                current_position = math.ceil(current_position)

    print("Wanted number is not found. It is probably out of range.")
    return None
