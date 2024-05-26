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

class PlateStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []

    def push(self, value):
        if not self.stacks or len(self.stacks[-1]) == self.capacity:
            self.stacks.append([])
        self.stacks[-1].append(value)

    def pop(self):
        if not self.stacks:
            raise Exception("Stack is empty")
        value = self.stacks[-1].pop()
        if not self.stacks[-1]:
            self.stacks.pop()
        return value

    def pop_at(self, index):
        if index >= len(self.stacks):
            raise Exception("Invalid index")
        value = self.stacks[index].pop()
        if not self.stacks[index]:
            self.stacks.pop(index)
        return value

    def __str__(self):
        return str(self.stacks)


# Exercise 4
# implement a queue using two stacks

class MyQueue:
    def __init__(self):
        self.stack_newest = []
        self.stack_oldest = []

    def size(self):
        return len(self.stack_newest) + len(self.stack_oldest)

    def add(self, value):
        self.stack_newest.append(value)

    def shift_stacks(self):
        if not self.stack_oldest:
            while self.stack_newest:
                self.stack_oldest.append(self.stack_newest.pop())

    def peek(self):
        self.shift_stacks()
        return self.stack_oldest[-1]

    def remove(self):
        self.shift_stacks()
        return self.stack_oldest.pop()

    def __str__(self):
        return str(self.stack_newest) + str(self.stack_oldest)


# Exercise 5
# animal shelter for dogs and cats, only oldest animal can be adopted

class Animal:
    def __init__(self, name):
        self.name = name
        self.order = 0

    def __str__(self):
        return self.name


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)


class AnimalShelter:
    def __init__(self):
        self.dogs = []
        self.cats = []
        self.order = 0

    def enqueue(self, animal):
        animal.order = self.order
        self.order += 1
        if isinstance(animal, Dog):
            self.dogs.append(animal)
        elif isinstance(animal, Cat):
            self.cats.append(animal)

    def dequeue_any(self):
        if not self.dogs:
            return self.dequeue_cat()
        if not self.cats:
            return self.dequeue_dog()
        if self.dogs[0].order < self.cats[0].order:
            return self.dequeue_dog()
        else:
            return self.dequeue_cat()

    def dequeue_dog(self):
        if not self.dogs:
            raise Exception("No dogs available")
        return self.dogs.pop(0)

    def dequeue_cat(self):
        if not self.cats:
            raise Exception("No cats available")
        return self.cats.pop(0)
