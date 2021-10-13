#========== Info ========#
#This file contain some sorting funtions

#========= Directories and files ========#
from Rand_numbers import rand_numbers

#Function 1 - bubble sort
def bubble_sort(_list = []):
    list = _list

    i = 0
    j = 0
    while i != (len(list) - 1):
        while j != (len(list) - 1):
            if int(list[j]) > int(list[j+1]):
                help_var = list[j]
                list[j] = list[j+1]
                list[j+1] = help_var
            j += 1
        j = 0
        i += 1

    return list

    #print sorted list: 10 numbers in row
    #print()
    #i = 0
    #for item in list:
    #    if i % 10 != 0:
    #        print(item, end=" ")
    #    else:
    #        print()
    #        print(item, end=" ")
    #    i += 1