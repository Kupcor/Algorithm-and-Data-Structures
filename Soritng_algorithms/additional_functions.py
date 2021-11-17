# ========== Info ========#
# This file contain some additional functions to sorting algorithms

# ========= Directories and files ========#
from Data_structures.linked_list import LinkedList

# Function 1 - split function
# Function will divide list into two sublists
def split(list_of_values):
    """
    Divide the unsorted list at midpoint into sublists
    Returns two sublists - left and right
    """
    mid = len(list_of_values) // 2
    left = list_of_values[:mid]  # stopping value is not included
    right = list_of_values[mid:]

    # we are returning two values in this function
    return left, right


# Function 2 - merge function.
# This function will sort and merge two sublists for mergesort
def merge(left, right):
    """
    Merges two lists (arrays), sorting them in the process
    :param left:
    :param right:
    :return: list_of_values
    """
    list_of_values = []
    i = 0  # indexes in the left list
    j = 0  # indexes in the right list

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            list_of_values.append(left[i])  # add element of left list to list_of_value which will be returned
            i += 1
        else:
            list_of_values.append(right[j])
            j += 1

    # in case in which they would stay some items from left list
    while i < len(left):
        list_of_values.append(left[i])
        i += 1

    # in case in which they would stay some items from right list
    while j < len(right):
        list_of_values.append(right[j])
        j += 1

    return list_of_values

# Function 3 - split function
# Function will divide list into two sublists
def split_linked_list(linked_list):
    """
    Divide the unsorted list at midpoint into sublists
    Returns two sublists - left and right
    """

    if linked_list == None or linked_list.head == None:
        left_half = linked_list
        right_half = None

        return left_half, right_half
    else:
        # calculate mid point of the linked list
        size = linked_list.size()
        mid = size // 2

        mid_node = linked_list.node_at_index(mid - 1)  # size always return a value grater than len
        left_half = linked_list
        right_half = LinkedList()
        right_half.head = mid_node.next_node  # creating and assigned right half of linked list
        mid_node.next_node = None  # Cut second half of left_half of linked list

        # we are returning two values in this function
        return left_half, right_half

# Function 4 - merge function for linked list.
# This function will sort and merge two sublists for mergesort
def merge_linked_list(left, right):
    """
    Merges two linked lists, sorting them in the process
    :param left:
    :param right:
    :return: list_of_values
    """

    # Create a new linked list that contains nodes from
    # merging left and right
    merged = LinkedList()

    # Add a fake head. It will be discarded later
    merged.add(0)

    # Set current to the head of the linked list
    current = merged.head

    # Obtain head nodes for left and right linked lists
    left_head = left.head
    right_head = right.head

    # Iterate over left and right until we reach the tail node
    # of either
    while left_head or right_head:
        # If the head node of left is None, we past the tail
        # Add the node from right to merged linked list
        if left_head is None:
            current.next_node = right_head
            # Call next on right to set lop condition to false
            right_head = right_head.next_node
        # If the head node of right is None, we're past the tail
        # Add the tail node from left to merged linked list
        elif right_head is None:
            current.next_node = left_head
            # Call next on left to set loop condition to false
            left_head = left_head.next_node
        else:
            # Not at either tail node
            # Obtain node data to perform comparison operations
            left_data = left_head.data
            right_data = right_head.data
            # Comparison
            if left_data < right_data:
                current.next_node = left_head
                left_head = left_head.next_node
            # If data on left is greater than right:
            else:
                current.next_node = right_head
                right_head = right_head.next_node

        # Move current to next node
        current = current.next_node

    # Discard fake head and set first merged node as head
    head = merged.head.next_node
    merged.head = head

    return merged

