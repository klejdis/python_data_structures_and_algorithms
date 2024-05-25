"""
Circular Doubly Linked List

A circular doubly linked list is a list that has a head and a tail.
The head points to the first node in the list and the tail points to the last node in the list.
The last node in the list points to the head and the head points to the last node in the list.
Each node in the list has a pointer to the next node and a pointer to the previous node.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.head.next = self.tail
            self.head.prev = self.tail
            self.tail.next = self.head
            self.tail.prev = self.head
        else:
            new_node.prev = self.tail
            new_node.next = self.head
            self.tail.next = new_node
            self.head.prev = new_node
            self.tail = new_node
        self.size += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.head.next = self.tail
            self.head.prev = self.tail
            self.tail.next = self.head
            self.tail.prev = self.head
        else:
            new_node.prev = self.tail
            new_node.next = self.head
            self.tail.next = new_node
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def insert(self, index, value):
        if index >= self.size:
            self.append(value)
        elif index == 0:
            self.prepend(value)
        else:
            new_node = Node(value)
            current_node = self.head
            for i in range(index - 1):
                current_node = current_node.next
            new_node.prev = current_node
            new_node.next = current_node.next
            current_node.next.prev = new_node
            current_node.next = new_node
            self.size += 1

    def remove(self, index):
        if index >= self.size:
            print("Index out of range")
        elif index == 0:
            self.head = self.head.next
            self.head.prev = self.tail
            self.tail.next = self.head
            self.size -= 1
        else:
            current_node = self.head
            for i in range(index):
                current_node = current_node.next
            current_node.prev.next = current_node.next
            current_node.next.prev = current_node.prev
            self.size -= 1

    def __len__(self):
        return self.size

    def __str__(self):
        result = []
        current_node = self.head
        for i in range(self.size):
            result.append(current_node.value)
            current_node = current_node.next
        return f"[{', '.join(str(value) for value in result)}]"


# Circular Doubly Linked List
cdll = CircularDoublyLinkedList()
cdll.append(1)
cdll.append(2)
cdll.append(3)
cdll.append(4)
cdll.append(5)
print(cdll)  # [1, 2, 3, 4, 5]
cdll.prepend(0)
print(cdll)  # [0, 1, 2, 3, 4, 5]
cdll.insert(3, 10)
print(cdll)  # [0, 1, 2, 10, 3, 4, 5]