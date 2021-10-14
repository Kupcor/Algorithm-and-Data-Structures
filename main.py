# ========= Directories and files ========#
from Soritng_algorithms import sorting_algorithms
from Rand_numbers import rand_numbers
from Searching_algorithms import searching_algorithms
from Verification_functions import verification_function

x = rand_numbers.list_of_numbers(501)
print(x)

# result = searching_algorithms.linear_search(100, x)
# verification_function.verification_search(result)
#result = searching_algorithms.binary_search(0, x)
#verification_function.verification_search(result)
result = searching_algorithms.recursive_binary_search(500, x)
verification_function.verification_search(result)

