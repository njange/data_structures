import collections
stack = collections.deque()
stack.append(10)
stack.append(20)
stack.append(30)
print(stack)

print(stack.pop())
print(stack.pop())
print(stack.pop())

# Using queue module
import queue
stack = queue.LifoQueue(3)
stack.put(10)
stack.put(20)
stack.put(30)
print(stack)

print(stack.get())

# Timeout parameter
print(stack.get(timeout=1))
