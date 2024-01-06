import collections
q = collections.deque()
print(q)

q.appendleft(10)
q.appendleft(20)
q.appendleft(30)
print(q)

print(q.pop())

print(q.append(40))
print(q)

print(not q)

print(q[0])

print(q[-1])

import queue
q1 = queue.Queue()
q1.put(10)
q1.put(20)
q1.put(30)
print(q1)

print(q1.get())
print(q1.get())
print(q1.get())

# Priority Queue
q2 = []
q2.append(2)
q2.append(1)
q2.append(3)
print(q2)
print(q2.sort())
print(q2)

q3 = queue.PriorityQueue()
q3.put(10)
q3.put(20)
q3.put(30)
print(q3)

print(q3.get())

q4 = []
q4.append((2, "work"))
q4.append((1, "eat"))
q4.append((3, "sleep"))
print(q4)
print(q4.sort())
print(q4)