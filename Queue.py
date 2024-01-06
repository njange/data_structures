# FIFO
# Queue data structure allows insertion of an element at one end and deletion of an element at the other end.
# This queue is called First In First Out (FIFO) queue because the element which is inserted first is retrieved first.
# Enqueue: Insertion operation is called enqueue.
# Dequeue: Deletion operation is called dequeue.
# isEmpty: Check if the queue is empty.
# isFull: Check if the queue is full.
# peek: Get the value of the front of the queue without removing it.

queue = []
queue.append(10)
print(queue)
queue.append(20)
queue.append(30)
print(queue)

print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))