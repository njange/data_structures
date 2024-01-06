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

queue.insert(0, 10)
queue.insert(0, 20)
queue.insert(0, 30)
print(queue)

queue.pop()
print(queue)

print(not queue)

queue.append(40)
print(queue)

print(queue[0])

queue1 = []
def enqueue():
    element = input("Enter the element to be inserted: ")
    queue1.append(element)
    print(element, "is inserted into the queue")

def dequeue():
    if not queue1:
        print("Queue is empty")
    else:
        e = queue1.pop(0)
        print("Removed element: ", e)

def display():
    print(queue1)

while True:
    print("Select the operation 1. Enqueue 2. Dequeue 3. Display 4. Exit")
    choice = int(input())
    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        display()
    elif choice == 4:
        break
    else:
        print("Enter a valid choice")

