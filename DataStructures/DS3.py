# FIFO - First In First Out
from queue import Queue

q1 = Queue(maxsize=8)
q1.put("Ranjith")
q1.put("Srinika")
q1.put("Madhuri")
# q1.get(block=False)

print(q1.get())
print(q1.get())
print(q1.get())
print(q1.full())
print(q1.empty())

# LIFO - Last In First Out
from queue import LifoQueue

q2 = LifoQueue(maxsize=8)
q2.put("Ranjith")
q2.put("Srinika")
q2.put("Madhuri")

print(q2.get())
print(q2.get())
print(q2.get())
print(q2.full())
print(q2.empty())


