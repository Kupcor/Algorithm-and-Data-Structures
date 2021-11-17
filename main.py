# ========= Directories and files ========#
from Soritng_algorithms import sorting_algorithms
from Rand_numbers import rand_numbers
from Searching_algorithms import searching_algorithms
from Verification_functions import verification_function
from Data_bases import reading_data_base
from Data_bases import writing_data_base
from Data_structures.linked_list import LinkedList

# Testing writing and reading an excel files
# define file paths to files
# file_path = "C:/Users/kupco/Desktop/Programy Python/Algorithms and Data Structures/Data_bases/Odczyt_z_pliku.xlsx"
# file_path_2 = "C:/Users/kupco/Desktop/Programy Python/Algorithms and Data Structures/Data_bases/Sorted_numbers.xlsx"
# add new values to file from file_path variable
# first_data_base = rand_numbers.rand_number(100, 30)
# writing_data_base.write_base(file_path, len(first_data_base), first_data_base)
# load first data base
# loaded_data_base = reading_data_base.load_data_base(file_path)
# sort loaded data base
# loaded_data_base = sorting_algorithms.bubble_sort(loaded_data_base)
# save lodaded data base to new file
# writing_data_base.write_base(file_path_2, len(loaded_data_base), loaded_data_base)


"""
# Merge sort testing
list = rand_numbers.rand_number(10, 2)
print(list)
list = sorting_algorithms.merge_sort(list)
print(list)
print(verification_function.verify_sorted(list))
"""
l = LinkedList()
rand_numbers = rand_numbers.rand_number(20, 100)
for number in rand_numbers:
    l.add(number)
print(l)
print(sorting_algorithms.linked_list_merge_sort(l))


