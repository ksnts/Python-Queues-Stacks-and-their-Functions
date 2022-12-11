from collections import deque
# Queue: Building a queue data type
class Queue:
    def __init__(self):
        self._elements=deque()

    def enqueue(self, element):
        self._elements.append(element)
    
    def dequeue(self):
        return self._elements.popleft()

from queues import Queue

fifo = Queue()

fifo.enqueue("1st")
fifo.enqueue("2nd")
fifo.enqueue("3rd")
fifo.enqueue("4th")

print(fifo.dequeue())
print(fifo.dequeue())
print(fifo.dequeue())
print(fifo.dequeue())





