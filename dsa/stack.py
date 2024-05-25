"""
Stack implementation using list
are LIFO (Last In First Out) data structures
"""


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def __str__(self):
        return str(self.stack)


# Using LinkedList as a stack

from dsa.linked_list import Node


class Stack:
    def __init__(self):
        self.head = None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.is_empty():
            return None
        item = self.head.data
        self.head = self.head.next
        return item

    def peek(self):
        if self.is_empty():
            return None
        return self.head.data

    def is_empty(self):
        return self.head is None

    def __str__(self):
        items = []
        current = self.head
        while current:
            items.append(current.data)
            current = current.next
        return str(items)


if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack)
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack)
    print(stack.is_empty())
    stack.push(4)
    print(stack.peek())
    print(stack)
    print(stack.is_empty())
    print(stack.pop())
    print(stack.is_empty())
    print(stack.pop())
    print(stack.is_empty())