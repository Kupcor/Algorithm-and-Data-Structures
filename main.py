#========= Directories and files ========#
from Soritng_algorithms import sorting_algorithms
from Rand_numbers import rand_numbers
from Searching_algorithms import searching_algorithms

#searching_algorithms.linear_search(100000,100000)
#searching_algorithms.binary_search(16,16)

x = rand_numbers.unique_rand_numbers(55, 1000)
print(x)

searching_algorithms.linear_search(7,x)






