#========== Info ========#
#This file contain mainly function to creating list of random numbers to sort

#========= Directories ==========#
import random


#Funtion 1 - random numbers generating
def rand_number(size, boundary):
    rand_list = []

    for item in range(1, size):
        rand_list.append(random.randint(1,boundary))

    i = 0
    for item in rand_list:
        if i % 10 != 0:
            print(item,end=" ")
        else:
            print()
            print(item, end = " ")
        i+=1

    return rand_list

#Funtion 2 - list of numbers
def list_of_numbers(reach):
    list = []

    for item in range(1, reach):
        list.append(item)

    return list

#Function 3 - list of random, unique numbers
#TODO add some restriction
def unique_rand_numbers(size,reach):
    list = []

    while len(list) != size:
        rand_number = random.randint(1, reach)

        if rand_number not in list:
            list.append(rand_number)

    return list