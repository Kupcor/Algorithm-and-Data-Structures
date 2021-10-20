# ========= Directories and files ========#
from Soritng_algorithms import sorting_algorithms
from Rand_numbers import rand_numbers
from Searching_algorithms import searching_algorithms
from Verification_functions import verification_function
from Data_bases import reading_data_base
from Data_bases import writing_data_base

# define file paths to files
file_path = "C:/Users/kupco/Desktop/Programy Python/Algorithms and Data Structures/Data_bases/Odczyt_z_pliku.xlsx"
file_path_2 = "C:/Users/kupco/Desktop/Programy Python/Algorithms and Data Structures/Data_bases/Sorted_numbers.xlsx"

# add new values to file from file_path variable
first_data_base = rand_numbers.rand_number(100, 30)
writing_data_base.write_base(file_path, len(first_data_base), first_data_base)

# load first data base
loaded_data_base = reading_data_base.load_data_base(file_path)

# sort loaded data base
loaded_data_base = sorting_algorithms.bubble_sort(loaded_data_base)

# save lodaded data base to new file
writing_data_base.write_base(file_path_2, len(loaded_data_base), loaded_data_base)

# result = searching_algorithms.linear_search(100, x)
# verification_function.verification_search(result)
#result = searching_algorithms.binary_search(0, x)
#verification_function.verification_search(result)
#result = searching_algorithms.recursive_binary_search(500, x)
#verification_function.verification_search(result)

