# ========== Info ========#
# This file contain some sorting functions

# ========= Directories and files ========#
from Soritng_algorithms import additional_functions

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


# Sorting algorithm 2 - Merge Sort
"""
Sorts a list in ascending order -> returns a new sorted list
1.Devide: find a the midpoint pf the list and divide into sublists
2.Conques: Recursively sort the sublists in previous step
3.Combine: merge the sorted sublist created in previous step
"""
def merge_sort(list_of_values):
    if len(list_of_values) <= 1:
        return list_of_values

    # recursive part of algorithm
    # if list has len = 1 then single-elements list will return
    # by each loop pass to merge sort function will be called
    # split function devide imputed list into two sublists
    left_half, right_half = additional_functions.split(list_of_values)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return additional_functions.merge(left, right)
