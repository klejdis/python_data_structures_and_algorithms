"""
Circular Queue implementation using Python list
are FIFO (First In First Out) data structures
"""


class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def enqueue(self, item):
        if (self.rear + 1) % self.size == self.front:
            return "Queue is full"
        elif self.is_empty():
            self.front = self.rear = 0
            self.queue[self.rear] = item
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        elif self.front == self.rear:
            item = self.queue[self.front]
            self.front = self.rear = -1
            return item
        else:
            item = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            return item

    def is_empty(self):
        return self.front == -1

    def __str__(self):
        if self.is_empty():
            return "Queue is empty"
        elif self.rear >= self.front:
            return str(self.queue[self.front:self.rear + 1])
        else:
            return str(self.queue[self.front:] + self.queue[:self.rear + 1])
