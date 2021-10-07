#========== Info ========#
#This file contain mainly function to creating list of random numbers to sort

#========= Directories ==========#
import random


#Funtion 1 - random numbers generating
def rand_number(size, boundary):
    rand_list = []

    for item in range(0,size):
        rand_list.append(random.randint(0,boundary))

    i = 0
    for item in rand_list:
        if i % 10 != 0:
            print(item,end=" ")
        else:
            print()
            print(item, end = " ")
        i+=1

    return rand_list