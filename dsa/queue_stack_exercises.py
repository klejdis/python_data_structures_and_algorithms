# Exercise 1
# implement  a multistack in a list

class MultiStack:
    def __init__(self, stack_size):
        self.stack_size = stack_size
        self.num_stacks = 3
        self.array = [0] * (self.stack_size * self.num_stacks)
        self.sizes = [0] * self.num_stacks

    def push(self, stack_num, value):
        if self.is_full(stack_num):
            raise Exception("Stack is full")
        self.sizes[stack_num] += 1
        self.array[self.index_of_top(stack_num)] = value

    def pop(self, stack_num):
        if self.is_empty(stack_num):
            raise Exception("Stack is empty")
        value = self.array[self.index_of_top(stack_num)]
        self.array[self.index_of_top(stack_num)] = 0
        self.sizes[stack_num] -= 1
        return value

    def peek(self, stack_num):
        if self.is_empty(stack_num):
            raise Exception("Stack is empty")
        return self.array[self.index_of_top(stack_num)]

    def is_empty(self, stack_num):
        return self.sizes[stack_num] == 0

    def is_full(self, stack_num):
        return self.sizes[stack_num] == self.stack_size

    def index_of_top(self, stack_num):
        offset = stack_num * self.stack_size
        return offset + self.sizes[stack_num] - 1

    def __str__(self):
        return str(self.array)


ms = MultiStack(3)
ms.push(0, 1)
ms.push(0, 2)
ms.push(0, 3)
ms.push(0, 4)
ms.push(1, 5)
print(ms)


# Exercise 2
# implement a stack that returns the minimum value in O(1) time

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value):
        self.stack.append(value)
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self):
        if not self.stack:
            raise Exception("Stack is empty")
        value = self.stack.pop()
        if value == self.min_stack[-1]:
            self.min_stack.pop()
        return value

    def min(self):
        if not self.min_stack:
            raise Exception("Stack is empty")
        return self.min_stack[-1]

    def __str__(self):
        return str(self.stack)


# implement using linked list
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class MinStackList:
    def __init__(self):
        self.head = None
        self.min_head = None

    def push(self, value):
        if not self.head:
            self.head = Node(value)
            self.min_head = Node(value)
        else:
            self.head = Node(value, self.head)
            if value < self.min_head.value:
                self.min_head = Node(value, self.min_head)

    def pop(self):
        if not self.head:
            raise Exception("Stack is empty")
        value = self.head.value
        self.head = self.head.next
        if value == self.min_head.value:
            self.min_head = self.min_head.next
        return value

    def min(self):
        if not self.min_head:
            raise Exception("Stack is empty")
        return self.min_head.value

    def __str__(self):
        current = self.head
        stack = []
        while current:
            stack.append(current.value)
            current = current.next
        return str(stack)


# Exercise 3
# plate stack

