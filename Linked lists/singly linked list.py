# Operations on singly linked list:
# 1. Insertion
# 2. Deletion
# 3. Traversal

# create a node

class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


# create a linked list

class LinkedList:
    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref




