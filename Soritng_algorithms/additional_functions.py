# ========== Info ========#
# This file contain some additional functions to sorting algorithms

# ========= Directories and files ========#

# Function 1 - split function
# Function will divide list into two sublists
def split(list_of_values):
    """
    Divide the unsorted list at midpoint into sublists
    Returns two sublists - left and right
    """
    mid = len(list_of_values) // 2
    left = list_of_values[:mid]  # stopping value is not included
    right = list_of_values[mid:]

    # we are returning two values in this function
    return left, right


# Function 2 - merge function.
# This function will sort and merge two sublists for mergesort
def merge(left, right):
    """
    Merges two lists (arrays), sorting them in the process
    :param left:
    :param right:
    :return: list_of_values
    """
    list_of_values = []
    i = 0  # indexes in the left list
    j = 0  # indexes in the right list

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            list_of_values.append(left[i])  # add element of left list to list_of_value which will be returned
            i += 1
        else:
            list_of_values.append(right[j])
            j += 1

    # in case in which they would stay some items from left list
    while i < len(left):
        list_of_values.append(left[i])
        i += 1

    # in case in which they would stay some items from right list
    while j < len(right):
        list_of_values.append(right[j])
        j += 1

    return list_of_values
