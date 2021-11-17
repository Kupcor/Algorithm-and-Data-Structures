# ========= Info =========
# This file contain basic of the linked list in python

# ========= Directories =========
from Rand_numbers import rand_numbers


# Single linked list
# Creating class to represent a node
class Node:

    # object for storing a single node of a linked list
    data = None         # storage data
    next_node = None    # reference to the next value in linked list

    # adding constructor to ease creating this node
    def __init__(self, data):
        self.data = data

    # adding string representation of what will be printed on the console
    def __repr__(self):
        return "<Node data: %s>" % self.data


class LinkedList:

    # head is first node in the LinkedList
    # the rest of nodes will have a reference to the next nodes
    # [0] -> [1] -> [2] -> [3]
    def __init__(self):
        self.head = None

    # adding string representation of what will be printed on the console
    # it takes O(n) time
    def __repr__(self):

        # creating empty list
        nodes = []

        # current variable is a pointer to the head node
        current = self.head

        while current:  # if current is not empty then while loop will execute
            if current is self.head:
                nodes.append(("[Head: %s]" % current.data))  # Node which is head will be featured
            elif current.next_node is None:  # Node which is tail will be feature
                nodes.append(("[Tail: %s]" % current.data))
            else:
                nodes.append("[%s]" % current.data)

            # assigned next node to current variable
            current = current.next_node

        return '-> '.join(nodes)  # double string return

    # method to search item in linked list
    # if value is present in linked list method will return True
    # else method will return None
    # O(n) time
    def search(self, key):
        current = self.head

        while current:  # loop will run only if linked list exist, if it run to Tail it will end to
            if current.data == key:
                return True
            # if key is not found in
            else:
                current = current.next_node
        #  if searched value does not exist method will return None
        return None

    # insert method -> it will insert any values between any nodes in linked list
    # index is not exactly an index position of element in Linked list like in arrays, but
    # this serves as a countdown from the start to an position
    # overall it takes linear time O(n)
    def insert(self, data, index):
        if index == 0:
            self.add(data)
        elif index > self.size():
            return "Error: index values is greater tha linked list size"
        elif index > 0:
            new_node = Node(data)

            position = index
            current = self.head

            while position > 1:
                current = current.next_node
                position -= 1

            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new_node
            new_node.next_node = next_node

    # remove method -> it will delete first delivered value in linked list
    # in worse case scenario it takes linear time
    def remove(self, key):
        current = self.head
        previous = None
        found = False

        while current and not found:
            # we want to delete head of the list
            if current.data == key and current == self.head:
                self.head = current.next_node
                found = True

            # if key is not a head
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            # if key value is not found
            else:
                previous = current
                current = current.next_node

        return current

    # delete method -> deleting method by Node position (index variable)
    def delete(self, index):
        current = self.head

        # First case -> we want to delete head
        if index == 0:
            self.head = current.next_node
        elif index > self.size():
            return "Error: this position does not exist in this linked list"
        elif index > 0:
            position = index

            while position > 1:
                current = current.next_node
                position -= 1

            next_value = current.next_node
            current.next_node = next_value.next_node

    # method to check if LinkedList is empty or not
    def is_empty(self):
        return self.head == None

    # method to check size of the linked list
    # to check size we have to go by each Node until reach Tail Node
    # returning size of the list has linear time: O(n)
    def size(self):
        current = self.head
        count = 0  # iterator

        while current:  # if current storage value it return True value
            count += 1  # counting Nodes
            current = current.next_node

        return count  # returning size of the LinkedList

    def add(self, data):

        # creating new Node object, which will be added to linked list
        new_node = Node(data)

        # adding new node to the head of the list so that new node is new head of the list
        # assigned reference of new node to current head of the list, if list is empty new reference will be
        # assigned as None
        # and then assigned self.head var to the new node
        # it is constant time operation: O(1)
        new_node.next_node = self.head
        self.head = new_node

    # return a node at a given index
    def node_at_index(self, index):
        if index == 0:
            return self.head
        else:
            current = self.head
            position = 0

            # calculate an index of current Node
            while position < index:
                current = current.next_node
                position += 1
            return current

    # method to add multiple values to linked list, which are stored in array/list ect.
    def add_list(self, list_of_values):

        for i in range(0, len(list_of_values)):
            self.add(list_of_values[i])

