# ========== Info ========#
# This file contain some sorting functions
"""
List of sorting algorithms:
Function 1 - bubble sort
Function 2 - merger sort
Function 3 - merge sort for Linked List
Function 4 - bogo sort

"""

# ========= Directories and files ========#
import random

from Soritng_algorithms import additional_functions
from Data_structures import linked_list


# Function 1 - bubble sort
# Function will return sorted list of element.
def bubble_sort(_list=[]):
    input_list = _list

    i = 0
    j = 0
    while i != (len(input_list) - 1):
        while j != (len(input_list) - 1):
            if int(input_list[j]) > int(input_list[j + 1]):
                help_var = input_list[j]
                input_list[j] = input_list[j + 1]
                input_list[j + 1] = help_var
            j += 1
        j = 0
        i += 1

    return input_list


# Sorting algorithm 2 - Merge Sort
"""
Sorts a list in ascending order -> returns a new sorted list
1.Devide: find a the midpoint pf the list and divide into sublist
2.Conques: Recursively sort the sublist in previous step
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


"""
    Function 3 - linked list merge sort
"""


def linked_list_merge_sort(linked_list):
    """
    Function Sorts a linked list in ascending order
    Recursively divide the linked list into sublists containing single node
    Repeatedly merge the sublist to produce sorted sublists until one remains

    Return a sorted linked list
    :param linked_list:
    :return:
    """
    # If linked list has only one element than it will be returned right away
    # Size function of linked list is already defined in Linked_List file
    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list

    left_half, right_half = additional_functions.split_linked_list(linked_list)  # Split work properly
    left = linked_list_merge_sort(left_half)
    right = linked_list_merge_sort(right_half)

    # Final merge
    return additional_functions.merge_linked_list(left, right)


"""
    Function 4 - bogo sort
    Bogo sort randomize the order of the list until it is sorted. Yea...
    Do not use this algorithm...
    Efficiency -> efficiency is totally random
"""


def bogo_sort(list_of_values):
    is_sorted = False
    # Checking if list of numbers is sorted
    while not is_sorted:
        for index in range(len(list_of_values)-1):
            if list_of_values[index] > list_of_values[index + 1]:
                break
            else:
                if index == len(list_of_values) - 2:
                    return list_of_values

        random.shuffle(list_of_values)  # function to randomize elements positions in the sorted list


"""  
    Function 5 - selection sort
    We are creating one empty list/array for sorted numbers.
    Then we moving step by step the smallest number from unsorted array/list to sorted array list.
    Function will return sorted list.
"""


def selection_sort(list_of_values):
    sorted_list = []

    while len(list_of_values) != 0:
        smallest_number = list_of_values[0]

        for iterator in range(len(list_of_values)):
            if list_of_values[iterator] < smallest_number:
                smallest_number = list_of_values[iterator]

        sorted_list.append(smallest_number)
        list_of_values.remove(smallest_number)

    return sorted_list


"""
    Function 6 - Quick Sort
    Divide and conquer method,
    First element of the list is a pivot. Than we are creating two sublist.
    First sublist contains elements that are smaller than a pivot, second contains numbers greater than a pivot.
    Base condition of the function: size of array is equal or less than 1.
    And that all. This is awesome! 
"""


def quick_sort(list_of_values):

    if len(list_of_values) <= 1:
        return list_of_values

    smaller_values = []  # values smaller than the pivot
    greater_values = []  # values grater than the pivot
    pivot = list_of_values[0]
    for iterator in range(1, len(list_of_values)):  # we are starting from second element of the list
        if list_of_values[iterator] <= pivot:
            smaller_values.append(list_of_values[iterator])
        else:
            greater_values.append(list_of_values[iterator])
    return quick_sort(smaller_values) + [pivot] + quick_sort(greater_values)
