# ========== Info ========#
# This file contain some searching functions

# ========= Directories and files ========#
from Soritng_algorithms import sorting_algorithms


# Function 1 - linear search
# 1. Start at the beginning of the list/range
# 2. Compare the current number/values with the value you are looking for
# 3. If this is the wanted number then stop searching
# 4. If this is not the wanted number then go to the next value
# 5. Go to step 2

# Function will return the index position of the wanted number/target if found, else return None

def linear_search(wanted_value, _list=[]):
    input_list = _list

    for index in range(0, len(input_list)):
        if input_list[index] == wanted_value:
            return index

    print("Wanted value is not found. It is probably out of range.")
    return None


# Function 2 - binary search
# Input precondition - values have to be sorted
# 1. Go to the middle of the list/range
# 2. Compare the current number/values with the value you are looking for
# 3. If this is the wanted number then stop searching
# 4. If wanted number is greater than current value than define new range of searching:
#       (first value = current value +1, end of range). We do not include checked value
# 5. If wanted number is lower than current values than define new range of searching:
#       (first value, end of range = current value0. We do not include checked value
# 6. Go to step 1

# Function will return the index position of the wanted number/target if found, else return None

def binary_search(wanted_value, _list=[]):
    input_list = _list

    max_range = len(input_list) - 1  # last element of the input_list; position of last element of the input_list
    min_range = 0  # first element of the input_list; position of the first element of the input_list

    # If user imput empty list
    while min_range <= max_range:

        current_position = (max_range + min_range) // 2  # current position of the compared value

        if input_list[current_position] == wanted_value:
            return current_position  # position of the wanted item

        else:
            if input_list[current_position] >= wanted_value:
                max_range = current_position - 1
            elif input_list[current_position] <= wanted_value:
                min_range = current_position + 1

    print("Wanted number is not found. It is probably out of range.")
    return None


# Function 3 - recursive binary search
# Input precondition - values have to be sorted
# Function will be perform binary search by using recursion

# Function will return the True value if wanted_number exist in the list, else it will return False
def recursive_binary_search(wanted_number, _list=[]):

    # if list doesn't exist then function will return False value
    if len(_list) == 0:
        return False
    else:
        current_value = len(_list) // 2

        # Recursion implementation
        if _list[current_value] == wanted_number:
            return True
        else:
            if _list[current_value] < wanted_number:
                # Returning new list, from midpoint to end
                return recursive_binary_search(wanted_number, _list[current_value + 1:])
            else:
                return recursive_binary_search(wanted_number, _list[:current_value - 1])


