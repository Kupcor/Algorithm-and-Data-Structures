#========= Directories and files ========#
from Soritng_algorithms import sorting_algorithms
from Rand_numbers import rand_numbers
from Searching_algorithms import searching_algorithms


x = rand_numbers.unique_rand_numbers(100,100)
#print(x)
x = sorting_algorithms.bubble_sort(x)
print(x)
#print(x)
#sorting_algorithms.bubble_sort(x)
#searching_algorithms.linear_search(7, x)
#searching_algorithms.linear_search(7,x)
searching_algorithms.binary_search(100, x)




