from queue import Queue
q = Queue(maxsize = 5)
print(f"Empty: {q.empty()}")
q.put(1)
q.put(2)
q.put(3)
q.put(4)
q.put(5)
print(f"Full: {q.full()}")