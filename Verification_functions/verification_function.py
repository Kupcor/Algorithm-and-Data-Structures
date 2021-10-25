# ========== Info ========#
# This file contain some function, which will be verify algorithms in this project

# ========= Directories and files ========#


# Function 1 - verification searching algorithms

def verification_search(index):
    if index is None:
        print("Index is not found")
    else:
        print("Index is found. Position of the wanted number is: ", index)


# Function 2 - verification searching algorithms, recursive version
def verification_search(result):
    print("Wanted number found: ", result)


# Function 3 - verification of sorting algorithm
def verify_sorted(list):
    if len(list) <= 1:
        return True

    return list[0] <= list[1] and verify_sorted(list[1:])
