# Adding a new node at the beginning of the linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None
class LinkedList:
    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, "--->", end=" ")
                n = n.ref

# Adding a new node at the beginning of the linked list

    def add_begin(self, data):
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node


LL1 = LinkedList()
LL1.add_begin(10)
LL1.add_begin(20)
LL1.add_begin(30)
print(LL1)


# Adding a new node after a node with a given value

    def add_after(self, data, x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.ref
        if n is None:
            print("Node is not present in the Linked List")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node



