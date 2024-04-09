Adding or inserting a new node before a node with a given value

add_before(self, data, x):
    if self.head is None:
        print("Linked List is empty")
        return
    if x == self.head.data:
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
        return
    n = self.head
    while n.ref is not None:
        if x == n.ref.data:
            break
        n = n.ref
    if n.ref is None:
        print("Node is not present in the Linked List")
    else:
        new_node = Node(data)
        new_node.ref = n.ref
        n.ref = new_node
        return