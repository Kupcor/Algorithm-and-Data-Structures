#========== Info ========#
#This file contain some searching funtions

#========= Directories and files ========#
import math
from Soritng_algorithms import sorting_algorithms

from Rand_numbers import rand_numbers

#Function 1 - linear search
#1. Start at the begining of the list/range
#2. Compare the current number/values with the value you are looking for
#3. If this is the wanted number then stop searching
#4. If this is not the wanted number then go to the next value
#5. Go to step 2

#Function will return the index position of the wanted number/target if found, else return None

def linear_search(wanted_number,_list = []):

    list = sorting_algorithms.bubble_sort(_list)

    for i in range(0, len(list)):
        if list[i] == wanted_number:
            print("Linear search: wanted number is found. This is: ", wanted_number)
            print("Amount of attemps: ", i+1)
            print("Position of wanted number is: ", i)
            return i

    print("Wanted number is not found. It is probably out of range.")
    return None

#Function 2 - binary search
#Input precondiction - values have to be sorted
#1. Go to the middle of the list/range
#2. Compare the current number/values with the value you are looking for
#3. If this is the wanted number then stop searching
#4. If wanted number is greater than current value than define new range of searching: (first value = current value, end of range>
#5. If wanted number is lower than current values than define new range of searching: (first value, end of range = current value
#5. Go to step 1
#TODO correct algorithm. It doesn't return properly index.

def binary_search(wanted_number, _list = []):
    list = _list
    attemps = 0

    max_range = len(list)
    min_range = 0 #change to 0
    current_value = int((max_range + min_range) / 2)

    while attemps != len(list):
        attemps += 1
        print(current_value)

        if current_value == wanted_number:
            print("Binary search: wanted number is found. This is: ", wanted_number)
            print("Amount of attemps: ", attemps)
            return current_value - 1 #position of the wanted item
        else:
            if current_value > wanted_number:
                max_range = current_value
                current_value = (max_range + min_range) / 2
                current_value = math.floor(current_value)
            else:
                min_range = current_value
                current_value = (max_range + min_range) / 2
                current_value = math.ceil(current_value)

    print("Wanted number is not found. It is probably out of range.")
    return None

