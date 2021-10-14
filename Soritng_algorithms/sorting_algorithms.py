# ========== Info ========#
# This file contain some sorting functions

# ========= Directories and files ========#


# Function 1 - bubble sort
# Function will return sorted list of element.

def bubble_sort(_list=[]):
    input_list = _list

    i = 0
    j = 0
    while i != (len(input_list) - 1):
        while j != (len(input_list) - 1):
            if int(input_list[j]) > int(input_list[j+1]):
                help_var = input_list[j]
                input_list[j] = input_list[j+1]
                input_list[j+1] = help_var
            j += 1
        j = 0
        i += 1

    return input_list
