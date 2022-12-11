from collections import deque
# Queue: Building a queue data type
class Queue:

    def __init__(self, *elements):
        self._elements=deque(elements)

    def __len__(self):
        return len(self._elements)

    def _iter__(self):
        while len(self) > 0:
            yield self.dequeue()

    def enqueue(self, element):
        self._elements.append(element)
    
    def dequeue(self):
        return self._elements.popleft()
        
# This part is for the python interpreter but it is coded here in vs for commiting purposes
# from queues import Queue

# fifo = Queue()

# fifo.enqueue("1st")
# fifo.enqueue("2nd")
# fifo.enqueue("3rd")
# fifo.enqueue("4th")

# fifo.dequeue
# fifo.dequeue
# fifo.dequeue
# fifo.dequeue

# from queues import Queue

# fifo =Queue("1st", "2nd", "3rd")
# len(fifo)

# for element in fifo:
#     print(element)

#     len(fifo)
