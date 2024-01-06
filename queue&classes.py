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