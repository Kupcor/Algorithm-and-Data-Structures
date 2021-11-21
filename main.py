# ========= Directories and files ========#
from Soritng_algorithms import sorting_algorithms
from Rand_numbers import rand_numbers
from Searching_algorithms import searching_algorithms
from Verification_functions import verification_function
from Data_bases import reading_data_base
from Data_bases import writing_data_base
from Data_structures.linked_list import LinkedList
from Time import timing

# name database:
names = ["Piotr", "Anna", "Marek", "Paweł", "Alfreda", "Amelia", "Aneta", "Fabian", "Ida", "Halina", "Kinga", "Zygmunt", "Henryk", "Angela", "Aleksandra", "Ola", "Bartosz", "Michał"]
print(names)
sorted_list = sorting_algorithms.quick_sort(names)
print(sorted_list)
searching_name = searching_algorithms.linear_search("Ida", sorted_list)
print(searching_name)