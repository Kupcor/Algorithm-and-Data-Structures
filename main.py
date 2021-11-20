# ========= Directories and files ========#
from Soritng_algorithms import sorting_algorithms
from Rand_numbers import rand_numbers
from Searching_algorithms import searching_algorithms
from Verification_functions import verification_function
from Data_bases import reading_data_base
from Data_bases import writing_data_base
from Data_structures.linked_list import LinkedList
from Time import timing


numbers = rand_numbers.unique_rand_numbers(10, 30)
sorted_list = sorting_algorithms.quick_sort(numbers)
print(sorted_list)
