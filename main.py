#========= Directories and files ========#
from Soritng_algorithms import sorting_algorithms
from Rand_numbers import rand_numbers
from Searching_algorithms import searching_algorithms


x = rand_numbers.unique_rand_numbers(100000, 100000)
print(x)
print(sorting_algorithms.bubble_sort(x))
#sorting_algorithms.bubble_sort(x)
#searching_algorithms.linear_search(7,x)
searching_algorithms.binary_search(100000,x)





