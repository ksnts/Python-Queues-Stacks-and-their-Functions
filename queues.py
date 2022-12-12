from collections import deque
# Queue: Building a queue data type
class Queue:

    def __init__(self, *elements):
        self._elements=deque(elements)

    def __len__(self):
        return len(self._elements)

    def __iter__(self):
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

class Stack(Queue):
    def dequeue(self):
        return self._elements.pop()

# from queues import Stack

# lifo=Stack("1st", "2nd", "3rd")
# for element in lifo:
#     print(element)

from heapq import heappop, heappush
from itertools import count 

class PriorityQueue:
    def __init__(self):
        self._elements = []
        self.counter = count()

    def enqueue_with_priority(self, priority, value):
        element = (-priority, next(self._counter), value)
        heappush(self._elements, element)

    def dequeue(self):
        return heappop(self._elements)[-1]

# from queues import PriorityQueue

# CRITICAL = 3
# IMPORTANT = 2
# NEUTRAL = 1

# messages = PriorityQueue()
# messages.enqueue_with_priority(IMPORTANT, "Windshield wipers turned on")
# messages.enqueue_with_priority(NEUTRAL, "Radio station tuned in")
# messages.enqueue_with_priority(CRITICAL, "Brake pedal depressed")
# messages.enqueue_with_priority(IMPORTANT, "Hazard lights turned on")

# messages.dequeue()
