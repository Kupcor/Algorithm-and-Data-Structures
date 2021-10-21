# ========= Info =========
# This file contain basic of the arrays in python

new_list = [] # empty array define
new_array = [1, 2, 3, 4, 5]  # new array with some values define

result = new_array[0]  # access to value: '1' from new_array array. We do not call entire list

# This instruction will check if value: '1' is in "new_array" array
# It could be also check by any searching algorithm or by by another loop
if 1 in new_array:
    print(True)

# This instruction will exactly do the same as previous
for n in new_array:
    if n == 1:
        print(True)

    break

# Insert values to array
# By insert -> this function insert any value to any index and shift indexes of the rest values
new_array.insert(0, 100)
print(new_array)

# By append -> this function insert any value to the end of the array
new_array.append(31)
print(new_array)

# By add one list to another
new_array.extend([54, "pen", 1])
print(new_array)

# Deleting values is as reversed inserting. This function delete first inserted value in the list
new_array.remove(1)
print(new_array)


