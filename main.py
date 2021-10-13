#========= Directories and files ========#
from Soritng_algorithms import sorting_algorithms
from Rand_numbers import rand_numbers
from Searching_algorithms import searching_algorithms
from Verification_functions import verification_function

x = rand_numbers.unique_rand_numbers(100,100)
x = sorting_algorithms.bubble_sort(x)
print(x)
#result = searching_algorithms.linear_search(100, x)
#verification_function.verification_search(result)
result = searching_algorithms.binary_search(100, x)
verification_function.verification_search(result)


