# ========= Info =========
# This file contain basic of the linked list in python

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

        while current: # if current is not empty then while loop will execute
            if current is self.head:
                nodes.append(("[Head: %s]" % current.data))  # Node which is head will be featured
            elif current.next_node is None:  # Node which is tail will be feature
                nodes.append(("[Tail: %s]" % current.data))
            else:
                nodes.append("[%s]" % current.data)

            # assigned next node to current variable
            current = current.next_node

        return '-> '.join(nodes)  # double string return

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


l = LinkedList()
l.add(10)
l.add(13)
l.add(34)
size = l.size()
print(size)
list = l.__repr__()
print(list)